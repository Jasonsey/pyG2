# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/23 16:40
#
# =============================================================================
"""chart"""
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class ChartBase:
    container: str = 'container'
    """指定 chart 绘制的 DOM，可以传入 DOM id"""
    width: int = 640
    """图表宽度"""
    height: int = 480
    """图表高度"""
    depth: int = 0
    """图表深度，在 3D 图表中使用"""
    autoFit: bool = False
    """图表是否自适应容器宽高，默认为 false，用户需要手动设置 width 和 height。
    当 autoFit: true 时，会自动取图表容器的宽高，如果用户设置了 height，那么会以用户设置的 height 为准。"""
    padding: int = 30
    """图表内边距"""
    kwargs: Optional[Dict[str, Any]] = None
