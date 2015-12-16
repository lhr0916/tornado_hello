import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class WhoHandler(tornado.web.RequestHandler):
    def get(self, name):
        items = ["first","last","age"]
        self.render("../templates/who.html", question=items)
        # self.write("My name is " + name)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/who/([aA-zZ]+)", WhoHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8081)
    tornado.ioloop.IOLoop.current().start()