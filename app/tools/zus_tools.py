import pandas as pd
import os

# Load outlet data
OUTLETS_CSV = os.path.join(os.path.dirname(__file__), '../../data/outlets.csv')
PRODUCTS_CSV = os.path.join(os.path.dirname(__file__), '../../data/products.csv')


def get_outlet_hours(location: str) -> str:
    df = pd.read_csv("data/outlets.csv")
    result = df[df['location'].str.lower() == location.lower()]
    if not result.empty:
        return result.iloc[0]['opening_hours']
    return "Sorry, I couldn't find the opening hours for that location."


def get_product_info(product: str) -> str:
    df = pd.read_csv("data/products.csv")
    result = df[df['product'].str.lower().str.contains(product.lower())]
    if not result.empty:
        row = result.iloc[0]
        return f"{row['product']}: RM{row['price']} - {row['availability']}"
    return "Sorry, I couldn't find that product."

