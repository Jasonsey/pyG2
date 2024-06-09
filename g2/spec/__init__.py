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
class G2SpecBasic:
    width: Optional[number] = None
    height: Optional[number] = None
    depth: Optional[number] = None
    autoFit: Optional[boolean] = None


@dataclass
class G2SpecMark(Mark, G2SpecBasic):
    pass


@dataclass
class G2SpecComposition(Composition, G2SpecBasic):
    pass


@dataclass
class G2SpecAxisComponent(AxisComponent, G2SpecBasic):
    pass


@dataclass
class G2SpecLegendComponent(LegendComponent, G2SpecBasic):
    pass


G2Spec = Union[G2SpecMark, G2SpecComposition, G2SpecAxisComponent, G2SpecLegendComponent]
