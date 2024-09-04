from elasticsearch import Elasticsearch, helpers
import csv

# Fonction pour se connecter à Elasticsearch et insérer les données
def load_data_to_elasticsearch(csv_file, index_name):
    try:
        es = Elasticsearch(
            ["https://localhost:9200"],
            http_auth=("elastic", "49Y5CKCQbX4ofPvuktbo"),
            ssl_show_warn=False,  # Ignorer les avertissements SSL
            verify_certs=False,  # Ne pas vérifier les certificats SSL
            request_timeout=60
        )

        # Créer l'index si nécessaire
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)
            print(f"Index '{index_name}' créé.")

        actions = []
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                action = {
                    "_index": index_name,
                    "_source": {
                        "title": row['Title'],
                        "company": row['Company'],
                        "location": row['Location'],
                        "description": row['Description'],
                        "url": row['URL']
                    }
                }
                actions.append(action)

        # Insertion en masse des documents dans Elasticsearch
        helpers.bulk(es, actions)
        print(f"Les données ont été insérées dans l'index '{index_name}' avec succès.")

    except Exception as e:
        print(f"Erreur lors de l'insertion des données dans Elasticsearch: {e}")

if __name__ == "__main__":
    load_data_to_elasticsearch('job_offers.csv', 'job_offers')
