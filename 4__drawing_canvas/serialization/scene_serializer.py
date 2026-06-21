from PySide6.QtWidgets import QGraphicsScene
from pathlib import Path

from items.base_item import BaseItem

import json



class SceneSerializer:
    @staticmethod
    def save(
        scene: QGraphicsScene,
        file_path: str | Path,
    ) -> None:
        data: dict[str, list[dict[str, float | str]]] = {
            "items": []
        }
        
        for item in scene.items():
            if isinstance(item, BaseItem):
                data["items"].append(item.to_dict())
        
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
