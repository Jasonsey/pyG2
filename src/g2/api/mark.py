# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/17 09:48
#
# =============================================================================
"""mark"""
from typing import *

from g2.spec.data import InlineConnector, Data, FetchConnector
from g2.spec.scale import Scale
from g2.spec.transform import TransformTypes
from g2.spec.coordinate import CoordinateTypes, Coordinate
from g2.spec.animate import Animation
from g2.spec.interaction import Interaction
from g2.spec.theme import Theme, ThemeTypes

from g2.utils.common import ChannelTypes, dump_to_js_string
from g2.core.plot import PlotForAPI


class Mark(PlotForAPI):

    def data(self, item: Data | list | dict):
        if isinstance(item, list):
            item = InlineConnector(value=item)
        elif isinstance(item, dict):
            if item['type'] == 'fetch':
                item = FetchConnector(**item)
            elif item['type'] == 'inline':
                item = InlineConnector(**item)
            else:
                raise KeyError('Unknown item type')
        item = dump_to_js_string(item)
        self.render_data[-1].append(f"data({item})")
        return self

    def encode(self, channel: ChannelTypes, value: str):
        channel = dump_to_js_string(channel)
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"encode({channel}, {value})")
        return self

    def scale(self, channel: ChannelTypes, value: Scale | dict):
        channel = dump_to_js_string(channel)
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"scale({channel}, {value})")
        return self

    def transform(self, value: Dict[Literal['type'], TransformTypes]):
        self.render_data[-1].append(f"transform({value})")
        return self

    def layout(self, value: Dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"layout({value})")
        return self

    def coordinate(self, value: Dict[Literal['type'], CoordinateTypes] | Coordinate):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"coordinate({value})")
        return self

    def style(self, key, value):
        key = dump_to_js_string(key)
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"style({key}, {value})")
        return self

    def view_style(self, key, value):
        key = dump_to_js_string(key)
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"viewStyle('{key}', {value})")
        return self

    def animate(self, key: Literal['enter', 'update', 'exit'], value: Animation | dict):
        key = dump_to_js_string(key)
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"animate('{key}', {value})")
        return self

    def state(self, key: Literal['active', 'inactive', 'selected', 'unselected'], value: dict):
        key = dump_to_js_string(key)
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"state('{key}', {value})")
        return self

    def label(self, value: dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"label({value})")
        return self

    def title(self, value: Dict[Literal['title', 'subtitle'], str]):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"title({value})")
        return self

    def axis(self, value: dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"axis({value})")
        return self

    def legend(self, value: dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"legend({value})")
        return self

    def tooltip(self, value: dict | bool):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"tooltip({value})")
        return self

    def scrollbar(self, value: dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"scrollbar({value})")
        return self

    def slider(self, value: dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"slider({value})")
        return self

    def interaction(self, value: Interaction | dict):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"interaction({value})")
        return self

    def theme(self, value: Theme | Dict[Literal['type'], ThemeTypes]):
        value = dump_to_js_string(value)
        self.render_data[-1].append(f"theme({value})")
        return self
