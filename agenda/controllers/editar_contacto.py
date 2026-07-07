import web
import sqlite3

render = web.template.render('views', base='layout')

class Editar_contacto:
    
    def buscarContacto(self, id_contacto:int):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto= ?"
            cursor.execute(query, (id_contacto,))            
            
            row = cursor.fetchone()
            contactos = []
            
            if row:
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                contactos.append(contacto)

            conn.close()     
            return contactos
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        finally:
            if conn:
                conn.close()

    def GET(self, id_contacto):
        contacto = self.buscarContacto(id_contacto)
        if contacto:
            return render.editar_contacto(contacto[0])
        else:
            return "Contacto no encontrado"