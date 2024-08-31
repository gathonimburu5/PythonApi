from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from model import db, Book, Student, Recipe, Post, Comment, Supplier
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

api = Api(app, version= '2.5', title='Sample API', description='A Sample Flask API')
    
# book serializer
book_model = api.model(
    'Book',
    {
        'Id':fields.Integer(),
        'Tittle':fields.String(),
        'Author':fields.String(),
        'DateCreated': fields.Date()
    }
)
# student serializer
student_model = api.model(
    'Student',
    {
        'Id':fields.Integer(),
        'FullNames':fields.String(),
        'EmailAddress': fields.String(),
        'Phone':fields.String(),
        'Address':fields.String(),
        'County': fields.String(),
        'CreatedOn': fields.Date()
    }
)
# recipe serializer
recipe_model = api.model(
    'Recipe',
    {
        'Id':fields.Integer(),
        'Tittle':fields.String(),
        'Details':fields.String(),
        'Review':fields.String(),
        'Status':fields.String(),
        'Category':fields.String(),
        'CreatedOn':fields.Date()
    }
)
# post serializer
post_model = api.model(
    'Post',
    {
        'Id': fields.Integer(),
        'Tittle': fields.String(),
        'Description': fields.String(),
        'CreatedOn': fields.Date()
    }
)
# comment serializer
comment_model = api.model(
    'Comment',
    {
        'Id': fields.Integer(),
        'Contents': fields.String(),
        'PostId': fields.Integer(),
        'CreatedOn': fields.Date()
    }
)
# supplier serializer
supplier_model = api.model(
    'Supplier',
    {
        'Id': fields.Integer(),
        'SupplierName': fields.String(),
        'EmailAddress': fields.String(),
        'PhoneNumber': fields.String(),
        'DateOfBirth': fields.Date(),
        'PostalAddress': fields.String(),
        'Address': fields.String(),
        'County': fields.String(),
        'SubCounty': fields.String(),
        'CreatedOn': fields.Date()
    }
)

@api.route("/supplier")
class SuppliersResource(Resource):
    @api.marshal_list_with(supplier_model, code = 200)
    def get(self):
        supplier_list = Supplier.query.all()
        return supplier_list, 200
    
    @api.marshal_with(supplier_model, code = 200)
    @api.expect(supplier_model)
    def post(self):
        data = request.get_json()
        supplier_data = Supplier(
            SupplierName = data.get('SupplierName'),
            EmailAddress = data.get('EmailAddress'),
            PhoneNumber = data.get('PhoneNumber'),
            DateOfBirth = data.get('DateOfBirth'),
            PostalAddress = data.get('PostalAddress'),
            Address = data.get('Address'),
            County = data.get('County'),
            SubCounty = data.get('SubCounty')
        )
        db.session.add(supplier_data)
        db.session.commit()
        return supplier_data, 200

@api.route("/supplier/<int:id>")
class supplierResource(Resource):
    @api.marshal_with(supplier_model, code = 200)
    def get(self, id):
        supplier = Supplier.query.get_or_404(id)
        return supplier, 200
    
    @api.marshal_with(supplier_model, code = 200)
    @api.expect(supplier_model)
    def put(self, id):
        supplier_to_update = Supplier.query.get_or_404(id)
        data = request.get_json()
        supplier_to_update.SupplierName = data.get('SupplierName')
        supplier_to_update.EmailAddress = data.get('EmailAddress')
        supplier_to_update.PhoneNumber = data.get('PhoneNumber')
        supplier_to_update.DateOfBirth = data.get('DateOfBirth')
        supplier_to_update.PostalAddress = data.get('PostalAddress')
        supplier_to_update.Address = data.get('Address')
        supplier_to_update.County = data.get('County')
        supplier_to_update.SubCounty = data.get('SubCounty')
        db.session.commit()
        return supplier_to_update, 200
    
    @api.marshal_with(supplier_model, code = 200)
    def delete(self, id):
        supplier_to_delete = Supplier.query.get_or_404(id)
        db.session.delete(supplier_to_delete)
        db.session.commit()
        return supplier_to_delete, 200

@api.route("/comments")
class CommentsResource(Resource):
    @api.marshal_list_with(comment_model, code = 200)
    def get(self):
        comment_list = Comment.query.all()
        return comment_list, 200
    
    @api.marshal_with(comment_model, code = 200)
    @api.expect(comment_model)
    def post(self):
        data = request.get_json()
        new_comment = Comment(Contents = data.get('Contents'), PostId = data.get('PostId'))
        db.session.add(new_comment)
        db.session.commit()
        return new_comment, 200

@api.route("/comment/<int:id>")
class CommentResource(Resource):
    @api.marshal_with(comment_model, code = 200)
    def get(self, id):
        comment = Comment.query.get_or_404(id)
        return comment, 200
    
    @api.marshal_with(comment_model, code = 200)
    @api.expect(comment_model)
    def put(self, id):
        comment_to_update = Comment.query.get_or_404()
        data = request.get_json()
        comment_to_update.Contents = data.get('Contents')
        comment_to_update.PostId = data.get('PostId')   
        db.session.commit()
        return comment_to_update, 200   

    @api.marshal_with(comment_model, code = 200)
    def delete(self, id):
        comment_to_delete = Comment.query.get_or_404(id)
        db.session.delete(comment_to_delete)
        db.session.commit()
        return comment_to_delete, 200

@api.route("/posts")
class PostsResource(Resource):
    @api.marshal_list_with(post_model, code = 200, envelope = "posts")
    def get(self):
        post_list = Post.query.all()
        return post_list, 200
    
    @api.marshal_with(post_model, code = 200)
    @api.expect(post_model)
    def post(self):
        data = request.get_json()
        new_post = Post(Tittle = data.get('Tittle'), Description = data.get('Description'))
        db.session.add(new_post)
        db.session.commit()
        return new_post, 200
    
