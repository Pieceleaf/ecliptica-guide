# Ecliptica 日蚀攻略站（VRChat 多人肉鸽）

基于社区调研（英 wiki Miraheze / 日 wiki wikiwiki.jp / B站社区 / X）整理的 Ecliptica 攻略站。
**当前版本：v0.51（2026-07-29）**

## 页面

| 页面 | 内容 |
|---|---|
| `index.html` | 首页：游戏简介、操作键位、每关流程、难度体系、商店概览、版本情报 |
| `classes.html` | 8 职业一览（ATTACK/HEAVY/SUPPORT）+ 职业技能与职业专属升级详情 |
| `upgrades.html` | 升级图鉴：**技能 ↔ 点位双向查询**（3 个商店筛选、稀有度、职业、关键词），中/英/日三语 |
| `builds.html` | **最终毕业加点（真实攻略）**：13 套方案全部来自网上攻略——中文图鉴站 36 点构筑（8 职业）、日文 wiki build 页（书奶/盾法师）、B站玩家实测（书奶进阶流 A_Soulsoul 视频+JohnUmane7/JO丁评论、枪手双枪流 JO丁、法锤抛锤核爆流 落羽松_Taxod），来源逐一标注 |
| `simulator.html` | **加点模拟器**：搜索技能 → 点「＋」加点（同技能可叠多层，中英双语）→ 实时给出该技能在该流派下的绝对优先级排名（进度联动：已达标降权/软上限提示/互斥/Build 缺口）；「一键填充」按攻略构筑 36 点全量填充。**手机端**：搜索改按钮展开式弹窗、点击技能先看详情再在弹窗内加减点、优先级三商店选项卡切换 |
| `stats.html` | 属性软/硬上限表 + 溢出点数使用思路 |
| `changelog.html` | v0.51 版本日志（全职业平衡改动）+ 对 Build 的影响解读 |

## 使用

```bash
cd site
python -m http.server 8765
# 打开 http://localhost:8765
```

纯静态站，无任何依赖，也可直接双击 index.html 打开（模拟器/图鉴为本地 JS，均可用）。

## 数据维护

- 数据全部在 `data.js`（由 `data_part*.py` 分片生成，运行 `python build_data.py` 重新生成）。
- 数据分片：
  - `data_part1.py` 忍耐之晶（生存商店 24 技能）
  - `data_part2.py` 机动之晶（18 技能）
  - `data_part3.py` 时空法师（20 技能）
  - `data_part4a/b.py` 8 职业专属升级（54 技能）
  - `data_part5.py` 职业定义
  - `data_part6.py` 属性/状态/符文/版本日志
  - `data_part7a.py` / `data_part7b.py` 10 套真实攻略 Build（来源：中文图鉴站 Ecliptica Codex v0.51 36 点构筑 + 日文 wiki build 页；must 每项带具体层数）
- 技能字段：`id/en/jp/zh/rarity/desc/descZh/stack/tags/base/notes`；`base` 为优先级基准分（0-100），`tags` 用于软上限联动，`notes` 为社区备注（互斥、实测数值等）。
- 版本更新时：更新 `data_part6.py` 的 CHANGELOG + 调整 `data_part7a/b.py` 的 Build，重新生成即可。

## 优先级计算逻辑（simulator.html）

```
score = base（社区共识基准分）
      + Build 修正（must +18 / nice +4 / avoid 压到 ≤22）
      + 进度修正（已点 ≥ 目标层数 → -45 并标"已达标"；未点必须项 +18）
      + 软上限近似降权（按 tags 累计层数超估算阈值 → -18 + 提示）
      + 互斥排除（-60）
```

⚠ 优先级模型与软上限估算为攻略站整理（非官方数值），Build 来源见各页标注。

## 调研原始材料

`../research/`：
- `wiki/` Miraheze 全站 61 页 wikitext + 结构化 JSON
- `jp_wiki/` wikiwiki.jp 22 页（更新日志/流程/职业/build）
- `bili/` 14 个 B站视频元数据+评论（+教程视频 ASR 转写）
- `yt_*.txt` YouTube MFMC 系列字幕

## 主要社区结论（2026-07 ~ 08，v0.51）

- 光法（Twinmage 圣光手）当前最强输出；攻速拉到 200% 即可
- 书奶（Thaumaturge）v0.51 削弱明显，建议双书奶互保
- 核爆锤（Spellhammer 投掷流）成型伤害上限约 1550
- 推荐队伍：1 盾法师 + 2 书奶 + 1 猫奶 + 输出
