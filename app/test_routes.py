# app/test_routes.py

import unittest
import json
from app import create_app, db
from app.models import Item

class TestRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        cls.app_context.pop()

    def test_create_item(self):
        response = self.client.post('/item', json={'name': 'Test Item', 'description': 'This is a test item'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Item created successfully!', response.get_data(as_text=True))

    def test_get_items(self):
        self.client.post('/item', json={'name': 'Test Item', 'description': 'This is a test item'})
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Item', response.get_data(as_text=True))

    def test_update_item(self):
        item = Item(name='Old Name', description='Old Description')
        db.session.add(item)
        db.session.commit()
        response = self.client.put(f'/item/{item.id}', json={'name': 'New Name', 'description': 'New Description'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item updated successfully!', response.get_data(as_text=True))

    def test_delete_item(self):
        item = Item(name='To Be Deleted', description='Delete me!')
        db.session.add(item)
        db.session.commit()
        response = self.client.delete(f'/item/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item deleted successfully!', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
