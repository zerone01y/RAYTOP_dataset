import os
import pandas as pd
# This script will copy the Demand_U*.csv files from S1, 
# and adapt the data to 
dirs = os.listdir()
dirs.sort()
for dir in dirs:
    if os.path.isfile(dir) and "Demand" in dir:
        demand = pd.read_csv(dir, index_col=[0])
        new_demand = pd.DataFrame(columns=range(1, len(demand.columns) * 2 + 1), index=demand.index)
        demand.columns = demand.columns.astype(int)
        for c_name, col in demand.items():
            new_demand[2 * c_name - 1] = col/2
            new_demand[2 * c_name] = col/2
        new_demand.to_csv(dir)



