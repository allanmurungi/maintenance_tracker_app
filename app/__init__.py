from flask import Flask

app=Flask(__name__);

from app import routes

from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = 'mga'

jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'amg'

db = SQLAlchemy(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


@jwt.token_in_my_endpoint
def check_if_token(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti(jti)

@app.before_first_request
def create_tables():
    db.create_all()
