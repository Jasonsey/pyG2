# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 10:34
#
# =============================================================================
"""coordinate_transform"""
from typing import *
from dataclasses import dataclass

from g2.utils.common import number

__all__ = [
    'CoordinateTransformTypes',
    'TransposeCoordinate',
    'FisheyeCoordinate',
    'CoordinateTransform'
]

CoordinateTransformTypes = Literal['transpose', 'fisheye']


@dataclass
class TransposeCoordinate:
    type: Optional[CoordinateTransformTypes] = 'transpose'


@dataclass
class FisheyeCoordinate:
    type: Optional[CoordinateTransformTypes] = 'fisheye'
    focusX: Optional[number] = None
    focusY: Optional[number] = None
    distortionX: Optional[number] = None
    distortionY: Optional[number] = None
    visual: Optional[bool] = None


CoordinateTransform = Union[TransposeCoordinate, FisheyeCoordinate]
