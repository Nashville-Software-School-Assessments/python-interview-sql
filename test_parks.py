import unittest
from request_handler import app


class ParkTests(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/parks', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 11)
        

    


if __name__ == '__main__':
    unittest.main()
