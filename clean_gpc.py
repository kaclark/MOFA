import mmap
import sys

unfiltered_data = []

input_file = sys.argv[1]
dir = "../../scmnt/acc/gpc_level/"
path = dir + input_file
with open(path, 'r+b') as input_map:
    first_line = True
    im = mmap.mmap(input_map.fileno(), 0)
    for line in iter(im.readline, b""):
        if first_line:
            first_line = False
            continue
        ln = line.split(b"\n")[0]
        lz = ln.split(b"\t")
        data = [lz[0], lz[1], lz[4]]
        unfiltered_data.append([l.decode('UTF-8') for l in data])

filtered = [','.join([gpc[0],gpc[1]]) for gpc in unfiltered_data if int(gpc[2]) == 1]
output = '\n'.join(filtered)
print(output)
