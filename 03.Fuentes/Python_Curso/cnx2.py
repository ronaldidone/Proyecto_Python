import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-4HI2N1B5\SQLEXPRESS;'
                      'Database=SISMETROIL;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('exec [dbo].[sp_cd_lst_laboratorio]')

rows = cursor.fetchall()

while rows:
    print(rows)
    if cursor.nextset():
        rows = cursor.fetchall()
    else:
        rows = None