import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'data.xlsx', sheet_name=1, header=2)
beefData = data.iloc[1986:2090, 1:487]

landUseData = beefData.iloc[:, 43]
greenhouseGasData = beefData.iloc[:, 64]
acidData = beefData.iloc[:, 97]
eutrData = beefData.iloc[:, 107]
waterWithdrawData = beefData.iloc[:, 117]
waterScData = beefData.iloc[:, 124]
productionData = beefData.iloc[:, 396]
combinedData = beefData.iloc[:, [396, 64]]  # , 64]]


def removeDashes(row):
    if row.iloc[0] == '-' or row.iloc[1] == '-':  # or row.iloc[2] == '-':
        row.iloc[0] = 0
        row.iloc[1] = 0
        # row.iloc[2] = 0
    return row


combinedData = combinedData.apply(removeDashes, axis=1)
combinedData.plot.scatter(x=0, y=1)  # , c=2, colormap='Blues')
plt.show()
