#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""为所有页面注入移动端底部导航（app 式 tab bar）"""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

# 页面 -> 对应 tab 的 data-key
TABS = [
    ("index.html", "home"), ("classes.html", "classes"), ("upgrades.html", "upgrades"),
    ("builds.html", "builds"), ("simulator.html", "simulator"),
    ("stats.html", "stats"), ("changelog.html", "changelog"),
]

NAV_ITEMS = [
    ("home", "🏠", "首页"), ("classes", "⚔️", "职业"), ("upgrades", "📖", "图鉴"),
    ("builds", "🛠️", "Build"), ("simulator", "🎯", "模拟器"),
    ("stats", "📊", "属性"), ("changelog", "📜", "日志"),
]

def nav_html(active_key):
    items = "".join(
        f'<a href="{page}" class="{"active" if key == active_key else ""}" data-key="{key}">'
        f'<span class="bn-ico">{ico}</span>{label}</a>'
        for key, ico, label in NAV_ITEMS
        for page, page_key in [("index.html" if key == "home" else f"{key}.html", key)]
        if key == page_key
    )
    return f'\n<nav class="bottom-nav">{items}</nav>\n'

# 注意上面推导式写复杂了，重新用简单方式
def nav_html2(active_key):
    page_map = {"home": "index.html"}
    items = ""
    for key, ico, label in NAV_ITEMS:
        page = page_map.get(key, key + ".html")
        items += (f'<a href="{page}" class="{"active" if key == active_key else ""}">'
                  f'<span class="bn-ico">{ico}</span>{label}</a>')
    return f'\n<nav class="bottom-nav">{items}</nav>\n'

for fname, key in TABS:
    path = os.path.join(BASE, fname)
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if "bottom-nav" in html:
        print(f"{fname}: already has bottom-nav, skip")
        continue
    if "</main>" not in html:
        print(f"{fname}: no </main>, skip")
        continue
    html = html.replace("</main>", "</main>" + nav_html2(key), 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{fname}: injected ({key})")
print("DONE")
