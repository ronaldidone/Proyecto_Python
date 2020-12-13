import pyodbc 

def conex():
    
    return pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-4HI2N1B5\SQLEXPRESS;'
                      'Database=SISMETROIL;'
                      'Trusted_Connection=yes;')