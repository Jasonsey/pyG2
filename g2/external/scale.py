# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/7 07:42
#
# =============================================================================
"""scale.py"""
from typing import *
from dataclasses import dataclass

from g2.common import number

TickMethodType = TypeVar("TickMethodType", number, str)
TickMethod = Callable[[TickMethodType, TickMethodType, Optional[number], List], List[Any]]
"""获得 ticks 的方法"""

NiceMethod = TickMethod
"""nice domain 的方法"""

Interpolator = Callable[[number], Any]
"""插值器函数"""

InterpolateType = Union[number, str]
Interpolates = Callable[[InterpolateType, InterpolateType], InterpolateType]
"""所有支持的插值器工厂"""

Comparator = Callable[[Any, Any], number]
"""比较器"""

TickMethodOptions = Callable[[number|str, number|str, number, Optional[number], Optional[bool]], Optional[bool]]
"""tickMethod 和 nice 需要使用的参数"""

Transform = Callable[[Any], Any]
"""柯里化后的函数的类型，对输入的值进行处理"""

CreateTransform = Callable[[List], Transform]
"""柯里化后的函数的工厂函数类型"""


@dataclass
class BaseOptions:
    """通用的配置"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Optional[List] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""


@dataclass
class IdentityOptions:
    """Identity 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Optional[List] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""


@dataclass
class ConstantOptions:
    """Constant 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Optional[List] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""


@dataclass
class ContinuousOptions:
    """Constant 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Optional[List] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""
    nice: Optional[bool] = None
    """是否需要对定义域的范围进行优化"""
    clamp: Optional[bool] = None
    """是否需要限制输入的范围在值域内"""
    round: Optional[bool] = None
    """是否需要对输出进行四舍五入"""
    interpolate: Optional[Interpolates] = None
    """插值器的工厂函数，返回一个对归一化后的输入在值域指定范围内插值的函数"""


@dataclass
class LinearOptions:
    """Linear 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""
    nice: Optional[bool] = None
    """是否需要对定义域的范围进行优化"""
    clamp: Optional[bool] = None
    """是否需要限制输入的范围在值域内"""
    round: Optional[bool] = None
    """是否需要对输出进行四舍五入"""
    interpolate: Optional[Interpolates] = None
    """插值器的工厂函数，返回一个对归一化后的输入在值域指定范围内插值的函数"""


@dataclass
class PowOptions(LinearOptions):
    """Pow 比例尺的选项"""
    exponent: Optional[number] = None
    """指数"""


SqrtOptions = LinearOptions
"""Sqrt 比例尺的选项"""


@dataclass
class LogOptions(LinearOptions):
    """Log 比例尺的选项"""
    base: Optional[number] = None
    """底数"""


@dataclass
class TimeOptions:
    """time 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""
    nice: Optional[bool] = None
    """是否需要对定义域的范围进行优化"""
    clamp: Optional[bool] = None
    """是否需要限制输入的范围在值域内"""
    round: Optional[bool] = None
    """是否需要对输出进行四舍五入"""
    interpolate: Optional[Interpolates] = None
    """插值器的工厂函数，返回一个对归一化后的输入在值域指定范围内插值的函数"""
    tickInterval: Optional[number] = None
    """getTick 的时间间隔"""
    mask: Optional[str] = None
    """格式化的形式"""
    utc: Optional[bool] = None
    """是否是 utc 时间"""


@dataclass
class OrdinalOptions:
    """OrdinalOptions 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    compare: Optional[Comparator] = None
    """比较器"""


@dataclass
class BandOptions:
    """详细请参阅 scale/band.ts"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    round: Optional[bool] = None
    """是否需要对输出进行四舍五入"""
    paddingInner: Optional[number] = None
    """内部边距"""
    paddingOuter: Optional[number] = None
    """两侧边距"""
    padding: Optional[number] = None
    """同时定义内部边距和两侧边距，如果该值大于 0，则 paddingInner 和 paddingOuter 无效"""
    align: Optional[number] = None
    """对齐，取值为 0 - 1 的整数，例如 0.5 表示居中"""
    compare: Optional[Comparator] = None
    """比较器，用于对 domain 进行排序"""
    flex: Optional[List[number]] = None
    """每个条的宽度 (bandWidth) 的比例"""


@dataclass
class PointOptions:
    """Point 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    round: Optional[bool] = None
    """是否需要对输出进行四舍五入"""
    padding: Optional[number] = None
    """同时定义内部边距和两侧边距，如果该值大于 0，则 paddingInner 和 paddingOuter 无效"""
    align: Optional[number] = None
    """对齐，取值为 0 - 1 的整数，例如 0.5 表示居中"""
    compare: Optional[Comparator] = None
    """比较器，用于对 domain 进行排序"""
    flex: Optional[List[number]] = None
    """每个条的宽度 (bandWidth) 的比例"""


@dataclass
class ThresholdOptions:
    """Threshold 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""


@dataclass
class QuantizeOptions:
    """Quantize 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    nice: Optional[bool] = None
    """是否需要对定义域的范围进行优化"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""


@dataclass
class QuantileOptions:
    """Quantile 比例尺的选项"""
    unknown: Optional[Any] = None
    """当需要映射的值不合法的时候，返回的值"""
    range: Union[List[number], List[str], None] = None
    """值域，默认为 [0, 1]"""
    domain: Optional[List] = None
    """定义域，默认为 [0, 1]"""
    tickCount: Optional[number] = None
    """tick 个数，默认值为 5"""
    tickMethod: Optional[TickMethod] = None
    """计算 ticks 的算法"""


@dataclass
class SequentialOptions(LinearOptions):
    """Sequential 比例尺的选项"""
    interpolator: Optional[Interpolator] = None


@dataclass
class DivergingOptions(LinearOptions):
    """Diverging 比例尺的选项"""
    interpolator: Optional[Interpolator] = None
