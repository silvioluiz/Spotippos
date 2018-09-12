import click
from app import db
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    return db

def close_db(e=None):
    print('close_db')

def init_db():
    db.create_all()