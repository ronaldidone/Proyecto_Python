import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-4HI2N1B5\SQLEXPRESS;'
                      'Database=SISMETROIL;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM DBO.ALMACEN')

for row in cursor:
    print(row)