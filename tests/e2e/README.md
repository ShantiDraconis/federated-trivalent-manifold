# Teste end-to-end

O teste usa Playwright contra um servidor HTTP local da pasta `app/`.

```bash
python -m http.server 8765 --directory app
npm install --save-dev playwright
npx playwright install chromium
node tests/e2e/test_app.mjs
```

Em sistemas com navegador já instalado, defina `BROWSER_EXECUTABLE`.
