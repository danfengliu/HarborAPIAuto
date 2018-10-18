class TestProjects(unittest.TestCase):
    """UserGroup unit test stubs"""
    def setUp(self):      
        pass

    def tearDown(self):
        pass

    def testAddProject(self):
        """Test UserGroup"""
        project = Project.create_project("project_dan", {"public": "string","enable_content_trust": "string","prevent_vulnerable_images_from_running": "string","prevent_vulnerable_images_from_running_severity": "string","automatically_scan_images_on_push": "string"},endpoint="https://10.192.127.8/api")

        pass


if __name__ == '__main__':
    unittest.main()