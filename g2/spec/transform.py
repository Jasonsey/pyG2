# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 21:07
#
# =============================================================================
""" 数据转换工具

G2 中的标记转换（Mark Transform） 提供了一个方便的机制，去转换数据和标记的选项，主要用于分析数据。标记转换的本质是一个函数，这个函数会筛选 、修改 、聚合和产生新的通道值。

转换是一个数组，声明的转换会按照顺序执行。
"""
from typing import *
from dataclasses import dataclass

from g2.common import string, number, Primitive, boolean, ChannelTypes

TransformTypes = Literal[
    'dodgeX',
    'stackY',
    'normalizeY',
    'stackEnter',
    'jitter',
    'jitterX',
    'jitterY',
    'symmetryY',
    'diffY',
    'select',
    'selectY',
    'selectX',
    'groupX',
    'groupY',
    'group',
    'groupColor',
    'sortX',
    'sortColor',
    'sortY',
    'flexX',
    'pack',
    'sample',
    'filter',
    'kde',
]


TransformOrder = Union[
    Literal['value', 'sum', 'series', 'maxIndex'],
    List[string],
    None,
    Callable[[Dict[string, Primitive]], Primitive]
]


@dataclass
class DodgeXTransform:
    type: str = 'dodgeX'
    groupBy: Union[None, string, List[string]] = None
    reverse: Optional[boolean] = None
    orderBy: Optional[TransformOrder] = None
    padding: Optional[number] = None


@dataclass
class StackYTransform:
    type: str = 'stackY'
    groupBy: Union[None, string, List[string]] = None
    reverse: Optional[boolean] = None
    orderBy: Optional[TransformOrder] = None
    y: Optional[Literal['y', 'y1']] = None
    y1: Optional[Literal['y', 'y1']] = None
    series: Optional[boolean] = None


@dataclass
class NormalizeYTransform:
    type: str = 'normalizeY'
    series: Optional[boolean] = None
    groupBy: Union[None, string, List[string]] = None
    basis: Optional[Literal['deviation', 'first', 'last', 'max', 'mean', 'median', 'min', 'sum']] = None


@dataclass
class JitterTransform:
    type: str = 'jitter'
    padding: Optional[number] = None
    paddingX: Optional[number] = None
    paddingY: Optional[number] = None
    random: Optional[Callable[[], number]] = None


@dataclass
class JitterXTransform:
    type: str = 'jitterX'
    padding: Optional[number] = None
    random: Optional[Callable[[], number]] = None


@dataclass
class JitterYTransform:
    type: str = 'jitterY'
    padding: Optional[number] = None
    random: Optional[Callable[[], number]] = None


@dataclass
class StackEnterTransform:
    type: str = 'stackEnter'
    groupBy: Union[None, string, List[string]] = None
    orderBy: Optional[string] = None
    reverse: Optional[boolean] = None
    duration: Optional[number] = None
    reducer: Optional[Callable[[List[number], List], Any]] = None


@dataclass
class SymmetryYTransform:
    type: str = 'symmetryY'
    groupBy: Union[None, string, List[string]] = None


@dataclass
class DiffYTransform:
    type: str = 'diffY'
    groupBy: Union[None, string, List[string]] = None
    series: Optional[boolean] = None


Selector = Union[
    Literal['min', 'max', 'first', 'last', 'mean', 'median'],
    Callable[[List[number], List[number]], List[number]]
]


@dataclass
class SelectTransform:
    type: str = 'select'
    groupBy: Union[None, string, List[string]] = None
    channel: Optional[ChannelTypes] = None
    selector: Optional[Selector] = None


@dataclass
class SelectXTransform:
    type: str = 'selectX'
    groupBy: Union[None, string, List[string]] = None
    selector: Optional[Selector] = None


@dataclass
class SelectYTransform:
    type: str = 'selectY'
    groupBy: Union[None, string, List[string]] = None
    selector: Optional[Selector] = None


