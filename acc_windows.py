import mmap

window = 150
gpc_windows = []
with open('./data/acc/acc_uq.csv', 'r+b') as input_map:
    #perform operations on this line
    im = mmap.mmap(input_map.fileno(), 0)
    for line in iter(im.readline, b""):
        lz = line.split(b',')
        chrom = str(lz[0].decode('UTF-8'))
        pos = int(lz[1].decode('UTF-8'))
        left_pos = int(pos - (window / 2))
        right_pos = int(pos + (window / 2))
        gpc_window = chrom + "," + str(left_pos) + "," +  str(right_pos)
        gpc_windows.append(gpc_window)

export = open('./data/acc/acc_windows_150.txt', 'w')
data = '\n'.join(gpc_windows)
export.write(data)
export.close()

