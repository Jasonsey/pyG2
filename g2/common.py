# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/6 23:20
#
# =============================================================================
"""common"""
from typing import *
from typing import Literal

number = Union[int, float]
Primitive = Union[int, float, str]
string = str
boolean = bool
ChannelTypes = Literal[
    'x',
    'y',
    'z',
    'x1',
    'y1',
    'series',
    'color',
    'opacity',
    'shape',
    'size',
    'key',
    'groupKey',
    'position',
    'series',
    'enterType',
    'enterEasing',
    'enterDuration',
    'enterDelay',
    'updateType',
    'updateEasing',
    'updateDuration',
    'updateDelay',
    'exitType',
    'exitEasing',
    'exitDuration',
    'exitDelay',
]
