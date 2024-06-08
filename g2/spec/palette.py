# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 09:07
#
# =============================================================================
"""palette.py"""
from typing import *
from dataclasses import dataclass




@dataclass
class Category10Palette:
    type: str = 'category10'


@dataclass
class Category20Palette:
    type: str = 'category20'


Palette = Union[Category10Palette, Category20Palette]
PaletteTypes = Literal['category10', 'category20']
