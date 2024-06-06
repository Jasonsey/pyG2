from typing import *
from dataclasses import dataclass, field

from g2.common import number


@dataclass
class SortByTransform:
    type: str = 'sortBy'
    # /** type: [field, order]; order: true => ascend, false => descend */
    fields: Optional[Union[List[str], List[str, Optional[bool]]]] = None


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
    # The filter condition, same with [Array.prototype.filter](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).
    callback: Optional[Callable[[Any, number, List[Any]], bool]] = None


@dataclass
class SliceTransform:
    type: str = 'slice'
    # The start index for slice. Default is 0.
    start: Optional[number] = None
    # The end index for slice. Default is arr.length - 1
    end: Optional[number] = None


@dataclass
class SortTransform:
    """由于没办法实现python->js的转换，所以这里的callback无法使用"""
    type: str = 'sort'
    # The sort comparator, same with [Array.prototype.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort).
    callback: Optional[Callable[[Any, Any], number]] = None


@dataclass
class FoldTransform:
    type: str = 'fold'
    # Set fields will be folded.
    fields: Optional[List[str]] = None
    # Fold key field, default is `key`.
    key: Optional[str] = None
    # Fold value field, default is `value`.
    value: Optional[str] = None


@dataclass
class JoinTransform:
    # The dataset to be joined.
    join: List[Dict[str, Any]]
    # Join keys of 2 dataset, [k1, k2] means join on ds1.k1 === ds2.k2. 由于python到js的限制不支持lambda函数
    on: str
    # Select fields from joined dataset.
    select: List[str]
    # Rename the select fields, default: keep the original name. TODO：json格式化时需要把as_转换为as
    as_: Optional[List[str]] = None
    # When not matched, use `unknown` instead.
    unknown: Optional[Any] = None
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
    # Kernel Density Estimation field.
    field_: str
    # Group data by fields.
    groupBy: List[str]
    # Generate new fields, default: ['y', 'size']
    as_: Optional[List[str]] = field(default_factory=lambda: ['y', 'size'])
    # Defaults to the smallest value in the array minus some threshold.
    min: Optional[number] = None
    # Defaults to the largest value in the array plus some threshold.
    max: Optional[number] = None
    # Number of points to represent the pdf. Defaults to 10.
    size: Optional[number] = None
    # Determine how many points to the left and right does an element affect,
    # similar to bandwidth in kernel density estimation. Defaults to 2.
    width: Optional[number] = None
    type: str = 'kde'


@dataclass
class VennDataTransform:
    # Set the generated fields, includes: [key, x, y, path]
    as_: List[str, str]
    # Canvas padding for 4 direction.
    # Default is `0`.
    padding: Optional[number] = None
    # Set the sets field.
    # Default is `sets`.
    sets: Optional[str] = None
    # Set the size field for each set.
    # Default is `size`.
    size: Optional[str] = None
    type: str = 'venn'


@dataclass
class LogDataTransform:
    type: str = 'log'


@dataclass
class CustomTransform:
    kwargs: Dict[str, Any]
    type: Optional[Any] = None


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
    CustomTransform,
]
