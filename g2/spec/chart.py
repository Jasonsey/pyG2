from typing import *
from dataclasses import dataclass


@dataclass
class Transform:
    pass


@dataclass
class Data:
    type: str = 'inline'
    value: List
    transform: Transform


@dataclass
class Options:
    data: Data
    type: Literal['area', 'box', 'boxplot', 'cell', 'chord', 'density', 'gauge', 'heatmap', 'image', 'interval',
                   'line', 'lineX', 'lineY', 'link', 'liquid', 'point', 'polygon', 'range', 'rangeX', 'rangeY', 'rect', 
                   'shape', 'text', 'vector', 'wordCloud']
    