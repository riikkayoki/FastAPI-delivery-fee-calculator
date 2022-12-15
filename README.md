# Delivery Fee Calculator with FastAPI

![CI](https://github.com/riikkayoki/FastAPI-delivery-fee-calculator/workflows/CI/badge.svg) [![Codecov](https://codecov.io/gh/riikkayoki/FastAPI-delivery-fee-calculator/branch/master/graph/badge.svg?token=IM0CP0V2L2)](https://codecov.io/gh/riikkayoki/FastAPI-delivery-fee-calculator)

This is a [FastAPI](https://fastapi.tiangolo.com/)  workshop project inspired by [Wolt!](https://github.com/woltapp/engineering-summer-intern-2022) challenge from spring 2022.

You can find FastAPI documentation [here](https://fastapi.tiangolo.com/).


## Usage

**Prerequisites**
* Python 3.8 or later
* Poetry

### Install dependencies & Run the app

Install the dependencies:
```
poetry install
```

Activate the poetry environment:
```
poetry shell
```
Run the server:
```
poetry run invoke start
```

The API documentation is available in http://127.0.0.1:8000/docs.



### Example of Usage

This is an example case provided [Wolt!](https://github.com/woltapp/engineering-summer-intern-2022)

Example:
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
```

##### Field details

| Field             | Type  | Description                                                           | Example value                             |
|:---               |:---   |:---                                                                   |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                               |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.  |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.               |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in [ISO format](https://en.wikipedia.org/wiki/ISO_8601).    |__2021-01-16T13:00:00Z__                   |

##### Response
Example:
```json
{"delivery_fee": 710}
```

###### Field details

| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|delivery_fee   |Integer|Calculated delivery fee __in cents__.  |__710__ (710 cents = 7.10€)|



### Test the app

Test the app:
```
poetry run invoke test
```

Create coverage html:

```
poetry run invoke coverage
```

Get coverage report:

```
poetry run invoke coverage-report
```

View report on Firefox browser:

```
poetry run invoke view-report
```

### Other commands

In this application, I have used Pylint for code analysis and Autopep8 for code formatting.

Pylint:

```
poetry run invoke pylint
```

Autopep8:
```
poetry run invoke autopep
```
