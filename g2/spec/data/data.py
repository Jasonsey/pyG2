from typing import *
from dataclasses import dataclass

from .data_transform import Transform


@dataclass
class Data:
    type: str


@dataclass
class DataCustom(Data):
    callback: Callable
    type: str = 'custom'


@dataclass
class DataFetch(Data):
    value: str
    transform: List[Transform]
    type: str = 'fetch'
    

@dataclass
class DataInline(Data):
    value: List[Dict[str, AnyStr]]
    transform: List[Transform]
    type: str = 'inline'