@dataclass
class SortColorTransform:
    type: str = 'sortColor'
    reverse: Optional[boolean] = None
    by: Optional[string] = None
    slice: Union[None, number, Tuple[number, number]] = None
    reducer: Union[
        None,
        Literal['max', 'min', 'sum', 'first', 'last', 'mean', 'median'],
        Callable[[List[number], List[Primitive]], Primitive],
    ] = None


@dataclass
class SortXTransform:
    type: str = 'sortX'
    reverse: Optional[boolean] = None
    by: Optional[string] = None
    slice: Union[None, number, Tuple[number, number]] = None
    ordinal: Optional[boolean] = None
    reducer: Union[
        None,
        Literal['max', 'min', 'sum', 'first', 'last', 'mean', 'median'],
        Callable[[List[number], List[Primitive]], Primitive],
    ] = None


@dataclass
class SortYTransform:
    type: str = 'sortY'
    reverse: Optional[boolean] = None
    by: Optional[string] = None
    slice: Union[None, number, Tuple[number, number]] = None
    reducer: Union[
        None,
        Literal['max', 'min', 'sum', 'first', 'last', 'mean', 'median'],
        Callable[[List[number], List[Primitive]], Primitive],
    ] = None


@dataclass
class FlexXTransform:
    type: str = 'flexX'
    field: Union[None, string, Callable[[Any], Primitive]] = None
    channel: Optional[string] = None
    reducer: Union[
        None,
        Literal['sum'],
        Callable[[List[number], List[Primitive]], Primitive],
    ] = None


@dataclass
class PackTransform:
    type: str = 'pack'
    padding: Optional[number] = None
    direction: Optional[Literal['row', 'col']] = None


Reducer = Union[
    Literal['mean', 'max', 'count', 'min', 'median', 'sum', 'first', 'last'],
    Callable[[List[number], List[Primitive]], Primitive],
]


@dataclass
class GroupXTransform:
    type: str = 'groupX'
    kwargs: Optional[Dict[ChannelTypes, Reducer]] = None


@dataclass
class GroupYTransform:
    type: str = 'groupY'
    kwargs: Optional[Dict[ChannelTypes, Reducer]] = None


@dataclass
class GroupColorTransform:
    type: str = 'groupColor'
    kwargs: Optional[Dict[ChannelTypes, Reducer]] = None


@dataclass
class GroupTransform:
    type: str = 'group'
    kwargs: Optional[Dict[ChannelTypes, Reducer]] = None


@dataclass
class BinXTransform:
    type: str = 'binX'
    thresholds: Optional[number] = None
    kwargs: Optional[Dict[ChannelTypes, Reducer]] = None


@dataclass
class BinTransform:
    type: str = 'bin'
    thresholdsX: Optional[number] = None
    thresholdsY: Optional[number] = None
    kwargs: Optional[Dict[ChannelTypes, Reducer]] = None


SampleFunction = Callable[[List[number], List[number], List[number], number], List[number]]


@dataclass
class SampleTransform:
    type: str = 'sample'
    strategy: Union[None, Literal['lttb', 'median', 'max', 'min', 'first', 'last'], SampleFunction] = None
    """Sample strategy. Default is 'median'."""
    thresholds: Optional[number] = None
    """
    * The thresholds of sample, when data size great then thresholds, sample will take effect.
    * Default is 2000.
    """
    groupBy: Union[None, string, List[string]] = None
    """Group data by fields, for series data."""


@dataclass
class FilterTransform:
    type: str = 'filter'
    kwargs: Optional[Dict[
        ChannelTypes,
        Union[List, Callable[[Primitive], boolean]]
    ]] = None


Transform = Union[
    StackYTransform,
    DodgeXTransform,
    NormalizeYTransform,
    StackEnterTransform,
    JitterTransform,
    JitterXTransform,
    JitterYTransform,
    SymmetryYTransform,
    DiffYTransform,
    SelectTransform,
    SelectXTransform,
    SelectYTransform,
    GroupXTransform,
    GroupYTransform,
    GroupColorTransform,
    SortXTransform,
    SortYTransform,
    SortColorTransform,
    GroupTransform,
    PackTransform,
    BinXTransform,
    BinTransform,
    SampleTransform,
    FlexXTransform,
    FilterTransform,
]
