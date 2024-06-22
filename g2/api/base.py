# -*- coding: utf-8 -*-
#
# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/18 08:37
#
# =============================================================================
"""base"""
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import *

from jinja2 import Environment

from g2.utils.common import json_dump_to_js, HTML
from g2.utils.engine import Engine
from g2.utils.plot import G2PLOT_LIB


class Mark:

    def data(self, item: dict):
        pass

    def encode(self, *args):
        pass

    def scale(self, *args):
        pass

    def transform(self, *args):
        pass

    def layout(self):
        pass

    def coordinate(self):
        pass

    def style(self):
        pass

    def view_style(self):
        pass

    def animate(self):
        pass

    def state(self):
        pass

    def label(self):
        pass

    def title(self):
        pass

    def axis(self):
        pass

    def legend(self):
        pass

    def tooltip(self):
        pass

    def scrollbar(self):
        pass

    def slider(self):
        pass

    def interaction(self):
        pass

    def theme(self):
        pass


@dataclass
class PlotForAPI:
    """instance with plot type string"""
    plot_api_type: Literal['api', 'spec'] = 'api'
    """绘图使用的接口类型"""
    plot_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    render_data: List[List[str]] = field(default_factory=list)
    """用于生成API的数据"""
    dependencies: Optional[List[Dict[str, str]]] = None
    page_title: str = 'PyG2'
    """page setting"""

    def render_notebook(self, env: Optional[Environment] = None, **kwargs) -> HTML:
        """render plot into jupyter"""
        self.dump_options()
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="notebook.jinja",
            **kwargs
        ))

    def render_jupyter_lab(self, env: Optional[Environment] = None, **kwargs) -> HTML:
        """ render plot into jupyter lab """
        self.dump_options()
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="jupyter-lab.jinja",
            **kwargs
        ))

    def render_html(self, env: Optional[Environment] = None, **kwargs) -> str:
        """ render plot to html string """
        self.dependencies = [{
            "name": "G2",
            "asset": G2PLOT_LIB,
        }]
        # get html string
        return Engine(env=env).render(
            plot=self,
            template_name="plot.jinja",
            **kwargs
        )

    def render(self, path: str = "./tmp/plot.html", env: Optional[Environment] = None, **kwargs) -> str:
        """ render the plot into html file """
        # get html string
        html = self.render_html(env, **kwargs)
        # write output into file
        if not Path(path).parent.exists():
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(html)
        return path
