import mmap
import sys
from pathlib import Path

directory = sys.argv[1]
pathlist = Path(directory).glob('*.tsv')

gpcs = []
for pre_path in pathlist:
    path = str(pre_path)
    with open(path, 'r+b') as input_map:
        first_line = True
        im = mmap.mmap(input_map.fileno(), 0)
        for line in iter(im.readline, b""):
            if first_line:
                first_line = False
                continue
            ln = line.split(b"\n")[0]
            lz = ln.split(b"\t")
            lz = [l.decode('UTF-8') for l in lz]
            gpcs.append(','.join(lz))
    gpcs = list(set(gpcs))
output = '\n'.join(gpcs)
print(output)
