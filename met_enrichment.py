import pickle

#open methlyation data
#A dictionary where the key entries are cell names
#Key values are lists of chromosome and position for example [[4, 323532]...]
with open('./data/met/met_data.pickle', 'rb') as pickle_in:
    met_data = pickle.load(pickle_in)

#get list of chromosomes
obtained = False
chromosomes = []
expected_chrom_entries = 20

#grab a single cell, if that cell doesn't have 21 entries (19 chrom + X and Y) then run again
while obtained == False:
    for cell in met_data.keys():
        #gather all chromosomes numbers found in this cell's data
        subject = [dt[0] for dt in met_data[cell]]
        #remove duplicates
        chromosomes = list(set(subject))
        #if the list of chromosomes isn't the right length try again and clear the list
        obtained = True if (len(chromosomes) >= expected_chrom_entries) else chromosomes.clear()
    #Break the while loop once all cells have been looked through
    #Notify that the process has failed
    if obtained == False:
        print("Error: no cell has expected number of chromosomes")
        exit()
#remove clutter
chromosomes.remove('MT')
chromosomes.remove('9')

#Get the positions of methlyation marks in each cell organized by chromosome
cell_met_by_chrom = {}
for cell in met_data.keys():
    met_by_chrom = {}
    #cell data is a list of lists [[chrom, pos]..]
    cell_data = [dt for dt in met_data[cell]]
    for chrom in chromosomes:
        #gather list of positions for each chromosome in this cell
        positions = [dt[1] for dt in cell_data if dt[0] == chrom]
        positions.sort()
        met_by_chrom[chrom] = positions
    cell_met_by_chrom[cell] = met_by_chrom
#set window to look for density calc
window = 100
density = []
#count how many other methlyation marks are in the window
# genome: ------|---x-----x-----o-x-------x-----|-----
# | = window boundary
# x = methlyation mark
# o = position in question/center of window
#run calcualtion by chromosome
avg_densities = []
for cell in cell_met_by_chrom.keys():
    met_by_chrom = cell_met_by_chrom[cell]
    for chromo in met_by_chrom:
        positions = met_by_chrom[chromo]
        #count number of methlyation marks in the window for each mark
        #pos is the center of window
        for pos in positions:
            #right of window
            ceiling = pos + (window/2)
            #left of window
            floor = pos - (window/2)
            #index value for right window search
            upind = positions.index(pos)
            #index value for left window search
            downind = positions.index(pos)
            pos_density = 0
            #initalize other methylation marks as the center-mark
            upst = pos
            downst = pos
            #count to the right of the center
            while upst < ceiling:
                #add one to the index for each iteration
                upind += 1
                #ensure that the index is not out of bounds
                if not upind > (len(positions) -1):
                    #set right mark to next value to the right 
                    upst = positions[upind]
                    if not upst == pos:
                        pos_density += 1
                else:
                    break
            #count to the left of the center
            while downst > floor:
                #subtract one from the index for each iteration
                downind -= 1
                #ensure taht the index is not out of bounds
                if not downind < 0:
                    #set left mark to the next value on the right
                    downst = positions[downind]
                    if not downst == pos:
                        pos_density += 1
                else:
                    break
            #add the density to the list for this cell
            density.append(pos_density)
    #calculate the average density for the cell
    avg = sum(density) / len(density)
    avg_densities.append(avg)
#calculate the average density of the average desnities for all cells
avgg = sum(avg_densities) / len(avg_densities)
print("The average density across all cells is " + str(avgg) + " methlyation marks in a " + str(window) + "bp window")
