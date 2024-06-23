# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/9 22:52
#
# =============================================================================
"""test_g2"""
from g2.spec import G2Spec
from g2.spec.mark import LineMark


def test_mark():
    mark = LineMark()
    a = G2Spec(extend=mark)
    print(a)
