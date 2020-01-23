# coding: utf-8
import tornado.web, tornado.gen
from tornado.escape import json_encode, json_decode
from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

class IndexHandler(MainHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("<h1>heyyyyy</h1>")


class SecondHandler(MainHandler):
    def get(self):
        self.render("index.html")


class DetailModule(tornado.web.UIModule):
    def render(self, res):
        tps = ["Hello", "Hi", "Test"]
        return self.render_string("modules/detail.html", tps=tps, res=res)

class Auth(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("admin")


# let the magic of multiple inheritece ;)
class Comments(MainHandler, Auth):
    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        cursor = db.message.find()
        comments = yield cursor.to_list(length=None)
        self.render("comments.html", comments=comments)