@api.route("/posts/<int:id>")
class PostResource(Resource):
    @api.marshal_with(post_model, code = 200)
    def get(self, id):
        post = Post.query.get_or_404(id)
        return post, 200
    
    @api.marshal_with(post_model, code = 200)
    @api.expect(post_model)
    def put(self, id):
        post_to_update = Post.query.get_or_404(id)
        data = request.get_json()
        post_to_update.Tittle = data.Tittle
        post_to_update.Description = data.Description

        db.session.commit()
        return post_to_update, 200
    
    @api.marshal_with(post_model, code = 200)
    def delete(self, id):
        post_to_delete = Post.query.get_or_404(id)
        
        db.session.delete(post_to_delete)
        db.session.commit()
        return post_to_delete, 200

@api.route("/recipes")
class RecipesResource(Resource):
    @api.marshal_list_with(recipe_model, code = 200, envelope = "recipes")
    def get(self):
        recipe_list = Recipe.query.all()
        return recipe_list, 200

    @api.marshal_with(recipe_model, code = 200, envelope = "recipe")
    @api.expect(recipe_model)
    def post(self):
        data = request.get_json()
        tittle = data.get('Tittle')
        detail = data.get('Details')
        review = data.get('Review')
        status = data.get('Status')
        category = data.get('Category')

        new_recipe = Recipe(Tittle = tittle, Details = detail, Review = review, Status = status, Category = category)
        db.session.add(new_recipe)
        db.session.commit()
        return new_recipe, 200

@api.route("/recipes/<int:id>")
class RecipeResource(Resource):
    @api.marshal_with(recipe_model, code = 200)
    def get(self, id):
        recipe = Recipe.query.get_or_404(id)
        return recipe, 200

    @api.marshal_with(recipe_model, code = 200)
    @api.expect(recipe_model)
    def put(self, id):
        recipe_to_update = Recipe.query.get_or_404(id)
        data = request.get_json()
        recipe_to_update.Tittle = data.get('Tittle')
        recipe_to_update.Details = data.get('Details')
        recipe_to_update.Review = data.get('Review')
        recipe_to_update.Status = data.get('Status')
        recipe_to_update.Category = data.get('Category')

        db.session.commit()
        return recipe_to_update, 200 

    @api.marshal_with(recipe_model, code = 200)
    def delete(self, id):
        recipe_to_delete = Recipe.query.get_or_404(id)
        db.session.delete(recipe_to_delete)
        db.session.commit()
        return recipe_to_delete, 200

@api.route("/students")
class Students(Resource):
    @api.marshal_list_with(student_model, code = 200, envelope = "students")
    def get(self):
        students = Student.query.all()
        # studen = text(""" select * from student  """)
        return students, 200 
    
    @api.marshal_with(student_model, code = 200, envelope = "student")
    def post(self):
        data = request.get_json()
        fullName = data.get('FullNames')
        emailAddress = data.get('EmailAddress')
        phone = data.get('Phone')
        address = data.get('Address')
        county = data.get('County')

        new_student = Student(FullNames = fullName, EmailAddress = emailAddress, Phone = phone, Address = address, County = county)
        db.session.add(new_student)
        db.session.commit()
        return new_student, 200

@api.route("/students/<int:id>")
class StudentsResource(Resource):
    @api.marshal_with(student_model, code = 200, envelope = "student")
    def get(self, id):
        student = Student.query.get_or_404(id)
        return student, 200
    
    @api.marshal_with(student_model, code = 200, envelope = "student")
    def put(self, id):
        student_to_update = Student.query.get_or_404(id)
        data = request.get_json()
        student_to_update.FullNames = data.get('FullNames')
        student_to_update.EmailAddress = data.get('EmailAddress')
        student_to_update.Phone = data.get('Phone')
        student_to_update.Address = data.get('Address')
        student_to_update.County = data.get('County')

        db.session.commit()
        return student_to_update, 200

    @api.marshal_with(student_model, code = 200, envelope = "student")
    def delete(self, id):
        student_to_delete = Student.query.get_or_404(id)
        db.session.delete(student_to_delete)
        db.session.commit()
        return student_to_delete, 200

@api.route("/books")
class Books(Resource):
    @api.marshal_list_with(book_model, code= 200, envelope = "books")
    def get(self):
        books = Book.query.all()
        return books
    @api.marshal_with(book_model, code = 200, envelope = "book")
    @api.doc(params = {"Tittle":"enter tittle", "Author": "enter an author"})
    def post(self):
        data = request.get_json()
        tittle = data.get('Tittle')
        author = data.get('Author')
        new_book = Book(Tittle = tittle, Author = author)
        db.session.add(new_book)
        db.session.commit()
        return new_book, 200

@api.route("/books/<int:id>")
class BooksResource(Resource):
    @api.marshal_with(book_model, code = 200, envelope = "book")
    def get(self, id):
        book = Book.query.get_or_404(id)
        return book, 200
    
    @api.marshal_with(book_model, code = 200, envelope = "book")
    def put(self, id):
        book_to_update = Book.query.get_or_404(id)
        data = request.get_json()
        book_to_update.Tittle = data.get('Tittle')
        book_to_update.Author = data.get('Author')
        db.session.commit()
        return book_to_update, 200

    @api.marshal_with(book_model, code = 200, envelope = "book")
    def delete(self, id):
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return book_to_delete, 200

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book, 'Student' : Student, 'Recipe' : Recipe, 'Post' : Post, 'Comment' : Comment, 'Supplier': Supplier}

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=8888)
