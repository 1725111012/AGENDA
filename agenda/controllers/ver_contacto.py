import web

render = web.template.render('views')

class Ver_contacto:
    def GET(self):
        return render.ver_contacto()