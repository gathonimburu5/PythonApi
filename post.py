from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Post

post_nc = Namespace('post')

# post serializer
post_model = post_nc.model(
    'Post',
    {
        'Id': fields.Integer(),
        'Tittle': fields.String(),
        'Description': fields.String(),
        'CreatedOn': fields.Date()
    }
)

@post_nc.route("/posts")
class PostsResource(Resource):
    @post_nc.marshal_list_with(post_model, code = 200, envelope = "posts")
    def get(self):
        post_list = Post.query.all()
        return post_list, 200
    
    @post_nc.marshal_with(post_model, code = 200)
    @post_nc.expect(post_model)
    def post(self):
        data = request.get_json()
        new_post = Post(Tittle = data.get('Tittle'), Description = data.get('Description'))
        db.session.add(new_post)
        db.session.commit()
        return new_post, 200
    
@post_nc.route("/posts/<int:id>")
class PostResource(Resource):
    @post_nc.marshal_with(post_model, code = 200)
    def get(self, id):
        post = Post.query.get_or_404(id)
        return post, 200
    
    @post_nc.marshal_with(post_model, code = 200)
    @post_nc.expect(post_model)
    def put(self, id):
        post_to_update = Post.query.get_or_404(id)
        data = request.get_json()
        post_to_update.Tittle = data.Tittle
        post_to_update.Description = data.Description

        db.session.commit()
        return post_to_update, 200
    
    @post_nc.marshal_with(post_model, code = 200)
    def delete(self, id):
        post_to_delete = Post.query.get_or_404(id)
        
        db.session.delete(post_to_delete)
        db.session.commit()
        return post_to_delete, 200
