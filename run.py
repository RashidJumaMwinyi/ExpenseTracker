from application import app
from gevent.pywsgi import WSGIServer



#if __name__ == "__main__":
#   app.run(debug = False)



if __name__ == '__main__':
    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()