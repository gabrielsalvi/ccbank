CREATE TABLE public.client
(
    client_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    cpf VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    income NUMERIC NOT NULL,
    credit_card VARCHAR NOT NULL,
    monthly_limit NUMERIC NOT NULL,
    available_credit NUMERIC NOT NULL,
    salt BYTEA NOT NULL,
    key_pass BYTEA NOT NULL
);

CREATE TABLE public.purchase
(
    purchase_id SERIAL PRIMARY KEY,
    client_id INT,
    category VARCHAR NOT NULL,
    price NUMERIC NOT NULL,
    date VARCHAR NOT NULL,
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES client(client_id)	
);


CREATE TABLE public.administrator
(
    admin_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    salt BYTEA NOT NULL,
    key_pass BYTEA NOT NULL
);

CREATE TABLE public.limit_increase_request
(
    request_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    admin_id INT,
    new_income NUMERIC NOT NULL, 
    new_monthly_limit NUMERIC NOT NULL, 
    new_available_credit NUMERIC NOT NULL,
    status VARCHAR NOT NULL,
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES client(client_id),
    CONSTRAINT fk_admin FOREIGN KEY (admin_id) REFERENCES administrator(admin_id)	
);

