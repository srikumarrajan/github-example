import pandas as pd
import numpy as np
#from sklearn.cluster import KMeans

import requests
url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

r = requests.get(url)
tables = pd.read_html(r.text)
df=pd.DataFrame(tables[0])
df.columns=['Postcode','Borough','Neighbourhood']

df.drop([0],axis=0,inplace=True)
df.reset_index()
df = df[df.Borough != 'Not assigned']
df = df.groupby(['Postcode', 'Borough'])['Neighbourhood'].apply(list).apply(lambda x:', '.join(x)).to_frame().reset_index()
for index, row in df.iterrows():
    if row['Neighbourhood'] == 'Not assigned':
        row['Neighbourhood'] = row['Borough']
print(df)
