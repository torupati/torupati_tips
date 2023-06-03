import pandas as pd

infile = "./timestamp.csv"
df = pd.read_csv(infile)
print(df.dtypes)
print(df)

#df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S.%f')
df['datetime'] = pd.to_datetime(df['datetime'])
print(df.dtypes)
print(df)

