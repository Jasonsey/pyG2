# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/9 21:42
#
# =============================================================================
"""composition

G2 中视图复合（View Composition） 提供了在一个可视化中绘制多个图表的能力。G2 定义了一个视图树（View Graph） 去描述多视图图表（Multi-View Plot）。
一句话总结：属于view组件，用于绘制多图。如果只有一个图，用mark就好
"""
from typing import *
from dataclasses import dataclass

from g2.common import number, string, boolean
from .utils import Closeable, Padding
from .data import Data
from .coordinate import Coordinate
from .interaction import Interaction, InteractionTypes
from .transform import Transform
from .theme import Theme
from .mark import Mark, PositionChannelTypes, AtheisticChanelTypes
from .component import (AxisComponent, LegendComponent, TooltipComponent, SliderComponent, ScrollbarComponent,
                        TitleComponent)
from .scale import Scale
from .label import LabelTransform

CompositionTypes = Literal[
    'view',
    'getView',
    'geoPath',
    'spaceLayer',
    'spaceFlex',
    'facetRect',
    'facetCircle',
    'repeatMatrix',
    'timingKeyframe',
]


@dataclass
class ViewComposition:
    type: str = 'view'
    x: Optional[number] = None
    y: Optional[number] = None
    z: Optional[number] = None
    width: Optional[number] = None
    height: Optional[number] = None
    depth: Optional[number] = None
    data: Optional[Data] = None
    key: Optional[string] = None
    class_: Optional[string] = None
    padding: Optional[Padding] = None
    paddingLeft: Optional[Padding] = None
    paddingRight: Optional[Padding] = None
    paddingTop: Optional[Padding] = None
    paddingBottom: Optional[Padding] = None
    margin: Optional[number] = None
    marginLeft: Optional[number] = None
    marginBottom: Optional[number] = None
    marginTop: Optional[number] = None
    marginRight: Optional[number] = None
    inset: Optional[number] = None
    insetLeft: Optional[number] = None
    insetTop: Optional[number] = None
    insetBottom: Optional[number] = None
    insetRight: Optional[number] = None
    coordinate: Optional[Coordinate] = None
    interaction: Optional[Dict[InteractionTypes, Interaction]] = None
    transform: Optional[List[Transform]] = None
    theme: Optional[Theme] = None
    children: Optional[Union[List[Mark], List[AxisComponent], List[LegendComponent]]] = None
    scale: Optional[Dict[string, Scale]] = None
    frame: Optional[boolean] = None
    labelTransform: Optional[List[LabelTransform]] = None
    axis: Union[Closeable, Dict[PositionChannelTypes, Union[Closeable, AxisComponent]]] = None
    legend: Union[Closeable, Dict[AtheisticChanelTypes, Union[Closeable, LegendComponent]]] = None
    tooltip: Optional[TooltipComponent] = None
    slider: Union[Closeable, Dict[PositionChannelTypes, Union[Closeable, SliderComponent]]] = None
    scrollbar: Union[Closeable, Dict[PositionChannelTypes, Union[Closeable, ScrollbarComponent]]] = None
    title: Union[None, string, TitleComponent] = None
    style: Optional[Dict[string, Any]] = None
    clip: Optional[boolean] = None


@dataclass
class GeoViewComposition(ViewComposition):
    type: str = 'geoView'
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class GeoPathComposition(ViewComposition):
    type: str = 'geoPath'
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class SpaceLayerComposition:
    type: str = 'spaceLayer'
    key: Optional[string] = None
    data: Optional[Any] = None
    children: Optional[List["Node"]] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class SpaceFlexComposition:
    type: str = 'spaceFlex'
    key: Optional[string] = None
    data: Optional[Data] = None
    direction: Optional[Literal['col', 'row']] = None
    ratio: Optional[List[number]] = None
    padding: Optional[Padding] = None
    children: Optional[List["Node"]] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class FacetContext:
    columnField: Union[None, string, number] = None
    columnIndex: Optional[number] = None
    columnValue: Union[None, string, number] = None
    columnValuesLength: Optional[number] = None
    rowField: Union[None, string, number] = None
    rowIndex: Optional[number] = None
    rowValue: Union[None, string, number] = None
    rowValuesLength: Optional[number] = None


@dataclass
class FacetRectCompositionEncode:
    x: Optional[string] = None
    y: Optional[string] = None


@dataclass
class FacetRectCompositionScale:
    x: Optional[Scale] = None
    y: Optional[Scale] = None
    color: Optional[Scale] = None


