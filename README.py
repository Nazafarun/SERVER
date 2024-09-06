from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("178.197.210.21", 80)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print('start server')
print("192.168.56.1:1111")
httpd.serve_forever()
