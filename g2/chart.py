# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/23 16:42
#
# =============================================================================
"""chart"""
from dataclasses import dataclass

from g2.api.chart_for_api import ChartForAPI
from g2.spec.chart_for_spec import ChartForSpec


@dataclass
class Chart(ChartForSpec, ChartForAPI):
    pass
