import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1s10mm8QXpY4bhXkHnPZDuhK9IYBZwsn'