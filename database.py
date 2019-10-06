from peewee import *

db = SqliteDatabase('artworkCatalog.sqlite', pragmas={
    'foreign_keys': 1,
})

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

class Artwork(Model):
    artist = ForeignKeyField(Artist)
    artwork = CharField()
    price = IntegerField()
    availability = CharField()

    class Meta:
        database = db

db.connect
db.create_tables([Artist, Artwork])
