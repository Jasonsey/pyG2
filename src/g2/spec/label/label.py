from typing import *
from dataclasses import dataclass

from .label_transform import LabelTransform

__all__ = ["Label"]


@dataclass
class Label:
    font_size: Optional[int] = None
    font_family: Optional[str] = None
    font_weight: Optional[int] = None
    line_weight: Optional[int] = None
    text_align: Literal['center', 'end', 'left', 'right', 'start'] = 'start'
    text_baseline: Literal['top', 'middle', 'bottom', 'alphabetic', 'hanging'] = 'bottom'
    fill: Optional[str] = None
    fill_opacity: Optional[int] = None
    stroke: Optional[str] = None
    stroke_opacity: Optional[int] = None
    line_width: Optional[int] = None
    line_dash: Optional[Tuple[int, int]] = None
    opacity: Optional[int] = None
    shadow_color: Optional[str] = None
    shadow_blur: Optional[int] = None
    shadow_offset_x: Optional[int] = None
    shadow_offset_y: Optional[int] = None
    cursor: str = 'default'
    position: Optional[Literal[
        'top', 'left', 'right', 'bottom', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'inside', 'outside',
        'spider', 'surround', 'area']] = None
    selector: Optional[Literal['last', 'first']] = None
    connector: Optional[bool] = None
    background: Optional[bool] = None
    transform: Optional[List[LabelTransform]] = None

    connector_stroke: Optional[str] = None
    connector_line_width: Optional[int] = None

    background_fill: Optional[str] = None
    background_radius: Optional[int] = None
    background_padding: Optional[List[int]] = None
