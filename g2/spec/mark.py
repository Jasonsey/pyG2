# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 17:31
#
# =============================================================================
"""mark

在 G2 中没有图表的概念，而是把标记（Mark）作为基本的视觉组成单元，任何一个图表都是多个标记组合而成的。和传统的绘制系统不同，标记提供了绘制抽象数据的能力。
"""
from typing import *
from dataclasses import dataclass

from .encode import Encode

from .data import Data
from .transform import Transform
from .scale import Scale
from .coordinate import Coordinate
from .animate import Animation
from .component import TooltipComponent, AxisComponent, LegendComponent, SliderComponent, ScrollbarComponent, \
    TitleComponent
from .interaction import Interaction, InteractionTypes
from .theme import Theme
from g2.utils.common import number, ChannelTypes
from .utils import Padding, Closeable


MarkTypes = Literal[
    'auto',
    'interval',
    'rect',
    'line',
    'point',
    'text',
    'cell',
    'area',
    'node',
    'edge',
    'link',
    'image',
    'polygon',
    'box',
    'vector',
    'lineX',
    'lineY',
    'connector',
    'range',
    'rangeX',
    'rangeY',
    'sankey',
    'chord',
    'path',
    'treemap',
    'pack',
    'boxplot',
    'shape',
    'forceGraph',
    'tree',
    'wordCloud',
    'gauge',
    'density',
    'heatmap',
    'liquid',
]

PositionChannelTypes = Literal[
    'x',
    'y',
    'z',
    'position',
]

AtheisticChanelTypes = Literal['size', 'color', 'shape', 'opacity']


@dataclass
class BaseMark:
    type: Optional[MarkTypes] = None
    class_: Optional[str] = None
    key: Optional[str] = None
    x: Optional[number] = None
    y: Optional[number] = None
    width: Optional[number] = None
    height: Optional[number] = None
    paddingLeft: Optional[Padding] = None
    paddingRight: Optional[Padding] = None
    paddingBottom: Optional[Padding] = None
    paddingTop: Optional[Padding] = None
    padding: Optional[Padding] = None
    inset: Optional[number] = None
    insetLeft: Optional[number] = None
    insetBottom: Optional[number] = None
    insetTop: Optional[number] = None
    insetRight: Optional[number] = None
    margin: Optional[number] = None
    marginLeft: Optional[number] = None
    marginBottom: Optional[number] = None
    marginTop: Optional[number] = None
    marginRight: Optional[number] = None
    facet: Optional[bool] = None
    frame: Optional[bool] = None
    zIndex: Optional[number] = None
    cartesian: Optional[bool] = None
    clip: Optional[bool] = None
    data: Optional[Data] = None
    transform: Optional[List[Transform]] = None
    layout: Optional[Dict[str, Any]] = None
    encode: Union[Dict[ChannelTypes, Union[Encode, List[Encode]]], None] = None
    scale: Optional[Dict[ChannelTypes, Scale]] = None
    coordinate: Optional[Coordinate] = None
    style: Optional[Dict[str, Any]] = None
    viewStyle: Optional[Dict[str, Any]] = None
    state: Optional[Dict[
        Literal['active', 'selected', 'inactive', 'unselected'],
        Dict[str, Any]
    ]] = None
    animate: Union[Closeable, Dict[
        Literal['enter', 'update', 'exit'],
        Union[Closeable, Animation]
    ]] = None
    labels: Optional[List[Dict[str, Any]]] = None
    tooltip: Optional[TooltipComponent] = None
    axis: Union[Closeable, Dict[PositionChannelTypes, Union[Closeable, AxisComponent]]] = None
    legend: Union[Closeable, Dict[AtheisticChanelTypes, Union[Closeable, LegendComponent]]] = None
    slider: Union[Closeable, Dict[PositionChannelTypes, Union[Closeable, SliderComponent]]] = None
    scrollbar: Union[Closeable, Dict[PositionChannelTypes, Union[Closeable, ScrollbarComponent]]] = None
    title: Union[str, TitleComponent, None] = None
    interaction: Optional[Dict[InteractionTypes, Interaction]] = None
    theme: Optional[Theme] = None


