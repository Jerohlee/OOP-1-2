import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\lee\Documents\Database01.accdb;')
    print("Database is Connected")

    user_id=10
    database = connect.cursor()
    database.execute('delete from Table1 where id=?',(user_id))
    database.commit()
    print("record is deleted")


except pyodbc.Error:
    print("Error in Connection")