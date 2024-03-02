import unittest
from budget import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget("TestUser", 100)

    def test_add_transaction(self):
        self.budget.add_transaction(50, 'Income')
        self.assertEqual(self.budget.get_balance(), 150,
                         "Balance should be 150 after adding 50.")

    def test_categorize_transaction(self):
        self.budget.add_transaction(-20, "Groceries")
        self.assertIn((-20, 'Groceries'), self.budget.transactions,
                      "Transaction should be in transactions list.")
        self.assertEqual(
            self.budget.category_totals["Groceries"], -20, "Category total for Groceries should be -20.")


if __name__ == "__main__":
    unittest.main()
