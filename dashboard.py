# layout tudo que vai see visualizado
# callback funcionlidades que voce tera do dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Carrega os dados do arquivo Excel
df = pd.read_excel("Dashboard.xlsx")

# Cria o gráfico inicial
fig = px.bar(df, x="PRODUTO", y="VALOR FINAL", color="ID", barmode="group")

# Opções para o dropdown
opcoes = list(df["ID"].unique())
opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children="Quantidade de produtos"),
    html.H2(children="Gráfico de faturamento de produtos por loja"),
    dcc.Dropdown(id="lista_lojas", options=[{"label": loja, "value": loja} for loja in opcoes], value="Todas as Lojas"),
    dcc.Graph(id="grafico_quantidade_produto", figure=fig)
])

@app.callback(
    Output("grafico_quantidade_produto", "figure"),
    Input("lista_lojas", "value")
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="PRODUTO", y="VALOR FINAL", color="ID", barmode="group")
    else:
        tabela_filtrada = df.loc[df["ID"] == value, :]
        fig = px.bar(tabela_filtrada, x="PRODUTO", y="VALOR FINAL", color="ID", barmode="group")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
