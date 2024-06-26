# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/8 09:55
#
# =============================================================================
"""animate

动画组件
"""
from typing import *
from dataclasses import dataclass

from g2.utils.common import number


AnimationTypes = Literal[
    'fadeIn',
    'fadeOut',
    'scaleInX',
    'scaleOutX',
    'scaleInY',
    'scaleOutY',
    'waveIn',
    'morphing',
    'zoomIn',
    'zoomOut',
    'pathIn',
    'growInX',
    'growInY',
]


@dataclass
class BaseAnimation:
    type: Optional[AnimationTypes] = None
    duration: Optional[number] = None
    delay: Optional[number] = None
    easing: Optional[str] = None
    fill: Optional[Literal['forwards', 'none', 'backwards', 'both', 'auto']] = None


@dataclass
class FadeInAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'fadeIn'


@dataclass
class FadeOutAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'fadeOut'


@dataclass
class ScaleInXAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'scaleInX'


@dataclass
class ScaleOutXAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'scaleOutX'


@dataclass
class ScaleInYAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'scaleInY'


@dataclass
class ScaleOutYAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'scaleOutY'


@dataclass
class WaveInAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'waveIn'


@dataclass
class MorphingAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'morphing'


@dataclass
class ZoomInAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'zoomIn'


@dataclass
class ZoomOutYAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'zoomOut'


@dataclass
class PathInAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'pathIn'


@dataclass
class GrowInXAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'growInX'


@dataclass
class GrowInYAnimation(BaseAnimation):
    type: Optional[AnimationTypes] = 'growInY'


Animation = Union[
    FadeInAnimation,
    FadeOutAnimation,
    ScaleInXAnimation,
    ScaleOutXAnimation,
    ScaleInYAnimation,
    ScaleOutYAnimation,
    WaveInAnimation,
    MorphingAnimation,
    ZoomInAnimation,
    ZoomOutYAnimation,
    PathInAnimation,
    GrowInXAnimation,
    GrowInYAnimation,
]
