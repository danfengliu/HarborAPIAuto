from __future__ import absolute_import
import os
import sys
import unittest

from library.project import Project

class TestProjects(unittest.TestCase):
    """UserGroup unit test stubs"""
    def setUp(self):      
        pass

    def tearDown(self):
        pass

    def testAddProject(self):
        """Test UserGroup"""
        project = Project()
        id, name = project.create_project("project_dan1", {},endpoint="https://10.192.127.8/api")
        print id
        print name

        pass


if __name__ == '__main__':
    unittest.main()
 
