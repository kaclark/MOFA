import mmap

windows = []
chroms = []
with open('./data/acc/acc_windows.bed', 'r+b') as input_map:
    im = mmap.mmap(input_map.fileno(), 0)
    for line in iter(im.readline, b""):
        lz = line.split(b'\t')
        chrom = str(lz[0].decode('UTF-8'))
        left_pos = int(lz[1].decode('UTF-8'))
        right_pos = int(lz[2].decode('UTF-8'))
        windows.append([chrom, left_pos, right_pos])
        if chrom not in chroms:
            chroms.append(chrom)

distances = []
for chrom in chroms:
    windows_in_chrom = [[win[1],win[2]] for win in windows if str(win[0]) == str(chrom)]
    win_in_chrom = sorted(windows_in_chrom.sort, key=lambda x: int(x[1]))
    for ind, window in enumerate(win_in_chrom):
        if ind == (len(windows_in_chrom) -1):
            continue
        next_window = win_in_chrom[ind + 1]
        window_end = window[1]
        next_start = next_window[0]
        distance = int(next_start) - int(window_end)
        distances.append(str(distance))

export = open('./data/acc/acc_window_distances.txt', 'w')
data = '\n'.join(distances)
export.write(data)
export.close()
