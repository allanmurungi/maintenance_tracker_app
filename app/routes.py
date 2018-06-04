from app import app
from flask import jsonify
from flask_restful import Resource, Api, reqparse
from models import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import random


parser = reqparse.RequestParser()
parser.add_argument('email', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

api = Api(app)

""" A dictionary to hold the requests"""
Requets={}

class myrequest{
    """ A template class for the request object """
    def __init__(self,req_title,req_details,req_owner):

        self.title=req_title
        self.details=req_details
        self.req_id=random.randint(1,1000000)
        self.req_owner=req_owner
    
    def getId(self):
        return self.req_id

    def getreqtitle(self):
        return self.title

    def getreqdetails(self):
        return self.details

    def getreqemail(self):
        return self.req_owner

    }

class myIndex(Resource):
    def index():
        return jsonify({'message': 'maintenance tracker endpoints!'});
    


class login(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_email(data['email'])
        if(data['email']==""):
            return {'message':'no username/email entered'}
            
        elif(data['password']==""):
            return {'message':'no password given'}
            
        elif(data['email']=="" and data['email']=="" ):
            return {'message':'you have not entered email and password'}
            
        if not current_user:
            return {'message': 'User doesn\'t exist'}
        
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'Logged in as {}'.format(current_user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class signup(Resource):

    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return {'message': 'User already exists'}
        new_user = UserModel(
            email = data['email'],
            password = UserModel.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'User {} was created'.format(data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

class logout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500

    def get():
        pass

class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
        
class getrequests(Resource):

    def get(self):
        
        pass
    
class getrequest(Resource):

    def get(self,req_id):
        if(Requests[req_id]==None):
            return 'request does not exist'
        if(req_id==""):
            return 'request does not exist'
        return {"message":"successfully got request","req_title":Requests[req_id].getreqtitle,"req_details":Requests[req_id].getreqdetails,"req_author":Requests[req_id].getreqemail
                ,"req_id":Requests[req_id].getId}
        pass

class editrequest(Resource):

    def editrequest(self):
        pass

class deleterequest(Resource):

    def get(self,req_id):
        if(Requests[req_id]==None):
            return 'request does not exist'
        if(req_id==""):
            return 'requests not deleted succesfully'
        
        del Requests[req_id]
        return 'requests deleted succesfully'
        pass

class createrequest(Resource):

    def post(self):
        if(data['requesttitle']=="" and data['requestdetails']!=""):
            return 'missing title on request'

        elif(data['requesttitle']!="" and data['requestdetails']==""):
            return 'missing request details'

        elif(data['requesttitle']=="" and data['requestdetails']==""):
            return 'missing request information'
        req=myrequest(data['requesttitle'],data['requestdetails'])   
        Requests.update({req.getId: myrequest})
        return "request has been sent"
        

api.add_resource(login, '/login')
api.add_resource(login, '/signup')
api.add_resource(login, '/logout')
api.add_resource(createrequest, '/createrequest')
api.add_resource(getrequest, '/getrequest/<string:req_id>')
api.add_resource(getrequests, '/getrequests/<string:email>')
api.add_resource(editrequest, '/editrequest/<string:req_id>')
api.add_resource(deleterequest, '/deleterequest/<string:req_id>')

