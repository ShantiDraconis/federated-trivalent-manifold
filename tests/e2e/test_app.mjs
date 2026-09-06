import { chromium } from "playwright";

const launchOptions = { headless: true };
if (process.env.BROWSER_EXECUTABLE) launchOptions.executablePath = process.env.BROWSER_EXECUTABLE;
const browser = await chromium.launch(launchOptions);
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const errors = [];
page.on("console", (message) => {
  if (message.type() === "error") errors.push(message.text());
});
page.on("pageerror", (error) => errors.push(error.message));

await page.goto("http://127.0.0.1:8765/", { waitUntil: "networkidle" });
await page.waitForSelector(".problem-button");
if (await page.locator(".problem-button").count() !== 7) throw new Error("Expected seven problem buttons");
const orbitBoxes = await page.locator(".orbit-node").evaluateAll((nodes) => nodes.map((node) => {
  const box = node.getBoundingClientRect(); return [Math.round(box.x), Math.round(box.y), node.getAttribute("style")];
}));
if (new Set(orbitBoxes.map((box) => box.slice(0,2).join(","))).size !== 7) throw new Error(`Orbit nodes overlap: ${JSON.stringify(orbitBoxes)}`);
if (await page.locator(".lemma-node").count() < 8) throw new Error("Riemann lemma tree did not render");
await page.locator('.problem-button[data-id="navier-stokes"]').click();
if (!(await page.locator("#problemHeader").textContent()).includes("Navier-Stokes")) throw new Error("Problem selection failed");
await page.locator("#delta").fill("0.2");
if (!(await page.locator("#diagnostic").textContent()).includes("contrafactual")) throw new Error("Lab diagnostic failed");
await page.locator("#themeToggle").click();
if (!(await page.locator("body").getAttribute("class") || "").includes("light")) throw new Error("Theme toggle failed");
await page.screenshot({ path: process.env.APP_SCREENSHOT || "app-preview.png", fullPage: true });
if (errors.length) throw new Error(`Console errors: ${errors.join(" | ")}`);
console.log(JSON.stringify({ title: await page.title(), problems: 7, orbitPositions: orbitBoxes, errors: 0 }));
await browser.close();
