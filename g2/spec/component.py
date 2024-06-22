# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 11:02
#
# =============================================================================
"""component"""
from typing import *
from dataclasses import dataclass

from g2.utils.common import number, Primitive


@dataclass
class TitleComponent:
    size: Optional[number] = None
    """Height of title, default is 36."""
    title: Optional[str] = None
    """Text of title."""
    subtitle: Optional[str] = None
    """Text of subtitle."""
    align: Optional[Literal['left', 'center', 'right']] = None
    """Align method for title."""
    spacing: Optional[number] = None
    """The vertical spacing between title and subtitle, default is 2."""
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是title或subtitle"""


@dataclass
class AxisComponent:
    type: Optional[Literal['axisX', 'axisY', 'axisZ']] = None
    tickCount: Optional[number] = None
    labelFormatter: Optional[Any] = None
    tickFilter: Optional[Any] = None
    title: Optional[Any] = None
    state: Optional[Dict[
        Literal['active', 'selected', 'inactive', 'unselected'],
        Dict[str, Any]
    ]] = None
    scale: Optional[Dict[str, Any]] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class LegendComponent:
    type: Optional[Literal['legends']] = None
    tickCount: Optional[number] = None
    labelFormatter: Optional[Any] = None
    tickFilter: Optional[Any] = None
    title: Optional[Any] = None
    position: Optional[str] = None
    state: Optional[Dict[
        Literal['active', 'selected', 'inactive', 'unselected'],
        Dict[str, Any]
    ]] = None
    scale: Optional[Dict[str, Any]] = None
    kwargs: Optional[Dict[str, Any]] = None


SliderComponent = Any
ScrollbarComponent = Any


@dataclass
class TooltipItemValue:
    name: Optional[str] = None
    color: Optional[str] = None
    value: Optional[Primitive] = None


@dataclass
class _TooltipTitle:
    field: Optional[str] = None
    channel: Optional[str] = None
    value: Optional[str] = None


TooltipTitle = Union[_TooltipTitle, str]
EncodeableType = TypeVar('EncodeableType', Primitive, TooltipItemValue, TooltipTitle)
Encodeable = Callable[[Any, Optional[number], Optional[List], Optional[Any]], EncodeableType]


@dataclass
class _TooltipItem:
    name: Optional[str] = None
    color: Optional[str] = None
    channel: Optional[str] = None
    field: Optional[str] = None
    value: Optional[str] = None
    valueFormatter: Optional[Callable[[Any], str]] = str


TooltipItem = Union[str, _TooltipItem, Encodeable]


@dataclass
class _TooltipComponent:
    title: Optional[Encodeable] = None
    items: Union[List[TooltipItem], Literal[False], None] = None
    kwargs: Optional[Dict[str, Any]] = None


TooltipComponent = Union[TooltipItem, List[TooltipItem], _TooltipComponent, None, Literal[False]]
