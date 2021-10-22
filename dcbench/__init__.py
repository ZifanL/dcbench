"""The dcbench module is a collection for benchmarks that test various apsects of data preparation and handling
in the context of AI workflows.
"""

from .__main__ import main
from .version import __version__

from .common import Scenario, Solution, Artefact
from .scenarios.miniclean import *

