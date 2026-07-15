from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from gateway_model.model import Measurements, Parameters, action, beta_critical, decay, mass_proxy


OUT = ROOT / "outputs"


def _font(size: int, bold: bool = False):
    path = Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf")
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()


def _chart(path: Path, title: str, xlabel: str, ylabel: str, series, vertical=None, point=None):
    w, h = 1440, 864
    margin = (130, 80, 70, 120)
    left, top, right, bottom = margin[0], margin[1], w-margin[2], h-margin[3]
    xs = [x for _, data, _ in series for x, _ in data]
    ys = [y for _, data, _ in series for _, y in data]
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    pad = (ymax-ymin) * .08 or 1
    ymin, ymax = ymin-pad, ymax+pad
    sx = lambda x: left + (x-xmin)/(xmax-xmin)*(right-left)
    sy = lambda y: bottom - (y-ymin)/(ymax-ymin)*(bottom-top)
    im = Image.new("RGB", (w,h), "white"); d = ImageDraw.Draw(im)
    for i in range(6):
        yy = top + i*(bottom-top)/5
        d.line((left,yy,right,yy), fill="#d9e1e7", width=1)
        val = ymax-i*(ymax-ymin)/5
        d.text((left-18,yy), f"{val:.2f}", font=_font(24), fill="#46535e", anchor="rm")
    d.line((left,top,left,bottom), fill="#26343f", width=2); d.line((left,bottom,right,bottom), fill="#26343f", width=2)
    if ymin <= 0 <= ymax: d.line((left,sy(0),right,sy(0)), fill="#26343f", width=2)
    colorset = ["#285f91", "#d97706", "#25855a", "#8e4a9b"]
    for idx, (name, data, color) in enumerate(series):
        pts = [(sx(x),sy(y)) for x,y in data]
        d.line(pts, fill=color or colorset[idx], width=5)
        d.line((right-330, top+idx*38+18, right-280, top+idx*38+18), fill=color or colorset[idx], width=5)
        d.text((right-265, top+idx*38+18), name, font=_font(24), fill="#26343f", anchor="lm")
    if vertical is not None:
        xx=sx(vertical); d.line((xx,top,xx,bottom), fill="#c36b0a", width=3)
    if point is not None:
        x,y=point; xx,yy=sx(x),sy(y); d.ellipse((xx-9,yy-9,xx+9,yy+9), fill="#b91c1c")
    d.text((w/2,34), title, font=_font(34,True), fill="#16324f", anchor="mm")
    d.text((w/2,h-50), xlabel, font=_font(27), fill="#26343f", anchor="mm")
    d.text((38,h/2), ylabel, font=_font(27), fill="#26343f", anchor="mm")
    im.save(path)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    m, p = Measurements(), Parameters()
    bcrit = beta_critical(p.alpha, m.total, p.e_norm)
    result = {
        "scope": "gateway model parameters; not Millennium Problem constants",
        "measurements_seconds": {**m.__dict__, "total": m.total},
        "parameters": p.__dict__,
        "derived": {
            "action": action(p.alpha, p.beta, m.total, p.e_norm),
            "beta_critical": bcrit,
            "mass_proxy": mass_proxy(p.beta, p.e_norm),
            "example_alpha_0_1_beta_5": action(0.1, 5.0, m.total, 0.3),
        },
    }
    (OUT / "constantes.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    betas = [15*i/499 for i in range(500)]
    values = [action(p.alpha, b, m.total, p.e_norm) for b in betas]
    _chart(OUT/"action_regimes.png", "Gateway action and the actual critical point", "beta", "S_eff",
           [("S = alpha t^2 - beta e^2", list(zip(betas,values)), "#285f91")], vertical=bcrit,
           point=(p.beta,result["derived"]["action"]))

    times = [20*i/299 for i in range(300)]
    curves = [(f"lambda = {lam}", [(x,decay(p.e_norm,lam,x)) for x in times], color)
              for lam,color in zip((0.1,0.2,0.5),("#285f91","#d97706","#25855a"))]
    _chart(OUT/"exodus_decay.png", "Exponential decay of the exodus variable", "time", "e(t)", curves)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
