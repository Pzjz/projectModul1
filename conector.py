import mysql.connector

class dataBase:

    def __init__(self):
        self.cnn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            dataBase="hospital"
        )
    
    def __str__(self):
        datos=self.consulta_pacientes()
        aux=""
        for row in datos:
            aux= aux + str(row) + "\n"
        return aux
    
    def consulta_pacientes(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM pacientes")
        datos= cur.fetchall()
        cur.close()
        return datos
    
    def buscar_paciente(self,id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM pacientes WHERE nombre = {}".format(id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    
    def insertar_paciente(self,nombre,apellido,cedula,residencia,numero_Telefono,enfermedad,fecha_consulta,registro_medico):
        cur = self.cnn.cursor()
        sql= '''INSERT INTO pacientes (nombre,apellido,cedula,residencia,numero_Telefono,enfermedad,fecha_consulta,registro_medico)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(nombre,apellido,cedula,residencia,numero_Telefono,enfermedad,fecha_consulta,registro_medico)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.cursor()
        cur.close()
        return n
    
    def elimina_Paciente(self,id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM pacientes WHERE nombre = {}'''.format(id)
        n = cur.execute(sql)
        self.cnn.commit()
        cur.close()
        return n
    
    def modificar_paciente(self,nombre,apellido,cedula,residencia,numero_Telefono,enfermedad,fecha_consulta,registro_medico):
        cur = self.cnn.cursor()
        sql='''UPDATE pacientes SET nombre='{}',apellido='{}',cedula='{}',residencia='{}',numero_Telefono='{}',enfermedad='{}',fecha_consulta='{}',registro_medico='{}',
        CurrencyCode = '{}' WHERE nombre={}'''.format(nombre,apellido,cedula,residencia,numero_Telefono,enfermedad,fecha_consulta,registro_medico)
        cur.execute(sql)
        n= cur.rowcount
        self.cnn.commit()
        cur.close()
        return n