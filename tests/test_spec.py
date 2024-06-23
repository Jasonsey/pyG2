# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/13 14:03
#
# =============================================================================
"""test_chart"""
from g2.spec.chart_for_spec import ChartForSpec
from g2.spec.data import InlineConnector
from g2.spec.mark import IntervalMark
from g2.spec.encode import FieldEncode
from g2.spec import G2Spec


class TestChart:
    @classmethod
    def setup_class(cls):
        cls.chart = ChartForSpec()
        data = InlineConnector(value=[
            {'genre': 'Sports', 'sold': 275},
            {'genre': 'Strategy', 'sold': 115},
            {'genre': 'Action', 'sold': 120},
            {'genre': 'Shooter', 'sold': 350},
            {'genre': 'Other', 'sold': 150},
        ])
        mark = IntervalMark(
            data=data,
            encode={'x': FieldEncode(value='genre'), 'y': FieldEncode(value='sold')},
        )
        cls.spec = G2Spec(extend=mark)

    def test_render_html(self):
        chart = self.chart.options(self.spec)
        res = chart.render_html()
        print(res)

    def test_render(self):
        chart = self.chart.options(self.spec)
        res = chart.render()
        print(res)
