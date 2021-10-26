import uuid

import flask
from flask import Flask, request

discount_codes = {'5739c588-2943-4748-a8d4-a7346f94a420': {'85219126-6d32-4ccc-b03a-c4de1c0d77e4'}}

api = Flask(__name__)


@api.route('/discount/post', methods=['GET'])
def post_discount():
    if request.args.get('product_id') is None:
        flask.abort(400)
    product_id = request.args.get('product_id')
    discount_code = str(uuid.uuid4())
    if product_id in discount_codes.keys():
        discount_codes[product_id].add(discount_code)
        return discount_code
    discount_codes[product_id] = {discount_code}
    return discount_code


@api.route('/discount/get', methods=['GET'])
def get_discount():
    if request.args.get('product_id') is None:
        return flask.abort(400)
    product_id = request.args.get('product_id')
    for _ in discount_codes.keys():
        return discount_codes[product_id].pop()
    return flask.abort(404)


if __name__ == '__main__':
    api.run()
