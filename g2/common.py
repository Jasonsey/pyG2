# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/6 23:20
#
# =============================================================================
"""common"""
from typing import *
from dataclasses import dataclass, asdict, is_dataclass

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


def spec2options(data: Union[list, tuple, dict, Any], /, *, strip_param=True):
    if isinstance(data, (list, tuple)):
        res = []
        for item in data:
            item = spec2options(item, strip_param=strip_param)
            res.append(item)
    elif isinstance(data, dict):
        res = {}
        for key, value in data.items():
            value = spec2options(value, strip_param=strip_param)
            res[key] = value
    elif is_dataclass(data):
        res = {}
        for key, value in data.__dict__.items():
            if value is None or (isinstance(value, (dict, list, tuple)) and len(value) == 0):
                continue
            if strip_param:
                key = key.strip('_')
            if key == 'kwargs':
                value = spec2options(value, strip_param=strip_param)
                res.update(value)
            elif key == 'extend':
                value = spec2options(value, strip_param=strip_param)
                if isinstance(value, (list, tuple)):
                    for item in value:
                        res.update(item)
                else:
                    res.update(value)
            else:
                value = spec2options(value, strip_param=strip_param)
                res[key] = value
    else:
        # 非dataclass
        res = data
    return res


def as_options(obj):
    assert is_dataclass(obj)
    data = spec2options(obj)
    return data
