from flask import jsonify, abort, request
from models import *

@app.route('/methods/getContact/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    if contact:
        return jsonify(contact.to_dict())
    abort(400)

@app.route('/methods/deleteContact/<int:contact_id>', methods=['GET'])
def delete_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    if contact:
        db.session.delete(contact)
        db.session.commit()
    abort(400)

@app.route('/methods/createContact', methods=['POST'])
def create_contact():
    params = request.args
    if not params and ('firstname' in params and 'phone' in params) :
        abort(400)
    for param in params:
        if param not in Contact.__mapper__.c:
            abort(400)

    contact = Contact(**params)
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.to_dict())

@app.route('/methods/updateContact', methods=['POST'])
def update_contact():
    params = request.args
    if not params and 'id' not in params:
        abort(400)

    for param in params:
        if param not in Contact.__mapper__.c:
            abort(400)

    Contact.query.filter_by(id=params['id']).update(params)
    contact = Contact.query.filter_by(id=params['id']).first()
    db.session.commit()
    return jsonify(contact.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
