# Projet ELK pour la Gestion des Offres d'Emploi

## Description

Ce projet utilise la pile ELK (Elasticsearch, Logstash, Kibana) pour la gestion et la visualisation des données d'offres d'emploi. Initialement, Logstash devait être utilisé pour ingérer et transformer les données, mais en raison de problèmes de configuration, nous avons remplacé Logstash par un script Python personnalisé. Ce script se charge de l'ingestion des données dans Elasticsearch.

L'application Flask fournit une interface de recherche pour les offres d'emploi, et les résultats sont affichés de manière conviviale. L'interface de gestion du tableau de bord est accessible via Kibana.

## Technologies Utilisées

- **Elasticsearch** : Moteur de recherche et d'analyse.
- **Logstash** (Remplacé) : Outil d'ingestion et de transformation des données. Remplacé par un script Python pour simplifier le processus.
- **Kibana** : Interface de visualisation des données.
- **Flask** : Framework web utilisé pour créer l'application de recherche.
- **Docker** : Conteneurisation des services pour une installation simplifiée et une portabilité accrue.
- **Python** : Langage utilisé pour remplacer Logstash avec un script d'ingestion.

## Prérequis

- Docker et Docker Compose installés sur votre machine.

## Installation et Démarrage

### Étape 1: Cloner le dépôt

```bash
git clone https://github.com/username/nom-du-projet.git
cd nom-du-projet
```

### Étape 2: Démarrer les services avec Docker

Le projet est entièrement conteneurisé avec Docker. Pour démarrer Elasticsearch, Kibana et l'application Flask, exécutez :

```bash
docker-compose up -d
```

Cela démarrera les services suivants :

- Elasticsearch sur `http://localhost:9200`
- Kibana sur `http://localhost:5601`
- Application Flask sur `http://localhost:5000`

### Étape 3: Accéder au Tableau de Bord Kibana

Une fois les services démarrés, vous pouvez accéder au tableau de bord Kibana via le lien suivant :

[Accéder au Tableau de Bord Kibana](http://localhost:5601/app/dashboards#/view/4ae46299-b8c1-4589-a964-535f55145b32?_g=(refreshInterval%3A(pause%3A!t%2Cvalue%3A60000)%2Ctime%3A(from%3Anow-15m%2Cto%3Anow)))

### Étape 4: Utilisation de l'Application Flask

L'application Flask fournit une interface utilisateur pour rechercher dans les offres d'emploi. Pour y accéder, ouvrez votre navigateur et rendez-vous sur :

[http://localhost:5000](http://localhost:5000)

### Étape 5: Remplacement de Logstash par un Script Python

Le script Python (`ingestion_script.py`) remplace Logstash pour l'ingestion des données dans Elasticsearch. Ce script traite les données en les formatant et en les envoyant à Elasticsearch.

Pour exécuter le script d'ingestion :

```bash
python ingestion_script.py
```

## Structure du Projet

- **/app** : Contient l'application Flask.
- **/scripts** : Contient le script Python pour l'ingestion des données.
- **/docker-compose.yml** : Fichier Docker Compose pour gérer les services.
- **/static** : Contient les fichiers CSS et autres fichiers statiques pour l'application Flask.
- **/templates** : Contient les fichiers HTML pour l'application Flask.

## Problèmes Connus

- **Logstash** : Des difficultés avec la configuration de Logstash ont conduit à son remplacement par un script Python personnalisé. Ce script est plus simple à configurer et offre une flexibilité accrue pour l'ingestion des données.

## Contribuer

Les contributions sont les bienvenues! Veuillez soumettre une pull request pour toute amélioration ou suggestion.

