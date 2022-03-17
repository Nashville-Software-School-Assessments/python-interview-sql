import sqlite3


def dict_fetch_all(cursor):
    """Return all rows from a cursor as a list of dictionaries"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_all_parks():
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        # TODO: Write a sql query to get all the parks
        #       with each parks state name and type label information
        db_cursor.execute("""
            
        """)

        dataset = dict_fetch_all(db_cursor)
    return dataset


def get_parks_by_type(type_id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # TODO: Write a sql query to get the parks filtered by the park type
        db_cursor.execute("""
            
        """)

        dataset = dict_fetch_all(db_cursor)
    return dataset


def get_parks_ordered_by_name():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # TODO: Write a sql query to get all the parks
        #       in alphabetical order by the park name
        db_cursor.execute("""
            
        """)

        dataset = dict_fetch_all(db_cursor)
    return dataset
