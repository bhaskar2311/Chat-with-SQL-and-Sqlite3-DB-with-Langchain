import sqlite3

## Connect to sqllite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table
cursor = connection.cursor()

## Create the table
table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Bhaskar','Optimization','B',83)''')
cursor.execute('''Insert Into STUDENT values('Deepti','Optimization','B',84)''')
cursor.execute('''Insert Into STUDENT values('XYZ','Optimization','E',50)''')
cursor.execute('''Insert Into STUDENT values('ABC','Statistics','A',99)''')
cursor.execute('''Insert Into STUDENT values('EFG','SML','B',86)''')

## Display all the records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit you changes in the database
connection.commit()
connection.close()
