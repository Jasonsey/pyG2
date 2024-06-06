from typing import *
from dataclasses import dataclass


@dataclass
class Transform:
    type: str


@dataclass
class TransformFilter(Transform):
    callback: Callable
    type: str = 'filter'


@dataclass
class TransformFold(Transform):
    fields: List[str]
    key: str
    value: str
    type: str = 'fold'


@dataclass
class TransformJoin(Transform):
    join: List[Dict[str, Any]]
    on: List[str]
    select: List[str]
    type: str = 'join'


@dataclass
class TransformKde(Transform):
    field: str
    groupBy: List[str]
    as_: List[str]
    type: str = 'kde'


@dataclass
class TransformLog(Transform):
    type: str = 'log'


@dataclass
class TransformMap(Transform):
    callback: Callable
    type: str = 'map'


@dataclass
class Transform(Transform):
    field: List[str]
    type: str = 'pick'


@dataclass
class TransformRename(Transform):
    renameField: List[str]
    type: str = 'rename'


@dataclass
class TransformSlice(Transform):
    start: int
    type: str = 'slice'


@dataclass
class TransformSort(Transform):
    callback: Callable
    type: str = 'sort'


@dataclass
class TransformSortBy(Transform):
    fields: List[str]
    type: str = 'sortBy'
