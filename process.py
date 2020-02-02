import os
import subprocess

try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, 'wb')

def get_pids_open():
    file='marvel.json'
    for f in file:
        if not isinstance(f, str):
            raise ValueError('invalid file name %s' % f)
    pids = set()
    try:
        out = subprocess.check_output(['lsof', '+wt']+list(file),
                stderr=DEVNULL)
    except Exception as e:
        out = str(e.output)
    if not out.strip():
        return []
    lines = out.strip().split('\n')
    for line in lines:
        pids.add(int(line))
        
    return list(pids)