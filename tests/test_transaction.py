# coding:utf-8
import os
import unittest

from pagarme.transaction import Transaction


class TransactionTest(unittest.TestCase):

    def setUp(self):
        self.encryption_key = os.environ['PAGARME_ENCRYPTION_KEY']