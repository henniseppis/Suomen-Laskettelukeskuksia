CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
    
);

CREATE TABLE skicenters (
    id SERIAL PRIMARY KEY,
    name TEXT,
    location TEXT

);

CREATE TABLE info (
    id SERIAL PRIMARY KEY,
    skicenter_id INTEGER REFERENCES skicenters,
    slopes INTEGER,
    lifts INTEGER,
    stars INTEGER
    
);


