from typing import Union
import pandas as pd

from fastapi import FastAPI

app = FastAPI()

df = pd.read_csv("/home/tiagolopes/copilot/olist_processed_dataset.csv")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/filtro/{item_id}")
def filtro(item_id):
    result = df[df['customer_id'] == item_id].head(5)
    return result.to_json()

@app.get("/filtro_cidade/{cidade}")
def filtro_cidade(cidade):
    result = df[df['customer_city'] == cidade].head(5)
    return result.to_json()

@app.get("/filtro_data/{data}")
def filtro_data(data):
    result = df[df['customer_order_purchase_timestamp'].str.startswith(data)].head(5)
    return result.to_json()
