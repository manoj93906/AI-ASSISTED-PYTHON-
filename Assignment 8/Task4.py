# AI-generated test cases for a ShoppingCart class.
# Methods assumed:
#   add_item(name, price)
#   remove_item(name)
#   total_cost()

class ShoppingCart:
    def __init__(self):
        self.items = {}  # name -> price

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        return sum(self.items.values())


def generate_shopping_cart_test_cases():
    """
    Generates diverse test cases for ShoppingCart:
    - Adding items
    - Removing items (existent/non-existent)
    - Calculating total cost (empty, after add, after remove)
    Returns a list of (description, test_fn) for manual running.
    """
    cases = []

    # Test 1: Add a single item, check total
    def test_add_one():
        cart = ShoppingCart()
        cart.add_item("apple", 1.20)
        assert cart.total_cost() == 1.20, "Total should be 1.20 after adding apple"

    cases.append(("Add one item, check total", test_add_one))

    # Test 2: Add multiple items, check total
    def test_add_multiple():
        cart = ShoppingCart()
        cart.add_item("apple", 1.20)
        cart.add_item("banana", 0.80)
        cart.add_item("milk", 2.25)
        assert cart.total_cost() == 1.20 + 0.80 + 2.25, "Total mismatch after multiple adds"

    cases.append(("Add multiple items, check total", test_add_multiple))

    # Test 3: Remove an item, check total
    def test_remove_one():
        cart = ShoppingCart()
        cart.add_item("apple", 1.20)
        cart.add_item("banana", 0.80)
        cart.remove_item("apple")
        assert cart.total_cost() == 0.80, "Total mismatch after removing apple"

    cases.append(("Remove item, check total", test_remove_one))

    # Test 4: Remove non-existent item
    def test_remove_nonexistent():
        cart = ShoppingCart()
        cart.add_item("apple", 1.20)
        cart.remove_item("orange")  # Should do nothing
        assert cart.total_cost() == 1.20, "Total should stay the same after removing nonexistent"

    cases.append(("Remove non-existent item", test_remove_nonexistent))

    # Test 5: Add, remove, then add again
    def test_add_remove_add():
        cart = ShoppingCart()
        cart.add_item("apple", 1.20)
        cart.remove_item("apple")
        cart.add_item("apple", 2.00)
        assert cart.total_cost() == 2.00, "Item should update to new price"

    cases.append(("Add, remove, add again", test_add_remove_add))

    # Test 6: Remove all, total should be zero
    def test_remove_all():
        cart = ShoppingCart()
        cart.add_item("apple", 1.20)
        cart.add_item("banana", 0.80)
        cart.remove_item("apple")
        cart.remove_item("banana")
        assert cart.total_cost() == 0.0, "Total should be 0 after removing all"

    cases.append(("Remove all items, total zero", test_remove_all))

    # Test 7: Add duplicate items (should overwrite)
    def test_duplicate_add():
        cart = ShoppingCart()
        cart.add_item("apple", 1.00)
        cart.add_item("apple", 2.00)  # update price
        assert cart.total_cost() == 2.00, "Duplicate add should update price"

    cases.append(("Add duplicate item (update price)", test_duplicate_add))

    # Test 8: Empty cart
    def test_empty_cart():
        cart = ShoppingCart()
        assert cart.total_cost() == 0.0, "Empty cart should have total 0"

    cases.append(("Empty cart", test_empty_cart))

    return cases


def run_shopping_cart_tests():
    test_cases = generate_shopping_cart_test_cases()
    passed = 0
    for i, (desc, test_fn) in enumerate(test_cases):
        try:
            test_fn()
            print(f"Test {i+1}: {desc:35} - PASS")
            passed += 1
        except AssertionError as e:
            print(f"Test {i+1}: {desc:35} - FAIL ({e})")
        except Exception as e:
            print(f"Test {i+1}: {desc:35} - ERROR ({e})")
    print(f"Passed {passed}/{len(test_cases)} ShoppingCart tests.")


if __name__ == "__main__":
    run_shopping_cart_tests()
