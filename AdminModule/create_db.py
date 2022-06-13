import sqlite3

def create_db():
    con = sqlite3.connect(database=r'../ims.db')
    # To write any querries, we need to establish a cursor
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, utype text, address text, salary text)")
    # cur.execute("INSERT INTO employee VALUES(1, 'William Admin', 'william@gmail.com', 'Male', '0300434678576', '12/12/1991', '01/01/2010', '1111', 'ADMIN', 'NY', 10000)")
    # cur.execute("INSERT INTO employee VALUES(2, 'David Manager', 'david@gmail.com', 'Male', '03003454355', '12/12/1985', '01/01/2012', '1111', 'MANAGER', 'CA', 8000)")
    # cur.execute("INSERT INTO employee VALUES(3, 'John Guard', 'john@gmail.com', 'Male', '03009887343', '12/12/1990', '01/01/2013', '1111', 'GUARD', 'DC', 7000)")
    print('employee')

    cur.execute("CREATE TABLE IF NOT EXISTS roles(id INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    #cur.execute("INSERT INTO roles VALUES(1, 'ADMIN')")
    #cur.execute("INSERT INTO roles VALUES(2, 'MANAGER')")
    #cur.execute("INSERT INTO roles VALUES(3, 'GUARD')")
    print('roles')

    cur.execute("CREATE TABLE IF NOT EXISTS visitors(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, address text, vehicle text, covisitors text, belongings text, hostname text, hostcontact text)")
    print('visitors')

    cur.execute("CREATE TABLE IF NOT EXISTS visitors_log(id INTEGER PRIMARY KEY AUTOINCREMENT, visitorid INTEGER, approved INTEGER DEFAULT 0, approvedbyemployeeid INTEGER DEFAULT NULL, createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP,entrytime TIMESTAMP DEFAULT NULL, validtill TIMESTAMP DEFAULT NULL, exittime TIMESTAMP DEFAULT NULL)")
    print('visitors_log')

    con.commit()
    # we need to run it only once to create the table and then we close it.
    print('completed')
    
create_db()
