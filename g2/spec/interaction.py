# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 17:31
#
# =============================================================================
"""interaction

G2 中交互（Interaction） 提供了按需探索数据的能力。
"""
from typing import *
from dataclasses import dataclass

from .coordinate.coordinate_transform import FisheyeCoordinate
from .component import TooltipItemValue
from g2.common import number


TooltipPosition = Literal[
    'top',
    'bottom',
    'left',
    'right',
    'top-left',
    'top-right',
    'bottom-left',
    'bottom-right',
]

InteractionTypes = Literal[
    'elementHighlight',
    'elementHighlightByX',
    'elementHighlightByColor',
    'fisheye',
    'chartIndex',
    'elementSelect',
    'elementSelectByX',
    'elementSelectByColor',
    'fisheye',
    'tooltip',
    'legendFilter',
    'legendHighlight',
    'brushXHighlight',
    'brushYHighlight',
    'brushHighlight',
    'brushFilter',
    'brushXFilter',
    'brushYFilter',
    'sliderFilter',
    'poptip',
]


@dataclass
class BBox:
    x: Optional[number] = None
    y: Optional[number] = None
    width: Optional[number] = None
    height: Optional[number] = None


@dataclass
class BrushHighlightInteraction:
    type: str = 'brushHighlight'
    brushKey: Optional[str] = None
    reverse: Optional[bool] = None
    series: Optional[bool] = None
    facet: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class BrushXHighlightInteraction:
    type: str = 'brushXHighlight'
    brushKey: Optional[str] = None
    reverse: Optional[bool] = None
    series: Optional[bool] = None
    facet: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class BrushYHighlightInteraction:
    type: str = 'brushYHighlight'
    brushKey: Optional[str] = None
    reverse: Optional[bool] = None
    series: Optional[bool] = None
    facet: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class BrushAxisHighlightInteraction:
    type: str = 'brushAxisHighlight'
    reverse: Optional[bool] = None
    brushKey: Optional[str] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class BrushFilterInteraction:
    type: str = 'brushFilter'
    reverse: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class BrushXFilterInteraction:
    type: str = 'brushXFilter'
    reverse: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class BrushYFilterInteraction:
    type: str = 'brushYFilter'
    reverse: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是mask"""


@dataclass
class ElementHighlightInteraction:
    type: str = 'elementHighlight'
    link: Optional[bool] = None
    background: Optional[bool] = None
    offset: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是link或者background"""


@dataclass
class ElementSelectInteraction:
    type: str = 'elementSelect'
    single: Optional[bool] = None
    background: Optional[bool] = None
    offset: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是link或者background"""


@dataclass
class ElementSelectByColorInteraction:
    type: str = 'elementSelectByColor'
    single: Optional[bool] = None
    offset: Optional[number] = None
    background: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是link或者background"""


@dataclass
class ElementSelectByXInteraction:
    type: str = 'elementSelectByX'
    single: Optional[bool] = None
    background: Optional[bool] = None
    offset: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是link或者background"""


@dataclass
class ElementHighlightByXInteraction:
    type: str = 'elementHighlightByX'
    link: Optional[bool] = None
    background: Optional[bool] = None
    offset: Optional[number] = None
    delay: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是link或者background"""


@dataclass
class ElementHighlightByColorInteraction:
    type: str = 'elementHighlightByColor'
    color: Optional[str] = None
    background: Optional[bool] = None
    link: Optional[bool] = None
    offset: Optional[number] = None
    delay: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是link或者background"""


@dataclass
class PoptipInteraction:
    type: str = 'poptip'
    offsetX: Optional[number] = None
    offsetY: Optional[number] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是tip"""


@dataclass
class LegendFilterInteraction:
    type: str = 'legendFilter'


@dataclass
class LegendHighlightInteraction:
    type: str = 'legendHighlight'


@dataclass
class ChartIndexInteraction:
    type: str = 'chartIndex'
    wait: Optional[number] = None
    leading: Optional[bool] = None
    trailing: Optional[bool] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是rule或label"""


@dataclass
class SliderFilterInteraction:
    type: str = 'sliderFilter'
    wait: Optional[number] = None
    leading: Optional[bool] = None
    trailing: Optional[bool] = None


@dataclass
class TooltipInteraction:
    type: str = 'tooltip'
    shared: Optional[bool] = None
    series: Optional[bool] = None
    facet: Optional[bool] = None
    body: Optional[bool] = None
    crosshairs: Optional[bool] = None
    marker: Optional[bool] = None
    groupName: Optional[bool] = None
    position: Optional[TooltipPosition] = None
    bounding: Optional[BBox] = None
    mount: Optional[str] = None
    css: Optional[Dict[str, Any]] = None
    enterable: Optional[bool] = None
    sort: Optional[Callable[[TooltipItemValue], Any]] = None
    filter: Optional[Callable[[TooltipItemValue], Any]] = None
    render: Optional[Callable[
        [Any, Dict[Literal['string'], List[TooltipItemValue]]],
        str
    ]] = None
    kwargs: Optional[Dict[str, Any]] = None
    """key的prefix必须是marker或marker"""


@dataclass
class FisheyeInteraction(FisheyeCoordinate):
    type: str = 'fisheye'
    wait: Optional[number] = None
    leading: Optional[bool] = None
    trailing: Optional[bool] = None


Interaction = Union[
    ElementHighlightInteraction,
    ElementHighlightByColorInteraction,
    ElementHighlightByXInteraction,
    ElementSelectByColorInteraction,
    ElementSelectByXInteraction,
    ElementSelectInteraction,
    TooltipInteraction,
    FisheyeInteraction,
    ChartIndexInteraction,
    LegendFilterInteraction,
    LegendHighlightInteraction,
    BrushHighlightInteraction,
    BrushXHighlightInteraction,
    BrushYHighlightInteraction,
    BrushAxisHighlightInteraction,
    BrushFilterInteraction,
    BrushYFilterInteraction,
    BrushXFilterInteraction,
    SliderFilterInteraction,
    PoptipInteraction,
]
