#!/usr/bin/env python

from django.test import TestCase

from min_filter.templatetags.min_filter import min


class TestMin_filter(TestCase):

    def setUp(self):
        pass

    def test_filter(self):
        with self.settings(DEBUG=True):
            assert min('test.js') == 'test.js'
            assert min('test....css') == 'test....css'
            assert min('asdf') == 'asdf'
        with self.settings(DEBUG=False):
            assert min('test.js') == 'test.min.js'
            assert min('test....css') == 'test....min.css'
            assert min('asdf') == 'asdf'

    def tearDown(self):
        pass
