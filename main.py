import uuid

import flask
from flask import Flask, request

discount_codes = [
    {
        'product_id': 'd81e8989-647d-45fa-8aa9-b8dd68830ad7',
        'discount_code': '983fcf98-0bd5-4fd3-9e71-5c9c334c8b1b'
    }
]

api = Flask(__name__)


@api.route('/discount/post', methods=['POST'])
def post_discount():
    if request.args.get('product_id') is None:
        flask.abort(400)
    product_id = request.args.get('product_id')
    discount_code = str(uuid.uuid4())
    discount_codes.append(dict([('product_id', str(product_id)),
                                ('discount_code', discount_code)]))
    return discount_code


@api.route('/discount/get', methods=['GET'])
def get_discount():
    if request.args.get('product_id') is None:
        return flask.abort(400)
    for index in range(len(discount_codes)):
        if discount_codes[index]['product_id'] == request.args.get('product_id'):
            return str(discount_codes[index]['discount_code'])
    return flask.abort(404)


if __name__ == '__main__':
    api.run()
