"""Tiny expense tracker used as the live demo project for level 25.

Deliberately small: the point of the lesson is the workflow around the code
(branch -> PR -> CI -> review -> merge), not the code itself.
"""

from collections import defaultdict

# Every expense is a dict: {"title": str, "amount": float, "category": str}
Expense = dict


def total(expenses: list[Expense]) -> float:
    """Return the sum of all expense amounts."""
    return sum(item["amount"] for item in expenses)


def by_category(expenses: list[Expense]) -> dict[str, float]:
    """Group expenses by category and sum the amounts in each one."""
    grouped: dict[str, float] = defaultdict(float)
    for item in expenses:
        grouped[item["category"]] += item["amount"]
    return dict(grouped)


def average(expenses: list[Expense]) -> float:
    """Return the average expense amount, or 0.0 for an empty list."""
    if not expenses:
        return 0.0
    return total(expenses) / len(expenses)


def top_category(expenses: list[Expense]) -> str | None:
    """Return the category with the largest total, or None if there is nothing."""
    grouped = by_category(expenses)
    if not grouped:
        return None
    return max(grouped, key=grouped.get)


if __name__ == "__main__":
    demo = [
        {"title": "Coffee", "amount": 85.0, "category": "food"},
        {"title": "Transit pass", "amount": 500.0, "category": "transport"},
        {"title": "Lunch", "amount": 240.0, "category": "food"},
    ]
    print(f"Total:         {total(demo):.2f} UAH")
    print(f"Average:       {average(demo):.2f} UAH")
    print(f"Top category:  {top_category(demo)}")
    print(f"By category:   {by_category(demo)}")
