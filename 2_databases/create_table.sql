CREATE TABLE IF NOT EXISTS car (
	model_id serial PRIMARY KEY,
	model_name VARCHAR ( 4000 ),
	manufacturer VARCHAR ( 4000 ),
	weight NUMERIC(12,3)
);

CREATE TABLE IF NOT EXISTS transaction (
	transaction_id serial PRIMARY KEY,
	model_id INT,
	serial_number VARCHAR ( 400 ),
	salesperson VARCHAR ( 400 ),
	customer_id INT,
	price NUMERIC(12,2),
	transaction_datetime TIMESTAMP
);


CREATE TABLE IF NOT EXISTS customer (
	customer_id serial PRIMARY KEY,
	name VARCHAR ( 400 ),
	phone VARCHAR ( 400 )
);