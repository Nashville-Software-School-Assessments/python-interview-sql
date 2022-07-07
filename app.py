import json
from flask import Flask, request
from views.parks_requests import (
    create_park, delete_park, get_all_parks, get_parks_by_type, get_parks_ordered_by_name)

app = Flask(__name__)


@app.route("/parks")
def list_parks():
    """Returns a list of all the parks"""
    search = request.args.get('type', None)
    order_by = request.args.get('order_by', None)
    if search:
        data = get_parks_by_type(search)
    elif order_by:
        data = get_parks_ordered_by_name()
    else:
        data = get_all_parks()

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        content_type='application/json'
    )
    return response


@app.route('/parks', methods=['POST'])
def post_park():
    data = create_park(request.json)

    response = app.response_class(
        response=json.dumps(data),
        status=201,
        content_type='application/json'
    )
    return response


@app.route('/parks/<id>', methods=['DELETE'])
def remove_park(id):
    delete_park(id)

    response = app.response_class(
        status=204,
    )
    return response
