CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
    
);

CREATE TABLE skicenters (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    location TEXT

);

CREATE TABLE info (
    id SERIAL PRIMARY KEY,
    skicenter_id INTEGER REFERENCES skicenters,
    slopes INTEGER,
    lifts INTEGER,
    park BOOLEAN,
    description TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    skicenter_id INTEGER REFERENCES skicenters,
    stars INTEGER
    
);

CREATE TABLE propositions (
    id SERIAL PRIMARY KEY,
    name TEXT,
    user_id INTEGER REFERENCES users
 
 );
    

