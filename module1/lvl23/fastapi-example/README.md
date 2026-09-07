# Level 23 — асинхронні ітератори у FastAPI

Три «сервіси», кожен по 1 секунді (`asyncio.sleep`). Обидва ендпоінти
споживають результат однаково — через `async for`. Різниця лише в тому,
коли стартують корутини.

- `one_by_one()` — `await fetch(...)` всередині циклу: наступний запит
  починається після завершення попереднього → **~3 s**
- `all_at_once()` — спочатку `create_task()` для всіх, потім `await` →
  **~1 s**

Тобто `async for` сам по собі паралелізму не дає. Паралелізм з'являється,
коли корутини запущені *до* того, як ти почав їх чекати.

## Запуск

```bash
source ../.venv/Scripts/activate     # Git Bash
uvicorn main:app --reload
```

```bash
curl -s localhost:8000/sequential    # {"elapsed":3.0, ...}
curl -s localhost:8000/parallel      # {"elapsed":1.0, ...}
```
