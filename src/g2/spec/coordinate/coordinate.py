# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 10:34
#
# =============================================================================
"""coordinate"""
from typing import *
from dataclasses import dataclass

from .coordinate_transform import CoordinateTransform
from g2.utils.common import number

__all__ = [
    'CoordinateTypes',
    'PolarCoordinate',
    'HelixCoordinate',
    'RadarCoordinate',
    'ThetaCoordinate',
    'RadialCoordinate',
    'CartesianCoordinate',
    'ParallelCoordinate',
    'GeoCoordinate',
    'Coordinate'
]

CoordinateTypes = Union[str, Literal[
    'polar',
    'helix',
    'transpose',
    'theta',
    'cartesian',
    'cartesian3D',
    'parallel',
    'fisheye',
    'radial',
    'radar',
]]


@dataclass
class BaseCoordinate:
    transform: Optional[List[CoordinateTransform]] = None


@dataclass
class PolarCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'polar'
    startAngle: Optional[number] = None
    endAngle: Optional[number] = None
    innerRadius: Optional[number] = None
    outerRadius: Optional[number] = None


@dataclass
class HelixCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'helix'
    startAngle: Optional[number] = None
    endAngle: Optional[number] = None
    innerRadius: Optional[number] = None
    outerRadius: Optional[number] = None


@dataclass
class RadarCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'radar'
    startAngle: Optional[number] = None
    endAngle: Optional[number] = None
    innerRadius: Optional[number] = None
    outerRadius: Optional[number] = None


@dataclass
class ThetaCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'theta'
    startAngle: Optional[number] = None
    endAngle: Optional[number] = None
    innerRadius: Optional[number] = None
    outerRadius: Optional[number] = None


@dataclass
class RadialCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'radial'
    startAngle: Optional[number] = None
    endAngle: Optional[number] = None
    innerRadius: Optional[number] = None
    outerRadius: Optional[number] = None


@dataclass
class CartesianCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'cartesian'


@dataclass
class ParallelCoordinate(BaseCoordinate):
    type: Optional[CoordinateTypes] = 'parallel'


@dataclass
class GeoCoordinate(BaseCoordinate):
    type: Optional[str] = None
    """type is required for this case"""
    kwargs: Optional[dict[str, Any]] = None


Coordinate = Union[
    PolarCoordinate,
    HelixCoordinate,
    ThetaCoordinate,
    CartesianCoordinate,
    ParallelCoordinate,
    RadialCoordinate,
    RadarCoordinate,
    GeoCoordinate,
]
