from flask import Flask
from flask_restx import Api
from model import db, Book, Student, Recipe, Post, Comment, Supplier, Users, Accounts
from flask_migrate import Migrate
from auth import auth_nc
from book import book_ns
from comment import comment_nc
from post import post_nc
from recipe import recipe_nc
from student import student_ns
from supplier import supplier_nc
from account import account_ns
from flask_jwt_extended import JWTManager
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
app.config["JWT_SECRET_KEY"] = "f18923792ddcc0ce0d7a8e5b"
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
    
api = Api(app, version= '2.0', title='Flask RestX API Sample', authorizations = authorization)
api.add_namespace(auth_nc)
api.add_namespace(book_ns)
api.add_namespace(comment_nc)
api.add_namespace(post_nc)
api.add_namespace(recipe_nc)
api.add_namespace(student_ns)
api.add_namespace(supplier_nc)
api.add_namespace(account_ns)
    
@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'Book': Book, 'Student' : Student, 'Recipe' : Recipe, 'Post' : Post, 'Comment' : Comment, 'Supplier': Supplier, 'Users': Users, 'Accounts': Accounts }
        

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=8888)

