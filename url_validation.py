import requests
import mysql.connector
from mysql.connector import Error

def validate_urls():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='wegmans',
            user='abhijith_user',
            password='Abhi@1212'
        )
        cursor = connection.cursor()
        
        cursor.execute("SELECT id, url FROM products")
        urls = cursor.fetchall()

        for id, url in urls:
            try:
                response = requests.get(url)
                is_active = response.status_code == 200
            except requests.RequestException:
                is_active = False

            cursor.execute(
                "UPDATE products SET is_active = %s WHERE id = %s",
                (is_active, id)
            )
        
        connection.commit()
        print("URL validation completed")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
validate_urls()
