import pickle
import pandas as pd

print("imports finished")

#open methlyation data
#A dictionary where the key entries are cell names
#Key values are lists of chromosome and position for example [[4, 323532]...]
with open('./data/met/met_data.pickle', 'rb') as pickle_in:
    met_data = pickle.load(pickle_in)

print("cpg data loaded")

#variables used for giving periodic progress reports
total_count = len(met_data.keys())
checkpoints = 10
divisor = total_count / checkpoints

regions = []
for ind, cell in enumerate(met_data.keys()):
    #add cell's regions to the list
    regions.extend(met_data[cell])
    #remove duplicates
    regions = list(set(regions))
    if ind / divisor % 10 == 0:
        print("Collection " + str(((ind/total_count) * 100)) + " percent complelete")

print("regions collected")

export = pd.DataFrame(regions)
print("regions converted to dataframe")
path = "./data/met/met_uq_regions.txt"
export.to_csv(path, index=False, header=False)
print("export complete. data is located at " + path)
