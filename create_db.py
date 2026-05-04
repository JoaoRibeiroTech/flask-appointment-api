from Agendamento import app, database
from Agendamento.models import Usuario, Appointment

#Criação do DB ao invés de rodar no 'flask shell' no terminal
with app.app_context():
    database.create_all()