from confluent_kafka import Producer, Consumer
# Producer: publish processed product metadata and URL
p = Producer({'bootstrap.servers':'kafka:9092'})  # cluster bootstrap
def publish_product(topic, key, value):
    p.produce(topic, key=key, value=value)        # enqueue message
    p.flush()                                      # ensure delivery

# Consumer: distribute products to CDN or archive
c = Consumer({'bootstrap.servers':'kafka:9092', 'group.id':'dist', 'auto.offset.reset':'earliest'})
c.subscribe(['processed_products'])               # subscribe topic
while True:
    msg = c.poll(1.0)                              # blocking poll
    if msg is None: continue
    if msg.error(): continue
    # msg.key() is product id; msg.value() is JSON manifest
    deliver_to_cdn(msg.key(), msg.value())        # custom delivery routine