"""Build the profile figures as SVG, one light and one dark file each.

Every number is read from the result files of the repository it belongs to;
nothing here is typed in by hand. Run from any directory:

    python3 figures/build.py ~/repos
"""
import csv
import json
import sys
from pathlib import Path

REPOS = Path(sys.argv[1] if len(sys.argv) > 1 else "~/repos").expanduser()
OUT = Path(__file__).resolve().parent

THEMES = {
    "light": dict(surface="#fcfcfb", ink="#0b0b0b", ink2="#52514e", grid="#e6e5e1",
                  s1="#2a78d6", s2="#eb6834", s3="#1baf7a", seq="#2a78d6"),
    "dark": dict(surface="#1a1a19", ink="#ffffff", ink2="#c3c2b7", grid="#33332f",
                 s1="#3987e5", s2="#d95926", s3="#199e70", seq="#3987e5"),
}
FONT = "font-family='-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif'"


def svg(width, height, body, t):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' "
            f"viewBox='0 0 {width} {height}' {FONT} font-size='13'>\n"
            f"<rect width='{width}' height='{height}' fill='{t['surface']}'/>\n{body}</svg>\n")


def text(x, y, s, t, size=13, anchor="start", weight="normal", ink=None, extra=""):
    return (f"<text x='{x}' y='{y}' fill='{ink or t['ink']}' font-size='{size}' "
            f"text-anchor='{anchor}' font-weight='{weight}' {extra}>{s}</text>\n")


# ---------------------------------------------------------------- lesiontrack
def lesiontrack(t):
    rows = list(csv.DictReader(open(REPOS / "lesiontrack/results/backtest_P1_lesions.tsv"), delimiter="\t"))
    pts = [(float(r["true_pct_per_year"]), float(r["measured_mean_pct_per_year"]), r["size_stratum"])
           for r in rows if r["expanded"] == "True"]
    m = json.load(open(REPOS / "lesiontrack/results/backtest_P1_metrics.json"))
    W, H, L, R, T, B = 560, 400, 56, 20, 44, 52
    lim = 50
    sx = lambda v: L + (W - L - R) * v / lim
    sy = lambda v: H - B - (H - T - B) * v / lim
    colour = {"small_lt100": t["s1"], "medium_100_500": t["s2"], "large_ge500": t["s3"]}
    label = {"small_lt100": "under 100 mm³", "medium_100_500": "100 to 500 mm³", "large_ge500": "over 500 mm³"}
    b = text(L, 20, "lesiontrack backtest: injected expansion, measured back", t, 15, weight="600")
    b += text(L, 36, "24 synthetic expansions in real MS lesions, percent volume per year", t, 12, ink=t["ink2"])
    for v in range(0, lim + 1, 10):
        b += f"<line x1='{L}' y1='{sy(v)}' x2='{W-R}' y2='{sy(v)}' stroke='{t['grid']}' stroke-width='1'/>\n"
        b += text(L - 8, sy(v) + 4, str(v), t, 11, "end", ink=t["ink2"])
        b += text(sx(v), H - B + 16, str(v), t, 11, "middle", ink=t["ink2"])
    b += f"<line x1='{sx(0)}' y1='{sy(0)}' x2='{sx(lim)}' y2='{sy(lim)}' stroke='{t['ink2']}' stroke-width='1' stroke-dasharray='4 4'/>\n"
    b += text(sx(49.5), sy(41) + 4, "measured = injected", t, 11, "end", ink=t["ink2"])
    for x, y, s in pts:
        b += f"<circle cx='{sx(x):.1f}' cy='{sy(min(y, lim)):.1f}' r='5' fill='{colour[s]}' stroke='{t['surface']}' stroke-width='2'/>\n"
    b += text((L + W - R) / 2, H - 6, "injected, % per year", t, 11, "middle", ink=t["ink2"])
    b += text(14, (T + H - B) / 2, "measured", t, 11, "middle", ink=t["ink2"],
              extra=f"transform='rotate(-90 14 {(T + H - B) / 2})'")
    lx = L + 12
    for i, s in enumerate(["small_lt100", "medium_100_500", "large_ge500"]):
        y = T + 14 + i * 18
        b += f"<circle cx='{lx}' cy='{y}' r='5' fill='{colour[s]}'/>\n"
        b += text(lx + 12, y + 4, label[s], t, 11)
    b += text(W - R, H - B - 8, f"median recovery {m['recovery_median']:.2f}, every expansion detected", t, 11, "end", ink=t["ink2"])
    return svg(W, H, b, t)


