# Test suite to verify MongoDB read operations (retrieving products from the collection)

from pymongo import MongoClient
import unittest

class TestMongoRead(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient('mongodb+srv://Ankit114:123Ankit@cluster0.35cii.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client['shop_db'] 
        self.collection = self.db['products'] 

    def tearDown(self):
        self.client.close()

    def test_read_product(self):
        sample_product = {"name": "Laptop_Test_123", "price": 1200}

        self.collection.delete_one({"name": "Laptop_Test_123"})

        self.collection.insert_one(sample_product)

        result = self.collection.find_one({"name": "Laptop_Test_123"})

        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Laptop_Test_123")
        self.assertEqual(result["price"], 1200)

        self.collection.delete_one({"name": "Laptop_Test_123"})

    def test_no_product_found(self):
        result = self.collection.find_one({"name": "NonExistentProduct"})
        
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
