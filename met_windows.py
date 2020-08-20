import mmap

window = 150
cpg_windows = []
with open('./data/met/met_uq.csv', 'r+b') as input_map:
    #perform operations on this line
    im = mmap.mmap(input_map.fileno(), 0)
    for line in iter(im.readline, b""):
        lz = line.split(b',')
        chrom = str(lz[0].decode('UTF-8'))
        pos = int(lz[1].decode('UTF-8'))
        left_pos = int(pos - (window / 2))
        right_pos = int(pos + (window / 2))
        cpg_window = chrom + "," + str(left_pos) + "," +  str(right_pos)
        cpg_windows.append(cpg_window)

export = open('./data/met/met_windows.txt', 'w')
data = '\n'.join(cpg_windows)
export.write(data)
export.close()