@dataclass
class FacetRectComposition:
    type: str = 'facetRect'
    transform: Optional[Transform] = None
    data: Optional[Data] = None
    padding: Optional[Padding] = None
    paddingLeft: Optional[Padding] = None
    paddingRight: Optional[Padding] = None
    paddingTop: Optional[Padding] = None
    paddingBottom: Optional[Padding] = None
    margin: Optional[number] = None
    marginLeft: Optional[number] = None
    marginBottom: Optional[number] = None
    marginTop: Optional[number] = None
    marginRight: Optional[number] = None
    key: Optional[string] = None
    title: Union[None, string, TitleComponent] = None
    encode: Optional[FacetRectCompositionEncode] = None
    scale: Optional[FacetRectCompositionScale] = None
    shareData: Optional[boolean] = None
    shareSize: Optional[boolean] = None
    children: Union[None, List["Node"], Callable[[FacetContext], "Node"]] = None
    axis: Union[None, Dict[string, Any], boolean] = None
    legend: Union[None, Dict[string, Any], boolean] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class RepeatMatrixCompositionEncode:
    x: Union[None, List[string], string] = None
    y: Union[None, List[string], string] = None
    position: Optional[List[string]] = None


@dataclass
class RepeatMatrixCompositionScale:
    x: Optional[Scale] = None
    y: Optional[Scale] = None
    color: Optional[Scale] = None


@dataclass
class RepeatMatrixComposition:
    type: str = 'repeatMatrix'
    padding: Optional[Padding] = None
    paddingLeft: Optional[Padding] = None
    paddingRight: Optional[Padding] = None
    paddingTop: Optional[Padding] = None
    paddingBottom: Optional[Padding] = None
    margin: Optional[number] = None
    marginLeft: Optional[number] = None
    marginBottom: Optional[number] = None
    marginTop: Optional[number] = None
    marginRight: Optional[number] = None
    transform: Optional[Transform] = None
    title: Union[None, string, TitleComponent] = None
    data: Optional[Data] = None
    key: Optional[string] = None
    encode: Optional[RepeatMatrixCompositionEncode] = None
    scale: Optional[RepeatMatrixCompositionScale] = None
    axis: Union[None, Dict[string, Any], boolean] = None
    legend: Union[None, Dict[string, Any], boolean] = None
    children: Union[None, List["Node"], Callable[[FacetContext], "Node"]] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class FacetCircleCompositionEncode:
    position: Optional[string] = None


@dataclass
class FacetCircleCompositionScale:
    x: Optional[Scale] = None
    y: Optional[Scale] = None
    color: Optional[Scale] = None


@dataclass
class FacetCircleComposition:
    type: str = 'facetCircle'
    padding: Optional[Padding] = None
    paddingLeft: Optional[Padding] = None
    paddingRight: Optional[Padding] = None
    paddingTop: Optional[Padding] = None
    paddingBottom: Optional[Padding] = None
    margin: Optional[number] = None
    marginLeft: Optional[number] = None
    marginBottom: Optional[number] = None
    marginTop: Optional[number] = None
    marginRight: Optional[number] = None
    transform: Optional[Transform] = None
    title: Union[None, string, TitleComponent] = None
    data: Optional[Data] = None
    key: Optional[string] = None
    encode: Optional[FacetCircleCompositionEncode] = None
    scale: Optional[FacetCircleCompositionScale] = None
    children: Union[None, List["Node"], Callable[[FacetContext], "Node"]] = None
    axis: Union[None, Dict[string, Any], boolean] = None
    legend: Union[None, Dict[string, Any], boolean] = None
    kwargs: Optional[Dict[str, Any]] = None


@dataclass
class TimingKeyframeComposition:
    type: str = 'timingKeyframe'
    duration: Optional[number] = None
    key: Optional[string] = None
    easing: Optional[string] = None
    iterationCount: Union[None, Literal['infinite'], number] = None
    direction: Optional[Literal['normal', 'reverse', 'alternate', 'reverse-alternate']] = None
    children: Optional[List["Node"]] = None
    kwargs: Optional[Dict[str, Any]] = None


Composition = Union[
    ViewComposition,
    GeoViewComposition,
    GeoPathComposition,
    SpaceLayerComposition,
    SpaceFlexComposition,
    RepeatMatrixComposition,
    FacetRectComposition,
    FacetCircleComposition,
    TimingKeyframeComposition,
]

Node = Union[Mark, Composition]
