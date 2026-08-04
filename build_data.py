# -*- coding: utf-8 -*-
"""聚合所有数据分片 -> data.js (网站数据层)"""
import json, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_part1 import SHOP_PERS
from data_part2 import SHOP_MOB
from data_part3 import SHOP_CHRONO
from data_part4a import CLASS_UP_SS, CLASS_UP_TM, CLASS_UP_GM, CLASS_UP_FM
from data_part4b import CLASS_UP_SH, CLASS_UP_SM, CLASS_UP_TH, CLASS_UP_NK
from data_part5 import CLASSES
from data_part6 import STATS, STATUS_EFFECTS, RUNES, ARTIFACTS, CHANGELOG
from data_part7a import BUILDS_A
from data_part7b import BUILDS_B
BUILDS = BUILDS_A + BUILDS_B

from data_part8a import RUNES_FULL, CURSES_FULL, ARTIFACTS_FULL
from data_part8b import STAT_EFFECTS
from data_part9 import VRCT_BUILDS
from data_part10 import BOSSES, ENEMIES, BOSS_ENEMIES

# 技能图标（英文名 -> 图标文件 URL，来自 wiki 表格）
ICONS_BY_EN = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research", "wiki", "icons.json"), encoding="utf-8"))
# wiki 表格技能名与展示英文名的别名
ICON_ALIASES = {"Gunmancer: Overcharged (VA-11 Blast Cannon)": "Gunmancer: Overcharged"}
def icon_for(en):
    return ICONS_BY_EN.get(en) or ICONS_BY_EN.get(ICON_ALIASES.get(en, ""), "")

# 商店（点位）定义
SHOPS = [
 {"id":"perseverance","en":"Crystal of Perseverance","zh":"忍耐之晶","jp":"忍耐のクリスタル","theme":"生存：最大HP/防御/回复","skills":SHOP_PERS},
 {"id":"mobility","en":"Crystal of Mobility","zh":"机动之晶","jp":"モビリティのクリスタル","theme":"机动：移速/攻速/辅助CD","skills":SHOP_MOB},
 {"id":"chrono","en":"Chrono Wizard","zh":"时空法师","jp":"クロノウィザード","theme":"特殊：伤害/暴击/元素/类专","skills":SHOP_CHRONO},
]

# 职业 -> 专属升级映射
CLASS_UPGRADES = {
 "spellsword": CLASS_UP_SS, "twinmage": CLASS_UP_TM, "gunmancer": CLASS_UP_GM,
 "fistmage": CLASS_UP_FM, "spellhammer": CLASS_UP_SH, "shieldmage": CLASS_UP_SM,
 "thaumaturge": CLASS_UP_TH, "nekomancer": CLASS_UP_NK,
}

DATA = {
 "meta": {
   "name": "Ecliptica 日蚀攻略站",
   "version": "v0.51 (2026-07-29)",
   "world": "wrld_0fb88df3-2057-4c2f-8e06-e948864378fd",
   "author": "Mantibro (SlashCo VR team)",
   "updated": "2026-08-03",
   "sources": [
     "https://ecliptica.miraheze.org/ (英wiki)",
     "https://wikiwiki.jp/ecliptica/ (日wiki)",
     "B站社区视频/评论",
     "https://ecliptica.0862233.xyz/ (中文图鉴站)",
     "X @ruralistvevo / @mantibro",
   ],
 },
 "shops": SHOPS,
 "classes": CLASSES,
 "class_upgrades": CLASS_UPGRADES,
 "builds": BUILDS,
 "icons": {sk["id"]: "icons/" + sk["id"] + ".png" for s in SHOPS for sk in s["skills"]} | {sk["id"]: "icons/" + sk["id"] + ".png" for ups in CLASS_UPGRADES.values() for sk in ups},
 "stats": STATS,
 "status_effects": STATUS_EFFECTS,
 "runes": RUNES_FULL,
 "curses": CURSES_FULL,
 "artifacts": ARTIFACTS_FULL,
 "stat_effects": STAT_EFFECTS,
 "vrct_builds": VRCT_BUILDS,
 "bosses": BOSSES,
 "enemies": ENEMIES,
 "boss_enemies": BOSS_ENEMIES,
 "changelog": CHANGELOG,
 "difficulties": [
   {"en":"Primal","zh":"原始"},
   {"en":"Penumbra","zh":"半影"},
   {"en":"Antumbra","zh":"环影"},
   {"en":"Umbra","zh":"本影"},
   {"en":"Eclipse","zh":"日蚀"},
   {"en":"Eye of the Eclipse","zh":"日蚀之眼"},
 ],
 "flow": [
   "选择职业 → 大厅高台全员集合开始 Run",
   "战斗阶段：清理小怪（提示收集 3 个 Token，位置随机）",
   "准备阶段：收集神器献祭给中央祭坛（此阶段获得加速状态，趁机捡 Token）",
   "Boss 阶段：击杀 Boss（v0.51 起开门时全队满血）",
   "休憩阶段（世界狭间）：用 Token 购买升级（3 个商店 + 1 次免费重随）；可花 95% Token 在日蚀处换职业（每 3 轮 1 次）",
 ],
 "game_mechanics": [
   "难度：Primal→Penumbra→Antumbra→Umbra→Eclipse→Eye of the Eclipse；随进度解锁，决定小怪/Boss 池",
   "Token（蓝水晶）：局内拾取（每局固定 3 个，扣除符文增减）；未用完可存留",
   "进度平衡：加入别人房间时会按进度补发 Token",
   "升级购买后商店自动刷新，可重复购买同一技能",
   "单排时：背水一战（Clutch or Kick）与献祭羔羊（Sacrificial Lamb）不会出现",
   "Flaming Spirit 与 Frozen Heart 互斥（二者只能取其一）",
   "倒地（0 HP）：可被队友以 50% 最大生命复活（健康守护可降至 25%）；复活获得致命诅咒（召唤 Boss 时移除一次）",
 ],
}

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.js"), "w", encoding="utf-8") as f:
    f.write("// Ecliptica 日蚀攻略站 数据层 (v0.51, 2026-08-03)\n")
    f.write("// 自动生成自 data_part*.py 数据分片，请勿手改。\n")
    f.write("const ECLIPTICA_DATA = ")
    json.dump(DATA, f, ensure_ascii=False, indent=1)
    f.write(";\n")

# 统计
n_skills = sum(len(s["skills"]) for s in SHOPS)
n_class_up = sum(len(v) for v in CLASS_UPGRADES.values())
print(f"shops: {len(SHOPS)} ({n_skills} skills)")
print(f"classes: {len(CLASSES)}")
print(f"class upgrades: {n_class_up}")
print(f"builds: {len(BUILDS)}")
print(f"stats: {len(STATS)}, status: {len(STATUS_EFFECTS)}, changelog entries: {sum(len(v['items']) for v in CHANGELOG)}")
print("OK -> data.js")
