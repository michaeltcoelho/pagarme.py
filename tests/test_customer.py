# coding:utf-8
import unittest

from pagarme.resources import Customer


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = {
            'name': 'nome do cliente',
            'document_number': '18152564000105',
            'email': 'eee@email.com',
            'born_at': '13121988',
            'gender': 'M',
            'address': {
                'street': 'Av. Brigadeiro Faria Lima',
                'complementary': '8º andar',
                'street_number': '2941',
                'zipcode': '01452000',
                'neighborhood': 'Jardim Paulistano',
                'state': 'SP',
                'country': 'Brasil'
            },
            'phone': {
                'ddi': '55',
                'ddd': '11',
                'number': '30713261'
            }
        }

    def test_create(self):
        customer = Customer(self.customer)
        customer.create()

        self.assertEqual(customer.success(), True)
        self.assertEqual(customer.name, self.customer['name'])
        self.assertEqual(customer.document_number, self.customer['document_number'])
        self.assertEqual(customer.email, self.customer['email'])

    def test_find(self):
        customer = Customer.find(17142)

        self.assertEqual(customer.success(), True)
        self.assertEqual(customer.name, self.customer['name'])
        self.assertEqual(customer.document_number, self.customer['document_number'])
        self.assertEqual(customer.email, self.customer['email'])

    def test_all(self):
        customers = Customer.all()
        customer = customers[0]

        self.assertGreater(len(customers), 0)
        self.assertEqual(customer.success(), True)
