import pandas as pd
import plotly.express as px

data = pd.read_csv('data.csv', header=[2])
oilData = data.iloc[1166:1188, 1:487]
fruitData = data.iloc[1188:1203, 1:487]
df = pd.DataFrame.append(oilData, fruitData)


y_axis = [  # Tuples of (column name, pretty print name for axis labels)
            ('Land Use (m2*yr)', 'Average Land Use (m^2 * yr)'),
            ('GHG Emis \n(kg CO2 eq)', 'Average GHG Emissions (kg CO2 eq)'),
            ('Freshwtr. Withdr. (L)', 'Average Freshwater Withdrawn')
]

for y, name in y_axis:
    df[y] = df[y].replace(',', '', regex=True).astype(float)    # remove commas
    data = df.groupby('Country')[y].mean()

    fig = px.bar(x=data.index,
                 template='plotly_dark',
                 y=data,
                 title=f'{name} vs. Country',
                 labels={'x': 'Country', 'y': name})
    fig.show()

    fig = px.scatter_geo(size=data,
                         locations=data.index,
                         locationmode='country names',
                         title=name,
                         template='plotly_dark',
                         labels={'locations': 'Country', 'size': name})

    fig.show()
