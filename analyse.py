import pandas as pd
import matplotlib.pyplot as plt

products = pd.read_excel("products.xlsx")

change_column = ["title", "price", "battery-time", "review-count", "star-count", "img-link"]
products = products.reindex(columns=change_column)

products.to_excel("products_new.xlsx", index=False)

new_products = pd.read_excel("products_new.xlsx")

new_products['price'] = pd.to_numeric(new_products['price'].replace('[\$,]', '', regex=True), errors='coerce')

price_by_title = new_products.groupby('title')['price'].sum()

price_by_title.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Price Distribution by Product Title')
plt.ylabel('')
plt.show()
