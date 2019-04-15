import numpy as np
import pandas as pd

df = pd.DataFrame([[0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0]],
                  columns=["Start","Length","1","2","3","4","5","6"])

# enters start values for beginning of shift
df.loc[:,"Start"] = [1,3,3,4]

# enters test values for length of shift
df.loc[:,"Length"] = [2,3,3,2]

# creation of python lists for dataframe columns
keys = ['1','2','3','4','5','6']
values = [i for i in range(2,8)]

# python lists zipped into a dictionary
test_hour_table = dict(zip(keys,values))


# iterating though the dataframe to assess each row individually
for index, row in df.iterrows():

    # pulls start hour and feeds it into hour_table to get the column index
    # row.Start comes as a float, needs to be converted to integer, then as string
    # however, the currenct zeros in the fields, from np.zeros, are floats and need to be converted
    hour = test_hour_table[str(int(row.Start))]
        
    # pulls length value into a variable
    length = row.Length

    # initiate count value with the start_hour from above
    # variable must be instantiated before next loop
    count = hour
        
    # cycles through a single row, once for each unit of length
    for i in range(length):
        
        
        # enter 1 into start hour column
        row.iloc[count] = 1
        
        # increment count variable for next iteration
        count += 1

