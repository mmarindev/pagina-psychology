from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('indexx.html')

@app.route('/about')

def about():
    return render_template('about.html')
@app.route('/contact')

def contact():
    return render_template('contact.html')

@app.route('/services')

def services():
    return render_template('services.html')

@app.route('/blog')

def blog():
    return render_template('blog.html')
if __name__ == '__main__':
    app.run(debug=True)