import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.functions import carregar_dataset

# Criar novas colunas 'Rota_Aeroporto' e 'Rota_Cidade'
carregar_dataset.df['Rota_Aeroporto'] = carregar_dataset.df['Aeroporto.Origem'] + " ; " + carregar_dataset.df['Aeroporto.Destino']
carregar_dataset.df['Rota_Cidade'] = carregar_dataset.df['Cidade.Origem'] + " ; " + carregar_dataset.df['Cidade.Destino']

# Calcular as rotas por aeroporto
rotas_aeroporto = carregar_dataset.df['Rota_Aeroporto'].value_counts().head(20).sort_values(ascending=True).reset_index()
rotas_aeroporto.columns = ['Rota', 'Number of Flights']

# Calcular as rotas por cidade
rotas_cidade = carregar_dataset.df['Rota_Cidade'].value_counts().head(20).sort_values(ascending=True).reset_index()
rotas_cidade.columns = ['Rota', 'Number of Flights']

# Criar o gráfico de barras das rotas por aeroporto
fig_aeroporto = px.bar(rotas_aeroporto,
                    x='Number of Flights',
                    y='Rota',
                    orientation='h',
                    labels={'Rota': 'Rotas', 'Number of Flights': 'Número de voos'},
                    text='Number of Flights')

# Atualizar o layout do gráfico
fig_aeroporto.update_layout(
    title={
        'text': 'Principais rotas por aeroporto',
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font_size=20,
    width=1800,  # Você pode ajustar a largura conforme necessário
    height=768  # Ajustar a altura
)

# Personalizar as cores e posição do texto
fig_aeroporto.update_traces(marker_color='green', textposition='outside')

######################################################################################################################################################

# Criar o gráfico de barras das rotas por cidade
fig_cidade = px.bar(rotas_cidade,
                    x='Number of Flights',
                    y='Rota',
                    orientation='h',
                    labels={'Rota': 'Rotas', 'Number of Flights': 'Número de voos'},
                    text='Number of Flights')

fig_cidade.update_traces(marker_color='green', textposition='outside')

fig_cidade.update_layout(
    title={
        'text': 'Principais rotas por cidade',
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font_size=20,
    width=1800,
    height=768
)

# Personalizar as cores e posição do texto
fig_cidade.update_traces(marker_color='green', textposition='outside')
