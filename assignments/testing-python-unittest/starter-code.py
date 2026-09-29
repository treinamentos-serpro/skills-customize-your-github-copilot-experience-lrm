import unittest


def calculate_discount(price, percentage):
    """Return the price after applying a percentage discount."""
    if percentage < 0 or percentage > 100:
        raise ValueError("percentage must be between 0 and 100")
    return round(price * (1 - percentage / 100), 2)


def format_username(username):
    """Return a normalized username."""
    return username.strip().lower()


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if quantity <= 0:
            raise ValueError("quantity must be greater than zero")
        self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name):
        self.items.pop(name, None)

    def total(self):
        return sum(item["price"] * item["quantity"] for item in self.items.values())


class TestFunctions(unittest.TestCase):
    def test_calculate_discount(self):
        # TODO: Add assertions for regular discount calculations.
        pass

    def test_format_username(self):
        # TODO: Test whitespace removal and lowercase conversion.
        pass

    def test_invalid_discount(self):
        # TODO: Use assertRaises for invalid percentages.
        pass


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # TODO: Create a new cart before each test.
        self.cart = None

    def test_add_item_and_total(self):
        # TODO: Add items and verify the total.
        pass

    def test_remove_item(self):
        # TODO: Remove an existing item and verify the result.
        pass

    def test_invalid_quantity(self):
        # TODO: Use assertRaises for zero or negative quantities.
        pass


if __name__ == "__main__":
    unittest.main()
