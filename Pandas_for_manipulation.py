# import pandas

import pandas as pd

# import our grocery data

sales_data = pd.read_csv("grocery_sales.csv")

# fill in missing sales values

avg_sales = sales_data["sales"].mean()
sales_data["sales"].fillna(value = avg_sales, inplace = True)

# sum sales by day

sales_summary = sales_data.groupby("transaction_date")["sales"].sum()

# plot sales over time

sales_summary.plot(rot = 45)