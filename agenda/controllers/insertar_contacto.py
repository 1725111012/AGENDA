import web

render = web.template.render('views')

class Insertar_contacto:
    def GET(self):
        return render.insertar_contacto()