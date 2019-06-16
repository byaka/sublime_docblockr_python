"""Tools for handling registering additional plugins.

Variables:
    REGISTRY {dict} -- Contains the Registered Parsers
"""

REGISTRY = {}


def register(Cls):
    """Add the passed class object to the registry of formatters.

    If the friendly class name matches the base formatters, it will
    not be added to the registry.

    Arguments:
        Cls {class} -- Uninitialized class object

    Returns:
        {class} -- Uninitialized class object
    """
    if Cls.name is None:
        return Cls

    global REGISTRY
    REGISTRY[Cls.name] = Cls
    return Cls


def populate_registry():
    """Import the list of built in parsers and adds them to the registry."""
    from . import (  # noqa: F401
        base,
        PEP0257,
        docblock,
        google,
        sphinx,
        sphinx2,
        numpy
    )
