import web

urls = (
    '/', 'Index',
        '/registro', 'Registro',
        '/lista_contactos', 'ListaContactos'


)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class Registro:
    def GET(self):
            return render.registro()

class ListaContactos:
    def GET(self):
            return render.lista_contactos()

if __name__ == "__main__":
    app.run()