@dataclass
class CompositeMark(BaseMark):
    """由于不支持自定义函数，因此这个方法暂时无效"""
    type: Optional[Callable[
        [Dict[str, Any], Dict[str, Any]],
        List
    ]] = None


_IntervalMarkType = Union[Literal['series'], ChannelTypes]


@dataclass
class IntervalMark(BaseMark):
    type: str = 'interval'
    encode: Optional[Dict[_IntervalMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_IntervalMarkType, Scale]] = None


@dataclass
class RectMark(BaseMark):
    type: str = 'rect'


_LineMarkType = Union[Literal['position'], str, ChannelTypes]
"""可以传入position{number}的string"""


@dataclass
class LineMark(BaseMark):
    type: str = 'line'
    encode: Optional[Dict[_LineMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_LineMarkType, Scale]] = None


@dataclass
class PointMark(BaseMark):
    type: str = 'point'


_TextMarkType = Union[Literal['text', 'fontSize', 'fontWeight', 'rotate'], ChannelTypes]


@dataclass
class TextMark(BaseMark):
    type: str = 'text'
    encode: Optional[Dict[_TextMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_TextMarkType, Scale]] = None


@dataclass
class LineXMark(BaseMark):
    type: str = 'lineX'


@dataclass
class LineYMark(BaseMark):
    type: str = 'lineY'


@dataclass
class RangeMark(BaseMark):
    type: str = 'range'


@dataclass
class RangeXMark(BaseMark):
    type: str = 'rangeX'


@dataclass
class RangeYMark(BaseMark):
    type: str = 'rangeY'


@dataclass
class ConnectorMark(BaseMark):
    type: str = 'connector'


@dataclass
class CellMark(BaseMark):
    type: str = 'cell'


@dataclass
class AreaMark(BaseMark):
    type: str = 'area'


@dataclass
class NodeMark(BaseMark):
    type: str = 'node'


@dataclass
class EdgeMark(BaseMark):
    type: str = 'edge'


@dataclass
class LinkMark(BaseMark):
    type: str = 'link'


_ImageMarkType = Union[Literal['src'], ChannelTypes]


@dataclass
class ImageMark(BaseMark):
    type: str = 'image'
    encode: Optional[Dict[_ImageMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_ImageMarkType, Scale]] = None


@dataclass
class PolygonMark(BaseMark):
    type: str = 'polygon'


@dataclass
class BoxMark(BaseMark):
    type: str = 'box'


@dataclass
class BoxPlotMark(BaseMark):
    type: str = 'box'


@dataclass
class ShapeMark(BaseMark):
    type: str = 'shape'


_VectorMarkType = Union[Literal['rotate', 'size'], ChannelTypes]


@dataclass
class VectorMark(BaseMark):
    type: str = 'vector'
    encode: Optional[Dict[_VectorMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_VectorMarkType, Scale]] = None


@dataclass
class SankeyMarkLayout:
    nodeId: Optional[Callable[[Any], str]] = None
    nodes: Optional[Callable[[Any], Any]] = None
    links: Optional[Callable[[Any], Any]] = None
    nodeSort: Optional[Callable[[Any], number]] = None
    """
    - sankey.nodeSort(undefined) is the default and resorts by ascending breadth during each iteration.
    - sankey.nodeSort(null) specifies the input order of nodes and never sorts.
    - sankey.nodeSort(function) specifies the given order as a comparator function and sorts once on initialization.
    """
    linkSort: Optional[Callable[[Any, Any], number]] = None
    """
    - sankey.linkSort(undefined) is the default, indicating that vertical order of links within each node will be 
      determined automatically by the layout. If
    - sankey.linkSort(null) will resort by the input.
    - sankey.linkSort(function) specifies the given order as a comparator function and sorts once on initialization.
    """
    nodeAlign: Union[None, Literal['left', 'center', 'right', 'justify'], Callable[[Any, number], number]] = None
    nodeWidth: Optional[number] = None
    nodePadding: Optional[number] = None
    iterations: Optional[number] = None
    nodeDepth: Optional[Callable[[Any, number], number]] = None


