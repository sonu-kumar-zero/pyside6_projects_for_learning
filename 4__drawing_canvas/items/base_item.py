from items.graphics_item_type import GraphicsItemType

class BaseItem:
    ITEM_TYPE: GraphicsItemType
    
    def item_type(self) -> GraphicsItemType:
        return self.ITEM_TYPE

    def to_dict(self) -> dict[str, float | str]:
        raise NotImplementedError("Subclasses must implement to_dict method")
    
    @classmethod
    def from_dict(cls, data: dict[str, float | str]) -> 'BaseItem':
        raise NotImplementedError("Subclasses must implement from_dict method")