import pandas as pd
import os

table = pd.read_csv("cancelamentos_sample.csv")

table = table.drop(columns="CustomerID")

table.dropna()

column_cancelou = table["cancelou"]

print("Pre-resolution: ")
print(column_cancelou.value_counts(normalize=True).map("{:.0%}".format))


import plotly.express as px
import os

output_dir = "pre-resolution"
os.makedirs(output_dir, exist_ok=True)

for column in table.columns:
    graph = px.histogram(
        table,
        x=column,
        color="cancelou",
        category_orders={"cancelou": [0, 1]},
        color_discrete_map={1: "red", 0:"green"},
        text_auto=True,
        )
    graph.write_image(f"{output_dir}/{column}.png")

condition = table["idade"] <= 50
table = table[condition]

condition = table["ligacoes_callcenter"] <= 4
table = table[condition]

condition = table["duracao_contrato"] != "Monthly"
table = table[condition]

condition = table["dias_atraso"] <= 15
table = table[condition]

output_dir = "post-resolution"

os.makedirs(output_dir, exist_ok=True)

for column in table.columns:
    graph = px.histogram(
        table,
        x=column,
        color="cancelou",
        category_orders={"cancelou": [0, 1]},
        color_discrete_map={1: "red", 0:"green"},
        text_auto=True,
        )
    
    graph.write_image(f"{output_dir}/{column}.png")

print("Post-resolution: ")
print(table["cancelou"].value_counts(normalize=True).map("{:.0%}".format))
