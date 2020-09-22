from flask.views import MethodView
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range
from validators import LoginControllers_schema, RegistrerControllers_schema, RegisterCustomerControllers_schema, RegisterEquipmentControllers_schema, ManageLineControllers_schema, ManageLineControllers_put_schema, ManageLineControllers_get_schema, ManageBillControllers_get_Schema, ManageBillControllers_delete_Schema
from model import session, User
from helpers import QueryToList
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime

create_register_schema=RegistrerControllers_schema()
create_login_schema = LoginControllers_schema()
create_RegisterCustomerControllers_schema = RegisterCustomerControllers_schema()
create_RegisterEquipmentControllers_schema = RegisterEquipmentControllers_schema()
create_ManageLineControllers_schema = ManageLineControllers_schema()
create_ManageLineControllers_put_schema = ManageLineControllers_put_schema()
create_ManageLineControllers_get_schema = ManageLineControllers_get_schema()
create_ManageBillControllers_get_Schema = ManageBillControllers_get_Schema()
create_ManageBillControllers_delete_Schema = ManageBillControllers_delete_Schema()
class RegisterConsultantControllers(MethodView):
    """ Registro  del asesor"""

    def post(self):
        content = request.get_json()
        errors = create_register_schema.load(content)
        if errors:
            name = content.get('name')
            lastname = content.get('lastname')
            identificationCard = content.get('identificationCard')
            phone = content.get('phone')
            address = content.get('address')
            email = content.get('email')
            password = content.get('password')
            rol = content.get('rol')
            print("----------", email)
            salt = bcrypt.gensalt()
            hash_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
            hash_pass = hash_pass.decode('utf-8')
            print(hash_pass)
            user_lines = User(name=name, lastname=lastname,
                              identificationCard=identificationCard, phone=phone, address=address, email=email, password=hash_pass,rol=rol)
            session.add(user_lines)
            session.commit()
            return jsonify({"Status": "Register consultant successfully ",
                           }), 200
        else:
            return jsonify({"Status": "Error",}),403

class LoginControllers(MethodView):
    """Logeo para el usuario del sistema"""
    def post(self):
        content=request.get_json()
        errors = create_login_schema.load(content)
        if errors:
            content = request.get_json()
            email = content.get('email')     
            password = content.get('password')
            #Consulta a la base de datos del email ingresado
            user = session.query(User).filter_by(email=email).first()
            ##aqui la duda cae en como recuperar el has de la bd 
            if user:
                email_db=user.email
                password_db = user.password
                if bcrypt.checkpw(password.encode('utf8'), password_db.encode('utf8')):
                    # Se acude a jwt para generar un token codificado en formato json
                    encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300), 'email': email}, KEY_TOKEN_AUTH, algorithm='HS256')
                    return jsonify({"Status": "Login exitoso", "auth": True, "token": encoded_jwt.decode()}), 200
                return jsonify({"Status": "Login incorrecto 22","email":user.email}), 400
            return jsonify({"Status": "Login incorrecto 11"}), 400
        return jsonify({"Status": "Datos no validos reintente de nuevo"}),400
