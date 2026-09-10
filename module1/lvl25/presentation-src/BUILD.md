# Як перегенерувати `Git_lvl25.pdf`

Презентація зверстана на HTML/CSS і друкується в PDF через headless Chrome.
Слайд = `<section class="slide">` розміром рівно 960×540 pt — так само, як у файлі
першої частини.

## Збірка

```bash
"/c/Program Files/Google/Chrome/Application/chrome.exe" \
  --headless=new --disable-gpu --no-sandbox --allow-file-access-from-files \
  --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf="C:/шлях/до/Git_lvl25.pdf" \
  "file:///C:/шлях/до/slides.html"
```

Шрифти (`Montserrat`, `JetBrains Mono`) тягнуться з Google Fonts, тому для збірки
потрібен інтернет.

## Тема

Кольори й типографіка зняті з PDF першої частини:

| Роль | Значення |
|---|---|
| Заголовки | Montserrat ExtraBold 36pt, `#172b53` |
| Основний текст | Montserrat Medium 16pt, `#172b53` |
| Акцент | `#6550f8` |
| Титульний / фінальний слайд | `#9373f5` |
| Темні слайди й роздільники | `#121215` |
| Код у терміналі | тема Darcula з PyCharm (`#2b2b2b` фон) |

Логотипи в `img/` вирізані з оригінального PDF у 600 dpi.

## Класи, з яких складаються слайди

- `.slide` — світлий (за замовчуванням), `.slide--dark`, `.slide--sec` (роздільник
  «Практика»), `.slide--title` (титульний)
- `.term` — блок термінала; підсвітка через `<span class="c|p|s|kw|o">`
  (коментар / промпт / рядок / прапорець / вивід)
- `.note` (+ `.warn`, `.danger`, `.ok`) — виноски
- `table.t`, `.cards`/`.card`, `.flow`/`.step`, `.zones`/`.zone`, `.two` (дві колонки)

## Якщо контент перестав вміщатися

Тимчасово вставити перед `</body>` цей скрипт і відкрити файл у браузері —
`document.body.dataset.of` покаже, які слайди переповнені і на скільки пунктів:

```html
<script>
window.addEventListener('load', () => {
  const bad = [];
  document.querySelectorAll('.slide').forEach((sl, i) => {
    const sb = sl.getBoundingClientRect();
    let maxB = 0;
    sl.querySelectorAll('.body *').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.height && r.bottom > maxB) maxB = r.bottom;
    });
    const ov = Math.round(maxB - sb.bottom);
    if (ov > -10) bad.push(`${i + 1}(${ov})`);
  });
  document.body.setAttribute('data-of', bad.join(' ') || 'CLEAN');
});
</script>
```
