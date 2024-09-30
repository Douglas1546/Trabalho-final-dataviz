import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.functions import carregar_dataset


aeroporto = 'Presidente Juscelino Kubitschek'
df_aeroporto = carregar_dataset.df[(carregar_dataset.df['Aeroporto.Origem'] == aeroporto) | (carregar_dataset.df['Aeroporto.Destino'] == aeroporto)]

df_rotas_companhias = df_aeroporto.groupby(['Rota_Aeroporto', 'Companhia.Aerea']).size().unstack(fill_value=0)

for airline in ['AZUL', 'GOL', 'TAM', 'Others']:
    if airline not in df_rotas_companhias.columns:
        df_rotas_companhias[airline] = 0

df_rotas_companhias['Others'] = df_rotas_companhias.sum(axis=1) - df_rotas_companhias[['AZUL', 'GOL', 'TAM']].sum(axis=1)
df_rotas_companhias['Total'] = df_rotas_companhias[['AZUL', 'GOL', 'TAM', 'Others']].sum(axis=1)
df_rotas_top10 = df_rotas_companhias.nlargest(10, 'Total')

if df_rotas_top10.empty:
    print(f"Sem dados suficientes para o aeroporto {aeroporto}.")
else:
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df_rotas_top10.index,
        x=df_rotas_top10['AZUL'],
        name='AZUL',
        marker_color='blue',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        y=df_rotas_top10.index,
        x=df_rotas_top10['GOL'],
        name='GOL',
        marker_color='orange',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        y=df_rotas_top10.index,
        x=df_rotas_top10['TAM'],
        name='TAM',
        marker_color='red',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        y=df_rotas_top10.index,
        x=df_rotas_top10['Others'],
        name='Outros',
        marker_color='gray',
        orientation='h'
    ))

    fig.update_layout(
        barmode='stack',
        title={
            'text': f'Principais rotas do aeroporto {aeroporto}\nDivididas por companhia aérea',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        title_font_size=20,
        width=1800,
        height=768,
        xaxis=dict(
            title='Número de Voos'
        ),
        yaxis=dict(
            title='Rotas'
        ),
        legend=dict(
            title='Companhia Aérea:',
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        )
    )