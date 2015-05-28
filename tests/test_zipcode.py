# coding:utf-8
import unittest

from pagarme.resources import ZipCode


class ZipCodeTest(unittest.TestCase):

    def test_find_city_with_unique_cep(self):
        response = ZipCode.find('14820000')
        self.assertEqual(response.success(), True)
        self.assertEqual(response.city, u'Américo Brasiliense')
        self.assertEqual(response.state, 'SP')
        self.assertEqual(response.street, None)
        self.assertEqual(response.neighborhood, None)
        self.assertEqual(response.zipcode, '14820000')

    def test_find(self):
        response = ZipCode.find('01327000')
        self.assertEqual(response.success(), True)
        self.assertEqual(response.city, u'São Paulo')
        self.assertEqual(response.state, 'SP')
        self.assertEqual(response.street, 'Rua Treze de Maio')
        self.assertEqual(response.neighborhood, 'Bela Vista')
        self.assertEqual(response.zipcode, '01327000')

    def test_find_with_errors(self):
        response = ZipCode.find('101327000')
        self.assertEqual(response.success(), False)
        self.assertEqual(response.errors[0].message, u'CEP não encontrado')
