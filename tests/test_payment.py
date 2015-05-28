# coding:utf-8
import unittest

from pagarme.resources import Payment


class PaymentTest(unittest.TestCase):

    def test_all(self):
        payables = Payment.all()
        self.assertGreater(len(payables), 0)