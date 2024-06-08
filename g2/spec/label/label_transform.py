from typing import *
from dataclasses import dataclass

from g2.common import number


@dataclass
class OverlapHideLabelTransform:
    type: str = 'overlapHide'
    priority: Optional[Callable[[Any, Any], number]] = None
    """The hide priority, is the comparator for label.sort()."""


@dataclass
class OverlapDodgeYLabelTransform:
    type: str = 'overlapDodgeY'
    maxIterations: Optional[number] = None
    maxError: Optional[number] = None
    padding: Optional[number] = None


@dataclass
class ContrastReverseLabelTransform:
    type: str = 'contrastReverse'
    threshold: Optional[number] = None
    """Transform when the contrast ratio < threshold. Default is `4.5`."""
    palette: Optional[List[str]] = None
    """The optional color palette, default is [#000, #fff]."""


@dataclass
class OverflowHideLabelTransform:
    type: str = 'overflowHide'


@dataclass
class ExceedAdjustLabel:
    type: str = 'exceedAdjust'


LabelTransform = Union[
    OverlapHideLabelTransform,
    OverlapDodgeYLabelTransform,
    ContrastReverseLabelTransform,
    OverflowHideLabelTransform,
    ExceedAdjustLabel,
]
