import sqlite3
conn = sqlite3.connect('example.db')
sql_transaction = []
c = conn.cursor()
c.execute("""DROP TABLE patients;""")
c.execute("""DROP TABLE stocks;""")
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS patients
             (personID INT PRIMARY KEY, firstName TEXT, lastName TEXT, birthdate DATE, SSN int UNIQUE)''')

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS prescriptions
             (txn_id INT PRIMARY KEY, RxNumber INT, fillDate DATE, writtenDate DATE, patientID INT, physicianID INT)''')

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS physicians
             (physicianID INT PRIMARY KEY, birthdate TEXT, SSN INT UNIQUE)''')


# Insert a row of data
# Format: YYYY-MM-DD
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(1,'Mason','Hall','1997-05-08',12345678))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(2,'Jared','Rothstein','1996-05-07',13243414))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(3,'Cavan','Briody','1996-05-06',13412341))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(4,'Cory','Pitt','1995-05-05',59684342))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(5,'Breck','Stodghill','1994-05-04',43982404))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(6,'Dana','Zhang','1993-05-03',12340844))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(7,'Mike','Walker','1992-05-02',13458574))
c.execute("""INSERT INTO patients VALUES ({},"{}","{}","{}",{});""".format(8,'Doug','Schmidt','1991-05-01',57957881))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# c.execute("""UPDATE patients SET firstName = 'Mason', lastName = 'Hall', birthDate = '1997-05-08', ssn = 12345678 WHERE personID = 1;""")
# c.execute("""UPDATE patients SET firstName = 'Jared', lastName = 'Rothstein', birthDate = '1996-05-07', ssn = 13243414 WHERE personID = 2;""")
# c.execute("""UPDATE patients SET firstName = 'Cavan', lastName = 'Briody', birthDate = '1996-05-06', ssn = 13412341 WHERE personID = 3;""")
# c.execute("""UPDATE patients SET firstName = 'Cory', lastName = 'Pitt', birthDate = '1995-05-05', ssn = 59684342 WHERE personID = 4;""")
# c.execute("""UPDATE patients SET firstName = 'Breck', lastName = 'Stodghill', birthDate = '1994-05-04', ssn = 43982404 WHERE personID = 5;""")
# c.execute("""UPDATE patients SET firstName = 'Dana', lastName = 'Zhang', birthDate = '1993-05-03', ssn = 12340844 WHERE personID = 6;""")
# c.execute("""UPDATE patients SET firstName = 'Mike', lastName = 'Walker', birthDate = '1992-05-02', ssn = 13458574 WHERE personID = 7;""")
# c.execute("""UPDATE patients SET firstName = 'Doug', lastName = 'Schmidt', birthDate = '1991-05-01', ssn = 57957881 WHERE personID = 8;""")