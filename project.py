import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv("data.csv")
data = df["Avg Rating"].tolist()
hist_data = [data]
group_labels = ['Avg Rating Distribution Graph']
fig=ff.create_distplot(
    hist_data, group_labels, curve_type='normal')
fig.show()
