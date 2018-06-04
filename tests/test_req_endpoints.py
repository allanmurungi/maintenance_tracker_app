import os
import unittest
 
from app import app
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        
        self.assertEqual(app.debug, False)

    
    def edit_request(self,req_id,requesttitle,requestdetails):
        return self.app.post('/createrequest',data=dict(req_id=req_id,requesttitle=requesttitle,requestdetails=requestdetails),follow_redirects=True);
    def get_request(self,req_id):
        return self.app.get('/getrequest',data=dict(req_id=req_id),follow_redirects=True);
    def get_requests(self,email):
        return self.app.get('/getrequests',data=dict(email=email),follow_redirects=True);
        
    def create_request(self,requesttitle,requestdetails,req_owner):
        return self.app.post('/createrequest',data=dict(requesttitle=requesttitle,requestdetails=requestdetails,req_owner=req_owner),follow_redirects=True);
    def delete_request(self,req_id):
        return self.app.get('/deleterequest',data=dict(req_id=req_id),follow_redirects=True);
        
    def test_create_request(self):
        response=self.create_request("Water flow","The water flow is not consistent in the evenings.","p@gmail.com");
        self.assertEqual(response.status_code, 200)
        assert b'request has been sent' in response.data;
        
    def test_create_request_missing_title(self):
        response=self.create_request("","The water flow is not consistent in the evenings.","p@gmail.com");
        self.assertEqual(response.status_code, 400)
        assert b'missing title on request' in response.data    
 
     def test_create_request_missing_details(self):
        response=self.create_request("Water flow","","p@gmail.com");
        self.assertEqual(response.status_code, 400)
        assert b'missing request details' in response.data

    def test_create_request(self):
        response=self.create_request("","","p@gmail.com");
        self.assertEqual(response.status_code, 201)
        assert b'missing request information' in response.data

     def test_get_request_success(self):
        response=self.get_request("1");
        self.assertEqual(response.status_code, 200)
        assert b'successfully got request' in response.data
    def test_get_request_empty_id(self):
        response=self.get_request("");
        self.assertEqual(response.status_code, 200)
        assert b'request does not exist' in response.data

    def test_get_requests_success(self):
        response=self.get_requests("p@gmail.com");
        self.assertEqual(response.status_code, 200)
        assert b'requests succesfully fetched' in response.data
        
    def test_get_requests_empty_email(self):
        response=self.get_requests("");
        self.assertEqual(response.status_code, 200)
        assert b'requests not succesfully fetched' in response.data 

    def test_delete_request_empty_id(self):
        response=self.delete_requests("");
        self.assertEqual(response.status_code, 400)
        assert b'requests not deleted succesfully ' in response.data
        
    def test_delete_request_success(self):
        response=self.delete_requests("1");
        self.assertEqual(response.status_code, 204)
        assert b'requests deleted succesfully' in response.data
           
    def test_delete_request_not_exist(self):
        response=self.delete_requests("ghvv7999");
        self.assertEqual(response.status_code, 404)
        assert b'request does not exist' in response.data    
        
     def test_get_request_not_exist(self):
        response=self.get_request("ghvv7999");
        self.assertEqual(response.status_code, 404)
        assert b'request does not exist' in response.data

    def test_edit_request(self):
        response=self.edit_request("1","title","details");
        self.assertEqual(response.status_code, 200)
        assert b'request succesfully modified' in response.data
        
    def test_edit_request_no_title(self):
        response=self.edit_request("1","","details");
        self.assertEqual(response.status_code, 400)
        assert b'request missing title' in response.data
        
    def test_edit_request_no_details(self):
        response=self.edit_request("1","title","");
        self.assertEqual(response.status_code, 400)
        assert b'request missing details' in response.data
        
    # executed after each test
    def tearDown(self):
        pass

    
        
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        
 
 
if __name__ == "__main__":
    unittest.main()

