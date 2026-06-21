from PySide6.QtWidgets import QGraphicsScene

from pathlib import Path

import json
from typing import Any

from items.item_factory import ItemFactory

class SceneDeserializer:
    @staticmethod
    def load(
        scene: QGraphicsScene,
        file_path: str | Path,
    ) -> None:
        with open(file_path, "r", encoding="utf-8") as file:
            data: dict[str, Any] = json.load(file)
        
        scene.clear()
        
        for item_data in data.get("items", []):
            item = ItemFactory.create_item(item_data)
            scene.addItem(item)