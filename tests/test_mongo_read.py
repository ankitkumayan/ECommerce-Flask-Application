from pymongo import MongoClient
import unittest

class TestMongoRead(unittest.TestCase):

    def setUp(self):
        # Set up the MongoDB client connection
        self.client = MongoClient('mongodb+srv://Ankit114:123Ankit@cluster0.35cii.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client['shop_db']  # Replace with your DB name
        self.collection = self.db['products']  # Replace with your collection name

    def tearDown(self):
        # Close the MongoDB client connection after each test
        self.client.close()

    def test_read_product(self):
        # Sample product to test with a unique name to avoid conflict
        sample_product = {"name": "Laptop_Test_123", "price": 1200}

        # Clean up any existing product with the same name before inserting
        self.collection.delete_one({"name": "Laptop_Test_123"})

        # Insert the sample product into the collection
        self.collection.insert_one(sample_product)

        # Query for the product
        result = self.collection.find_one({"name": "Laptop_Test_123"})

        # Assert that the product exists and matches the data
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Laptop_Test_123")
        self.assertEqual(result["price"], 1200)

        # Clean up the test product after the test
        self.collection.delete_one({"name": "Laptop_Test_123"})

    def test_no_product_found(self):
        # Query for a product that doesn't exist
        result = self.collection.find_one({"name": "NonExistentProduct"})
        
        # Assert that no result is found
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
