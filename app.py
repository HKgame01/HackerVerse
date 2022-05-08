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
        {'id': 5, 'name': 'Microphone', 'barcode': '23455324', 'price': 50, 'AR': 'https://go.echo3d.co/ZB6b'},
        {'id': 6, 'name': 'Chair', 'barcode': '234552524', 'price': 60, 'AR': 'https://go.echo3d.co/ZB6b'},
        {'id': 7, 'name': 'Table', 'barcode': '234553224', 'price': 150, 'AR': 'https://go.echo3d.co/ZB7b'},
        {'id': 8, 'name': 'Mouse', 'barcode': '2345532224', 'price': 70, 'AR': 'https://go.echo3d.co/ZB8b'},
        {'id': 9, 'name': 'Charger', 'barcode': '236655324', 'price': 80, 'AR': 'https://go.echo3d.co/ZC9b'},
        {'id': 10, 'name': 'Bottle', 'barcode': '234565324', 'price': 15, 'AR': 'https://go.echo3d.co/ZH1b'},
        {'id': 11, 'name': 'Bagpack', 'barcode': '234255324', 'price': 70, 'AR': 'https://go.echo3d.co/ZJ2b'},
    ]
    return render_template('store.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)