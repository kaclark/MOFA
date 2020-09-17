import mmap
import pickle

#make list of files to mmap over
e45_files = open('index_E4.5.txt', 'r')
#-1 drops the \n character from the line
file_names = [line[:-1] for line in e45_files.readlines()]
#the index file grabbed itself as the last element, dropping it
file_names.pop()

#cells with their filtered gpcs
cell_E45 = {}

#unique filtered gpcs 
gpc_E45 = []

dir = './data/scmnt/acc/gpc_level/'
for file in file_names:
    unfiltered_data = []
    path = dir + file
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

    filtered = [str(gpc[0]) + ":" + str(gpc[1]) for gpc in unfiltered_data if int(gpc[2]) == 1]
    #keep track of unique gpcs
    gpc_E45.extend(filtered)
    gpc_E45 = list(set(gpc_E45))
    name = file.split('.tsv')[0]
    cell_E45[name] = filtered

#to make this data easily accessible later, I will pickle it
pickle.dump(cell_E45, './data/acc/E4.5_cells.pickle')

#output list of unique gpcs
pre_csv = []
for gpc in gpc_E45:
    data = gpc.split(':')
    export_line = ','.join(data)
    pre_csv.append(export_line)
export_data = '\n'.join(pre_csv)

with open("./data/acc/uq_gpc_E4.5.txt", "w") as uq_gpc_out:
    uq_gpc_out.write(export_data)


gpc_freq = {}
#iterate through each uq gpc
for gpc in gpc_E45:
    #iterate through each cell
    for cell in cell_E45.keys():
        #if it is in that cell increase the freq
        if gpc in set(cell_E45[cell]):
            gpc_freq[gpc] = gpc_freq.get(gpc, 0) + 1

gpc_freq_list = [str(gpc) + "," + str(gpc_freq[gpc]) for gpc in gpc_freq]
gpc_freq_export = '\n'.join(gpc_freq_list)
with open('gpc_E45_freq.csv', 'w') as gpc_freq_out:
    gpc_freq_out.write(gpc_freq_export)


