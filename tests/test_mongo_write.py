from pymongo import MongoClient
import unittest

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        """Set up the MongoDB client and collection."""
        self.client = MongoClient('mongodb+srv://Ankit114:123Ankit@cluster0.35cii.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client['shop_db']
        self.collection = self.db['products']

    def test_insert_document(self):
        """Test if a document can be inserted and verified."""
        test_document = {'name': 'Test Product', 'price': 10.99}
        insert_result = self.collection.insert_one(test_document)

        # Query the document
        fetched_document = self.collection.find_one({'_id': insert_result.inserted_id})
        self.assertIsNotNone(fetched_document)
        self.assertEqual(fetched_document['name'], 'Test Product')

        # Clean up
        self.collection.delete_one({'_id': insert_result.inserted_id})

if __name__ == "__main__":
    unittest.main()
