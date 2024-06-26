# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 09:55
#
# =============================================================================
""" G2 中编码（Encode） 主要用于指定视觉元素属性和数据之间的关系 """
from typing import *
from dataclasses import dataclass

from g2.utils.common import number


@dataclass
class ConstantEncode:
    type: str = 'constant'
    value: Optional[Any] = None


@dataclass
class FieldEncode:
    type: str = 'field'
    value: Optional[str] = None


@dataclass
class ColumnEncode:
    type: str = 'column'
    value: Optional[List[Any]] = None


@dataclass
class TransformEncode:
    type: str = 'transform'
    value: Optional[Callable[
        [Dict[str, Any], number, List[Dict[str, Any]]],
        Any
    ]] = None


@dataclass
class CustomEncode:
    type: Optional[Any] = None
    kwargs: Optional[Dict[str, Any]] = None


Encode = Union[ConstantEncode, FieldEncode, ColumnEncode, TransformEncode, CustomEncode]
