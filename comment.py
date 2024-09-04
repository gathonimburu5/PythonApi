from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Comment

comment_nc = Namespace('comment')

# comment serializer
comment_model = comment_nc.model(
    'Comment',
    {
        'Id': fields.Integer(),
        'Contents': fields.String(),
        'PostId': fields.Integer(),
        'CreatedOn': fields.Date()
    }
)

@comment_nc.route("/comments")
class CommentsResource(Resource):
    @comment_nc.marshal_list_with(comment_model, code = 200)
    def get(self):
        comment_list = Comment.query.all()
        return comment_list, 200
    
    @comment_nc.marshal_with(comment_model, code = 200)
    @comment_nc.expect(comment_model)
    def post(self):
        data = request.get_json()
        new_comment = Comment(Contents = data.get('Contents'), PostId = data.get('PostId'))
        db.session.add(new_comment)
        db.session.commit()
        return new_comment, 200

@comment_nc.route("/comment/<int:id>")
class CommentResource(Resource):
    @comment_nc.marshal_with(comment_model, code = 200)
    def get(self, id):
        comment = Comment.query.get_or_404(id)
        return comment, 200
    
    @comment_nc.marshal_with(comment_model, code = 200)
    @comment_nc.expect(comment_model)
    def put(self, id):
        comment_to_update = Comment.query.get_or_404()
        data = request.get_json()
        comment_to_update.Contents = data.get('Contents')
        comment_to_update.PostId = data.get('PostId')   
        db.session.commit()
        return comment_to_update, 200   

    @comment_nc.marshal_with(comment_model, code = 200)
    def delete(self, id):
        comment_to_delete = Comment.query.get_or_404(id)
        db.session.delete(comment_to_delete)
        db.session.commit()
        return comment_to_delete, 200
