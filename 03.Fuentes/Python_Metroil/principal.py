import conexion
import pyodbc

try:
    conn = conexion.conex()
    cursor = conn.cursor()

    Expediente=int(input('Expediente: '))
    Certificado=int(input('Certificado: '))
    Anio=int(input('Año: '))
    OTI=int(input('Ingrese OTI: '))
    Output = ""
    

    sql =" EXEC [dbo].[sp_py_ins_certificado]  ?, ?, ?,  ?, ?;"

    prm = (Expediente,Certificado,Anio,OTI,Output)

    cursor.execute(sql, prm)
    return_value=cursor.fetchone()
    print(return_value)
    conn.commit()
    conn.close()

except Exception as p:
    print(p)
    conn.close()




    
