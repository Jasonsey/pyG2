# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/17 09:48
#
# =============================================================================
"""chart"""
from typing import *
from dataclasses import dataclass, field

from .mark import Mark
from .base import PlotForAPI


@dataclass
class ChartDS:
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
    """图标生成字典对象"""
    kwargs: Optional[Dict[str, Any]] = None


class Chart(Mark):

    def interval(self):
        self.render_data.append(['interval()'])
        return self

    def rect(self):
        self.render_data.append(['rect()'])
        return self

    def point(self):
        self.render_data.append(['point()'])
        return self

    def area(self):
        self.render_data.append(['area()'])
        return self

    def line(self):
        self.render_data.append(['line()'])
        return self

    def vector(self):
        self.render_data.append(['vector()'])
        return self

    def link(self):
        self.render_data.append(['link()'])
        return self

    def polygon(self):
        self.render_data.append(['polygon()'])
        return self

    def image(self):
        self.render_data.append(['image()'])
        return self

    def text(self):
        self.render_data.append(['text()'])
        return self

    def line_x(self):
        self.render_data.append(['lineX()'])
        return self

    def line_y(self):
        self.render_data.append(['lineY()'])
        return self

    def range(self):
        self.render_data.append(['range()'])
        return self

    def range_x(self):
        self.render_data.append(['rangeX()'])
        return self
        pass

    def range_y(self):
        self.render_data.append(['rangeY()'])
        return self

    def connector(self):
        self.render_data.append(['connector()'])
        return self

    def sankey(self):
        self.render_data.append(['sankey()'])
        return self

    def treemap(self):
        self.render_data.append(['treemap()'])
        return self

    def boxplot(self):
        self.render_data.append(['boxplot()'])
        return self

    def density(self):
        self.render_data.append(['density()'])
        return self

    def heatmap(self):
        self.render_data.append(['heatmap()'])
        return self

    def shape(self):
        self.render_data.append(['shape()'])
        return self

    def pack(self):
        self.render_data.append(['pack()'])
        return self

    def force_graph(self):
        self.render_data.append(['forceGraph()'])
        return self

    def tree(self):
        self.render_data.append(['tree()'])
        return self

    def word_cloud(self):
        self.render_data.append(['wordCloud()'])
        return self

    def gauge(self):
        self.render_data.append(['gauge()'])
        return self

    def view(self):
        self.render_data.append(['view()'])
        return self

    def space_layer(self):
        self.render_data.append(['spaceLayer()'])
        return self

    def space_flex(self):
        self.render_data.append(['spaceFlex()'])
        return self

    def facet_rect(self):
        self.render_data.append(['facetRect()'])
        return self

    def facet_circle(self):
        self.render_data.append(['facetCircle()'])
        return self

    def repeat_matrix(self):
        self.render_data.append(['repeatMatrix()'])
        return self

    def geo_view(self):
        self.render_data.append(['geoView()'])
        return self

    def geo_path(self):
        self.render_data.append(['geoPath()'])
        return self

    def timing_keyframe(self):
        self.render_data.append(['timingKeyframe()'])
        return self

    def point_3d(self):
        self.render_data.append(['point3D()'])
        return self

    def interval_3d(self):
        self.render_data.append(['interval3D()'])
        return self

    def line_3d(self):
        self.render_data.append(['line3D()'])
        return self
