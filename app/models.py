""" App Models """

import os

from flask_admin.contrib.sqla import ModelView
from flask_admin.model import BaseModelView
from flask_admin.form import ImageUploadField
from werkzeug import secure_filename

from . import db
from .config import Config

import enum, datetime
from sqlalchemy.types import Enum

LABEL_NAMES = (
    "Food Preferences",
    "Dietary Requirements",
    "Environmental Impact",
)

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), nullable=False)
    of_type = db.Column(Enum(*LABEL_NAMES, name="Type"), nullable=False)
    icon = db.Column(db.String(256))
    def __repr__(self):
        return self.name
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'of_type': LABEL_NAME_EN[self.of_type],
            'labels': [ l.dict() for l in self.labels ],
        }

label_meal = db.Table(
    'label_meal',
    db.Column('label_id', db.Integer(), db.ForeignKey('label.id')),
    db.Column('meal_id', db.Integer(), db.ForeignKey('meal.id'))
)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(256))
    created = db.Column(db.DateTime(), default=datetime.datetime.now())
    labels = db.relationship('Label', secondary=label_meal,
        backref=db.backref('meals', lazy='dynamic'))
    def __repr__(self):
        return str(self.created)
    def thumb(self):
        if not self.photo: return None
        name, _ = ospath.splitext(self.photo)
        return '/photos/' + secure_filename('%s_thumb.jpg' % name)
    def dict(self):
        return {
            'id': self.id,
            'created': self.created,
            'photo': self.photo,
            'thumbnail': self.thumb(),
            'labels': [ l.dict() for l in self.labels ],
        }

class MealView(ModelView):
    column_list = ('created', 'labels')
    form_extra_fields = {
        'photo': ImageUploadField('Photo',
            base_path=Config.PHOTO_PATH,
            url_relative_path='photos/',
            thumbnail_size=(256, 256, True))
    }
    can_export = True