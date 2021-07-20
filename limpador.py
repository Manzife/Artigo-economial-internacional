import pandas as pd
import seaborn as sns
#importing data base
path = r'C:\Users\usuario\Downloads\base_internacional.csv'
df = pd.read_csv(path, sep = ';', decimal = '.')

#cleaning, keeping only the series 
countries = list(df['Country Group Name'].unique())
df_euroun = df[df['Country Group Name'] == countries[2]]
df_latam = df[df['Country Group Name'] == countries[3]]
df_g7 = df[df['Country Group Name'] == countries[1]]
df_euro = df[df['Country Group Name'] == countries[0]]

def cleaner(df):
    sub = df.drop(['Units',"Scale",'Country/Series-specific Notes'], axis = 1)
    name = sub['Country Group Name'].iloc[1]
    sub.rename(columns = {'Subject Descriptor':name}, inplace = True)
    sub = sub.drop('Country Group Name', axis = 1)
    sub.set_index(name,inplace = True)
    return sub

df_euro = cleaner(df_euro)
df_latam = cleaner(df_latam)
df_g7 = cleaner(df_g7)
df_euroun = cleaner(df_euroun)

