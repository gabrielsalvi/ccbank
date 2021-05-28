# Credit Card System <br><br>

## Tecnologies used:

---

* Python; 
* PostgresSQL (with psycopg2); <br><br>

## Description:

---

The system basically consists of the actions of the two types of users: **administrator** and **client**. <br><br>

The **administrator** is capable of: 
* Register other administrators;
* Register, alter and delete clients;
* See a list of all the clients;
* Decide to approval or deny a limit change request made by a client. <br><br>

The **client** is capable of:
* Add expenses and/or purchases;
* Request the generation of his bank statement;
* Request a new monthly credit limit;
* Change his password;<br><br>

## What I've learned Working With This Project:

---

* Integrate Python and PostgreSQL using Psycopg;
* Work with monetary values in a proper way;
* Handle with passwords: The code generates a unique salt for every password. After that, it encrypts the password with a PBKDF2_HMAC method, generating a key. So, the database only stores the sault and the key, not the password. See it below:<br>

	```python
	import os
	import hashlib

	salt = os.urandom(32)

	key = hashlib.pbkdf2_hmac(
      'sha256', # the hash digest algorithm for HMAC
      password.encode('utf-8'),  # convert the password to bytes
      salt,
      100000,  # number of iterations of SHA-256 (recommended to use at least 100,000)
	)
* How to use classes;
* How to use dictionaries; <br><br>

## Additional Information:

---

This application was the final project for the subject Algorithms and Programming, in the 1º semester of Computer Science at UFFS. Now, I'm using it to learn new concepts and improve my programming skills. <br><br>
