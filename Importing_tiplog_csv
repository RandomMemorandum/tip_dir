import numpy as np
import pandas as pdsns

tiplog = pd.read_csv("deliverytiplogtest.csv")

# reassigns object to include only the columns containing values
no_columns = _________

tiplog = tiplog.iloc[:,:no_columns]

# drops rows that have an empty space in at least one column space
# set tiplog to the new object, where columns are dropped
tiplog = tiplog.dropna()

# reset index
# inplace=True to adjust the current object, not create a new one
tiplog.reset_index(drop=True, inplace=True)

# writing back to a .csv
tiplog.to_csv("_____________.csv")
