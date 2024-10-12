
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection URI
client = MongoClient('mongodb+srv://ankit26114:123Ankit@cluster0.vgyrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Connect to the database and collection
db = client['shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # Fetch product data from MongoDB
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
