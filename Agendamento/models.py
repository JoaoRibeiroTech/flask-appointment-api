from Agendamento import database
from datetime import datetime

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String(50), nullable=False)
    
class Appointment(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name =database.Column(database.String, nullable=False)
    start_time = database.Column(database.DateTime, nullable=False, unique=True)
    end_time = database.Column(database.DateTime, nullable=False, unique=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)