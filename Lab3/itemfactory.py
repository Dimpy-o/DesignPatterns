from abc import ABC, abstractmethod


# Abstract Item class
class Item(ABC):
    def __init__(self, item_id, item_weight, item_count):
        self.item_id = item_id
        self.item_weight = item_weight
        self.item_count = item_count

    def get_total_item_weight(self) -> float:
        return self.item_weight * self.item_count

    @abstractmethod
    def item_type(self) -> str:
        pass
    

# Concrete Item classes
class Small(Item):
    def item_type(self) -> str:
        return "Small"


class Heavy(Item):
    def item_type(self) -> str:
        return "Heavy"


class Refrigerated(Item):
    def item_type(self) -> str:
        return "Refrigerated"


class Liquid(Item):
    def item_type(self) -> str:
        return "Liquid"


# Abstract Factory
class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, item_id, item_weight, item_count) -> Item:
        pass


# Concrete Factories
class SmallItemFactory(ItemFactory):
    def create_item(self, item_id, item_weight, item_count) -> Item:
        return Small(item_id, item_weight, item_count)


class HeavyItemFactory(ItemFactory):
    def create_item(self, item_id, item_weight, item_count) -> Item:
        return Heavy(item_id, item_weight, item_count)


class RefrigeratedItemFactory(ItemFactory):
    def create_item(self, item_id, item_weight, item_count) -> Item:
        return Refrigerated(item_id, item_weight, item_count)


class LiquidItemFactory(ItemFactory):
    def create_item(self, item_id, item_weight, item_count) -> Item:
        return Liquid(item_id, item_weight, item_count)