from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from model import db, Supplier

supplier_nc = Namespace('supplier')

# supplier serializer
supplier_model = supplier_nc.model(
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

@supplier_nc.route("/supplier")
class SuppliersResource(Resource):
    @supplier_nc.marshal_list_with(supplier_model, code = 200)
    def get(self):
        supplier_list = Supplier.query.all()
        return supplier_list, 200
    
    @supplier_nc.marshal_with(supplier_model, code = 200)
    @supplier_nc.expect(supplier_model)
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

@supplier_nc.route("/supplier/<int:id>")
class supplierResource(Resource):
    @supplier_nc.marshal_with(supplier_model, code = 200)
    def get(self, id):
        supplier = Supplier.query.get_or_404(id)
        return supplier, 200
    
    @supplier_nc.marshal_with(supplier_model, code = 200)
    @supplier_nc.expect(supplier_model)
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
    
    @supplier_nc.marshal_with(supplier_model, code = 200)
    def delete(self, id):
        supplier_to_delete = Supplier.query.get_or_404(id)
        db.session.delete(supplier_to_delete)
        db.session.commit()
        return supplier_to_delete, 200
