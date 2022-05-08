from flask import Flask, render_template

app = Flask(__name__)

#Decorator allows us to navigate the website
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
