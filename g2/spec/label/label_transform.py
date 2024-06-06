from typing import *
from dataclasses import dataclass

from g2.common import number


@dataclass
class OverlapHideLabelTransform:
    type: str = 'overlapHide'
    # The hide priority, is the comparator for label.sort().
    priority: Optional[Callable[[Any, Any], number]] = None


@dataclass
class OverlapDodgeYLabelTransform:
    type: str = 'overlapDodgeY'
    maxIterations: Optional[number] = None
    maxError: Optional[number] = None
    padding: Optional[number] = None


@dataclass
class ContrastReverseLabelTransform:
    type: str = 'contrastReverse'
    # Transform when the contrast ratio < threshold.
    # Default is `4.5`.
    threshold: Optional[number] = None
    # The optional color palette, default is [#000, #fff].
    palette: Optional[List[str]] = None


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
