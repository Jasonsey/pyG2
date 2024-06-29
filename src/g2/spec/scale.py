# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 09:07
#
# =============================================================================
"""比例尺

G2 中比例尺（Scale） 是可视化很重要的一个抽象：将抽象数据映射为视觉数据，它是抽象数据和视觉数据的桥梁。如果说编码决定了标记的哪些通道需要被可视化，那么比例尺决定了这些通道该如何被可视化。

G2 内部会根据数据类型以及标记的类型，去推断比例尺的类型、定义域和值域，但是仍然可以指定对应配置。
"""
from g2.external.scale import *
from .palette import PaletteTypes


ScaleTypes = Literal[
    'linear',
    'ordinal',
    'identity',
    'band',
    'point',
    'time',
    'log',
    'pow',
    'sqrt',
    'threshold',
    'quantize',
    'quantile',
    'sequential',
    'constant',
]


@dataclass
class BaseScale:
    type: Optional[ScaleTypes] = None
    palette: Optional[PaletteTypes] = None
    rangeMax: Optional[number] = None
    rangeMin: Optional[number] = None
    domainMax: Optional[number] = None
    domainMin: Optional[number] = None
    key: Optional[str] = None
    facet: Optional[bool] = None
    independent: Optional[bool] = None
    zero: Optional[bool] = None
    offset: Optional[Callable[[number], number]] = None
    relations: Optional[List[Tuple[Any, Any]]] = None


@dataclass
class LinearScale(BaseScale, LinearOptions):
    type: str = 'linear'


@dataclass
class OrdinalScale(BaseScale, OrdinalOptions):
    type: str = 'ordinal'


@dataclass
class IdentityScale(BaseScale, IdentityOptions):
    type: str = 'identity'


@dataclass
class BandScale(BaseScale, BandOptions):
    type: str = 'band'


@dataclass
class PointScale(BaseScale, PointOptions):
    type: str = 'point'


@dataclass
class TimeScale(BaseScale, TimeOptions):
    type: str = 'time'


@dataclass
class LogScale(BaseScale, LogOptions):
    type: str = 'log'


@dataclass
class PowScale(BaseScale, PowOptions):
    type: str = 'pow'


@dataclass
class SqrtScale(BaseScale, SqrtOptions):
    type: str = 'sqrt'


@dataclass
class ThresholdScale(BaseScale, ThresholdOptions):
    type: str = 'threshold'


@dataclass
class QuantileScale(BaseScale, QuantileOptions):
    type: str = 'quantile'


@dataclass
class QuantizeScale(BaseScale, QuantizeOptions):
    type: str = 'quantize'


@dataclass
class SequentialScale(BaseScale, SequentialOptions):
    type: str = 'sequential'


@dataclass
class ConstantScale(BaseScale, ConstantOptions):
    type: str = 'constant'


Scale = Union[
    LinearScale,
    OrdinalScale,
    IdentityScale,
    BandScale,
    PointScale,
    TimeScale,
    LogScale,
    PowScale,
    SqrtScale,
    ThresholdScale,
    QuantizeScale,
    QuantileScale,
    SequentialScale,
    ConstantScale,
]