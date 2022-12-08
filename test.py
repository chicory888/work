import requests
import numpy
import pandas
import pandas as pd
from decimal import Decimal

url = "https://fapi.binance.com/fapi/v1/premiumIndex"

res = requests.get(url)

list = []
for i in res.json():
    list.append([i["symbol"], Decimal(i["lastFundingRate"])])

data = numpy.array(list)
data = data.transpose()
data = {"symbol": data[0], "fundingRate":data[1]}
data = pandas.DataFrame(data)

data.sort_values(by=['fundingRate'],ascending=False,inplace=True,
                     na_position='first')
data.reset_index(drop=True, inplace=True)
pd.set_option('display.max_rows', None)
print(data)
