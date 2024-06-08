from typing import *
from dataclasses import dataclass

from .encode import Encode

from .data import Data
from .transform import Transform
from .scale import Scale
from .coordinate import Coordinate
from .animate import Animation
from .component import TooltipComponent
from g2.common import number
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

ChannelTypes = Literal[
    'x',
    'y',
    'z',
    'x1',
    'y1',
    'series',
    'color',
    'opacity',
    'shape',
    'size',
    'key',
    'groupKey',
    'position',
    'series',
    'enterType',
    'enterEasing',
    'enterDuration',
    'enterDelay',
    'updateType',
    'updateEasing',
    'updateDuration',
    'updateDelay',
    'exitType',
    'exitEasing',
    'exitDuration',
    'exitDelay',
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
    encode: Union[Dict[ChannelTypes, Encode], Dict[ChannelTypes, List[Encode]], None] = None
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
    axis?: Closeable<
      Partial<Record<PositionChannelTypes, Closeable<AxisComponent>>>
    >;
    legend?: Closeable<
      Partial<Record<AtheisticChanelTypes, Closeable<LegendComponent>>>
    >;
    slider?: Closeable<
      Partial<Record<PositionChannelTypes, Closeable<SliderComponent>>>
    >;
    scrollbar?: Closeable<
      Partial<Record<PositionChannelTypes, Closeable<ScrollbarComponent>>>
    >;
    title?: string | TitleComponent;
    interaction?: Literal2Object<Interaction> & Record<string, any>;
    theme?: Theme;


export type CompositeMarkType = (
  options: Record<string, any>,
  context: Record<string, any>,
) => any[];

export type CompositeMark = BaseMark<CompositeMarkType>;

export type IntervalMark = BaseMark<'interval', ChannelTypes | 'series'>;

export type RectMark = BaseMark<'rect', ChannelTypes>;

export type LineMark = BaseMark<
  'line',
  ChannelTypes | 'position' | `position${number}`
>;

export type PointMark = BaseMark<'point'>;

export type TextMark = BaseMark<
  'text',
  ChannelTypes | 'text' | 'fontSize' | 'fontWeight' | 'rotate'
>;

export type LineXMark = BaseMark<'lineX', ChannelTypes>;

export type LineYMark = BaseMark<'lineY', ChannelTypes>;

export type RangeMark = BaseMark<'range', ChannelTypes>;

export type RangeXMark = BaseMark<'rangeX', ChannelTypes>;

export type RangeYMark = BaseMark<'rangeY', ChannelTypes>;

export type ConnectorMark = BaseMark<'connector', ChannelTypes>;

export type CellMark = BaseMark<'cell', ChannelTypes>;

export type AreaMark = BaseMark<'area', ChannelTypes>;

export type NodeMark = BaseMark<'node', ChannelTypes>;

export type EdgeMark = BaseMark<'edge', ChannelTypes>;

export type LinkMark = BaseMark<'link', ChannelTypes>;

export type ImageMark = BaseMark<'image', ChannelTypes | 'src'>;

export type PolygonMark = BaseMark<'polygon', ChannelTypes>;

export type BoxMark = BaseMark<'box', ChannelTypes>;

export type BoxPlotMark = BaseMark<'box', ChannelTypes>;

export type ShapeMark = BaseMark<'shape', ChannelTypes>;

export type VectorMark = BaseMark<'vector', ChannelTypes | 'rotate' | 'size'>;

export type SankeyMark = BaseMark<
  'sankey',
  | 'source'
  | 'target'
  | 'value'
  | `node${Capitalize<ChannelTypes>}`
  | `link${Capitalize<ChannelTypes>}`
  | ChannelTypes
> & {
  layout?: {
    nodeId?: (node: any) => string;
    nodes?: (graph: any) => any;
    links?: (graph: any) => any;
    /**
     * sankey.nodeSort(undefined) is the default and resorts by ascending breadth during each iteration.
     * sankey.nodeSort(null) specifies the input order of nodes and never sorts.
     * sankey.nodeSort(function) specifies the given order as a comparator function and sorts once on initialization.
     */
    nodeSort?: null | undefined | ((a: any, b: any) => number);
    /**
     * sankey.linkSort(undefined) is the default, indicating that vertical order of links within each node will be determined automatically by the layout. If
     * sankey.linkSort(null) will resort by the input.
     * sankey.linkSort(function) specifies the given order as a comparator function and sorts once on initialization.
     */
    linkSort?: null | undefined | ((a: any, b: any) => number);
    nodeAlign?:
      | 'left'
      | 'center'
      | 'right'
      | 'justify'
      | ((node: any, n: number) => number);
    nodeWidth?: number;
    nodePadding?: number;
    iterations?: number;
    // support config the depth of node
    nodeDepth?: (datum: any, maxDepth: number) => number;
  };
  nodeLabels: Record<string, any>[];
  linkLabels: Record<string, any>[];
};

export type ChordMark = BaseMark<
  'chord',
  | 'source'
  | 'target'
  | 'value'
  | `node${Capitalize<ChannelTypes>}`
  | `link${Capitalize<ChannelTypes>}`
  | ChannelTypes
> & {
  layout?: {
    nodes?: (graph: any) => any;
    links?: (graph: any) => any;
    y?: number;
    id?: (node: any) => any;
    sortBy?:
      | 'id'
      | 'weight'
      | 'frequency'
      | null
      | ((a: any, b: any) => number);
    nodeWidthRatio?: number;
    nodePaddingRatio?: number;
    sourceWeight?(edge: any): number;
    targetWeight?(edge: any): number;
  };
  nodeLabels: Record<string, any>[];
  linkLabels: Record<string, any>[];
};

export type PathMark = BaseMark<'path', ChannelTypes | 'd'>;

export type TreemapMark = BaseMark<'treemap', 'value' | ChannelTypes> & {
  layout?: Record<string, any>;
};

export type PackMark = BaseMark<'pack', 'value' | ChannelTypes> & {
  layout?: Record<string, any>;
};

export type ForceGraphMark = BaseMark<
  'forceGraph',
  | 'source'
  | 'target'
  | 'color'
  | 'value'
  | `node${Capitalize<ChannelTypes>}`
  | `link${Capitalize<ChannelTypes>}`
> & {
  layout?: Record<string, any>;
  nodeLabels: Record<string, any>[];
  linkLabels: Record<string, any>[];
};

export type TreeMark = BaseMark<'tree', 'value' | ChannelTypes> & {
  layout?: {
    /**
     * Layout field. Default: 'value'.
     */
    field?: string;
    /**
     * Sets this cluster layout’s node size to the specified two-element array of numbers [width, height] and returns this cluster layout.
     * Default: null.
     */
    nodeSize?: any;
    /**
     * The separation accessor is used to separate neighboring leaves.  Default: (a, b) => a.parent == b.parent ? 1 : 2;
     */
    separation?: (a, b) => number;
    /**
     * Sort function by compare 2 nodes.
     */
    sortBy?: (a, b) => number;
    /**
     * Layout infomation saved into fields. Default: ['x', 'y'].
     */
    as?: [string, string];
  };
  nodeLabels: Record<string, any>[];
  linkLabels: Record<string, any>[];
};

export type WordCloudMark = BaseMark<
  'wordCloud',
  'value' | ChannelTypes | 'text'
> & {
  layout?: {
    /**
     * @description If specified, sets the rectangular [width, height] of the layout
     * @default [1, 1]
     */
    size?: [number, number];
    font?: string | ((word: any) => string);
    fontStyle?: string | ((word: any) => string);
    fontWeight?: any | ((word: any) => any);
    fontSize?: number | [number, number] | ((word: any) => number);
    padding?: number | ((word: any) => number);
    /**
     * @description sets the text accessor function, which indicates the text for each word
     * @default (d) => d.text
     */
    text?: (word: any) => number;
    rotate?: number | ((word: any) => number);
    timeInterval?: number;
    random?: number | (() => number);
    /**
     * @description sets the current type of spiral used for positioning words. This can either be one of the two built-in spirals, "archimedean" and "rectangular"
     * @default "archimedean"
     */
    spiral?:
      | 'archimedean'
      | 'rectangular'
      | ((size: [number, number]) => (t: number) => number[]);
    imageMask?: HTMLImageElement | string;
    on?:
      | ((type: 'end', details?: { cloud; words; bounds }) => void)
      | ((type: 'word', details?: { cloud; word }) => void);
  };
};

export type GaugeMark = BaseMark<
  'gauge',
  | `arc${Capitalize<ChannelTypes>}`
  | `indicator${Capitalize<ChannelTypes>}`
  | `pointer${Capitalize<ChannelTypes>}`
  | `pin${Capitalize<ChannelTypes>}`
  | ChannelTypes
>;

export type DensityMark = BaseMark<'density', ChannelTypes | 'series'>;
export type HeatmapMark = BaseMark<'heatmap'>;
export type LiquidMark = BaseMark<'liquid'>;

export type CustomMark = BaseMark<MarkComponent, ChannelTypes>;
