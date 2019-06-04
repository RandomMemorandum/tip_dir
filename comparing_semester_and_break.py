"""
Filter the dataframe for rows contained in the months ["June","July","August","December"]
which stand for the months during which the main academic semester is over.
"""


# view average values for tips and no_orders
mean_tips_month = pd.pivot_table(df, values=["tips","no_orders"],columns=["month"],aggfunc=np.mean)

# mean tips by day shift and month
mean_orders_month_day = pd.pivot_table(df, values=["no_orders"],index=["harsh_day"],columns=["month"],aggfunc=np.mean)

# mean orders by day shift and month
mean_tips_month_day = pd.pivot_table(df, values=["tips"],index=["harsh_day"],columns=["month"],aggfunc=np.mean)




