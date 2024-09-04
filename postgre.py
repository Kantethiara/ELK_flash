import psycopg2
import csv
import pandas as pd



def get_postgres_data():
    try:
        conn = psycopg2.connect(
        user="postgres",          # Remplacez par votre nom d'utilisateur PostgreSQL
        password="root",     # Remplacez par votre mot de passe PostgreSQL
        host="127.0.0.1",
        port="5432",
        database="jobscrap"
    )

     
        cursor = conn.cursor()
        
        # Exécuter une requête pour récupérer les données
        query = "SELECT title, company, location, description, url FROM job_offers"
        cursor.execute(query)
        
        # Récupérer les données
        rows = cursor.fetchall()
        
        # Fermer la connexion
        cursor.close()
        conn.close()
        
        return rows
    
    except Exception as e:
        print(f"Erreur de connexion PostgreSQL: {e}")
        return []

def save_to_csv(data, file_name):
    if data:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Company', 'Location', 'Description', 'URL'])
            writer.writerows(data)
        print(f"Les données ont été sauvegardées dans '{file_name}'.")
    else:
        print("Aucune donnée à sauvegarder.")

if __name__ == "__main__":
    data = get_postgres_data()
    save_to_csv(data, 'job_offers.csv')
