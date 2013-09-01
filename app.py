from urllib import unquote_plus

from bottle import Bottle, run, static_file, view, request


app = Bottle()

@app.route('/')
@app.route('/<reminder>')
@view('reminder')
def index(reminder='Remind yourself to send a reminder!'):
    background_color = request.query.background_color
    color = request.query.color
    return dict(reminder=unquote_plus(reminder), get_url=app.get_url,
                background_color=background_color, color=color)

@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(app, host='localhost', port=8080, debug=True)
