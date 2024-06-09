# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 09:55
#
# =============================================================================
"""spec"""
from typing import *
from dataclasses import dataclass

from g2.common import number, boolean

from .component import AxisComponent, LegendComponent
from .composition import Composition
from .mark import Mark


@dataclass
class G2Spec:
    extend: Union[Mark, Composition, AxisComponent, LegendComponent]
    width: Optional[number] = None
    height: Optional[number] = None
    depth: Optional[number] = None
    autoFit: Optional[boolean] = None
