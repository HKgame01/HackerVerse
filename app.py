from flask import Flask, render_template

app = Flask(__name__)

#Decorator allows us to navigate the website
@app.route('/')
@app.route('/home')

def home_page():
    return render_template('home.html')

@app.route('/store')
def store_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500, 'AR':''},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900, 'AR':''},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150, 'AR': ''}
    ]
    return render_template('store.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)