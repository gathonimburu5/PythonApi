from flask import request, jsonify
from flask_restx import Namespace, fields, Resource
from model import db, Book
from flask_jwt_extended import jwt_required

book_ns = Namespace('book')

# book serializer
book_model = book_ns.model(
    'Book',
    {
        'Id':fields.Integer(),
        'Tittle':fields.String(),
        'Author':fields.String(),
        'DateCreated': fields.Date()
    }
)

@book_ns.route("/books")
class Books(Resource):    
    method_decorators = [jwt_required()]
    @book_ns.marshal_list_with(book_model, code= 200, envelope = "books")
    @jwt_required()
    @book_ns.doc(security = "jsonWebToken")
    def get(self):
        books = Book.query.all()
        return books
    
    
    method_decorators = [jwt_required()]
    @book_ns.marshal_with(book_model, code = 200, envelope = "book")
    @book_ns.doc(params = {"Tittle":"enter tittle", "Author": "enter an author"})
    @jwt_required()
    @book_ns.doc(security = "jsonWebToken")
    def post(self):
        data = request.get_json()
        tittle = data.get('Tittle')
        author = data.get('Author')
        new_book = Book(Tittle = tittle, Author = author)
        db.session.add(new_book)
        db.session.commit()
        return new_book, 200

@book_ns.route("/books/<int:id>")
class BooksResource(Resource):
    method_decorators = [jwt_required()]
    @book_ns.marshal_with(book_model, code = 200, envelope = "book")
    @jwt_required()
    @book_ns.doc(security = "jsonWebToken")
    def get(self, id):
        book = Book.query.get_or_404(id)
        return book, 200
    
    
    method_decorators = [jwt_required()]
    @book_ns.marshal_with(book_model, code = 200, envelope = "book")
    @jwt_required()
    @book_ns.doc(security = "jsonWebToken")
    def put(self, id):
        book_to_update = Book.query.get_or_404(id)
        data = request.get_json()
        book_to_update.Tittle = data.get('Tittle')
        book_to_update.Author = data.get('Author')
        db.session.commit()
        return book_to_update, 200

    
    method_decorators = [jwt_required()]
    @book_ns.marshal_with(book_model, code = 200, envelope = "book")
    @jwt_required()
    @book_ns.doc(security = "jsonWebToken")
    def delete(self, id):
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return book_to_delete, 200
