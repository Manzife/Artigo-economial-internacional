import pandas as pd

#importing data base
path = r'C:\Users\usuario\Downloads\base_internacional.csv'
df = pd.read_csv(path, sep = ';', decimal = '.')

df_euroun = df[df['Country Group Name'] == 'European Union']
df_latam = df[df['Country Group Name'] == 'Latin Amereica and the Caribbean']
df_g7 = df[df['Country Group Name'] == 'Major advanced econmies (G7)']
df_euro = df[df['Country Group Name'] == 'Euro area']
#%%


def cleaner(df):
    sub = df.drop(['Units',"Scale",'Country/Series-specific Notes'], axis = 1)
    name = sub['Country Group Name'].iloc[1]
    sub.rename(columns = {'Subject Descriptor':name}, inplace = True)
    sub = sub.drop('Country Group Name', axis = 1)
    sub.set_index(name,inplace = True)
    return sub

x = cleaner(df_euro)
