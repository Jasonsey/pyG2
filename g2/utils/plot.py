# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/11 08:14
#
# =============================================================================
"""plot"""
import uuid
from typing import *
from pathlib import Path
from dataclasses import dataclass, field

from jinja2 import Environment

from .common import json_dump_to_js, HTML
from .engine import Engine


G2PLOT_LIB = 'https://unpkg.com/@antv/g2@5'


@dataclass
class Plot:
    """instance with plot type string"""
    plot_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    version: str = '2'
    options: Dict = field(default_factory=lambda: dict())
    js_options: str = ''
    dependencies: Optional[List[Dict[str, str]]] = None
    page_title: str = 'PyG2'
    """page setting"""

    def set_options(self, options: dict):
        """set the G2 options, documents [here](https://g2.antv.antgroup.com/)"""
        self.options = options
        return self

    def dump_options(self):
        """处理options关联内容"""
        self.js_options = json_dump_to_js(self.options)

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
        self.dump_options()
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
