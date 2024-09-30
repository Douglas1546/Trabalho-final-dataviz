import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Carregar o arquivo CSV
df = pd.read_csv('./data/BrFlights2.csv', encoding='latin1')