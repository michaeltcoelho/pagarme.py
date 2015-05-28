# coding:utf-8
import unittest

from pagarme.resources import Plan


class PlanTest(unittest.TestCase):
    def test_create(self):
        plan = {
            'name': 'Basic Plan',
            'amount': 10000,
            'days': 30,
            'trial_days': 30
        }
        plan = Plan(plan)
        self.assertEqual(plan.create(), True)

    def test_delete(self):
        plan = {
            'name': 'Basic Plan',
            'amount': 10000,
            'days': 30,
            'trial_days': 30
        }
        plan = Plan(plan)
        plan.create()
        self.assertEqual(plan.delete(), True)

    def test_find(self):
        plan = {
            'name': 'Basic Plan',
            'amount': 10000,
            'days': 30,
            'trial_days': 30
        }
        plan = Plan(plan)
        plan.create()
        plan_found = Plan.find(plan.id)
        self.assertDictEqual(plan.to_dict(), plan_found.to_dict())

    def test_all(self):
        plans = Plan.all()
        self.assertGreater(len(plans), 0)
