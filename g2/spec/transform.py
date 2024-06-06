from typing import *
from dataclasses import dataclass


Reducer = Literal['mean', 'max', 'count', 'min', 'median', 'sum', 'first', 'last']
TransformOrder = Union[Literal['value', 'sum', 'series', 'maxIndex'], List[str]]

@dataclass
class Transform:
    type: str


@dataclass
class TransformBin(Transform):
    thresholds_x: int = None
    thresholds_y: int = None
    reducer: Optional[Dict[str, Reducer]] = None
    type: str = 'bin'


@dataclass 
class TransormBinX(Transform):
    thresholds: int
    reducer: Optional[Dict[str, Reducer]] = None
    type: str = 'binX'


@dataclass
class TransformDiffY(Transform):
    group_by: Union[str, List[str]] = 'x'
    series: bool = True
    type: str = 'diffY'


@dataclass
class TransformDodgeX(Transform):
    group_by: Union[str, List[str]] = 'x'
    reverse: bool = False
    order_by: Optional[TransformOrder] = None
    padding: int = 0
    type: str = 'dodgeX'


@dataclass
class TransformFlexX(Transform):
    field: str
    channel: str = 'y'
    reducer: Literal['sum'] = 'sum'
    type: str = 'flexX'


@dataclass
class TransformGroup(Transform):
    channels: Union[str, List[str]] = ['x', 'y']
    type: str = 'group'


@dataclass
class TransformGroupColor(Transform):
    reducer: Optional[Dict[str, Reducer]] = None
    type: str = 'groupColor'


@dataclass
class TransformGroupX(Transform):
    reducer: Optional[Dict[str, Reducer]] = None
    type: str = 'groupX'


@dataclass
class TransformGroupY(Transform):
    reducer: Optional[Dict[str, Reducer]] = None
    type: str = 'groupY'


@dataclass
class TransformJitter(Transform):
    random: Callable
    padding: int = 0
    padding_x: int = 0
    padding_y: int = 0
    type: str = 'jitter'


@dataclass
class TransformJitterX(Transform):
    random: Callable
    padding: int = 0
    type: str = 'jitterX'


@dataclass
class TransformJitterY(Transform):
    random: Callable
    padding: int = 0
    type: str = 'jitterY'


@dataclass
class TransformNormalizeY(Transform):
    group_by: Union[str, List[str]] = 'x'
    basis: Literal['deviation', 'first', 'last', 'max', 'mean', 'median', 'min', 'sum'] = 'max'
    type: str = 'normalizeY'


@dataclass
class TransformPack(Transform):
    padding: int = 0
    direction: Literal['row', 'col'] = 'col'
    type: str = 'pack'


@dataclass
class TransformSample(Transform):
    group_by: Union[str, List[str]] = 'series'
    thresholds: int = 2000
    strategy: Literal['lttb', 'median', 'max', 'min', 'first', 'last'] = 'median'
    type: str = 'sample'


@dataclass
class TransformSelect(Transform):
    channel: str
    group_by: Union[str, List[str]] = 'series'
    selector: Literal['min', 'max', 'first', 'last', 'mean', 'median'] = 'first'
    type: str = 'select'


@dataclass
class TransformSelectX(Transform):
    group_by: Union[str, List[str]] = 'series'
    selector: Literal['min', 'max', 'first', 'last', 'mean', 'median'] = 'first'
    type: str = 'selectX'


@dataclass
class TransformSelectY(Transform):
    group_by: Union[str, List[str]] = 'series'
    selector: Literal['min', 'max', 'first', 'last', 'mean', 'median'] = 'first'
    type: str = 'selectY'


@dataclass
class TransformSortColor(Transform):
    reverse: bool = 'false'
    by: str = 'y'
    slice: Union[str, int, List[int, int]] = 'y'
    reducer: Reducer = 'max'
    type: str = 'sortColor'


@dataclass
class TransformSortX(Transform):
    reverse: bool = 'false'
    by: str = 'y'
    slice: Union[str, int, List[int, int]] = 'y'
    reducer: Reducer = 'max'
    ordinal: bool = True
    type: str = 'sortX'


@dataclass
class TransformSortY(Transform):
    reverse: bool = 'false'
    by: str = 'y'
    slice: Union[str, int, List[int, int]] = 'y'
    reducer: Reducer = 'max'
    type: str = 'sortY'


@dataclass
class TransformStackEnter(Transform):
    group_by: Union[str, List[str]] = 'x'
    order_by: Optional[str] = None
    reverse: bool = False 
    duration: int = 3000
    type: str = 'stackEnter'


@dataclass
class TransformStackY(Transform):
    group_by: Union[str, List[str]] = 'x'
    order_by: Optional[TransformOrder] = None
    y: str = 'y1'
    y1: str = 'y1'
    reverse: bool = False
    series: bool = True
    type: str = 'stackX'


@dataclass
class TransformSymmetryY(Transform):
    group_by: Union[str, List[str]] = 'x'
    type: str = 'symmetryY'
