# How many rows are in our dataset?
len(df)

# In total, how many non-cancelled flights were taken?
len(df[~df.Cancelled])

# In total, how many non-cancelled flights were taken from each airport?
df[~df.Cancelled].groupby('Origin').Origin.count().compute()

# What was the average departure delay from each airport?
df[~df.Cancelled].groupby('Origin').DepDelay.mean().compute()

# What day of the week has the worst average departure delay?
df[~df.Cancelled].groupby('DayOfWeek').DepDelay.mean().compute()
