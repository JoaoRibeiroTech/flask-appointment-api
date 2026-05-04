from Agendamento import database
from datetime import datetime

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String(50), nullable=False)
    appointments = database.relationship('Appointment', backref='user', lazy=True)
    
class Appointment(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name =database.Column(database.String, nullable=False)
    start_time = database.Column(database.DateTime, nullable=False)
    end_time = database.Column(database.DateTime, nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)