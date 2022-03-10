import json
import sqlite3


def get_all_parks():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # TODO: Write a sql query to get all the parks 
        #       with each parks state name and type label information
        db_cursor.execute("""
        
        """)

        parks = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            park = {
                'id': row['id'],
                'name': row['name'],
                'description': row['description'],
                'type': {
                    'label': row['label']
                },
                'state': {
                    'name': row['state_name']
                }
            }

            parks.append(park)
            

    return json.dumps(parks)


def get_parks_by_type(type_id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # TODO: Write a sql query to get the parks filtered by the park type
        db_cursor.execute("""
        
        """)

        parks = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            park = {
                'id': row['id'],
                'name': row['name'],
                'description': row['description'],
            }

            parks.append(park)
            

    return json.dumps(parks)

def get_parks_ordered_by_name():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # TODO: Write a sql query to get all the parks 
        #       in alphabetical order by the park name
        db_cursor.execute("""
        
        """)

        parks = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            park = {
                'id': row['id'],
                'name': row['name'],
                'description': row['description'],
            }

            parks.append(park)
            

    return json.dumps(parks)
