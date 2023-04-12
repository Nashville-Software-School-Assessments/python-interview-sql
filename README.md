# SQL Challenge

For this challenge, you will need to write 4 sql statements. The __only__ code that needs to change is in the `views/parks_requests.py` file. In that file, there are 4 TODO's to write the sql statements needed. 

Along with assessing your sql skills this will also assess your ability to solve problems and ask for help. Use your resources! This includes instructors, google, and past projects. This does not include teammates. 

## ERD
Here is the ERD for this challenge:
![](parks_erd.png)

## Set Up
After cloning the repo:
1. `pipenv shell`
2. `pipenv install`
3. `touch db.sqlite3`
4. Connect to the database file and run all the sql commands inside the `seed_db.sql` file. This will create the tables and insert the data
5. Create a `scratch.sql` file to try out any sql before you add it to the python file
## Requirements
### The **only** code that will be added is the sql statement in each method. No other changes will need to be made
1. The `get_all_parks` sql is assessing your knowledge of `joins` and ordering. It should return all the parks information along with the state_id abbr, park_type_id, and label. The parks should be ordered alphabetically by the park name
2. The `get_parks_by_type` sql is assessing your knowledge of filtering. It should return the parks associated with a specific park type
3. The `create_park` sql is assessing your knowledge of adding a row to the database. The new row should be inserted into the Park table with the correct information
4. The `delete_park` sql is assessing your knowledge of removing a row from the database. It should remove a park from the database based on the `id` passed to the function

## Testing Locally

### Testing with Postman
1. Running the server: Use the debug panel to run the server. The `launch.json` file is already set up so press play to start the debugger.
2. In Postman the url's to use are
    
    1. Testing **`get_all_parks`**: `http://localhost:8000/parks`
    2. Testing **`get_parks_by_type`**: `http://localhost:8000/parks?type=1`
        * Make sure it works with all park types 1-4
    3. Testing **`create_park`**: 
       * url: `http://localhost:8000/parks`
       * method: `POST`
       * body: 
            ```py
            {
                'name': 'Joshua Tree',
                'state_id': 3,
                'park_type_id': 1,
                'description': 'Joshua Tree description'
            }
            ```
    4. Testing **`delete_park`**: `http://localhost:8000/parks/1`
        * Make sure it works with other park ids

### Running the UnitTest file
To see the test output before pushing to github: `python3 test_parks.py`
