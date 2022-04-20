import pandas as pd
import plotly.figure_factory as ff

storeData = pd.read_csv('data.csv')
graph = ff.create_distplot([storeData['Avg Rating'].tolist()],['Average Rating'], show_hist = True)
graph.show()