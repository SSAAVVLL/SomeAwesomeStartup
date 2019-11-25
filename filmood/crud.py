from filmood import db
from flask import request, abort

class CRUD:
    @classmethod
    def get(cls, id):
        """
        This function back record from DB by PK

        Parameters:
        ----------
        cls: entity which will be used in action
        id: PK of target record on DB

        Returns:
        ---------
        String
            if record has being founded, returns instance in
            json interpretation

        Raises
        ---------
        KeyError
            raise Error 404 if record not exist
        """
        instance = cls.query.filter_by(id=id).first()
        return instance.to_json() if instance else abort(404)

    @classmethod
    def delete(cls, id):
        """
            This function delete record from DB by PK

            Parameters:
             ----------
             cls: entity which will be used in action
             id: PK of target record on DB

             Returns:
             ---------
             String
                 if record has being deleted, returns instance in
                 json interpretation

            Raises
            ---------
            KeyError
                raise Error 404 if record not exist
        """
        instance = cls.query.filter_by(id=id).first()
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return instance.to_json()
        return abort(404)

    @classmethod
    def update(cls, id, params):
        """
            This function update record in DB by PK

            Parameters:
            ----------
            cls: entity which will be used in action
            id: PK of target record on DB
            params: PLEASE STAND BY

            Returns:
            ---------
            String
                if record has being updated, returns instance in
                json interpretation

            Raises
            ---------
            KeyError
                raise Error 400 if record not exist or received not marked in mapping argument
        """
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
        """
            This function insert record to DB

            Parameters:
             ----------
             cls: entity which will be used in action
             params: PLEASE STAND BY

             Returns:
             ---------
             String
                 if record has being inserted, returns instance in
                 json interpretation

            Raises
            ---------
            KeyError
                raise Error 400 if received arguments not given or stem not marked in entity mapping
        """
        if not params:
            abort(400)

        for param in params:
            if param not in cls.__mapper__.c:
                abort(400)

        instance = cls(**params)
        db.session.add(instance)
        db.session.commit()

        return instance.to_json()
