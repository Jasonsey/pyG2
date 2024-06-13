# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/11 08:14
#
# =============================================================================
"""plot"""
import re
import uuid
import datetime
from typing import *
from pathlib import Path
from dataclasses import dataclass, field

import simplejson
from jinja2 import Environment

from .engine import Engine


G2PLOT_LIB = 'https://unpkg.com/@antv/g2@5'


class HTML:
    def __init__(self, data: Optional[str] = None):
        self.data = data

    def _repr_html_(self):
        return self.data

    def __html__(self):
        return self._repr_html_()


SEP = "!!-_-____-_-!!"


class JS:
    def __init__(self, js_code: str):
        self.js_code = "%s%s%s" % (SEP, js_code, SEP)

    def replace(self, pattern: str, repl: str):
        self.js_code = re.sub(pattern, repl, self.js_code)
        return self


def _json_dump_default(o: object):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, JS):
        return o.replace("\\n|\\t", "").replace(r"\\n", "\n").replace(r"\\t", "\t").js_code
    return o


def json_dump_to_js(options: object):
    return re.sub(
        '"?%s"?' % SEP,
        "",
        simplejson.dumps(options, indent=2, default=_json_dump_default, ignore_nan=True)
    )


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
