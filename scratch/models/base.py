from extensions import db


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=db.func.current_timestamp()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def select(cls, id):
        return cls.query.get(id)

    @classmethod
    def insert(cls, data):
        new_instance = cls(**data)
        db.session.add(new_instance)
        db.session.commit()
        return new_instance

    @classmethod
    def update(cls, id, data, set_nulls=False):
        instance = cls.query.get(id)
        if not instance:
            return None
        for key, value in data.items():
            if value is not None or set_nulls:
                setattr(instance, key, value)

        db.session.commit()
        return instance


    @classmethod
    def delete(cls, id):
        instance = cls.query.get(id)
        if not instance:
            return None
        db.session.delete(instance)
        db.session.commit()
