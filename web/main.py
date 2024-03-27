from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a web page :)'

# Routing & variables

@app.route('/user/<username>')
def user(username):
    return '<h1>Hi %s, how are you doing ?</h1>' % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h1>Post number %s.</h1>' % post_id 

if __name__ == '__main__':
    app.run(debug=True)