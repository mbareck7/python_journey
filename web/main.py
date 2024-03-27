from flask import Flask, request, render_template

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
    
# HTML templates
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

# Mapping multiple URLs
@app.route('/login')
@app.route('/login/<user>')
def login(user=None):
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)