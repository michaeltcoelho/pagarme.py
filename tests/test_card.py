# coding:utf-8
import unittest

from pagarme.resources import Card


class CardHashTest(unittest.TestCase):

    def test_create(self):
        card = Card({
            'card_number': '4901720080344448',
            'card_holder_name': 'Usuario de Teste',
            'card_expiration_date': '1217',
        })
        created = card.create()

        self.assertEqual(created, True)
        self.assertEqual(card.brand, 'visa')
        self.assertEqual(card.first_digits, '490172')
        self.assertEqual(card.last_digits, '4448')

    def test_find(self):
        card = Card.find('card_cia5jg9fz0049uu6dwj0mti7c')

        self.assertEqual(card.success(), True)
        self.assertEqual(card.brand, 'visa')
        self.assertEqual(card.first_digits, '490172')
        self.assertEqual(card.last_digits, '4448')
