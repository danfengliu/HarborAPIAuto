# -*- coding: utf-8 -*-

import sys
import base
import swagger_client
        
class User(base.Base):

    def create_user(self, name=None,
        email = None, password=None,realname = None, **kwargs):
        if name is None:
            name = base._random_name("user")
        if realname is None:
            realname = base._random_name("realname")
        if email is None:
            email = '%s@%s.com' % (realname,"vmware") 
        if password is None:
            password = "Harbor12345678"	
        client = self._get_client(**kwargs)
        user = swagger_client.User(None, name, email, password, realname, None, None, None, None, None, None, None, None, None)
        print user
        _, _, header = client.users_post_with_http_info(user)
        return base._get_id_from_header(header), name

    def get_users(self, username=None, email=None, page=None, page_size=None, **kwargs): 
        client = self._get_client(**kwargs)
        params={}
        if username is not None:
            params["username"] = username
        if email is not None:
            params["email"] = email 
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size 
            
        data, _, header = client.users_get_with_http_info(**params)
        return data
        
    def get_user(self, id, **kwargs): 
        client = self._get_client(**kwargs)
        data, _, header = client.users_user_id_get_with_http_info(id)
        print "data in lib:", data 
        return data
       
     
    def get_user_current(self, **kwargs): 
        client = self._get_client(**kwargs)
        data, _, header = client.users_current_get_with_http_info()
        return data
        
    def delete_user(self, id, **kwargs):
        client = self._get_client(**kwargs)
        _, _, header = client.users_user_id_delete_with_http_info(id)
        return id
        
    def update_user_pwd(self, id, new_password=None, old_password=None, **kwargs):
        if old_password is None:
            old_password  = ""
        password = swagger_client.Password(old_password, new_password)
        client = self._get_client(**kwargs)
        _, _, header = client.users_user_id_password_put_with_http_info(id, password)
        return id
        
    def update_uesr_profile(self, id, email=None, realname=None, comment=None, **kwargs):
        client = self._get_client(**kwargs)
        user_rofile = swagger_client.UserProfile(email, realname, comment)
        _, _, header = client.users_user_id_put_with_http_info(id, user_rofile)
        return id
        
    def update_uesr_role_as_sysadmin(self, id, IsAdmin, **kwargs):
        client = self._get_client(**kwargs)
        has_admin_role = swagger_client.HasAdminRole(IsAdmin)
        print "has_admin_role:", has_admin_role
        _, _, header = client.users_user_id_sysadmin_put_with_http_info(id, has_admin_role)
        return id
        
        
        