import pandas as pd
import numpy as np

df = pd.read_csv("speeddating.csv", low_memory=False)
df = df.applymap(lambda x: np.nan if x == '?' else x)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(df.isnull().any())

print(df.loc[2])