from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

MONGODB_USERNAME = os.getenv('Ankit114')
MONGODB_PASSWORD = os.getenv('123Ankit')

app = Flask(__name__)

client = MongoClient(f'mongodb+srv://Ankit114:123Ankit@cluster0.35cii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client['shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
