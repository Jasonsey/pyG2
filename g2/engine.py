# pyG2
#
# @Author: Lin, Max
# @Email : jason.max.lin@outlook.com
# @Time  : 2024/6/11 08:14
#
# =============================================================================
"""engine"""
import os
from dataclasses import dataclass

from jinja2 import Environment, FileSystemLoader
from typing import Optional


GLOBAL_ENV = Environment(
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "templates"
        )
    ),
)


@dataclass
class Engine:
    env: Optional[Environment] = None

    def render(self, plot: any, template_name: str, **kwargs):
        """ render plot to html string with template """
        # get template content
        env = GLOBAL_ENV if self.env is None else self.env
        tpl = env.get_template(template_name)
        # render with jinja2
        return tpl.render(plot=plot, **kwargs)
