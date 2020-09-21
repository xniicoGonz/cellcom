from flask.views import MethodView
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range
from validators import LoginControllers_schema, RegistrerControllers_schema, RegisterCustomerControllers_schema, RegisterEquipmentControllers_schema, ManageLineControllers_schema, ManageLineControllers_put_schema, ManageLineControllers_get_schema, ManageBillControllers_get_Schema, ManageBillControllers_delete_Schema
from model import session, User, Customer, equipment, Lines, Bill
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
                              identificationCard=identificationCard, phone=phone, 
                              address=address, email=email, password=hash_pass,rol=rol)
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


class RegisterCustomerControllers(MethodView):
    """Registro Clientes """

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            errors = create_RegisterCustomerControllers_schema.load(content)
            if errors:
                name = content.get('name')
                lastname = content.get('lastname')
                identificationCard = content.get('identificationCard')
                line = content.get('phone')
                dateBorn = content.get('dateBorn')
                identificationCard_bdvali = session.query(
                    Customer).filter_by(customerIdentification=identificationCard).first()
                if not identificationCard_bdvali:
                    print("entre al if")
                    manage_bd = Customer(namne=name,
                                        lastname=lastname,
                                        customerIdentification=identificationCard,
                                        line=line,
                                        dateBorn=dateBorn)
                    session.add(manage_bd)
                    session.commit()
                    manage_bd = Lines(numberline=line,
                                      customerIdentification=identificationCard,
                                      state='active')
                    session.add(manage_bd)
                    session.commit()
                    manage_bd=Bill(
                            value=32000,
                            id_bill=1,
                            collectionDay='2020-09-22',
                            customerIdentification=identificationCard,
                            numberLine=line
                        )
                        
                        
                    session.add(manage_bd)
                    session.commit()
                    return jsonify({"Status": "Register customer successfully, Autorizacion por token valida ",
                    }), 200
                return jsonify({"Status": "documento ya registrado"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403


class RegisterEquipmentControllers(MethodView):
    """ Registro equipo movil"""

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            errors = create_RegisterEquipmentControllers_schema.load(content)
            if errors:
                lineNumber = content.get('lineNumber')
                serial = content.get('serial')
                imei = content.get('imei')
                trademark = content.get('trademark')
                state = content.get('state')
                imei_bdvali = session.query(
                    equipment).filter_by(imei=imei).first()
                if not imei_bdvali:
                    manage_bd = equipment(lineNumber=lineNumber,
                                    serial=serial,
                                    imei=imei,
                                    trademark=trademark,
                                    state=state
                                    )
                    session.add(manage_bd)
                    session.commit()
                    return jsonify({"Status": "Proceso valido por autenticacion. Registro de equipo movil realizado con satisfaccion ",
                                    }), 200
                return jsonify({"Status": "Este equipo ya fue registrado"})
        return jsonify({"Status": "No ha enviado un token"}), 403


class ManageLineControllers(MethodView):
    """Manejo de las lineas telefonicos"""

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            errors = create_ManageLineControllers_schema.load(content)
            if errors:
                numberline = content.get("line2")
                customer_dentification_card = content.get("customerIdentificationCard")
                state = content.get("state")
                trademark=content.get("trademark")
                line_bdvali = session.query(
                    Lines).filter_by(numberline=numberline).first()
                if not line_bdvali:
                    manage_bd = Lines(numberline=numberline,
                                      customerIdentification=customer_dentification_card,
                                      state=state,
                                      trademark=trademark,
                                          )
                    session.add(manage_bd)
                    session.commit()
                    return jsonify({"Status": "Register line successfully",}), 200
                return jsonify({"Status": "Ya existe esta linea", }), 200
        return jsonify({"Status": 'no envio un token'}), 400

    def get(self, phone):
        if (request.headers.get('Authorization')):
            errors = create_ManageLineControllers_get_schema.validate(phone)
            if errors:
                phone_bdvali = session.query(
                    Lines).filter_by(numberline=phone).first()
                print(phone_bdvali.numberline,
                      phone_bdvali.customerIdentification, phone_bdvali.state)
                return jsonify({"Status": "Line Consulted Successfully",
                                'linea':  phone_bdvali.numberline,
                                'id': phone_bdvali.customerIdentification,
                                'state': phone_bdvali.state
                                }), 200
        return jsonify({"Status": "no se envio token"})

    def put(self, id_customer):
        if (request.headers.get('Authorization')):
            errors = create_ManageLineControllers_put_schema.validate(
                id_customer)
            if errors:
                content = request.get_json(self)
                line = content.get("line2")
                personID = content.get("personID")
                state = content.get("state")
                trademark=content.get("trademark")
                session.query(Lines).filter_by(numberline = line).update({'state': state})
                session.commit()
                return jsonify({"Status": "Line update successfully"}),200
            return jsonify({"Status": "errror",
                            }), 400
        return jsonify({"Status" "no se envio un token"})


class ManageBillControllers(MethodView):
    """Manejo de factura 88uu"""

    def get(self, line):
        if(request.headers.get('Authorization')):
            errors = create_ManageBillControllers_get_Schema.validate(line)
            if errors:
                 phone_bdvali = session.query(
                     Bill).filter_by(numberLine=line).first()
                 Identification=phone_bdvali.customerIdentification
                 user = session.query(Customer).filter_by(customerIdentification=Identification).first()

              
                 return jsonify({"Status": "Bill Consulted Successfully",
                                "name":user.namne,
                                 "lastname":user.lastname,
                                 "identification":user.customerIdentification, 
                                 "line":user.line,
                                 "value":phone_bdvali.value,
                                 "id_bill":phone_bdvali.id_bill,
                                 "collectionDay":phone_bdvali.collectionDay
                  }), 200
        return jsonify({"Status": "error en el token"}), 400

    def delete(self, line):
        if(request.headers.get('Authorization')):
            errors = create_ManageBillControllers_delete_Schema.validate(line)
            print(line)
            if errors:
                content = request.get_json(self)
                session.query(Bill).filter_by(numberLine = line).delete()
                session.commit()
                return jsonify({"Status": "Bill Deleted Successfully",
                                "linea": line,
                                }), 200

        return jsonify({"Status": "no se envio un token"

                        }), 400
