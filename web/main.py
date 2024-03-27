from flask import Flask, request

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

# HTTP methods

@app.route('/http')
def http():
    return 'This is a %s method' % request.method

@app.route('/http2', methods=['GET','POST'])
def http2():
    if request.method == 'POST':
        return 'This is a POST method'
    else:
        return 'This is probably a GET method'

if __name__ == '__main__':
    app.run(debug=True)