import unittest
from mock import patch

from app import get_orders_by_customer


class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_order_by_customer_bad_cust_name(self):
        results = get_orders_by_customer('bad name')
        assert results == []
