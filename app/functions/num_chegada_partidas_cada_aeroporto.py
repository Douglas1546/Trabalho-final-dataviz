import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.functions import carregar_dataset


carregar_dataset.df['Tipo.Voo'] = carregar_dataset.df.apply(lambda row:
                          'Internacional' if row['Pais.Origem'] != row['Pais.Destino']
                          else 'Regional' if row['Estado.Origem'] == row['Estado.Destino']
                          else 'Nacional', axis=1)

df_voos = carregar_dataset.df.groupby(['Aeroporto.Origem', 'Tipo.Voo']).size().unstack(fill_value=0)

df_voos['Nacional'] = df_voos.get('Nacional', 0)
df_voos['Internacional'] = df_voos.get('Internacional', 0)
df_voos['Regional'] = df_voos.get('Regional', 0)

df_voos['Total'] = df_voos['Nacional'] + df_voos['Internacional'] + df_voos['Regional']

df_voos_top20 = df_voos.nlargest(20, 'Total')

df_voos_top20 = df_voos_top20.iloc[::-1]

fig = go.Figure()

fig.add_trace(go.Bar(
    y=df_voos_top20.index,
    x=df_voos_top20['Nacional'],
    name='Nacional',
    marker_color='gray',
    orientation='h'
))

fig.add_trace(go.Bar(
    y=df_voos_top20.index,
    x=df_voos_top20['Internacional'],
    name='Internacional',
    marker_color='blue',
    orientation='h'
))

fig.add_trace(go.Bar(
    y=df_voos_top20.index,
    x=df_voos_top20['Regional'],
    name='Regional',
    marker_color='green',
    orientation='h'
))

fig.update_layout(
    barmode='stack',
    title={
        'text': 'Número de chegadas/partidas em cada aeroporto (Top 20)',
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font_size=20,
    width=1800,
    height=768,
    xaxis=dict(
        title='Número de voos'
    ),
    yaxis=dict(
        title='Aeroportos'
    ),
    legend=dict(
        title='Flight Type',
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    )
)
