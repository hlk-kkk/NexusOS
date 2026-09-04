"""Java code intelligence support for NexusOS.

Provides Java parsing, symbol extraction and impact analysis foundations.
"""

from .parser import JavaParser
from .call_graph import JavaCallGraph

__all__ = ["JavaParser", "JavaCallGraph"]
