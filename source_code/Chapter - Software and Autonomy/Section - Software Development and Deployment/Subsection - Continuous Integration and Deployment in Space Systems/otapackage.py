import hashlib, os
# read firmware and chunk for uplink
def chunks(path, size=64*1024):
    with open(path,'rb') as f:
        while True:
            b = f.read(size)
            if not b: break
            yield b

def package_firmware(path, outdir):
    os.makedirs(outdir, exist_ok=True)
    manifest = {'chunks': []}
    for i,blk in enumerate(chunks(path)):
        chk = hashlib.sha256(blk).hexdigest()             # per-chunk checksum
        fname = f'chunk_{i:04d}.bin'
        with open(os.path.join(outdir,fname),'wb') as fo:
            fo.write(blk)
        manifest['chunks'].append({'file':fname,'sha256':chk})
    # compute full-image hash and mock-sign (use HSM in production)
    with open(path,'rb') as f: full_hash = hashlib.sha256(f.read()).hexdigest()
    manifest['image_sha256'] = full_hash
    manifest['signature'] = f'signed({full_hash})'       # replace with HSM signature
    # write manifest
    import json
    with open(os.path.join(outdir,'manifest.json'),'w') as m:
        json.dump(manifest,m,indent=2)
# usage: package_firmware('build/flight.bin','out/package_v1')