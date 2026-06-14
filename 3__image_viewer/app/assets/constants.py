from dataclasses import dataclass

@dataclass
class Constants:
    # Zoom Constants
    ZOOM_IN_FACTOR: float = 1.15
    ZOOM_OUT_FACTOR: float = 0.8
    
    DEFAULT_ZOOM: float = 1.0
    
    MIN_ZOOM: float = 0.1
    MAX_ZOOM: float = 5.0
    
VALID_IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
    ".webp",
}