from flask import Flask, render_template

app = Flask(__name__)

#Decorator allows us to navigate the website
@app.route('/')
@app.route('/home')

def home_page():
    return render_template('home.html')

#AR Models are found on sketchfab.com
@app.route('/store')
def store_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '99944432', 'price': 500, 'AR':'https://go.echo3d.co/31qu'},
        {'id': 2, 'name': 'Laptop', 'barcode': '34059943', 'price': 900, 'AR':'https://go.echo3d.co/sZES'},
        {'id': 3, 'name': 'Keyboard', 'barcode': '23143512', 'price': 150, 'AR': 'https://go.echo3d.co/cgi7'},
        {'id': 4, 'name': 'Microphone', 'barcode': '23455324', 'price': 50, 'AR': 'https://go.echo3d.co/ZB6b'}
    ]
    return render_template('store.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)