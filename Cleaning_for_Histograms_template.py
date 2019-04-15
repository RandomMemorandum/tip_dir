import numpy as np
import pandas as pd
import scipy.stats as sts
import matplotlib.pyplot as plt

data = pd.read_csv("tiplog_droppedcol.csv")

data = data.iloc[:,1:5]

no_orders_tips = data.iloc[:,2:]
no_orders_tips.head()

# histogram is not working correctly
# this is because the datatype of the columns is "object" which means they are not integers
# https://stackoverflow.com/questions/42719749/pandas-convert-string-to-int
print(no_orders_tips.dtypes)

# now we have the row that has only "-"
print(no_orders_tips.iloc[50:70,:])

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
no_orders_tips = no_orders_tips.drop([53])
print(no_orders_tips.iloc[50:70,:])

# index 53 has been removed, now we must reset the index, so that they are continuous
no_orders_tips.reset_index(drop=True, inplace=True)

# force the values in the "tips" column to an "int" type
no_orders_tips.tips = pd.to_numeric(no_orders_tips.tips)

# we do the same for the no_orders columns
no_orders_tips.no_orders = pd.to_numeric(no_orders_tips.no_orders)


# histogram of "tips" columns with 20 bins
no_orders_tips["tips"].hist(bins=20)


# histogram of "no_orders" columns with 20 bins
no_orders_tips["no_orders"].hist(bins=20)

# scatterplot of "no_orders" and "tips" columns
no_orders_tips.plot.scatter(x="no_orders",y="tips", c="red")


# Pearson correlation coefficient
np.corrcoef(x=no_orders_tips.no_orders,y=no_orders_tips.tips)





