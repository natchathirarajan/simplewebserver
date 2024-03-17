from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Revenue Table</title>
<caption><h2>COMPANY REVENUE TABLE </h2></caption>
</head>
<body>
<table border ="2" cellpadding="2" width="600" height="300" bgcolor="black">
<tr bgcolor="Brown">
<th>s.no</th>
<th>Company Name</th>
<th>USD($) in Billon</th>
<th>Country</th>
<th>Industry</th>
</tr>
<tr bgcolor="pink">
<td>1</td>
<td>Apple</td>
<td>961.3</td>
<td>USA</td>
<td>Tech</td>
</tr>
<tr bgcolor="gray">
<td>2</td>
<td>Microsoft</td>
<td>946.5</td>
<td>USA</td>
<td>Tech</td>
</tr>
<tr bgcolor="pink">
<td>3</td>
<td>Amazon.com</td>
<td>916.1</td>
<td>USA</td>
<td>Tech</td>
</tr>
<tr bgcolor="gray">
<td>4</td>
<td>Alphabet</td>
<td>863.2</td>
<td>USA</td>
<td>Tech</td>
</tr>
<tr bgcolor="pink">
<td>5</td>
<td>Berkshire Hathaway</td>
<td>516.4</td>
<td>USA</td>
<td>Financials</td>
</tr>
<tr bgcolor="gray">
<td>6</td>
<td>Alibab</td>
<td>480.8</td>
<td>China</td>
<td>Tech</td>
</tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("Company Revenue  webserver is running...")
httpd.serve_forever()