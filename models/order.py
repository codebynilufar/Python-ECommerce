import json
import os
from datetime import datetime
from models.order_item import OrderItem

ORDERS_PATH = "database/orders.json"

class Order:
    def __init__(self, user_id, items, created_at=None):
        self.user_id = user_id
        self.items = items
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "items": [item.to_dict() for item in self.items],
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        items = [OrderItem.from_dict(d) for d in data["items"]]
        return cls(
            user_id=data["user_id"],
            items=items,
            created_at=data["created_at"]
        )

    @classmethod
    def load_orders(cls):
        if not os.path.exists(ORDERS_PATH):
            return []
        with open(ORDERS_PATH, "r") as f:
            try:
                data = json.load(f)
                return [cls.from_dict(d) for d in data]
            except json.JSONDecodeError:
                return []

    @classmethod
    def save_orders(cls, orders):
        with open(ORDERS_PATH, "w") as f:
            json.dump([order.to_dict() for order in orders], f, indent=4)

    @classmethod
    def add_order(cls, order):
        orders = cls.load_orders()
        orders.append(order)
        cls.save_orders(orders)
