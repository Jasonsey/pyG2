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


@dataclass
class Chart:
    _spec: Optional[G2Spec] = None
    _options: Optional[Dict[str, Any]] = None

    def options(self, options: Dict[str, Any]):
        self._options = options

    def render(self):
        if isinstance(self._spec, G2Spec):
            self._options = as_options(self._spec)
        pass
