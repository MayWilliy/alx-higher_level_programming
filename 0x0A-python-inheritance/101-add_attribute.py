#!/usr/bin/python3


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    try:
        setattr(obj, attribute, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
