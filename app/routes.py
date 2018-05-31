from app import app
from flask import jsonify
from flask_restful import Resource, Api


api = Api(app)



class myIndex(Resource):
    def index():
        return jsonify({'message': 'maintenance tracker endpoints!'});
    


class login(Resource):
    def post():
        pass


class signup(Resource):

    def post():
        pass

class logout(Resource):

    def get():
        pass

class getrequests(Resource):

    def get():
        pass
    
class getrequest(Resource):

    def get():
        pass

class editrequest(Resource):

    def editrequest():
        pass

class deleterequest(Resource):

    def get():
        pass

class createrequest(Resource):

    def post():
        pass


api.add_resource(createrequest, '/createrequest')
api.add_resource(getrequest, '/getrequest/<string:req_id>')
api.add_resource(getrequests, '/getrequests/<string:email>')
api.add_resource(editrequest, '/editrequest/<string:req_id>')
api.add_resource(deleterequest, '/deleterequest/<string:req_id>')

