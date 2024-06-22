# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/6 23:20
#
# =============================================================================
"""common"""
import datetime
import re
from typing import *
from dataclasses import dataclass, asdict, is_dataclass
from typing import Optional

import simplejson

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


SEP = "!!-_-____-_-!!"


class JS:
    def __init__(self, js_code: str):
        self.js_code = "%s%s%s" % (SEP, js_code, SEP)

    def replace(self, pattern: str, repl: str):
        self.js_code = re.sub(pattern, repl, self.js_code)
        return self


def _json_dump_default(o: object):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, JS):
        return o.replace("\\n|\\t", "").replace(r"\\n", "\n").replace(r"\\t", "\t").js_code
    return o


def json_dump_to_js(options: object):
    return re.sub(
        '"?%s"?' % SEP,
        "",
        simplejson.dumps(options, indent=2, default=_json_dump_default, ignore_nan=True)
    )


class HTML:
    def __init__(self, data: Optional[str] = None):
        self.data = data

    def _repr_html_(self):
        return self.data

    def __html__(self):
        return self._repr_html_()