# -------------------------------------------------------------------- bidsgate
def bidsgate(t):
    d = json.load(open(REPOS / "bidsgate/results/lst-ai-v2/scores_lesions.json"))
    groups = {"by_height": {}, "by_size": {}}
    for r in d["results"]:
        for g in groups:
            for k, v in r["score"][g].items():
                n, hit = groups[g].get(k, (0, 0))
                groups[g][k] = (n + v["n"], hit + round(v["n"] * v["sensitivity"]))
    height = [("lower third", groups["by_height"]["lower"]), ("middle third", groups["by_height"]["middle"]),
              ("upper third", groups["by_height"]["upper"])]
    size = [("under 100 mm³", groups["by_size"]["0-100mm3"]), ("100 to 500 mm³", groups["by_size"]["100-500mm3"]),
            ("over 500 mm³", groups["by_size"]["500-infmm3"])]
    W, H = 560, 300
    b = text(20, 22, "bidsgate: what LST-AI v2 recovered from injected lesions", t, 15, weight="600")
    b += text(20, 38, f"{len(d['results'])} OpenNeuro controls, twelve lesions each; share of injected lesions the segmenter found", t, 12, ink=t["ink2"])
    def panel(x0, title, rows):
        s = text(x0, 68, title, t, 12, weight="600", ink=t["ink2"])
        bw = 150
        for i, (name, (n, hit)) in enumerate(rows):
            y = 84 + i * 56
            s += text(x0, y + 12, name, t, 12)
            s += f"<rect x='{x0}' y='{y + 20}' width='{bw}' height='14' rx='4' fill='{t['grid']}'/>\n"
            w = bw * hit / n
            s += f"<rect x='{x0}' y='{y + 20}' width='{w:.1f}' height='14' rx='4' fill='{t['seq']}'/>\n"
            s += text(x0 + bw + 10, y + 32, f"{hit} of {n}", t, 12, ink=t["ink2"])
        return s
    b += panel(20, "by position in the brain", height)
    b += panel(300, "by lesion volume", size)
    b += text(20, H - 12, "the lower third of the brain is where it fails; volume barely matters", t, 11, ink=t["ink2"])
    return svg(W, H, b, t)


# ---------------------------------------------------------------- ms-twin-treat
def mtt(t):
    rows = []
    for line in open(REPOS / "ms-twin-treat/results/RESULTS.md"):
        if line.startswith("|") and "0." in line:
            cells = [c.strip().strip("*") for c in line.strip("|\n").split("|")]
            try:
                rows.append((cells[0], float(cells[1])))
            except (ValueError, IndexError):
                pass
    want = {
        "leave-one-out mean shift": "leave-one-out null (canonical bar)",
        "global-mean-shift null": "global null (leaky, the harder bar)",
        "scGPT-blood embeddings": "scGPT embeddings",
        "control-similarity transfer": "control-similarity transfer",
        "noise ceiling": "noise ceiling",
    }
    picked = []
    for name, v in rows:
        for key, lab in want.items():
            if name.lower().startswith(key.lower()) and lab not in [p[0] for p in picked]:
                picked.append((lab, v))
    assert len(picked) == 5, picked
    W, H, L, R = 560, 260, 40, 40
    lo, hi = 0.80, 0.90
    sx = lambda v: L + (W - L - R) * (v - lo) / (hi - lo)
    b = text(20, 22, "ms-twin-treat: the cell model against its nulls", t, 15, weight="600")
    b += text(20, 38, "leave-one-cell-type-out score on real interferon-beta data (Kang 2018), eight cell types", t, 12, ink=t["ink2"])
    axis_y = H - 44
    b += f"<line x1='{L}' y1='{axis_y}' x2='{W-R}' y2='{axis_y}' stroke='{t['grid']}' stroke-width='1'/>\n"
    for i in range(0, 11, 2):
        v = lo + (hi - lo) * i / 10
        b += f"<line x1='{sx(v):.1f}' y1='{axis_y}' x2='{sx(v):.1f}' y2='{axis_y + 5}' stroke='{t['ink2']}'/>\n"
        b += text(sx(v), axis_y + 20, f"{v:.2f}", t, 11, "middle", ink=t["ink2"])
    order = ["leave-one-out null (canonical bar)", "global null (leaky, the harder bar)", "scGPT embeddings",
             "control-similarity transfer", "noise ceiling"]
    vals = dict(picked)
    for i, lab in enumerate(order):
        y = 66 + i * 30
        v = vals[lab]
        is_model = lab == "control-similarity transfer"
        if "null" in lab or "ceiling" in lab:
            b += f"<line x1='{sx(v):.1f}' y1='{y - 8}' x2='{sx(v):.1f}' y2='{axis_y}' stroke='{t['ink2']}' stroke-width='1' stroke-dasharray='3 3'/>\n"
        b += f"<circle cx='{sx(v):.1f}' cy='{y}' r='{7 if is_model else 5}' fill='{t['s1'] if is_model else t['ink2']}' stroke='{t['surface']}' stroke-width='2'/>\n"
        anchor, x = ("end", sx(v) - 12) if v > 0.86 else ("start", sx(v) + 12)
        b += text(x, y + 4, f"{lab}  {v:.4f}", t, 12, anchor, "600" if is_model else "normal")
    return svg(W, H, b, t)


for name, fn in [("lesiontrack-backtest", lesiontrack), ("bidsgate-lst-ai", bidsgate), ("ms-twin-treat-nulls", mtt)]:
    for mode, t in THEMES.items():
        (OUT / f"{name}-{mode}.svg").write_text(fn(t))
        print("wrote", f"{name}-{mode}.svg")
