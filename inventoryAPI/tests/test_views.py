from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from inventoryAPI.models import Category, Product
from userAPI.models import User


class CategoryAPITestCase(APITestCase):
    
    def setUp(self):
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')

    def test_list_categories(self):
        url = reverse('category')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_retrieve_category(self):
        url = reverse('category', kwargs={'pk': self.category1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Category 1')

        
class ProductAPITestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='admin', is_staff=True)
        self.category = Category.objects.create(name='Category')
        self.product = Product.objects.create(
            name='Product',
            price=10.99,
            description='Product description',
            category=self.category,
            company=self.user
        )

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product')

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': 'New Product',
            'price': 15.99,
            'description': 'New product description',
            'category': self.category.pk,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Product')

    def test_create_product_unauthenticated(self):
        url = reverse('product-list')
        data = {
            'name': 'New Product',
            'price': 15.99,
            'description': 'New product description',
            'category': self.category.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
