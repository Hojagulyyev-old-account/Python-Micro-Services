from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<username>/")
def hello(username):
    if username:
        return "<h1>Hello %s</h1>" % username.title()
    else:
        return "<h1>Hello world</h1>"


if __name__ == '__main__':
    app.run(debug=True)

'''
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
'''
