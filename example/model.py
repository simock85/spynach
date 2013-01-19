from ming import schema
from ming.odm import FieldProperty
from ming.odm.declarative import MappedClass
from spynach.mongo_session import DBSession
from hashlib import sha256

class User(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'users'
        unique_indexes = [('name', )]

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String)
    _password = FieldProperty(schema.String)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = sha256(value).hexdigest()