from enum import StrEnum

class GraphicsItemType(StrEnum):
    """Enum for graphics item types."""

    LINE = "line"
    RECTANGLE = "rectangle"
    ELLIPSE = "ellipse"
    POLYGON = "polygon"
    PATH = "path"
    TEXT = "text"
    IMAGE = "image"