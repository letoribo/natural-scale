#!/usr/bin/env python
import webapp2
import os
 
from google.appengine.ext.webapp import template
 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, 'home.html')
        template_values = ''
        self.response.out.write(template.render(path, template_values))
                                          
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
