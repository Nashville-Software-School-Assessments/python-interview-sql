import unittest
from request_handler import app
from ddt import ddt, data
from parks import PARK_TYPES, PARKS, STATES


class FilterData(list):
    pass


def annotated_filter(park_type_id, num_of_parks):
    data = FilterData([park_type_id, num_of_parks])
    setattr(data, "__name__",
            f"test_type_{data[0]}_returns_length_of_{data[1]}")
    return data


@ddt
class ParkTests(unittest.TestCase):

    def test_join(self):
        tester = app.test_client(self)
        response = tester.get('/parks', content_type='application/json')
        self.assertEqual(response.status_code, 200,
                         "HINT: Check your sql for errors")
        self.assertEqual(len(response.json), 11,
                         "HINT: The response did not return the expected number of parks")

        json_response = response.json

        for actual in json_response:
            expected_park = next(
                (park for park in PARKS if park['park_id'] == actual['park_id']), {})
            expected_state = next(
                (state for state in STATES if state['state_id'] == expected_park['state_id']), {})
            expected_park_type = next(
                (pt for pt in PARK_TYPES if pt['park_type_id'] == expected_park['park_type_id']), {})
            self.assertEqual(actual['name'], expected_state['name'],
                             'HINT: The expected state name was not returned, check your State join')
            self.assertEqual(actual['label'], expected_park_type['label'],
                             'HINT: The expected park type label was not returned, check your ParkType join')

    @data(annotated_filter(1, 4), annotated_filter(2, 3), annotated_filter(3, 2), annotated_filter(4, 2))
    def test_filter(self, value):
        park_type_id, num_of_parks = value
        tester = app.test_client(self)
        response = tester.get(
            f'/parks?type={park_type_id}', content_type='application/json')
        self.assertEqual(response.status_code, 200,
                         "HINT: Check your sql for errors")
        self.assertEqual(len(response.json), num_of_parks,
                         "HINT: The response did not return the expected number of parks")

    def test_order_by(self):
        tester = app.test_client(self)
        response = tester.get('/parks?order_by=name',
                              content_type='application/json')
        expected_sorted = sorted(
            response.json, key=lambda park: park['moniker'])
        self.assertEqual(response.status_code, 200,
                         "HINT: Check your sql for errors")
        self.assertEqual(len(response.json), 11,
                         "HINT: The response did not return the expected number of parks")
        self.assertListEqual(response.json, expected_sorted,
                             "HINT: The result was not ordered as expected")


if __name__ == '__main__':
    unittest.main()
