import conexion

conn = conexion.conex()
cursor = conn.cursor()

my_dict = {}
my_dict = dict([('param1',76464), ('param2',2)])

sql = " exec [dbo].[sp_py_datos_certificado] @CH_NRO_EXPEDIENTE = ?, @ITEM = ? "
prm = (my_dict.get('param1'),my_dict.get('param2'))
cursor.execute(sql, prm)

for row in cursor:
    print(row)

    