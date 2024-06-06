from typing import *
from dataclasses import dataclass


@dataclass
class Transform:
    type: str


@dataclass
class TransformContrastReverse(Transform):
    threshold: float = 4.5
    palette: List[str] = ['#000', '#fff']
    type: str = 'contrastReverse'


@dataclass
class TransformExceedAdjust(Transform):
    type: str = 'exceedAdjust'


@dataclass
class TransformOverflowHide(Transform):
    type: str = 'overflowHide'


@dataclass
class TransformOverlapDodgeY(Transform):
    max_iterations: int = 10
    padding: int = 1
    max_error: int = 0.1
    type: str = 'overlapDodgeY'


@dataclass
class TransformOverlapHide(Transform):
    type: str = 'overlapHide'

