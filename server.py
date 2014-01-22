#!/usr/bin/python
import cherrypy
import os
import sysinfo as sysinfo
from mako.template import Template
from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=['./templates'])
dirMedia = os.path.join(os.path.abspath("."), u"media")

class HelloWorld(object):
  
  @cherrypy.expose
  def index(self):
    tmpl = lookup.get_template("index.html")
    
    total,used,free = sysinfo.diskUsage("/")
    
    top = sysinfo.top(20)
    
    title = sysinfo.hostInfo()
    print "title", title
    return tmpl.render(free=free,used=used,top=top,title=title)
  
  @cherrypy.expose
  def top(self, numlines=20, *args, **kw):
    return sysinfo.top(numlines);
conf = {
    '/media':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': dirMedia,
                },
    'global': {
        'server.socket_host': '192.168.1.109',
        'server.socket_port': 8080,
    }
}

cherrypy.quickstart(HelloWorld(), "/", config=conf)
