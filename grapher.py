import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

data = pd.read_excel(r'data.xlsx', sheet_name=1, header=2)
oilData = data.iloc[1166:1188, 1:487]
fruitData = data.iloc[1188:1203, 1:487]
palmData = pd.DataFrame.append(oilData, fruitData)


landUseData = palmData.iloc[:, 43]
greenhouseGasData = palmData.iloc[:, 64]
acidData = palmData.iloc[:, 97]
eutrData = palmData.iloc[:, 107]
# waterWithdrawData = palmData.iloc[:, 117]
# waterScData = palmData.iloc[:, 124]
productionData = palmData.iloc[:, 396]


combinedData = palmData.iloc[:, [64, 43]]  # , 64]]



def removeDashes(row):
    if row.iloc[0] == "-" or row.iloc[1] == "-":  # or row.iloc[2] == '-':
        row.iloc[0] = float("NaN")
        row.iloc[1] = float("NaN")
        # row.iloc[2] = 0
    return row

def removeNaN(li: list, other_li: list):
    i = 0
    while(i < len(li)):
        try:
            if math.isnan(li[i]) or li[i] == "-" or math.isnan(other_li[i]) or other_li[i] == "-":
                del(li[i])
                del(other_li[i])
                i -= 1
        except TypeError:
            del(li[i])
            del(other_li[i])
            i -= 1
        finally:
            i += 1


xlist = greenhouseGasData.tolist()
ylist = landUseData.tolist()

removeNaN(xlist, ylist)

x = np.array(xlist)
y = np.array(ylist)
m, b = np.polyfit(x, y, 1)

correlation_matrix = np.corrcoef(xlist, ylist)
correlation_xy = correlation_matrix[0, 1]
r_squared = round(correlation_xy**2, 10)

combinedData = combinedData.apply(removeDashes, axis=1)
combinedData.plot.scatter(x=0, y=1)  # , c=2, colormap='Blues')
plt.show()
combinedData.plot.scatter(x=0, y=1)  # , c=2, colormap='Blues')
plt.plot(x, m*x + b)
plt.text(min(xlist), max(ylist)*0.9, s=f"R$^2$ = {r_squared}")
plt.show()

