import datetime
import pandas as pd 
import requests
import json

today = datetime.date.today()
year = today.strftime("%Y")

lst = [['01/01/'+year, 'M01'], ['01/02/'+year, 'M02'], ['01/03/'+year, 'M03'],
        ['01/04/'+year, 'M04'], ['01/05/'+year, 'M05'], ['01/06/'+year, 'M06'],
       ['01/07/'+year, 'M07'], ['01/08/'+year, 'M08'], ['01/09/'+year, 'M09'],
       ['01/10/'+year, 'M10'], ['01/11/'+year, 'M11'], ['01/12/'+year, 'M12']]

df1 = pd.DataFrame(lst, columns =['Date', 'Month'])

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ["CUUR0100SA0","CUUR0110SA0","CUUR0120SA0","CUURA104SA0","CUURN100SA0","CUURS100SA0","CUURS11ASA0","CUURS12ASA0","CUURS12BSA0","CUUR0200SA0","CUUR0230SA0","CUUR0240SA0","CUURA210SA0","CUURA212SA0","CUURA213SA0","CUURA214SA0","CUURD200SA0","CUURN200SA0","CUURS200SA0","CUURS23ASA0","CUURS23BSA0","CUURS24ASA0","CUURS24BSA0","CUUR0300SA0","CUUR0350SA0"],"startyear":year, "endyear":year})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
df3 = pd.DataFrame()

for series in json_data['Results']['series']:
    seriesId = series['seriesID']
    lst3 = []
    for item in series['data']:
        period = item['period']
        value = item['value']
        lst2 = [period, value]
        lst3.append(lst2)
    df2 = pd.DataFrame(lst3, columns =['Month', seriesId])
    if df3.empty:
        df3 = df1.merge(df2, how='outer')
    else:
        df3 = df3.merge(df2, how='outer')

data = json.dumps({"seriesid": ["CUUR0360SA0","CUUR0370SA0","CUURA311SA0","CUURD300SA0","CUURN300SA0","CUURS300SA0","CUURS35ASA0","CUURS35BSA0","CUURS35CSA0","CUURS35DSA0","CUURS35ESA0","CUURS37ASA0","CUURS37BSA0","CUUR0400SA0","CUUR0480SA0","CUUR0490SA0","CUURA421SA0","CUURA425SA0","CUURN400SA0","CUURS400SA0","CUURS48ASA0","CUURS48BSA0","CUURS49ASA0","CUURS49BSA0","CUURS49CSA0"],"startyear":year, "endyear":year})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
df4 = pd.DataFrame()

for series in json_data['Results']['series']:
    seriesId = series['seriesID']
    lst3 = []
    for item in series['data']:
        period = item['period']
        value = item['value']
        lst2 = [period, value]
        lst3.append(lst2)
    df2 = pd.DataFrame(lst3, columns =['Month', seriesId])
    if df4.empty:
        df4 = df1.merge(df2, how='outer')
    else:
        df4 = df4.merge(df2, how='outer')

data = json.dumps({"seriesid": ["CUURS49DSA0","CUURS49ESA0","CUURS49FSA0","CUURS49GSA0"],"startyear":year, "endyear":year})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
df5 = pd.DataFrame()

for series in json_data['Results']['series']:
    seriesId = series['seriesID']
    lst3 = []
    for item in series['data']:
        period = item['period']
        value = item['value']
        lst2 = [period, value]
        lst3.append(lst2)
    df2 = pd.DataFrame(lst3, columns =['Month', seriesId])
    if df5.empty:
        df5 = df1.merge(df2, how='outer')
    else:
        df5 = df5.merge(df2, how='outer')

df6 = df3.merge(df4, how='outer')
df6 = df6.merge(df5, how='outer')
print(df6)
df6.to_csv("M:/Database/US/temp/sourcecpim04.csv", index=False)
