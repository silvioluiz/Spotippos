import os
import pytest
import tempfile

from app import create_app
from app.db_operations import init_db

@pytest.fixture
def app():
    
    app = create_app('Test')
    db_fd, temp_path = tempfile.mkstemp()
   
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(temp_path)

    with app.app_context():
        init_db()
        
    yield app

    os.close(db_fd)
    os.unlink(temp_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
