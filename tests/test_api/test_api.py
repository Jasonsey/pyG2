# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/22 22:28
#
# =============================================================================
"""test_api"""
from g2.api.chart_for_api import ChartForAPI


class TestAPI:
    @classmethod
    def setup_class(cls):
        cls.chart = ChartForAPI(container='container', width=640, height=480)

    def test_render(self):
        self.chart.interval().data([
            {'genre': 'Sports', 'sold': 275},
            {'genre': 'Strategy', 'sold': 115},
            {'genre': 'Action', 'sold': 120},
            {'genre': 'Shooter', 'sold': 350},
            {'genre': 'Other', 'sold': 150},
        ]).encode('x', 'genre').encode('y', 'sold').encode('color', 'genre')
        self.chart.render()
