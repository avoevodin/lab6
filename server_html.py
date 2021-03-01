from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus
from dp_grasshopper import count_min_cost


def response():
    min_cost, min_cost_route = count_min_cost(6, [2, 5, 10, 4, 0, 5])
    return """<!doctype html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                      content="width=device-width, user-scalable=no, 
                        initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Grasshopper</title>
            </head>
            <body>
            <h1>Count min cost route for grasshopper</h1>
            <hr>
            <div>Min cost: {}</div>
            <div>Min cost route: {}</div>
            </body>
            </html>""".format(min_cost, min_cost_route)


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(response().encode())


httpd = HTTPServer(('0.0.0.0', 8000), Handler)
httpd.serve_forever()
