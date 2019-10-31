from filmood import db
from flask import request, abort

class CRUD:
    @classmethod
    def get(cls, id):
        instance = cls.query.filter_by(id=id).first()
        return instance.to_json() if instance else abort(404)

    @classmethod
    def delete(cls, id):
        instance = cls.query.filter_by(id=id).first()
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return instance.to_json()
        return abort(404)

    @classmethod
    def update(cls, id, params):
        instance = cls.query.filter_by(id=id).first()
        if not instance or not params:
            abort(400)

        for param in params:
            if param not in cls.__mapper__.c:
                abort(400)

        cls.query.filter_by(id=id).update(params)
        db.session.commit()

        instance = cls.query.filter_by(id=id).first()
        return instance.to_json()

    @classmethod
    def insert(cls, params):
        if not params:
            abort(400)

        for param in params:
            if param not in cls.__mapper__.c:
                abort(400)

        instance = cls(**params)
        db.session.add(instance)
        db.session.commit()

        return instance.to_json()
