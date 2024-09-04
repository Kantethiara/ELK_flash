from flask import Flask, render_template

from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__, template_folder='templates')

# Configuration de la connexion à Elasticsearch
es = Elasticsearch(
    ["https://localhost:9200"],
    http_auth=("elastic", "49Y5CKCQbX4ofPvuktbo"),
    ssl_show_warn=False,
    verify_certs=False,
    request_timeout=60
)

@app.route('/')
def index():
    return render_template('dashboard.html')

# Route pour gérer les requêtes de recherche
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')

    if not query:
        return jsonify({"error": "Aucun terme de recherche fourni."}), 400

    # Requête de recherche Elasticsearch
    search_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "company", "location", "description"]
            }
        }
    }

    # Exécution de la requête
    response = es.search(index="job_offers", body=search_query)
    
    results = response['hits']['hits']

    return render_template('test.html',query=query, results= results)

if __name__ == '__main__':
    app.run(debug=True)

