from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # This is the "Home" route
def hello():
    # Server-side variable
    message = "Hello WIC!" # Though this variable is simple, imagine how complex this could be if we pulled it through from a database
    return render_template('index.html', message=message) # We are "rendering" the HTML, meaning we are building a page then sending it to a user

if __name__ == '__main__':
    app.run()