# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/29 15:11
#
# =============================================================================
"""chart"""
from g2 import Chart


def example_chart():
    chart = Chart(container='container', width=640, height=480)
    chart.interval().data([
        {'genre': 'Sports', 'sold': 275},
        {'genre': 'Strategy', 'sold': 115},
        {'genre': 'Action', 'sold': 120},
        {'genre': 'Shooter', 'sold': 350},
        {'genre': 'Other', 'sold': 150},
    ]).encode('x', 'genre').encode('y', 'sold').encode('color', 'genre')
    chart.render()
