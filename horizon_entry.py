"""Entrypoint for Prefect Horizon (FastMCP Cloud).

server.py uses relative imports, so add src/ to sys.path and import the server
as a package instead of relying on the project being installed.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))

from farnell_mcp.server import mcp  # noqa: E402

__all__ = ["mcp"]
