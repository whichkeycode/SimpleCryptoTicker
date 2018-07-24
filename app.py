from tornado import web, ioloop, httpclient, escape
import os

class DataHandler(web.RequestHandler): 
    async def get(self):
        http = httpclient.AsyncHTTPClient()
        response = await http.fetch("https://api.binance.com/api/v1/ticker/24hr",validate_cert=False)
        self.write(response.body)      

class ViewHandler(web.RequestHandler):
    async def get(self):
        http = httpclient.AsyncHTTPClient()
        response = await http.fetch("https://api.binance.com/api/v3/ticker/price",validate_cert=False)
        trading_pairs = escape.json_decode(response.body)
        self.render('ticker.html',pairs=trading_pairs)

def app_factory():
    """
        Create a simple Tornado Web Application with two 'get' endpoints:
             '/' - Cryptocurrency Ticker View 
             '/data' - Retrieve Ticker data from the Binance REST API (https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md)
    """
    settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}
    return web.Application([
        (r'/', ViewHandler),
        (r'/data', DataHandler),
    ],**settings)

if __name__ == '__main__':
    app  = app_factory()
    app.listen(8888)
    ioloop.IOLoop.current().start()
