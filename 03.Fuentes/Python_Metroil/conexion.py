import pyodbc 

def conex():
    
    return pyodbc.connect("Driver={SQL Server};"
                            "Server=192.168.0.14;"
                            "Database=SISMETROIL;"
                            "UID=sa;"
                            "PWD=system01;")


