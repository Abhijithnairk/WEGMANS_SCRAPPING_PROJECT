import mysql.connector
from mysql.connector import Error
import json

def process_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        
        product_info = []
        products = data.get('items', [])
        for product in products:
            name = product.get("name")
            price = product.get("base_price")
            url = product.get("href")        
            product_info.append((name, price, url))
        
        connection = mysql.connector.connect(
            host='localhost',
            database='wegmans',
            user='abhijith_user',
            password='Abhi@1212'
        )
        
        cursor = connection.cursor()
        cursor.executemany(
            "INSERT INTO products (name, price, url, is_active) VALUES (%s, %s, %s, %s)",
            [(name, price, url, True) for name, price, url in product_info]
        )
        connection.commit()
        print("Data processed and stored in the database")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

process_data()
