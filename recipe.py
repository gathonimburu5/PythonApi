from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Recipe

recipe_nc = Namespace('recipe')

# recipe serializer
recipe_model = recipe_nc.model(
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

@recipe_nc.route("/recipes")
class RecipesResource(Resource):
    @recipe_nc.marshal_list_with(recipe_model, code = 200, envelope = "recipes")
    def get(self):
        recipe_list = Recipe.query.all()
        return recipe_list, 200

    @recipe_nc.marshal_with(recipe_model, code = 200, envelope = "recipe")
    @recipe_nc.expect(recipe_model)
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

@recipe_nc.route("/recipes/<int:id>")
class RecipeResource(Resource):
    @recipe_nc.marshal_with(recipe_model, code = 200)
    def get(self, id):
        recipe = Recipe.query.get_or_404(id)
        return recipe, 200

    @recipe_nc.marshal_with(recipe_model, code = 200)
    @recipe_nc.expect(recipe_model)
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

    @recipe_nc.marshal_with(recipe_model, code = 200)
    def delete(self, id):
        recipe_to_delete = Recipe.query.get_or_404(id)
        db.session.delete(recipe_to_delete)
        db.session.commit()
        return recipe_to_delete, 200


