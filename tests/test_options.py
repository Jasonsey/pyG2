# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/13 14:03
#
# =============================================================================
"""test_chart"""
from g2.spec.chart_for_spec import ChartForSpec


class TestChart:
    @classmethod
    def setup_class(cls):
        cls.chart = ChartForSpec()
        cls.options = {
            'type': 'interval',
            'data': [
                {'genre': 'Sports', 'sold': 275},
                {'genre': 'Strategy', 'sold': 115},
                {'genre': 'Action', 'sold': 120},
                {'genre': 'Shooter', 'sold': 350},
                {'genre': 'Other', 'sold': 150},
            ],
            'encode': {
                'x': 'genre',
                'y': 'sold',
            },
        }

    def test_render_html(self):
        chart = self.chart.options(self.options)
        res = chart.render_html()
        print(res)

    def test_render(self):
        chart = self.chart.options(self.options)
        res = chart.render()
        print(res)
