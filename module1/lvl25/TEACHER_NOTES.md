# Рівень 25 — нотатки до пари

Друга частина Git. Формат: слайди + живе демо в **Git Bash**, домашнього завдання немає.
Презентація: `Git_lvl25.pdf` (31 слайд).

---

## Хронометраж

### Якщо 120 хвилин

| Слайди | Блок | Хв |
|---|---|---|
| 1–2 | Вступ, план | 3 |
| 3–6 | `.gitignore`: навіщо, синтаксис, шаблони, `git rm --cached` | 12 |
| 7 | **Практика 1** — порядок у репозиторії | 8 |
| 8–15 | Доступи: чому не пароль, SSH, `ssh-agent`, remote, PAT | 18 |
| 16 | **Практика 2** — доступ з нуля (SSH + токен) | 20 |
| 17 | **Перерва** | 10 |
| 18–22 | Три зони, `amend`, `reset`, `revert`, `stash` | 16 |
| 23 | **Практика 3** — ламаємо і чинимо | 12 |
| 24–28 | GitHub Flow, PR, code review, CI, `ci.yml` | 15 |
| 29 | **Практика 4** — повний цикл на живому проєкті | 20 |
| 30–31 | Підсумок | 3 |

### Якщо 90 хвилин — що ріжемо

- Перерва 5 хв замість 10.
- Блок `amend/reset/revert/stash` → 10 хв, **Практику 3 прибираємо повністю**
  (три режими `reset` показуємо прямо на слайді 20, без термінала).
- Слайд 22 (`stash`) — проклацати, згадати одним реченням.
- Практику 4 скорочуємо: CI-червоний не показуємо, PR одразу зі зеленим CI.

**Що не можна різати:** доступи (обіцяно на минулій лекції) і `git rm --cached`.

---

## Підготовка ДО пари

### 1. Зробити термінал «чистим» для демо доступів

Це найважливіше і найризикованіше. Робити **заздалегідь**, не наживо.

```bash
# 1. Прибрати SSH-ключі (оборотно — просто перейменовуємо теку)
mv ~/.ssh ~/.ssh.backup

# 2. Очистити ssh-agent, якщо він запущений
ssh-add -D 2>/dev/null

# 3. Прибрати збережений токен GitHub з Windows Credential Manager
cmdkey /list | grep -i github          # подивитись, що там є
cmdkey /delete:git:https://github.com  # видалити

# 4. Якщо стоїть GitHub CLI
gh auth logout 2>/dev/null

# 5. ПЕРЕВІРКА — має бути відмова
ssh -T git@github.com
# Очікуємо: git@github.com: Permission denied (publickey).
```

Ще перевірити:
- **PyCharm** → `Settings → Version Control → GitHub` — прибрати прив'язаний акаунт,
  інакше IDE тихо зробить push за тебе і демо втратить сенс.
- Якщо у Credential Manager кілька записів GitHub — видалити всі
  (Панель керування → Диспетчер облікових даних → Облікові дані Windows).

### Повернути все назад ПІСЛЯ пари

```bash
rm -rf ~/.ssh              # ключі, згенеровані на демо
mv ~/.ssh.backup ~/.ssh    # повертаємо свої
ssh -T git@github.com      # перевірка: Hi b7sj3o!
```

> Поки ключі перейменовані, **push у робочі репозиторії не працюватиме**. Тому
> чистимо середовище за 10–15 хвилин до пари, а не за день.

### 2. Що відкрити заздалегідь

- `Git_lvl25.pdf` — на весь екран.
- Git Bash, збільшений шрифт (правий клік по заголовку → Options → Text → Size 16–18).
- Браузер: вкладка з GitHub (залогінений в акаунт), вкладка `github.com/settings/keys`.
- PyCharm з відкритою текою `demo-project`.
- Цей файл і `LIVE_SNIPPETS.md` — на другому моніторі.

### 3. Про демо-репозиторій для CI

Код лежить у `demo-project/`. На GitHub його заливаємо **окремим новим репозиторієм**
(як `test_lvl24` минулого разу) — не в `javarush-lessons-2`, бо GitHub Actions читає
workflow тільки з кореня репозиторію.

Заздалегідь створювати не треба — робимо наживо, це частина демо. Але **план Б**:
якщо Actions не стартує або мережа гальмує, показати вже готовий PR
у будь-якому публічному репозиторії з CI.

