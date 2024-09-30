from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
import pandas as pd
from app import app
from app.functions import num_chegada_partidas_cada_aeroporto, rotas_aeroporto_e_cidade, principais_rotas_Brasilia, principais_rotas_Congonhas, principais_rotas_Galeao, principais_rotas_Guarulhos, principais_rotas_Val_De_Cans, mapa_rotas_Val_De_Cans, mapa_rotas_Guarulhos, mapa_rotas_Galeao, mapa_rotas_Congonhas, mapa_rotas_Brasilia



@app.route('/')
def index():
    
    fig_aeroporto = rotas_aeroporto_e_cidade.fig_aeroporto
    fig_cidade = rotas_aeroporto_e_cidade.fig_cidade
    
    fig_chegada_partida = num_chegada_partidas_cada_aeroporto.fig
    
    
    # Rotas dos aeroportos principais por companhia aérea
    fig_rotas_Brasilia = principais_rotas_Brasilia.fig
    fig_rotas_Congonhas = principais_rotas_Congonhas.fig
    fig_rotas_Galeao = principais_rotas_Galeao.fig
    fig_rotas_Guarulhos = principais_rotas_Guarulhos.fig
    fig_rotas_Val_De_Cans = principais_rotas_Val_De_Cans.fig
      
    
    # Converta o gráfico em HTML
    graph_html_1 = pio.to_html(fig_aeroporto, full_html=False)
    graph_html_2 = pio.to_html(fig_cidade, full_html=False)
    graph_html_3 = pio.to_html(fig_chegada_partida, full_html=False)
    
    # html das Rotas dos aeroportos principais por companhia aérea
    graph_html_4 = pio.to_html(fig_rotas_Brasilia, full_html=False)
    graph_html_5 = pio.to_html(fig_rotas_Congonhas, full_html=False)
    graph_html_6 = pio.to_html(fig_rotas_Galeao, full_html=False)
    graph_html_7 = pio.to_html(fig_rotas_Guarulhos, full_html=False)
    graph_html_8 = pio.to_html(fig_rotas_Val_De_Cans, full_html=False)
    
    
    # graficos de mapas de Rotas dos aeroportos principais para todos os destinos
    graph_html_9 = mapa_rotas_Brasilia.map_html
    graph_html_10 = mapa_rotas_Congonhas.map_html
    graph_html_11 = mapa_rotas_Galeao.map_html
    graph_html_12 = mapa_rotas_Guarulhos.map_html
    graph_html_13 = mapa_rotas_Val_De_Cans.map_html
    
    
    # Renderizar a página HTML e passar o gráfico
    return render_template('index.html', graph_aeroporto=graph_html_1, graph_cidade=graph_html_2, graph_chegada_partida=graph_html_3, graph_rotas_Brasilia=graph_html_4, graph_rotas_Congonhas=graph_html_5, graph_rotas_Galeao=graph_html_6, graph_rotas_Guarulhos=graph_html_7, graph_rotas_Val_De_Cans=graph_html_8, mapa_viagens_Brasilia=graph_html_9, mapa_viagens_Congonhas=graph_html_10, mapa_viagens_Galeao=graph_html_11, mapa_viagens_Guarulhos=graph_html_12, mapa_viagens_Val_De_Cans=graph_html_13)