"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from datetime import datetime, timedelta
from models import A, B

class TestQuerySets(TestCase):
    def setUp(self):
        for i in [1,2]:
            a1 = A.objects.create(name='a1')
            a2 = A.objects.create(name='a2')

            for d in range(0, 5):
                print datetime.now()-timedelta(days=d), datetime.now()

                B.objects.create(start=datetime.now()-timedelta(days=d),
                                 end=datetime.now(),
                                 A=a1,
                                 num=i)

    def test_normal_query(self):
        self.assertEqual(len(A.objects.filter(name='a1')), 2)
        self.assertEqual(len(A.objects.filter(name='a2')), 2)
        self.assertEqual(len(A.objects.filter(name='a1').select_related()), 2)

    def test_weirdness(self):
        self.assertEqual(len(A.objects.filter(b__num=1)), 5)
        self.assertEqual(len(A.objects.filter(b__num=1).distinct()), 1)

        print A.objects.filter(b__start__gte=datetime.now()-timedelta(days=5),
                               b__end__lte=datetime.now(),
                               name='a1')
