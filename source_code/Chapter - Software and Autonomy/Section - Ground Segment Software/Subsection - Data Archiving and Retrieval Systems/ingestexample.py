import hashlib, boto3, psycopg2
# compute checksum (streaming)
def sha256_stream(fileobj):
    h=hashlib.sha256()
    for chunk in iter(lambda: fileobj.read(8192), b''):
        h.update(chunk)
    return h.hexdigest()

# upload file to S3-compatible object store (preserve deterministic key)
def upload_obj(bucket,key,fileobj):
    s3=boto3.client('s3')  # configured with creds/endpoint
    fileobj.seek(0)
    s3.upload_fileobj(fileobj,bucket,key)  # small wrapper

# write metadata record (STAC fields simplified) to PostGIS table
def write_metadata(conn,record):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO assets(id,geom,acq_time,checksum,s3_key)
            VALUES (%s, ST_SetSRID(ST_MakePoint(%s,%s),4326), %s, %s, %s)
            """,
            (record['id'], record['lon'], record['lat'],
             record['time'], record['checksum'], record['s3_key'])
        )
        conn.commit()

# usage (pseudo)
# with open('frame.dat','rb') as f:
#   checksum=sha256_stream(f)
#   key=f"missionA/{checksum}.dat"  # deterministic key
#   upload_obj('archive-bucket', key, f)
#   write_metadata(pg_conn, {'id':'uuid','lon':12.3,'lat':45.6,'time':'2025-01-01T00:00:00Z','checksum':checksum,'s3_key':key})