import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from app.functions import carregar_dataset



df_val_de_cans = carregar_dataset.df[carregar_dataset.df['Aeroporto.Origem'] == 'Congonhas']

df_grouped = df_val_de_cans.groupby(['Aeroporto.Destino', 'LatDest', 'LongDest', 'Codigo.Tipo.Linha']).size().reset_index(name='Voos')

m = folium.Map(location=[df_val_de_cans['LatOrig'].iloc[0], df_val_de_cans['LongOrig'].iloc[0]], zoom_start=4)

tipo_voo_colors = {
    'Internacional': 'yellow',
    'Nacional': 'green',
    'Regional': 'blue'
}

for _, row in df_grouped.iterrows():
    origem = 'Val De Cans'
    destino = row['Aeroporto.Destino']

    folium.Marker(
        location=[df_val_de_cans['LatOrig'].iloc[0], df_val_de_cans['LongOrig'].iloc[0]],
        popup=origem,
        icon=folium.Icon(color='red')
    ).add_to(m)

    folium.Marker(
        location=[row['LatDest'], row['LongDest']],
        popup=destino,
        icon=folium.Icon(color='red')
    ).add_to(m)

    tooltip_msg = f"""<div style="font-size: 14pt;"><b>De {origem} para {destino}</b><br>Voos: {row['Voos']}</div>"""

    line = folium.PolyLine(
        locations=[(df_val_de_cans['LatOrig'].iloc[0], df_val_de_cans['LongOrig'].iloc[0]), (row['LatDest'], row['LongDest'])],
        color=tipo_voo_colors.get(row['Codigo.Tipo.Linha'], 'gray'),
        weight=5,
        opacity=0.6,
        tooltip=folium.Tooltip(tooltip_msg)
    )

    line.add_to(m)

legend_html = '''
     <div style="position: fixed;
     bottom: 50px; left: 50px; width: 150px; height: 90px;
     background-color: white; z-index:9999; font-size:14px;
     border:2px solid grey; padding: 10px;">
     <b>Tipo de voo</b> <br>
     <span style="background-color:green; width: 10px; height: 10px; display: inline-block;"></span> Nacional <br>
     <span style="background-color:blue; width: 10px; height: 10px; display: inline-block;"></span> Regional <br>
     <span style="background-color:yellow; width: 10px; height: 10px; display: inline-block;"></span> Internacional <br>
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))

map_html = m._repr_html_()

# html = f'''
# <div style="width: 1400px; height: 900px;">
#   {map_html}
# </div>
# '''

# from IPython.display import display, HTML
# display(HTML(html))