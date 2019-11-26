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
        if instance:
            return instance 
        raise ValidationError('Wrong id was given') 

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
        instance = cls.get(id)
        db.session.delete(instance)
        db.session.commit()
        return instance

    @classmethod
    def update(cls, id, **params):
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
        instance = cls.get(id)
        cls.validate_params(params)

        try:
            cls.query.filter_by(id=id).update(params)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValidationError('Invalid data was given') 

        instance = cls.get(id)
        return instance

    @classmethod
    def insert(cls, **params):
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
        cls.validate_params(params)
        
        instance = cls(**params)
        try:
            db.session.add(instance)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValidationError('Invalid data was given') 

        return instance

    @classmethod
    def validate_params(cls, params):
        if not params:
            raise ValidationError('Params were not given') 
            
        for param in params:
            if param not in cls.__mapper__.c and param not in cls.__mapper__.relationships:
                raise ValidationError('Wrong params were given')
