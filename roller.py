#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from urllib import unquote_plus

from bottle import Bottle, run, static_file, view, request


app = Bottle()

@app.route('/')
@app.route('/<reminder>')
@view('reminder')
def reminder(reminder='Remind yourself to send a reminder!'):
    return dict(
        reminder=unquote_plus(reminder),
        get_url=app.get_url,
        background_color=request.query.background_color,
        color=request.query.color
    )

@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

if __name__ == '__main__':
    app.run(
        server='gunicorn',
        workers=1,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
#        host='localhost',
#        port=8080,
        debug=True
    )
