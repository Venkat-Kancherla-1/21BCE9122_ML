# app/__init__.py
from flask import Flask
from pymongo import MongoClient
import redis
from threading import Thread
from .scraper import scrape_articles

client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client['document_db']  # Use your database name

def create_app():
    app = Flask(__name__)

    # Redis for caching
    cache = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Register routes
    from .routes import routes
    app.register_blueprint(routes)

    # Start scraper in a separate thread
    Thread(target=scrape_articles, daemon=True).start()

    return app, cache
