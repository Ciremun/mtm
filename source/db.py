import os
import json
from functools import wraps
from datetime import datetime
from typing import Dict, List, Tuple

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
def create_tier(c, title: str, author: str, added: datetime, items: Dict) -> Tuple[int]:
    sql = """\
INSERT INTO tier (title, author, added, items) VALUES \
(%s, %s, %s, %s) RETURNING id\
"""
    c.execute(sql, (title, author, added, json.dumps(items)))
    return c.fetchone()

@db
def tier_by_id(c, id: int) -> List[Tuple[str, str, datetime, Dict]]:
    c.execute("SELECT title, author, added, items FROM tier WHERE id = %s", (id,))
    return c.fetchall()


@db
def all_tiers(c) -> List[Tuple[str, str, datetime, Dict]]:
    c.execute('SELECT title, author, added, items FROM tier')
    return c.fetchall()


@db
def db_init(c):
    c.execute(open('init.sql').read())


db_init()
