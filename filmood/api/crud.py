from filmood import db
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError

class CRUD:
    @classmethod
    def get(cls, id):
        """Get instance of entity by id.

        Args:
            cls: class of the entity.
            id (int): id of instance.

        Returns:
            obj: If instance has been found, return it.

        Raises:
            ValidationError: If instance hasn't been found.
        """
        instance = cls.query.filter_by(id=id).first()
        if instance:
            return instance
        raise ValidationError('Wrong id was given')

    @classmethod
    def delete(cls, id):
        """Delete instance of entity by id.

            Args:
                cls: class of the entity.
                id (int): id of instance.

            Returns:
                obj: If instance has been found, delete and return it.
        """
        instance = cls.get(id)
        db.session.delete(instance)
        db.session.commit()
        return instance

    @classmethod
    def update(cls, id, **params):
        """Update instance of entity by id.

            Args:
                cls: class of the entity.
                id (int): id of instance.
                **params: keyword params of instance of entity that must be updated.

            Returns:
                obj: updated instance of entity.

            Raises:
                ValidationError: If given data was invalid.
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
        """Insert instance of entity

            Args:
                cls: class of the entity.
                **params: keyword params of instance of entity that must be updated.

            Returns:
                obj: inserted instance of entity.

            Raises:
                ValidationError: If given data was invalid.
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
        """Check are there params and are they valid.

        Args:
            cls: class of the entity.
            params (dict): dict of params.

        Raises:
            ValidationError: If there are no params or given params are wrong.
        """
        if not params:
            raise ValidationError('Params were not given') 
            
        for param in params:
            if param not in cls.__mapper__.c and param not in cls.__mapper__.relationships:
                raise ValidationError('Wrong params were given')

