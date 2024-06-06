from typing import *
from dataclasses import dataclass


@dataclass
class Scale:
    type: str


@dataclass
class ScaleBand(Scale):
    domain: Union[List[int], List[str], None] = None
    range: Union[List[int], List[str]] = [0, 1]
    round: bool = False
    padding_inner: int = 0
    padding_outer: int = 0
    padding: int = 0
    align: float = 0.5
    flex: Optional[List[int]] = None
    type: str = 'band'


@dataclass
class ScaleLinear(Scale):
    domain: Optional[List[int]] = None
    domain_min: Optional[int] = None
    domain_max: Optional[int] = None
    range: Union[List[int], List[str]] = [0, 1]
    range_min: Union[int, str] = 0
    range_max: Union[int, str] = 1
    tick_count: int = 5
    round: bool = False
    clamp: bool = False
    nice: bool = False
    type: str = 'linear'


@dataclass
class ScaleLog(Scale):
    domain: Optional[List[int]] = None
    domain_min: Optional[int] = None
    domain_max: Optional[int] = None
    range: Union[List[int], List[str]] = [0, 1]
    range_min: Union[int, str] = 0
    range_max: Union[int, str] = 1
    tick_count: int = 5
    round: bool = False
    clamp: bool = False
    nice: bool = False
    base: int = 10
    type: str = 'log'


@dataclass
class ScaleOrdinal(Scale):
    domain: Optional[List[int]] = None
    range: Union[List[int], List[str]] = [0, 1]
    type: str = 'ordinal'


@dataclass
class ScalePoint(Scale):
    domain: Optional[List[int]] = None
    range: Union[List[int], List[str]] = [0, 1]
    round: bool = False
    padding_inner: int = 0
    padding_outer: int = 0
    padding: int = 0
    align: float = 0.5
    type: str = 'point'


@dataclass
class ScalePow(Scale):
    domain: Optional[List[int]] = None
    domain_min: Optional[int] = None
    domain_max: Optional[int] = None
    range: Union[List[int], List[str]] = [0, 1]
    range_min: Union[int, str] = 0
    range_max: Union[int, str] = 1
    tick_count: int = 5
    round: bool = False
    clamp: bool = False
    nice: bool = False
    exponent: int = 2
    type: str = 'pow'


@dataclass
class ScaleQuantile(Scale):
    domain: Optional[List[int]] = None
    range: Optional[List[Any]] = None
    tick_count: int = 5
    nice: bool = False
    type: str = 'quantile'


@dataclass
class ScaleQuantize(Scale):
    domain: Optional[List[int]] = None
    range: Optional[List[Any]] = None
    tick_count: int = 5
    nice: bool = False
    type: str = 'quantize'


@dataclass
class ScaleSqrt(Scale):
    domain: Optional[List[int]] = None
    domain_min: Optional[int] = None
    domain_max: Optional[int] = None
    range: Union[List[int], List[str]] = [0, 1]
    range_min: Union[int, str] = 0
    range_max: Union[int, str] = 1
    tick_count: int = 5
    round: bool = False
    clamp: bool = False
    nice: bool = False
    exponent: float = 0.5
    type: str = 'sqrt'


@dataclass
class ScaleThreshold(Scale):
    domain: Optional[List[int]] = None
    range: Union[List[int], List[str]] = [0, 1]
    type: str = 'threshold'


@dataclass
class ScaleTime(Scale):
    domain: Optional[List[int]] = None
    domain_min: Optional[int] = None
    domain_max: Optional[int] = None
    range: Union[List[int], List[str]] = [0, 1]
    range_min: Union[int, str] = 0
    range_max: Union[int, str] = 1
    tick_count: int = 5
    tick_interval: Optional[int] = None
    round: bool = False
    clamp: bool = False
    nice: bool = False
    mask: Optional[str] = None
    utc: bool = False
    type: str = 'time'