---

## Практика 1 — порядок у репозиторії (8 хв)

Мета: студент бачить, як `.env` потрапляє в git, і як його звідти прибрати.

```bash
mkdir lvl25-demo && cd lvl25-demo
git init
python -m venv venv                       # створюємо «сміття»
echo "API_TOKEN=super-secret-123" > .env   # і «секрет»
echo "print('hello')" > main.py

git status
# ↑ показуємо: Git хоче забрати venv/ (сотні файлів!) і .env

git add .
git commit -m "initial commit"
git log --stat | head -20
# ↑ .env уже в історії — саме та помилка, про яку говоримо
```

Тепер рятуємо:

```bash
# .gitignore пишемо ПІСЛЯ факту — типова ситуація
cat > .gitignore <<'EOF'
venv/
__pycache__/
.env
.idea/
EOF

git status
# ↑ .env усе одно у змінах! Бо Git його вже відстежує — ось воно, головне непорозуміння

git rm --cached .env
git status                       # тепер deleted + .gitignore
git commit -m "chore: stop tracking .env"

# але секрет усе ще в історії:
git log -p --all | grep -i "super-secret"
```

**Що промовити:** `git rm --cached` рятує майбутнє, не минуле. Реальний фікс —
відкликати токен і випустити новий. Слайд 6 саме про це.

---

## Практика 2 — доступи з нуля (20 хв)

### SSH (основна частина)

```bash
# Показуємо, що ми «ніхто»
ssh -T git@github.com
# Permission denied (publickey).

ls ~/.ssh
# No such file or directory

# 1. Генеруємо
ssh-keygen -t ed25519 -C "твоя@пошта"
#   → Enter (шлях за замовчуванням)
#   → passphrase: на демо залишити ПОРОЖНІМ, щоб не витрачати час на ssh-agent
#     (і одразу проговорити, що на робочій машині так робити не варто)

ls -la ~/.ssh
# id_ed25519 (приватний) + id_ed25519.pub (публічний)

# 2. Показуємо різницю — це найважливіший момент блоку
cat ~/.ssh/id_ed25519.pub    # можна показувати на екрані
head -2 ~/.ssh/id_ed25519    # ← а ось це НЕ показуємо, тільки перші рядки
                             #   щоб було видно "OPENSSH PRIVATE KEY"

# 3. Копіюємо публічний
cat ~/.ssh/id_ed25519.pub | clip
```

→ Браузер: `github.com/settings/keys` → **New SSH key** → Title «Демо на парі» →
вставляємо → Add.

```bash
# 4. Перевіряємо
ssh -T git@github.com
#   Are you sure you want to continue connecting? → yes
#   Hi b7sj3o! You've successfully authenticated...
```

### Push по SSH

```bash
cd lvl25-demo                          # проєкт з практики 1
git remote -v                          # порожньо
git remote add origin git@github.com:b7sj3o/lvl25-demo.git
git push -u origin main
# ↑ ЖОДНОГО пароля — ось заради чого все це було
```

> Репозиторій `lvl25-demo` на GitHub створити перед цим (New repository, публічний,
> **без** README/gitignore/license — щоб не було конфлікту при першому push).

### PAT (коротко, 5 хв)

Не генерувати новий ключ, а показати:

1. `github.com/settings/personal-access-tokens` → **Generate new token** (fine-grained).
2. Repository access → **Only select repositories** → `lvl25-demo`.
3. Permissions → **Contents: Read and write** (Metadata: Read-only ставиться саме).
4. Expiration — 30 днів. Generate.
5. Показати екран «токен видно один раз» — і **не показувати сам токен на весь екран**
   (або одразу після демо натиснути Revoke).

```bash
# Перемикаємо remote назад на HTTPS, щоб показати, куди вводиться токен
git remote set-url origin https://github.com/b7sj3o/lvl25-demo.git
git push
#   Username: b7sj3o
#   Password: <вставляємо токен>

# І назад на SSH
git remote set-url origin git@github.com:b7sj3o/lvl25-demo.git
```

**Якщо часу мало** — PAT показати тільки в браузері (створення + скоупи), push по
токену пропустити.

---

## Практика 3 — ламаємо і чинимо (12 хв)

