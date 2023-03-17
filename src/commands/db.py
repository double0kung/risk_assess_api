from app import db
from flask import Blueprint
from model.users_model import User

db_cmd = Blueprint("db", __name__)

@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print('Database Created')


@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Database Deleted')


@db_cmd.cli.command('seed')
def seed_db():
    # Create some test users
    user1 = User(email='godofthunder@eavengers.com', first_name='Thor', last_name='Odinson', password='strongestavenger')
    user2 = User(email='captainamerica@avengers.com', first_name='Steve', last_name='Rogers', password='americasass')
    user3 = User(email='ironman@avengers.com', first_name='Tony', last_name='Stark', password='i.am.ironman')

    # Add users to the database
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Commit the changes
    db.session.commit()

    print('Database seeded with test users')