@dataclass
class _SankeyMark1:
    nodeLabels: List[Dict[str, Any]]
    """必须传递nodeLabels"""
    linkLabels: List[Dict[str, Any]]
    """必须传递linkLabels"""
    layout: Optional[SankeyMarkLayout] = None


_SankeyMark2Type = Union[Literal['source', 'target', 'value'], str, ChannelTypes]
"""除了列出的选项，还可以传输node+ChannelTypes或者link+ChannelTypes的string"""


@dataclass
class _SankeyMark2(BaseMark):
    type: str = 'sankey'
    encode: Optional[Dict[_SankeyMark2Type, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_SankeyMark2Type, Scale]] = None


@dataclass
class SankeyMark(_SankeyMark2, _SankeyMark1):
    pass


@dataclass
class ChordMarkLayout:
    nodes: Optional[Callable[[Any], Any]] = None
    links: Optional[Callable[[Any], Any]] = None
    y: Optional[number] = None
    id: Optional[Callable[[Any], Any]] = None
    sortBy: Union[None, Literal['id', 'weight', 'frequency'], Callable[[Any, Any], number]] = None
    sourceWeight: Optional[Callable[[Any], number]] = None
    targetWeight: Optional[Callable[[Any], number]] = None


@dataclass
class _ChordMark1:
    nodeLabels: List[Dict[str, Any]]
    """必须传递nodeLabels"""
    linkLabels: List[Dict[str, Any]]
    """必须传递linkLabels"""
    layout: Optional[ChordMarkLayout] = None


_ChordMark2Type = Union[Literal['source', 'target', 'value'], str, ChannelTypes]
"""除了列出的选项，还可以传输node+ChannelTypes或者link+ChannelTypes的string"""


@dataclass
class _ChordMark2(BaseMark):
    type: str = 'chord'
    encode: Optional[Dict[_ChordMark2Type, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_ChordMark2Type, Scale]] = None


@dataclass
class ChordMark(_ChordMark2, _ChordMark1):
    pass


_PathMarkType = Union[Literal['d'], ChannelTypes]


@dataclass
class PathMark(BaseMark):
    type: str = 'path'
    encode: Optional[Dict[_PathMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_PathMarkType, Scale]] = None


_TreemapMarkType = Union[Literal['value'], ChannelTypes]


@dataclass
class TreemapMark(BaseMark):
    type: str = 'treemap'
    encode: Optional[Dict[_TreemapMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_TreemapMarkType, Scale]] = None


_PackMarkType = Union[Literal['value'], ChannelTypes]


@dataclass
class PackMark(BaseMark):
    type: str = 'pack'
    encode: Optional[Dict[_PackMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_PackMarkType, Scale]] = None


@dataclass
class _ForceGraphMark1:
    nodeLabels: List[Dict[str, Any]]
    linkLabels: List[Dict[str, Any]]


_ForceGraphMark2Type = Union[Literal['source', 'target', 'color', 'value'], str]


@dataclass
class _ForceGraphMark2(BaseMark):
    type: str = 'forceGraph'
    encode: Optional[Dict[_ForceGraphMark2Type, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_ForceGraphMark2Type, Scale]] = None


@dataclass
class ForceGraphMark(_ForceGraphMark2, _ForceGraphMark1):
    pass


@dataclass
class TreeMarkLayout:
    field: Optional[str] = None
    """Layout field. Default: 'value'."""
    nodeSize: Optional[Any] = None
    """
    * Sets this cluster layout’s node size to the specified two-element array of numbers [width, height] and returns 
      this cluster layout.
    * Default: null.
    """
    separation: Optional[Callable[[Any, Any], number]] = None
    """
    The separation accessor is used to separate neighboring leaves.  Default: (a, b) => a.parent == b.parent ? 1 : 2;
    """
    sortBy: Optional[Callable[[Any, Any], number]] = None
    """Sort function by compare 2 nodes."""
    as_: Optional[Tuple[str, str]] = None
    """Layout information saved into fields. Default: ['x', 'y']."""


