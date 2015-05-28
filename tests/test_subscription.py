# coding:utf-8
import unittest

from pagarme.resources import Subscription, Plan, CardHash


class SubscriptionTest(unittest.TestCase):
    def setUp(self):
        self.card = {
            'card_number': '4901720080344448',
            'card_holder_name': 'Usuario de Teste',
            'card_expiration_date': '1217',
            'card_cvv': '314'
        }

    def test_create(self):
        hash_k = CardHash.generate_hash_key(self.card)
        subscription = Subscription({
            'plan_id': 16665,
            'card_hash': hash_k.card_hash,
            'postback_url': 'http://requestb.in/vg98k2vg',
            'customer': {
                'email': 'eee@email.com'
            },
            'metadata': {
                'id': 123
            }
        })
        created = subscription.create()
        self.assertEqual(created, True)

    def test_update(self):
        hash_k = CardHash.generate_hash_key(self.card)

        plan = Plan({
            'name': 'No Trial Days Plan',
            'amount': 30000,
            'days': 30,
            'trial_days': 0
        })
        plan.create()

        subscription = Subscription({
            'plan_id': plan.id,
            'card_hash': hash_k.card_hash,
            'postback_url': 'http://requestb.in/vg98k2vg',
            'customer': {
                'email': 'eee@email.com'
            },
            'metadata': {
                'id': 123
            }
        })
        created = subscription.create()

        self.assertEqual(created, True)
        self.assertEqual(subscription.plan.id, plan.id)

    def test_cancel(self):
        subscriptions = Subscription.all()[-1:]
        subscription = subscriptions[0]
        subscription.cancel()
        self.assertEqual(subscription.success(), True)
        self.assertEqual(subscription.status, 'canceled')

    def test_transactions(self):
        subscription = Subscription.find(18543)
        transaction = subscription.transactions()[0]
        self.assertEqual(transaction.success(), True)
        self.assertIsNotNone(transaction.card)
        self.assertIsNotNone(transaction.customer)

    def test_find(self):
        subscription = Subscription.find(18541)
        self.assertEqual(subscription.success(), True)
        self.assertEqual(subscription.id, 18541)
        self.assertEqual(subscription.card.holder_name, 'Usuario+de+Teste')

    def test_all(self):
        subscriptions = Subscription.all()
        subscription = subscriptions[0]
        self.assertEqual(subscription.success(), True)
        self.assertGreater(len(subscriptions), 0)
