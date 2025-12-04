from flask import Flask, request, send_from_directory, redirect, url_for, render_template_string
from pathlib import Path

app = Flask(__name__, static_url_path='', static_folder='.')
ROOT = Path(__file__).parent

@app.route('/', methods=['GET'])
def index():
    # Serve the static task1.html file from the workspace root
    return send_from_directory(str(ROOT), 'task1.html')


@app.route('/login', methods=['POST'])
def login():
    # Simple server-side validation — check for non-empty username and password
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()

    if not username or not password:
        # If fields are missing, redirect back with a simple message (could be improved)
        return render_template_string(
            '<h2>Login error</h2><p>Missing username or password. <a href="/">Back</a></p>'
        ), 400

    # On 'successful' login: print the username to the server console and show confirmation
    print(f"User logged in: {username}")

    return render_template_string(
        '<h2>Login successful</h2>'
        '<p>Welcome, <strong>{{username}}</strong>.</p>'
        '<p><a href="/">Back to home</a></p>',
        username=username,
    )
if __name__ == '__main__':
    # Run on localhost port 5000 — development only
    app.run('127.0.0.1', 5000, debug=True)
