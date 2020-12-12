import conexion
import pyodbc

conn = conexion.conex()
cursor = conn.cursor()

sql = """\
DECLARE @out nvarchar(max);
EXEC [dbo].[test_for_pyodbc] @param_in = ?, @param_out = @out OUTPUT;
SELECT @out AS the_output;
"""
params = ("Burma!", )
cursor.execute(sql, params)
rows = cursor.fetchall()
while rows:
    print(rows)
    if cursor.nextset():
        rows = cursor.fetchall()
    else:
        rows = None