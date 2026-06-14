from dataclasses import dataclass
from pathlib import Path

from app.assets.constants import Constants

@dataclass
class ImageState:
    current_file: Path | None = None
    zoom_factor: float = Constants.DEFAULT_ZOOM
    fit_to_window: bool = True
