import unittest
from SkryptGET import check_status_code, check_key_elements

class TestAPITestScript(unittest.TestCase):
    def test_check_status_code(self):
        self.assertTrue(check_status_code('{"userId": 1, "id": 1, "title": "test"}'))
        self.assertFalse(check_status_code('Invalid JSON'))

    def test_check_key_elements(self):
        response = '{"userId": 1, "id": 1, "title": "test"}'
        keys = ['userId', 'id', 'title']
        self.assertTrue(check_key_elements(response, keys))
        keys_missing = ['userId', 'id', 'body']
        self.assertFalse(check_key_elements(response, keys_missing))

if __name__ == '__main__':
    unittest.main()
