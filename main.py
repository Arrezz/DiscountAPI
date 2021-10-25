from flask import Flask, json, request, jsonify
import uuid

discount_codes = [{"product_id":"4d18db17-f1ce-4704-9b13-5cbe44a8c78d" , "discount_code": "c7aeeb72-8d9e-4a6a-834c-ed37003aa027"},
                  {"product_id":"2536c821-35c8-427c-a7c7-d14a269d58e1" , "discount_code": "c7aeeb72-8d9e-4a6a-834c-ed37003aa027"}]

api = Flask(__name__)


@api.route('/discount/post', methods=['GET'])
def post_discount():
    data = {'product_id': str(uuid.uuid4()), 'discount_code': str(uuid.uuid4())}
    discount_codes.append(json.dumps(data))
    return json.dumps(discount_codes)


@api.route('/discount/get', methods=['GET'])
def get_discount():
    product_id = request.args.get('product_id')
    return json.dumps(discount_codes)


if __name__ == '__main__':
    api.run()
