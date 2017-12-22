from functools import wraps

from flask import redirect, request, session, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authorized' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
