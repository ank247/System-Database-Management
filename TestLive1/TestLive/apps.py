# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class TestliveConfig(AppConfig):
    name = 'TestLive'

    def ready(self):
        import TestLive.signals
