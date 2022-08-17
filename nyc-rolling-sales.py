import pandas as pd
df=pd.read_csv("nyc-rolling-sales.csv")
def change_values(df):
    
    condition = df['BOROUGH'] == 1
    df.loc[condition,'BOROUGH'] = 'Manhattan'

    condition = df['BOROUGH'] == 2
    df.loc[condition,'BOROUGH'] = 'Bronx'

    condition = df['BOROUGH'] == 3
    df.loc[condition,'BOROUGH'] = 'Brooklyn'

    condition = df['BOROUGH'] == 4
    df.loc[condition,'BOROUGH'] = 'Queens'

    condition = df['BOROUGH'] == 5
    df.loc[condition,'BOROUGH'] = 'Staten Island'
    
    return df
    print(df.head())
        

