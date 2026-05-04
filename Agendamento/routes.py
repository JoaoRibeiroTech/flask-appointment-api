from Agendamento import app, database
from flask_login import login_user, logout_user, login_manager
from email_validator import validate_email, EmailNotValidError
from flask import request, jsonify
from Agendamento.utils import hash_password, check_password, send_email
from Agendamento.models import User, Appointment
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@login_manager.user_loader
def load_user(id_usuario):
    return User.query.get(int(id_usuario))

@app.route('/users', methods=['POST'])
def users():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'message':'Invalid Data'}), 400
        
    hashed_password = hash_password(password)
    
    try:
        valid = validate_email(email)
        email_valid = valid.email
    except EmailNotValidError as e:
        return jsonify({'message': str(e)}), 400
    
    user = User(
        email=email_valid,
        password=hashed_password
    )
    database.session.add(user)
    database.session.commit()


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    user = User.query.filter_by(email=data.get('email')).first()
    
    if not user or not check_password(data.get('password'), user.password):
        return jsonify({'message':'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.id)
    
    return jsonify({'access_token': access_token}), 200

@app.route('/appointments/create', methods=['POST'])
@jwt_required()
def create_appointments():
    data = request.json
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not all(k in data for k in ['name', 'start_time', 'end_time']):
        return jsonify({'message': 'Missing data'}), 400
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message':'User not found'}), 404

    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400
    
    if start_time >= end_time:
        return jsonify({'message':'Invalid time range'}), 400
    
    existing = Appointment.query.filter(
        Appointment.start_time < end_time,
        Appointment.end_time > start_time
    ).first()
    
    if existing:
        return jsonify({'message':'Time slot already booked'}), 409

    appointment = Appointment(
    name=data['name'], 
    start_time=start_time,
    end_time=end_time,
    user_id=user.id
    )
    database.session.add(appointment)
    database.session.commit()
    send_email(
    to=user.email,
    subject="Appointment Confirmed",
    body=f"Your appointment is scheduled from {start_time} to {end_time}")
    return jsonify({'message':'Appointment made'}), 201

@app.route('/appointment', methods=['GET'])
@jwt_required()
def get_appointment():
    date_param = request.args.get('date')
    user_id = get_jwt_identity()
    query = Appointment.query
    query = query.filter(Appointment.user_id == user_id)
    
    if date_param:
        try: 
            date = datetime.fromisoformat(date_param)
        except:
            return jsonify({'message':'Invalid date format'}), 400
        
        start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + timedelta(days=1)
        
        query =query.filter(
            Appointment.start_time >= start_of_day,
            Appointment.start_time < end_of_day
        )
    
    appointments = Appointment.query.order_by(Appointment.start_time).all()
    result = []
    
    for appointment in appointments:
        appointment_data = {
            'id': appointment.id,
            'name': appointment.name,
            'start_time': appointment.start_time.isoformat(),
            'end_time': appointment.end_time.isoformat(),
            'user_email': User.email
        }
        result.append(appointment_data)
    return jsonify(result)

@app.route('/appointment/delete/<int:appointment_id>', methods=['DELETE'])
@jwt_required()
def delete_appointment(appointment_id):
    user_id = get_jwt_identity
    appointment = Appointment.query.filter_by(
        id=appointment_id,
        user_id=user_id
    ).first()
    
    if appointment:
        database.session.delete(appointment)
        database.session.commit()
        return jsonify({'messagem': 'Appointment deleted successfully'})
    return jsonify({'messagem': 'Appointment not found'}), 404