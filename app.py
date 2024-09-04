from flask import Flask
from flask_restx import Api
from model import db, Book, Student, Recipe, Post, Comment, Supplier, Users
from flask_migrate import Migrate
from auth import auth_nc
from book import book_ns
from comment import comment_nc
from post import post_nc
from recipe import recipe_nc
from student import student_ns
from supplier import supplier_nc
from flask_jwt_extended import JWTManager

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    JWTManager(app)
    authorization = {
        "jsonWebToken":{
            "type":"apiKey",
            "in": "header",
            "name": "Authorization"
        }
    }
    api = Api(app, version= '2.5', title='Sample API', description='A Sample Flask API', authorizations = authorization)
    api.add_namespace(auth_nc)
    api.add_namespace(book_ns)
    api.add_namespace(comment_nc)
    api.add_namespace(post_nc)
    api.add_namespace(recipe_nc)
    api.add_namespace(student_ns)
    api.add_namespace(supplier_nc)
    
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db, 
            'Book': Book, 
            'Student' : Student, 
            'Recipe' : Recipe, 
            'Post' : Post, 
            'Comment' : Comment,
            'Supplier': Supplier, 
            'Users': Users
            }
    
    return app


