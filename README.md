# stock-portfolio

## Overview

This Flask application manages a stock portfolio for each user, including the user management aspects of a web application.

## Installation instructions

### Installation

Pull down the source code from this repository:

```sh
git clone git@github.com:nbbrdn/stock-portfolio.git
```

Create a new virtual environment:

```sh
$ cd flask-stock-portfolio
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages specified in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

### Running the Flask Application

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

Navigate to 'http://127.0.0.1:5000/' in your favorite web browser to view the website!
