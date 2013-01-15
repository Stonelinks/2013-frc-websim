import sys, os
#sys.stdout = sys.stderr # mod_wsgi flips out if this isn't here
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)

import frcsim.config
import web

urls = (
  '/', 'index',
  '/(static)/(.*)', 'static',
)

render = web.template.render('templates', base='base')

class index:
  def GET(self):
    return render.index()

def main():
  print "starting webserver on localhost on port", frcsim.config.local_server_port

  # annoying hack to make webpy start on the right port locally
  sys.argv.append(str(frcsim.config.local_server_port))

  app = web.application(urls, globals(), autoreload=True)
  app.internalerror = web.debugerror
  app.run()

#app = web.application(urls, globals(), autoreload=False)
#application = app.wsgifunc()
