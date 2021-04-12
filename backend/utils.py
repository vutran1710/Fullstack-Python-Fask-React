"""Flask-specific utilities / config
"""
from flask import g
from services import Cache, FileWriter, DataGenerator


def get_dependencies(*services):
    """Retrive the service-instance of either
    Cache, FileWriter or DataGenerator
    """
    if "ch" not in g:
        g.ch = Cache()

    if "fw" not in g:
        g.fw = FileWriter()

    if "dg" not in g:
        g.dg = DataGenerator()

    svcs = [getattr(g, s) for s in services]
    return svcs if len(svcs) > 1 else svcs[0]
