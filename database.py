import psycopg2

host = "localhost"
database = "ccbank"
user = "postgres"
password = "allrights"

# connect to the db
conn = psycopg2.connect(
    host = host,
    database = database, 
    user = user, 
    password = password, 
)

#cursor
cur = conn.cursor()

# execute insert query
# cur.execute("INSERT INTO teste_table (id, name) VALUES (%s, %s)", (9, 'Murilo'))

# # execute select query
# cur.execute("SELECT id, name FROM teste_table;")

#
# rows = cur.fetchall()

# for row in rows:
#     print(f"id: {row[0]} name: {row[1]}")

# send the new inserts to db
# conn.commit()

# # close the cursor
# cur.close()

# # close the connection
# conn.close()    