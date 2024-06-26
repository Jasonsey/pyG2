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
from typing import Literal, Dict, Optional, List

from jinja2 import Environment

from g2.utils.common import HTML
from g2.core.engine import Engine


G2PLOT_LIB = 'https://unpkg.com/@antv/g2@5'


@dataclass
class PlotBase:
    plot_api_type: Literal['api', 'spec'] = 'api'
    """绘图使用的接口类型"""
    plot_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    """图表唯一ID"""
    dependencies: Optional[List[Dict[str, str]]] = None
    """依赖包"""
    page_title: str = 'PyG2'
    """page setting"""

    def render_notebook(self, env: Optional[Environment] = None, **kwargs) -> HTML:
        """render plot into jupyter"""
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="notebook.jinja",
            **kwargs
        ))

    def render_jupyter_lab(self, env: Optional[Environment] = None, **kwargs) -> HTML:
        """ render plot into jupyter lab """
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
        return Engine(env=env).render(
            plot=self,
            template_name="plot.jinja",
            **kwargs
        )

    def render(self, path: str = "./tmp/plot.html", env: Optional[Environment] = None, **kwargs) -> str:
        """ render the plot into html file """
        html = self.render_html(env, **kwargs)
        if not Path(path).parent.exists():
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(html)
        return path


@dataclass
class PlotForAPI(PlotBase):
    plot_api_type: Literal['api', 'spec'] = 'api'
    """绘图使用的接口类型"""
    render_data: List[List[str]] = field(default_factory=list)
    """用于生成API的数据"""


@dataclass
class PlotForSpec(PlotBase):
    plot_api_type: Literal['api', 'spec'] = 'spec'
    """绘图使用的接口类型"""

    js_options: str = ''
    """写入js中的options选项"""

    # def options(self, options: dict):
    #     """set the G2 options, documents [here](https://g2.antv.antgroup.com/)"""
    #     self.js_options = json_dump_to_js(options)
    #     return self
