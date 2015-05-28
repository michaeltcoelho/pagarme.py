# coding:utf-8
import unittest

from pagarme.resources import CardHash


class CardHashTest(unittest.TestCase):

    def setUp(self):
        self.card = {
            'card_number': '4901720080344448',
            'card_holder_name': 'Usuario de Teste',
            'card_expiration_date': '1217',
            'card_cvv': '314'
        }

    def test_generate_hash_key(self):
        response = CardHash.generate_hash_key(self.card)
        self.assertEqual(response.success(), True)
