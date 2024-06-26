# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/11 00:40
#
# =============================================================================
"""chart"""
from dataclasses import dataclass

from g2.spec import G2Spec
from g2.utils.common import dump_to_js_string
from g2.core.plot import PlotForSpec
from g2.core.chart import ChartBase


@dataclass
class ChartForSpec(PlotForSpec, ChartBase):

    def options(self, value: dict | G2Spec):
        value = dump_to_js_string(value)
        self.js_options = value
        return self
