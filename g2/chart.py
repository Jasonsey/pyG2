# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/11 00:40
#
# =============================================================================
"""chart"""
from typing import *
from dataclasses import dataclass

from .spec import G2Spec
from .common import as_options
from .plot import Plot


@dataclass
class Chart(Plot):
    spec: Optional[G2Spec] = None

    def set_spec(self, spec: G2Spec):
        self.spec = spec
        return self

    def dump_options(self):
        """处理options关联内容"""
        if isinstance(self.spec, G2Spec):
            self.options = as_options(self.spec)
        super().dump_options()
