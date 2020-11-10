import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'data.xlsx', sheet_name=1, header=2)
palmData = data.iloc[2653:2706, 1:487]

# landUseData = palmData.iloc[:, 43]
# greenhouseGasData = palmData.iloc[:, 64]
# acidData = palmData.iloc[:, 97]
# eutrData = palmData.iloc[:, 107]
# waterWithdrawData = palmData.iloc[:, 117]
# waterScData = palmData.iloc[:, 124]
# productionData = palmData.iloc[:, 396]


combinedData = palmData.iloc[:, [43, 107]]  # , 64]]



def removeDashes(row):
    if row.iloc[0] == '-' or row.iloc[1] == '-':  # or row.iloc[2] == '-':
        row.iloc[0] = float("NaN")
        row.iloc[1] = float("NaN")
        # row.iloc[2] = 0
    return row


combinedData = combinedData.apply(removeDashes, axis=1)
combinedData.plot.scatter(x=0, y=1)  # , c=2, colormap='Blues')
plt.show()
