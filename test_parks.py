import unittest
from app import app
from ddt import ddt, data
from tests.helpers import check_for_assertion_error, format_message
from tests.parks import PARK_TYPES, PARKS, STATES
from tests.seed_db import seed_db


class FilterData(list):
    pass


def annotated_filter(park_type_id, num_of_parks):
    data = FilterData([park_type_id, num_of_parks])
    setattr(data, "__name__",
            f"test_type_{data[0]}_returns_length_of_{data[1]}")
    return data


@ddt
class ParkTests(unittest.TestCase):
    def setUp(self):
        seed_db()
        return super().setUp()

    @check_for_assertion_error
    def test_join(self):
        """get_all_parks"""
        tester = app.test_client(self)
        response = tester.get('/parks', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 11,
                         format_message("HINT: The response did not return the expected number of parks"))

        json_response = response.json

        expected_sorted = sorted(
            response.json, key=lambda park: park['name'])

        self.assertListEqual(response.json, expected_sorted,
                             format_message("HINT: The result was not ordered as expected"))

        for actual in json_response:
            expected_park = next(
                (park for park in PARKS if park['park_id'] == actual['park_id']), {})
            expected_state = next(
                (state for state in STATES if state['state_id'] == expected_park['state_id']), {})
            expected_park_type = next(
                (pt for pt in PARK_TYPES if pt['park_type_id'] == expected_park['park_type_id']), {})
            self.assertEqual(actual['abbr'], expected_state['abbr'],
                             format_message('HINT: The expected state abbr was not returned, check your State join'))
            self.assertEqual(actual['label'], expected_park_type['label'],
                             format_message('HINT: The expected park type label was not returned, check your ParkType join'))

    @data(annotated_filter(1, 4), annotated_filter(2, 3), annotated_filter(3, 2), annotated_filter(4, 2))
    @check_for_assertion_error
    def test_filter(self, value):
        """get_parks_by_type"""
        park_type_id, num_of_parks = value
        tester = app.test_client(self)
        response = tester.get(
            f'/parks?type={park_type_id}', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), num_of_parks,
                         format_message("HINT: The response did not return the expected number of parks"))
    
    def test_create(self):
        """create_park"""
        tester = app.test_client(self)

        new_park = {
            'name': 'Joshua Tree',
            'state_id': 3,
            'park_type_id': 1,
            'description': 'Joshua Tree description'
        }

        response = tester.post('/parks', json=new_park,
                               content_type='application/json')

        self.assertEqual(response.status_code, 201)
        actual = response.json
        self.assertTrue(actual['id'],
                        format_message("Hint: the id should be a number greater than 0"))

        updated_get_response = tester.get(
            '/parks', content_type='application/json')

        self.assertEqual(
            len(updated_get_response.json), 12,
            format_message("HINT: The amount of parks in the database did not go up. Make sure the sql is working as expected")
        )

    @check_for_assertion_error
    def test_delete(self):
        """delete_park"""
        tester = app.test_client(self)
        response = tester.delete('/parks/1', content_type='application/json')
        self.assertEqual(response.status_code, 204)

        updated_get_response = tester.get(
            '/parks', content_type='application/json')

        self.assertEqual(
            len(updated_get_response.json), 10,
            format_message("HINT: The amount of parks in the database did not go down. Make sure the sql is working as expected")
        )


if __name__ == '__main__':
    unittest.main()
