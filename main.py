#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

def loto():
    loto_num = []
    loto_num_count = 0

    while loto_num_count < 7:
        num = random.randint (1, 36)
        if num not in loto_num:
            loto_num.append(num)
            loto_num_count += 1
            stevilke = sorted(loto_num)
    return stevilke

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class LotoHandler(BaseHandler):
    def get(self):
        params = {"num":loto()}
        return self.render_template("loto.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', LotoHandler),
], debug=True)
