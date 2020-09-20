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

