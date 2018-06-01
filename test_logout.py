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

    
    def test_logout(self):
        response=self.logout();
        self.assertEqual(response.status_code, 200)
        assert b'you were logged out' in response.data
        
    
        
    def log_out():
        return self.app.get('/logout',follow_redirects=True);


        
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