@dataclass
class _TreeMark1:
    nodeLabels: List[Dict[str, Any]]
    linkLabels: List[Dict[str, Any]]
    layout: Optional[TreeMarkLayout] = None


_TreeMark2Type = Union[Literal['value'], ChannelTypes]


@dataclass
class _TreeMark2(BaseMark):
    type: str = 'tree'
    encode: Optional[Dict[_TreeMark2Type, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_TreeMark2Type, Scale]] = None


@dataclass
class TreeMark(_TreeMark2, _TreeMark1):
    pass


@dataclass
class WordCloudMarkLayout:
    size: Optional[Tuple[number, number]] = None
    """
    * @description If specified, sets the rectangular [width, height] of the layout
    * @default [1, 1]
    """
    font: Union[None, str, Callable[[Any], str]] = None
    fontStyle: Union[None, str, Callable[[Any], str]] = None
    fontWeight: Union[None, Any, Callable[[Any], Any]] = None
    fontSize: Union[None, number, Tuple[number, number], Callable[[Any], number]] = None
    padding: Union[None, number, Callable[[Any], str]] = None
    text: Optional[Callable[[Any], number]] = None
    """
    * @description sets the text accessor function, which indicates the text for each word
    * @default (d) => d.text
    """
    rotate: Union[None, number, Callable[[Any], number]] = None
    timeInterval: Optional[number] = None
    random: Union[None, number, Callable[[Any], number]] = None
    spiral: Union[None, Literal['archimedean', 'rectangular'], Callable[
        [Tuple[number, number]],
        Callable[[number], List[number]],
    ]] = None
    """
    * @description sets the current type of spiral used for positioning words. This can either be one of the two 
      built-in spirals, "archimedean" and "rectangular" 
    * @default "archimedean"""
    imageMask: Optional[str] = None
    on: Union[None, Callable[[Literal['end', 'word']], None]] = None


_WordCloudMarkType = Union[Literal['value', 'text'], ChannelTypes]


@dataclass
class WordCloudMark(BaseMark):
    type: str = 'wordCloud'
    encode: Optional[Dict[_WordCloudMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_WordCloudMarkType, Scale]] = None
    layout: Optional[WordCloudMarkLayout] = None


_GaugeMark = Union[str, ChannelTypes]
"""除了列出的选项，还可以传输arc+ChannelTypes, link+ChannelTypes, indicator+ChannelTypes, pointer+ChannelTypes, 
pin+ChannelTypes的string"""


@dataclass
class GaugeMark(BaseMark):
    type: str = 'gauge'
    encode: Optional[Dict[_GaugeMark, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_GaugeMark, Scale]] = None


_DensityMarkType = Union[Literal['series'], ChannelTypes]


@dataclass
class DensityMark(BaseMark):
    type: str = 'density'
    encode: Optional[Dict[_DensityMarkType, Union[Encode, List[Encode]]]] = None
    scale: Optional[Dict[_DensityMarkType, Scale]] = None


@dataclass
class HeatmapMark(BaseMark):
    type: str = 'heatmap'


@dataclass
class LiquidMark(BaseMark):
    type: str = 'liquid'


Mark = Union[
    IntervalMark,
    RectMark,
    LineMark,
    PointMark,
    TextMark,
    CellMark,
    AreaMark,
    NodeMark,
    EdgeMark,
    ImageMark,
    PolygonMark,
    BoxMark,
    VectorMark,
    LineXMark,
    LineYMark,
    RangeMark,
    RangeXMark,
    RangeYMark,
    ConnectorMark,
    SankeyMark,
    ChordMark,
    PathMark,
    TreemapMark,
    PackMark,
    BoxPlotMark,
    ShapeMark,
    ForceGraphMark,
    TreeMark,
    WordCloudMark,
    DensityMark,
    CompositeMark,
]
