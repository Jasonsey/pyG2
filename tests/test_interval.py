# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/10 14:35
#
# =============================================================================
"""test_interval"""
from g2.spec import G2Spec
from g2.spec.mark import IntervalMark
from g2.spec.data import InlineConnector
from g2.spec.encode import FieldEncode

from g2.utils.common import spec2options


def test_interval():
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
    spec = G2Spec(
        extend=mark
    )
    print(spec)


def test_as_options():
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
    spec = G2Spec(
        extend=mark
    )
    options = spec2options(spec)
    print(options)
