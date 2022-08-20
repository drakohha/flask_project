from flask import Flask , url_for , render_template


app= Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")



@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return 'user page: ' + name + "-" + str(id)



if __name__== '__name__':
    app.run(debug=True)