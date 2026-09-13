#!/usr/bin/env python3
"""Regenerate the profile record between the RECORD markers in README.md.

Two rules this script exists to enforce:

  1. No counts. Not totals, not per-repo multipliers, not "N across M projects".
     The work is the claim; badge-shaped numbers are not.
  2. Authoritative enumeration only. `gh search prs` is a lagging index that
     omits states you did not ask for. This walks user.pullRequests and
     reconciles the page count against totalCount, failing loudly on mismatch.

Hand-written blurbs in .github/data/record.json are never overwritten. A newly
merged PR is appended using its PR title as a placeholder so it is visible and
obviously unpolished; rewrite it in record.json at leisure.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / ".github" / "data" / "record.json"
README = ROOT / "README.md"
M_START, M_END = "<!-- RECORD:START -->", "<!-- RECORD:END -->"
I_START, I_END = "<!-- INREVIEW:START -->", "<!-- INREVIEW:END -->"

QUERY = """query($endCursor:String){
  user(login:"CedricConday"){
    pullRequests(first:100, after:$endCursor, states:[%s]){
      totalCount
      pageInfo{hasNextPage endCursor}
      nodes{number title repository{nameWithOwner}}
    }}}"""


def fetch(state):
    """Walk every page; reconcile against totalCount before returning."""
    nodes, cursor, total = [], None, None
    while True:
        cmd = ["gh", "api", "graphql", "-f", "query=" + QUERY % state]
        if cursor:
            cmd += ["-F", f"endCursor={cursor}"]
        data = json.loads(subprocess.run(cmd, capture_output=True, text=True,
                                         check=True).stdout)
        page = data["data"]["user"]["pullRequests"]
        total = page["totalCount"]
        nodes += page["nodes"]
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    if len(nodes) != total:
        sys.exit(f"{state}: enumerated {len(nodes)} but totalCount is {total}")
    return nodes


def render_merged(rec, prs):
    by_repo = {}
    for p in prs:
        by_repo.setdefault(p["repository"]["nameWithOwner"], []).append(p)

    placed = {r for b in rec["buckets"] for r in b["repos"]}
    for repo in by_repo:
        if repo not in placed:
            for b in rec["buckets"]:
                if b["name"] == rec["default_bucket"]:
                    b["repos"].append(repo)

    out, new = [], []
    for b in rec["buckets"]:
        repos = [r for r in b["repos"] if r in by_repo]
        if not repos:
            continue
        out.append(f"**{b['name']}**")
        for repo in repos:
            name = rec["display"].get(repo, repo)
            dom = rec["domains"].get(repo, "")
            items = []
            for p in sorted(by_repo[repo], key=lambda x: x["number"]):
                key = f"{repo}#{p['number']}"
                if key not in rec["blurbs"]:
                    rec["blurbs"][key] = p["title"]
                    new.append(key)
                url = f"https://github.com/{repo}/pull/{p['number']}"
                # Blurb rides along as the link title, so it is available on
                # hover without putting a paragraph on the page.
                tip = rec["blurbs"][key].replace('"', "'")
                items.append(f"[#{p['number']}]({url} \"{tip}\")")
            label = f"[{name}](https://github.com/{repo})"
            if dom:
                label += f" — {dom}"
            note = rec.get("notes", {}).get(repo)
            if note:
                label += f" · {note}"
            out.append(f"- {label} · " + " ".join(items))
        out.append("")
    return "\n".join(out).rstrip(), new


def render_inreview(rec, prs):
    by_repo = {}
    for p in prs:
        by_repo.setdefault(p["repository"]["nameWithOwner"], []).append(p)
    parts = []
    for repo in sorted(by_repo, key=lambda r: (-len(by_repo[r]), r)):
        short = rec["display"].get(repo, repo.split("/")[-1])
        parts.append(f"[{short}](https://github.com/{repo}/pulls/CedricConday)")
    return "Open, under review: " + ", ".join(parts) + "."


def splice(page, start, end, block):
    if start not in page or end not in page:
        sys.exit(f"README.md is missing {start} / {end}")
    return re.sub(re.escape(start) + r".*?" + re.escape(end),
                  lambda _: f"{start}\n{block}\n{end}", page, flags=re.S)


def main():
    rec = json.loads(DATA.read_text(encoding="utf-8"))
    merged, inreview = fetch("MERGED"), fetch("OPEN")
    block, new = render_merged(rec, merged)
    page = README.read_text(encoding="utf-8")
    page = splice(page, M_START, M_END, block)
    page = splice(page, I_START, I_END, render_inreview(rec, inreview))
    README.write_text(page, encoding="utf-8")
    DATA.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    print(f"record rebuilt: {len(merged)} merged, {len(inreview)} open")
    for k in new:
        print(f"  NEW (placeholder blurb, rewrite in record.json): {k}")


if __name__ == "__main__":
    main()
