from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Customer

customer_ns = Namespace('Customer')
#customer serialzer
customer_model = customer_ns.model(
    'Customer',
    {
        "Id":fields.Integer(),
        "Code":fields.String(),
        "CustomerName":fields.String(),
        "EmailAddress":fields.String(),
        "PhoneNumber":fields.String(),
        "PostalAddress":fields.String(),
        "Address":fields.String(),
        "CreatedOn":fields.Date()
    }
)

@customer_ns.route("/customer")
class CustomersResource(Resource):
    @customer_ns.marshal_list_with(customer_model, code=200)
    def get(self):
        customer_list = Customer.query.all()
        return customer_list, 200

    @customer_ns.marshal_with(customer_model, code=200)
    @customer_ns.expect(customer_model)
    def post(self):
        data = request.get_json()
        new_customer = Customer(
            Code = data.get('Code'),
            CustomerName = data.get('CustomerName'),
            EmailAddress = data.get('EmailAddress'),
            PhoneNumber = data.get('PhoneNumber'),
            PostalAddress = data.get('PostalAddress'),
            Address = data.get('Address')
        )
        db.session.add(new_customer)
        db.session.commit()
        return new_customer, 200

@customer_ns.route("/customer/<int:id>")
class CustomerResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass