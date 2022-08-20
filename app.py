from flask import Flask

app= Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return 'hello world'



@app.route('/about')
def about():
    return 'about us'


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return 'user page' + name + "-" + id



if __name__== '__name__':
    app.run(debug=True)