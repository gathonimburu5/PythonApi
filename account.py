from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Accounts

account_ns = Namespace('account')

#account serialization
account_model = account_ns.model(
    'Accounts',
    {
        "Id":fields.Integer(),
        "Name":fields.String(),
        "Group":fields.String(),
        "Currency":fields.String(),
        "StartBalance":fields.Float(),
        "CreatedOn": fields.Date()
    }
)

@account_ns.route("/account")
class AccountsResource(Resource):
    @account_ns.marshal_list_with(account_model, code=200)
    def get(self):
        account_list = Accounts.query.all()
        return account_list, 200

    @account_ns.marshal_with(account_model, code = 200)
    @account_ns.expect(account_model)
    def post(self):
        data = request.get_json()
        new_account = Accounts(
            Name = data.get('Name'),
            Group = data.get('Group'),
            Currency = data.get('Currency'),
            StartBalance = data.get('StartBalance')
        )
        db.session.add(new_account)
        db.session.commit()
        return new_account, 200

@account_ns.route("/account/<int:id>")
class AccountResource(Resource):
    @account_ns.marshal_with(account_model, code=200)
    def get(self, id):
        account = Accounts.query.get_or_404(id)
        return account, 200

    @account_ns.marshal_with(account_model, code=200)
    @account_ns.expect(account_model)
    def put(self, id):
        update_account = Accounts.query.get_or_404(id)
        data = request.get_json()
        update_account.Name = data.get('Name')
        update_account.Group = data.get('Group')
        update_account.Currency = data.get('Currency')
        update_account.StartBalance = data.get('StartBalance')
        db.session.commit()
        return update_account, 200
    
    @account_ns.marshal_with(account_model, code=200)
    def delete(self, id):
        delete_account = Accounts.query.get_or_404(id)
        db.session.delete(delete_account)
        db.session.commit()
        return delete_account, 200
    



