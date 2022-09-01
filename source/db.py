import os
from functools import wraps

import psycopg2

conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
conn.autocommit = True


def db(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        with conn.cursor() as c:
            return f(c, *args, **kwargs)
    return wrapper


@db
def db_init(c):
    c.execute(open('init.sql').read())


db_init()
