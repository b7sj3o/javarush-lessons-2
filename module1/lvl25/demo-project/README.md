# expenses — демо-проєкт до рівня 25

Маленький трекер витрат. Сам код тут не головне — він потрібен, щоб на живому
прикладі пройти повний робочий цикл: **гілка → Pull Request → CI → code review → merge**.

## Запуск

```bash
python -m venv venv
source venv/Scripts/activate      # Git Bash на Windows
pip install -r requirements.txt

python expenses.py                # подивитись, що воно рахує
```

## Перевірки — ті самі, що ганяє CI

```bash
ruff check .        # лінтер: стиль, невикористані імпорти, порядок імпортів
pytest -q           # тести
```

Якщо обидві команди зелені локально — зеленим буде і CI.

## Що всередині

| Файл | Навіщо |
|---|---|
| `expenses.py` | Чотири функції: `total`, `by_category`, `average`, `top_category` |
| `tests/test_expenses.py` | 7 тестів, включно з граничними випадками (порожній список) |
| `.github/workflows/ci.yml` | GitHub Actions: ставить залежності, ганяє `ruff` і `pytest` |
| `.gitignore` | `venv/`, `__pycache__/`, `.idea/`, `.env` — усе, що не має потрапити в репозиторій |
| `.env.example` | Шаблон для секретів. Реальний `.env` у git не потрапляє |
| `pyproject.toml` | Налаштування `ruff` і `pytest` |

## Секрети

```bash
cp .env.example .env    # і заповнити своїми значеннями
```

`.env` є в `.gitignore`, тому в репозиторій він не піде. У git комітимо **тільки**
`.env.example` — щоб інші знали, які змінні потрібні, але не бачили значень.
