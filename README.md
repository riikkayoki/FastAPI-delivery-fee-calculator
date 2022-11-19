# Delivery Fee Calculator with FastAPI

![CI](https://github.com/riikkayoki/FastAPI-delivery-fee-calculator/workflows/CI/badge.svg) [![Codecov](https://codecov.io/gh/riikkayoki/FastAPI-delivery-fee-calculator/branch/master/graph/badge.svg?token=IM0CP0V2L2)](https://codecov.io/gh/riikkayoki/FastAPI-delivery-fee-calculator)

This is a [FastAPI](https://fastapi.tiangolo.com/) workshop project inspired by [Wolt!](https://github.com/woltapp/engineering-summer-intern-2022)


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

### Other

In this application, I have used Pylint for code analysis and Autopep8 for code formatting.

Pylint:

```
poetry run invoke pylint
```

Autopep8:
```
poetry run invoke autopep
```


