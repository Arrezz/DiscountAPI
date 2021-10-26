# Discount Service

## Installation instructions

Install Python for your OS (https://www.python.org/downloads/release/python-397/).

To install Flask run the following command in your terminal:
`pip install flask`

Clone the project from GitHub.

Navigate to your folder where you cloned the project to in your terminal.

Run the following command `python main.py`

You can now access the API locally at `http://127.0.0.1:5000/`

## Discount API documentation

### Endpoints

The following two endpoints are used to create and get the discount codes.

#### Create discount
* Create discount code: `POST /discount:product_id`
  
Possible responses for the POST are:
* HTTP status code 400 if the product_id argument is not present in the request.
* The UUID of the discount code that was created.


#### Get discount
* Get discount : `GET /discount:product_id`

Possible responses for the GET are:

* HTTP status code 400 if the product_id argument is not present in the request.
* HTTP status code 404 if the product_id does not exist.
* The discount code of the product_id.
