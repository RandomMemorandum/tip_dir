import numpy as np
import pandas as pd

file = "________.csv"

df = pd.read_csv(file)

# gather relevant columns from DataFrame
df.columns

# reduced columns down to core information
df = df[['date', 'end_date', 'shift', 'no_orders', 'tips', 'day_of_week', 'StTmAdj',
       'EdTmAdj', 'No_hours', 'Day Shift']]

# Ensure columns only contain numbers
df = df.drop([46])
df.reset_index(drop=True, inplace=True)

# convert datatypes to numeric, so that calculations can be performed
df.no_orders = pd.to_numeric(df.no_orders)
df.tips = pd.to_numeric(df.tips)


# histogram of "tips" columns with 20 bins
df["tips"].hist(bins=20)

# histogram of "no_orders" columns with 20 bins
df["no_orders"].hist(bins=20)

# scatterplot of "no_orders" and "tips" columns
df.plot.scatter(x="no_orders",y="tips", c="red")

# Pearson correlation coefficient
np.corrcoef(x=df.no_orders,y=df.tips)

# find the mean of tips, grouped by day of the week
mean_tips_dow = df.groupby(["day_of_week"])["tips"].mean()

# mean of number of deliveries, also grouped by day of th week
mean_no_orders_dow = tiplog.groupby(["day_of_week"])["no_orders"].mean()
