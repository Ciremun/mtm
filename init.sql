CREATE TABLE IF NOT EXISTS 
tier(id serial primary key, title text NOT NULL, author text NOT NULL, timestamp added NOT NULL, items json NOT NULL);