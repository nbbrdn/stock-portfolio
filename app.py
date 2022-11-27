import logging

from flask import (
    Flask,
    escape,
    render_template,
    redirect,
    request,
    session,
    url_for,
    flash,
)
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
from pydantic import BaseModel, validator


app = Flask(__name__)

app.logger.removeHandler(default_handler)

file_handler = RotatingFileHandler(
    'stock-portfolio.log', maxBytes=16384, backupCount=20
)
file_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]'
)
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.secret_key = 'BAD_SECRET_KEY'

app.logger.info('Starting the Stock Portfolio App...')


@app.route('/about')
def about():
    flash('Thanks for learning about this site!', 'info')
    return render_template('about.html', company_name='TestDriven.io')
    # return render_template('about.html')


@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')


@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'


@app.route('/blog-posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'
