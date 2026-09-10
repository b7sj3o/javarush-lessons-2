# Готові шматки коду для практики 4

Копіювати під час пари, не набирати руками. Усе перевірено — падає й лагодиться саме так,
як описано.

---

## Крок 1 — «зламана» фіча у гілці `feature/median`

### 1.1 У `expenses.py` — додати імпорт зверху

Рядок `from collections import defaultdict` замінити на:

```python
import statistics
from collections import defaultdict
```

> `statistics` ніде не використовується — це і зловить `ruff` (правило F401).

### 1.2 У `expenses.py` — додати функцію перед `if __name__ == "__main__":`

```python
def median(expenses: list[Expense]) -> float:
    """Return the median expense amount."""
    amounts = sorted(item["amount"] for item in expenses)
    middle = len(amounts) // 2
    if len(amounts) % 2:
        return amounts[middle]
    return (amounts[middle - 1] + amounts[middle]) / 2
```

> Порожній список тут не оброблений — саме це впіймає тест.

---

## Крок 2 — тести

### 2.1 У `tests/test_expenses.py` — виправити рядок імпорту

```python
from expenses import average, by_category, median, top_category, total
```

### 2.2 Додати в кінець файлу

```python
def test_median(sample):
    assert median(sample) == 240.0


def test_median_empty():
    assert median([]) == 0.0
```

---

## Що буде в PR (перевірено)

**`ruff check .` — червоний:**

```
expenses.py:7:8: F401 [*] `statistics` imported but unused
Found 1 error.
```

**`pytest -q` — червоний:**

```
>       return (amounts[middle - 1] + amounts[middle]) / 2
E       IndexError: list index out of range

FAILED tests/test_expenses.py::test_median_empty - IndexError: list index out of range
1 failed, 8 passed
```

> На демо варто показати саме лог в Actions: два кроки, обидва впали, і видно точний рядок.

---

## Крок 3 — фікс

### 3.1 Прибрати перший рядок імпорту

```python
from collections import defaultdict
```

### 3.2 Додати перевірку на початок `median()`

```python
def median(expenses: list[Expense]) -> float:
    """Return the median expense amount, or 0.0 for an empty list."""
    if not expenses:
        return 0.0
    amounts = sorted(item["amount"] for item in expenses)
    ...
```

Після цього: `All checks passed!` + `9 passed`.

---

## Коментар для code review

Щоб не вигадувати наживо — у *Files changed* до рядка `if not expenses:` лишити:

> А що поверне `median()` для порожнього списку? У `average()` вище ми вже
> повертаємо `0.0` — зробимо однаково, щоб поведінка була передбачувана.

Далі: **Request changes** → показати, що PR заблокований → потім **Approve**.

---

## Опис PR (вставити в тіло)

```markdown
## Що зроблено
Додав `median()` — рахує медіанну витрату.

## Як перевірити
1. `pytest -q`
2. `python expenses.py`

## Пов'язані задачі
Fixes #1
```

> Щоб `Fixes #1` спрацював, перед PR створити Issue («Додати медіану») — заодно
> буде привід показати вкладку Issues і те, як merge автоматично її закриває.