```bash
# --- amend ---
echo "print('feature A')" > feature.py
git add feature.py
git commit -m "add featur A"          # з помилкою в тексті
git commit --amend -m "feat: add feature A"
git log --oneline                      # хеш змінився!

# --- reset --soft ---
echo "print('B')" > b.py && git add b.py && git commit -m "temp"
git reset --soft HEAD~1
git status                             # зміни в staging, коміта немає

# --- reset --mixed (за замовчуванням) ---
git commit -m "temp2"
git reset HEAD~1
git status                             # зміни є, але не в staging

# --- reset --hard: НАЙВАЖЛИВІШЕ ---
git add . && git commit -m "temp3"
git reset --hard HEAD~1
ls                                     # b.py зник фізично

# --- reflog: рятуємо ---
git reflog                             # шукаємо temp3
git reset --hard HEAD@{1}
ls                                     # повернувся

# --- revert ---
git log --oneline
git revert <хеш>                       # відкриється редактор → :wq у Vim
git log --oneline                      # старий коміт на місці + новий Revert
```

**Обов'язково промовити:** `reset` — поки коміти тільки в тебе. Запушив — `revert`.

---

## Практика 4 — повний цикл (20 хв)

Готові шматки коду для копіювання — у `LIVE_SNIPPETS.md`.

```bash
cd demo-project           # з цієї теки
git init
git add .
git commit -m "feat: expense tracker with tests and CI"
git branch -M main
git remote add origin git@github.com:b7sj3o/expenses-demo.git
git push -u origin main
```

→ На GitHub: вкладка **Actions** — workflow вже запустився сам. Дочекатись зеленого.

```bash
# Гілка під нову фічу
git switch -c feature/median

# ↓ вставити код з LIVE_SNIPPETS.md, крок 1 (функція median + невикористаний import)
# ↓ і крок 2 (тест, який упаде)

git add .
git commit -m "feat: add median()"
git push -u origin feature/median
```

→ GitHub сам запропонує **Compare & pull request**. Створюємо PR:
- перевірити напрямок: `base: main ← compare: feature/median`
- опис за шаблоном зі слайда 25
- **Checks — червоні.** Відкрити лог, показати, що саме сказав `ruff` і що впало в `pytest`

```bash
# ↓ фікс з LIVE_SNIPPETS.md, крок 3
git add . && git commit -m "fix: handle empty list in median()"
git push
```

→ CI перезапускається сам, стає зеленим.
→ **Code review:** у вкладці *Files changed* лишити коментар до рядка,
  показати **Request changes**, потім **Approve**.
→ **Squash and merge** → **Delete branch**.

```bash
git switch main
git pull
git log --oneline        # один коміт замість двох — ось що зробив squash
```

**Фінальний акорд:** відкрити на GitHub список файлів гілки — `venv/` і `.env` там немає.
Тому що `.gitignore` написали на початку заняття.

---

## Типові збої і що робити

| Що сталося | Швидкий фікс |
|---|---|
| `ssh -T` висить | Корпоративна/мобільна мережа ріже порт 22. Це якраз привід перейти на PAT — не боротись, а показати альтернативу наживо |
| При `git commit` відкрився Vim | `:wq` + Enter. Або одразу `git commit -m "..."` |
| `error: failed to push some refs` | На GitHub створили репозиторій з README. `git pull --rebase origin main`, потім push |
| Actions не стартує | Перевірити, що файл саме `.github/workflows/ci.yml` у **корені** репозиторію |
| Actions у черзі довше хвилини | Не чекати мовчки — перейти до code review, повернутись до CI пізніше |
| PyCharm сам робить push | Акаунт лишився прив'язаним у Settings → Version Control → GitHub |
| `ssh-add` каже «Could not open a connection» | Агент не запущений: `eval "$(ssh-agent -s)"` |

---

## Що прозвучало на минулій лекції і чого не варто повторювати

`init`, `add`, `commit`, `status`, `log`, `checkout`/`switch`, `branch`, `merge`,
конфлікти (і в терміналі, і в PyCharm), `remote add`, `push -u`, `git diff`,
створення репозиторію на GitHub, GitHub Pages, Fork.

Про `.gitignore` і три режими `reset` було сказано «детальніше наступного разу» —
саме це і закриваємо.
