from flask import Flask, request

from views.parks_requests import (
    get_all_parks, get_parks_by_type, get_parks_ordered_by_name)

app = Flask(__name__)


@app.route("/parks")
def list_parks():
    """Returns a list of all the parks"""
    search = request.args.get('type', None)
    order_by = request.args.get('order_by', None)
    if search:
        response = get_parks_by_type(search)
    elif order_by:
        response = get_parks_ordered_by_name()
    else:
        response = get_all_parks()

    return response
