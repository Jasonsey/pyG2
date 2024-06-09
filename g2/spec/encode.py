from typing import *
from dataclasses import dataclass

from g2.common import number


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
    kwargs: Optional[Dict[str, Any]] = None
    type: Optional[Any] = None


Encode = Union[ConstantEncode, FieldEncode, ColumnEncode, TransformEncode, CustomEncode]
