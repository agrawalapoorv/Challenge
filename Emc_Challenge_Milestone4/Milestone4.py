import SimpleHTTPServer
import SocketServer

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
      # Your code here
      print "Client requested:", self.command, self.path

      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8888

httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "Serving at port:", PORT
httpd.serve_forever()