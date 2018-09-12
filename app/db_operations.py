import click
from app import db
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    return db

def close_db(e=None):
    print('EM TESE session é fechada ao fechar o request')
    

def init_db():
    db.create_all()