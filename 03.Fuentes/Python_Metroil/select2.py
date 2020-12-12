import conexion
import pyodbc

conn = conexion.conex()
cursor = conn.cursor()

sql = "EXEC [dbo].[test2_for_pyodbc] @param1_in = ?,@param2_in = ?;"

params = ("PAR1","PAR2")
cursor.execute(sql, params)
rows = cursor.fetchall()
while rows:
    print(rows)
    if cursor.nextset():
        rows = cursor.fetchall()
    else:
        rows = None