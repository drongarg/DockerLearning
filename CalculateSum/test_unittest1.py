from apps import calsum
from unittest import TestCase

class TryTesting(TestCase):
    def test_first(self):
        a=4
        b=6
        
        assert calsum(a,b)==10, "test failed"

