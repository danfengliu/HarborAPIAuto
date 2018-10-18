from __future__ import absolute_import
import os
import sys
import unittest

from testutils import CLIENT
from library.user import User

class TestProjects(unittest.TestCase):
    """UserGroup unit test stubs"""
    def setUp(self):    
        user = User()
        self.user= user        
        pass

    def tearDown(self):
        #id = self.user.delete_user(self.id, **CLIENT)
        #print '======user id %s was deleted======' % (id)
        pass

    def test001AddUser(self):
        """Test Add User"""
        #name="userauto296"
        id, name = self.user.create_user(**CLIENT)
        TestProjects.id = id
        print '======id=%s name=%s======' % (id, name) 
        pass
        
    def test002ChangeUserPWD(self):
        id = TestProjects.id
        status = self.user.update_user_pwd(id, new_password="00000000", **CLIENT)
        print '======Change user password: %s ======' % (status)
        
    def test003ChangeAdminRole(self):
        id = TestProjects.id
        status = self.user.update_uesr_role_as_sysadmin(id, 1, **CLIENT)
        print '======Change user role to admin: %s ======' % (status)
 
    def test004GetUseCurrent(self):
        data = self.user.get_user_current(**CLIENT)
        print "data:", data
        print "data.username:", data.username
        self.assertEqual(data.username, "admin", msg="Current user is not admin")
        pass
        
    def test005GetUsers(self):
        #Search user by username
        data = self.user.get_users(username="user001", **CLIENT)
        #print "data:", data     
        self.assertTrue( len(data) == 1,msg=data)
 
        #Search user by email
        data = self.user.get_users(email="realname", **CLIENT)
        #print "data:", data     
        self.assertTrue( len(data) > 0,msg=data)
        
        #Search all uesrs
        data = self.user.get_users(**CLIENT)
        self.assertTrue( len(data) > 1,msg=data)        
        TestProjects.someuser = data[1]
        print TestProjects.someuser
        pass      
        
    def test006GetUser(self):
        print "TestProjects.someuser.user_id:", TestProjects.someuser.user_id       
        data = self.user.get_user(TestProjects.someuser.user_id, **CLIENT)
        print "data:", data   
        self.assertEqual(data.user_id, TestProjects.someuser.user_id, msg="Current user is not admin")
        pass         
if __name__ == '__main__':
    unittest.main()
 
