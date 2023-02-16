import psycopg2         #allias name of psycopg2 as pc
import psycopg2.extras

# All this creditnals are available in pgadmin

hostname = 'localhost'
database = 'finance_management_system'
username = 'postgres'
pwd = 'password'  # Note me password likha hai
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(host = hostname, dbname = database, user = username, password = pwd, port = port_id)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS customer")
    create_script = '''CREATE TABLE IF NOT EXISTS customer (
                            id         int PRIMARY KEY,
                            name       varchar(40) NOT NULL,
                            email      varchar(40) NOT NULL,
                            cont_no    numeric(10)   )'''

    cur.execute(create_script)
    insert_script = 'INSERT INTO customer(id,name,email,cont_no) VALUES (%s,%s,%s,%s)'
    insert_value = (1,"Abhijeet","random123@gmail.com",8181818181)
    cur.execute(insert_script,insert_value)
    #for mutliple value to be insert then we can use for loop
    cur.execute('SELECT * FROM customer')
    print(cur.fetchall())
    conn.commit()


except Exception as error:
    print(f"Failed to connect: {error}")

finally:
    if cur is not None:
        cur.close()  #Close the cursor before leaving
    if conn is not None:
        conn.close() #Close the connection before leaving 