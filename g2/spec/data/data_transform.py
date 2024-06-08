from typing import *
from dataclasses import dataclass, field

from g2.common import number


@dataclass
class SortByTransform:
    type: str = 'sortBy'
    fields: Optional[Union[List[str], List[str, Optional[bool]]]] = None
    """type: [field, order]; order: true => ascend, false => descend"""


@dataclass
class PickTransform:
    type: str = 'pick'
    fields: Optional[List[str]] = None


@dataclass
class RenameTransform:
    # TODO: json化后需要展开kwargs里面的参数
    kwargs: Dict[str, str]
    type: str = 'rename'


@dataclass
class FilterDataTransform:
    """由于没办法实现python->js的转换，所以这里的callback无法使用"""
    type: str = 'filter'
    callback: Optional[Callable[[Any, number, List[Any]], bool]] = None
    """The filter condition, same with 
    [Array.prototype.filter](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).
    """


@dataclass
class SliceTransform:
    type: str = 'slice'
    start: Optional[number] = None
    """The start index for slice. Default is 0."""
    end: Optional[number] = None
    """The end index for slice. Default is arr.length - 1"""


@dataclass
class SortTransform:
    """由于没办法实现python->js的转换，所以这里的callback无法使用"""
    type: str = 'sort'
    callback: Optional[Callable[[Any, Any], number]] = None
    """The sort comparator, same with 
    [Array.prototype.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort).
    """


@dataclass
class FoldTransform:
    type: str = 'fold'
    fields: Optional[List[str]] = None
    """Set fields will be folded."""
    key: Optional[str] = None
    """Fold key field, default is `key`."""
    value: Optional[str] = None
    """Fold value field, default is `value`."""


@dataclass
class JoinTransform:
    join: List[Dict[str, Any]]
    """The dataset to be joined."""
    on: str
    """Join keys of 2 dataset, [k1, k2] means join on ds1.k1 === ds2.k2. 由于python到js的限制不支持lambda函数"""
    select: List[str]
    """Selects fields from joined dataset."""
    as_: Optional[List[str]] = None
    """Rename the select fields, default: keep the original name. TODO：json格式化时需要把as_转换为as"""
    unknown: Optional[Any] = None
    """When not matched, use `unknown` instead."""
    type: str = 'join'


@dataclass
class MapTransform:
    """由于没办法实现python->js的转换，所以这里的callback无法使用"""
    type: str = 'map'
    callback: Optional[Callable[[Any], Any]] = None


@dataclass
class CustomDataTransform:
    type: str = 'custom'
    callback: Optional[Callable[[Any], Any]] = None


@dataclass
class KDEDataTransform:
    # TODO: json化时删除参数的下划线后缀
    field_: str
    """Kernel Density Estimation field."""
    groupBy: List[str]
    """Group data by fields."""
    as_: Optional[List[str]] = field(default_factory=lambda: ['y', 'size'])
    """Generate new fields, default: ['y', 'size']"""
    min: Optional[number] = None
    """Defaults to the smallest value in the array minus some threshold."""
    max: Optional[number] = None
    """Defaults to the largest value in the array plus some threshold."""
    size: Optional[number] = None
    """Number of points to represent the pdf. Defaults to 10."""
    width: Optional[number] = None
    """Determine how many points to the left and right does an element affect,
    similar to bandwidth in kernel density estimation. Defaults to 2."""
    type: str = 'kde'


@dataclass
class VennDataTransform:
    as_: List[str, str]
    """Set the generated fields, includes: [key, x, y, path]"""
    padding: Optional[number] = None
    """Canvas padding for 4 direction. Default is `0`."""
    sets: Optional[str] = None
    """Set the sets field. Default is `sets`."""
    size: Optional[str] = None
    """Set the size field for each set. Default is `size`."""
    type: str = 'venn'


@dataclass
class LogDataTransform:
    type: str = 'log'


DataTransform = Union[
    SortByTransform,
    PickTransform,
    RenameTransform,
    FilterDataTransform,
    SliceTransform,
    SortTransform,
    FoldTransform,
    JoinTransform,
    MapTransform,
    CustomDataTransform,
    KDEDataTransform,
    VennDataTransform,
    LogDataTransform,
]
