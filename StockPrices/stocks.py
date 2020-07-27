
import json 
import datetime as dt 
import pandas as pd
import yahoo_fin
from yahoo_fin import stock_info as si


df = pd.DataFrame(columns=('datetime','otc', 'names', 'price'))

# read shares attributes from json file aktien.json
with open('aktien.json', "r") as json_file:
    data = json.load(json_file)
    # parse json for observed shares
    for key in data:
        otc =  key['otc']
        name = key['name']
        time = dt.datetime.now() 
        # get life proce via otc request
        share_value = si.get_live_price(otc)
        df = df.append({'names': name, 'otc': otc, 'datetime': time, 'price': share_value}, ignore_index=True)
    # Save into csv w=write, a=append
    df.to_csv("stock_values_record.csv", mode='a', header=False)
print(df.info())
print(df.head())
    



































# # conda activate stocks 

# # import datetime as dt 
# # import matplotlib.pyplot as plt 
# # from matplotlib import style 
# import pandas as pd 

# from yahoo_fin import stock_info as si

# # Nasaq Kurs Daimler = ddaif
# print(si.get_live_price("ddaif"))
# print(si.get_live_price("baba"))







