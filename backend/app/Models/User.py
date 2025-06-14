import mongoengine as me

class User(me.Document):
    Name = me.StringField(required=True)
    Email = me.EmailField(required=True, unique=True)
    Password = me.StringField(required=True)