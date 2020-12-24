import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

data = pd.read_excel(r'data.xlsx', sheet_name=1, header=2)
oilData = data.iloc[1166:1187, 1:487]
fruitData = data.iloc[1188:1203, 1:487]
palmData = fruitData


landUseData = palmData.iloc[:, 43]
greenhouseGasData = palmData.iloc[:, 64]
acidData = palmData.iloc[:, 97]
eutrData = palmData.iloc[:, 107]
waterWithdrawData = palmData.iloc[:, 117]
waterScData = palmData.iloc[:, 124]
productionData = palmData.iloc[:, 396]


combinedData = palmData.iloc[:, [396, 43]]  # , 64]]



def removeDashes(row):
    if row.iloc[0] == '-' or row.iloc[1] == '-':  # or row.iloc[2] == '-':
        row.iloc[0] = float("NaN")
        row.iloc[1] = float("NaN")
        # row.iloc[2] = 0
    return row

def removeNaN(li: list):
    i = 0
    while(i < len(li)):
        if math.isnan(li[i]):
            del(li[i])
        else:
            i += 1
    return li

prodlist = productionData.tolist()
# del(prodlist[24])
# del(prodlist[27])
landlist = landUseData.tolist()
# del(landlist[24])
# del(landlist[27])

print(prodlist)
print(landlist)

x = np.array(removeNaN(prodlist))
y = np.array(removeNaN(landlist))
m, b = np.polyfit(x, y, 1)

combinedData = combinedData.apply(removeDashes, axis=1)
combinedData.plot.scatter(x=0, y=1)  # , c=2, colormap='Blues')
# plt.plot(x, m*x + b)
plt.show()
