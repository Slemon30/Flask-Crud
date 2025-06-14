from flask import Flask, jsonify
from mongoengine import connect
from app.Routes.UserRoutes import routes

def create_app():
    app = Flask(__name__)
    
    try: 
        connect(host = "mongodb://mongo:27017/Flask-CRUD")
        print("Connected to DB")
        app.register_blueprint(routes)
        return app
    except:
        return jsonify({"error": "Failed to connect to DB..."})
