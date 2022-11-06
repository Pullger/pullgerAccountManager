from pullgerAccountManager.tests.tools import unitOperationsAM
from django.test import TestCase


class Test001API(TestCase):
    def test_001_add_account(self):
        unitOperationsAM.add_account(self)
