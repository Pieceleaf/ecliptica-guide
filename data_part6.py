# -*- coding: utf-8 -*-
# Ecliptica 数据 Part 6: 属性上限 / 状态效果 / 符文 / 神器 / 版本日志

STATS = [
 {"id":"maxhp","zh":"最大生命","en":"Max Health","desc":"各职业基础不同；低于 20%（低血量）屏幕变暗、回血声音变小。","soft":None,"hard":None},
 {"id":"regen","zh":"自然回复","en":"Health Regeneration","desc":"基础每 2 秒回 1 HP；受伤延迟 5 秒（受自然回复影响）。","soft":None,"hard":None},
 {"id":"attackspeed","zh":"攻击速度","en":"Attack Speed","desc":"影响主手与多数副手技能频率；攻速越高状态异常触发率略降但总触发更多。","soft":250,"hard":400,"unit":"%"},
 {"id":"projectilespeed","zh":"弹道速度","en":"Projectile Speed","desc":"影响弹道型技能与升级弹；不影响 hit-scan（VA-11 爆能炮）。","soft":250,"hard":400,"unit":"%"},
 {"id":"movespeed","zh":"移动速度","en":"Movement Speed","desc":"基础 7m/s；同时提升部分位移技能距离；Haste 可突破上限。","soft":150,"hard":200,"unit":"%"},
 {"id":"jumpheight","zh":"跳跃高度","en":"Jump Height","desc":"基础 1 米；提升 Spellhammer 跳砸等技能强度。","soft":None,"hard":None},
 {"id":"healingrecv","zh":"受疗","en":"Healing Received","desc":"影响所有来源的治疗（不含自然回复）。","soft":None,"hard":200,"unit":"%"},
 {"id":"critchance","zh":"暴击率","en":"Critical Strike Chance","desc":"暴击时按暴伤倍率结算。","soft":40,"hard":60,"unit":"%"},
 {"id":"critdmg","zh":"暴击伤害","en":"Critical Strike Damage","desc":"暴击倍率。","soft":None,"hard":385,"unit":"%"},
 {"id":"utilitycd","zh":"辅助技能冷却速率","en":"Utility Cooldown Rate","desc":"影响位移/辅助技能 CD 恢复速度。","soft":200,"hard":300,"unit":"%"},
 {"id":"defense","zh":"总防御","en":"Overall Defense","desc":"全伤害类型减免，与元素防御乘算；Tank Buster（紫攻击）无视。","soft":200,"hard":None,"unit":"%"},
 {"id":"elemdefense","zh":"元素防御","en":"Elemental Defense","desc":"对应元素伤害减免，与总防御乘算；紫攻击无视。","soft":200,"hard":None,"unit":"%"},
 {"id":"damage","zh":"总伤害","en":"Overall Damage","desc":"所有技能与升级伤害倍率。","soft":None,"hard":None},
 {"id":"knockbackres","zh":"击退抗性","en":"Knockback Resistance","desc":"按比例减少被击退距离。","soft":None,"hard":None},
]

STATUS_EFFECTS = [
 {"en":"BURNING","zh":"灼烧","zh2":"火属性持续伤害"},
 {"en":"BLEEDING","zh":"出血","zh2":"物理持续伤害"},
 {"en":"FROZEN / FREEZING","zh":"冰冻","zh2":"冰属性控制/减速"},
 {"en":"PARALYZED","zh":"麻痹","zh2":"电属性控制"},
 {"en":"POISONED","zh":"中毒","zh2":"毒持续伤害"},
 {"en":"BREACHED","zh":"破甲","zh2":"暗属性，防御降低"},
 {"en":"WEAKENED","zh":"虚弱","zh2":"圣光施加，减伤"},
 {"en":"FRENZIED","zh":"狂乱","zh2":"攻速/移速提升"},
 {"en":"HASTE","zh":"急速","zh2":"移速大幅提升"},
 {"en":"EMPOWERED","zh":"强力","zh2":"伤害提升"},
 {"en":"GUARDED","zh":"守护","zh2":"减伤"},
 {"en":"ENFORCED","zh":"坚守","zh2":"防御提升"},
 {"en":"RESTORATION","zh":"恢复","zh2":"治疗/护盾"},
 {"en":"INVINCIBLE","zh":"无敌","zh2":"免疫伤害"},
 {"en":"STOP / GO","zh":"停/行","zh2":"交通法规切换状态"},
 {"en":"HEAVY","zh":"沉重","zh2":"减速"},
 {"en":"MORTAL CURSE","zh":"致命诅咒","zh2":"倒地后复活附加；召唤 boss 时移除一次"},
 {"en":"WEAKENED","zh":"虚弱","zh2":"减伤"},
]

RUNES = [
 {"zh":"巨大欲望","en":"Massive Greed","desc":"基础 20%→15%（v0.51），每层 +5%"},
 {"zh":"巨大贪婪","en":"Massive Gluttony","desc":"基础 20%→15%（v0.51），每层 +15%"},
 {"zh":"起爆符","en":"Detonation Tag","desc":"可与力量互叠（B站核爆锤玩法：白嫖符文叠至少 6 个力量）"},
 {"zh":"加速","en":"Haste Rune","desc":"移速类符文"},
 {"zh":"力量","en":"Strength Rune","desc":"增伤类符文"},
]
# 注：符文系统为通关后/局外解锁，日文 wiki 提供等效 token 分析（腾讯文档表），站内暂列已知条目。

ARTIFACTS = [
 {"zh":"神器（Artifacts）","en":"Artifacts","desc":"每局准备阶段需收集并献给中央祭坛的神器；影响当局 buff/机制。详见英文 wiki Artifacts 页。"},
]

CHANGELOG = [
 {"version":"v0.51","date":"2026-07-29","title":"Ecliptica Demo Playtest Changelog",
  "items":[
   {"cls":"Spellsword","zh":"剑术家","items":[
     "熟练：主手命中 2.5% 概率叠狂乱（最大 5 层）",
     "破盾者：念力斩额外 +25% 伤害",
     "奥义：新增自然回复 -100% 代价；出血回血 1→2",
     "熟练：穿刺打击射程 5m→4m",
   ]},
   {"cls":"Twinmage","zh":"双法师","items":[
     "圣光球基础伤害 50→35",
   ]},
   {"cls":"Gunmancer","zh":"枪术士","items":[
     "光子凝聚器熟练：蓄力附加弹数 +1→+2",
   ]},
   {"cls":"Fistmage","zh":"拳法师","items":[
     "激昂：加速最大 10 层起，每升级 +2",
     "跑者：叠乘倍率下调",
   ]},
   {"cls":"Shield Mage","zh":"盾法师","items":[
     "盾冲 CD 恢复 4 秒",
     "守望者：辅助 CD 惩罚 100%→50%",
     "守望者恢复不再干扰拳法师格挡",
   ]},
   {"cls":"Spellhammer","zh":"法锤士","items":[
     "投掷熟练：新增附加爆炸伤害（0.5m 起，每层 +0.5m）",
     "主手锤击 110→90",
     "投掷主宰：强力最大 5 层，每升级 +2",
     "主手挥击移速仅受移速影响（不再受攻速）",
     "投掷熟练伤害加成调整",
     "爆散空中可充能（更慢），着地恢复",
   ]},
   {"cls":"Thaumaturge","zh":"咒术师","items":[
     "毒面相受疗 -15%→-5%",
     "兴奋剂：守护有上限；自我 buff 最大 3 层",
     "（静默）兴奋剂：痛苦交换 CD +15%",
     "熟练：痛苦交换 CD 缩短 15%→10%",
     "自我治疗时 CD 恢复慢 75%",
     "分裂射击扩散修正 +2.5%",
   ]},
   {"cls":"Nekomancer","zh":"猫术士","items":[
     "僵尸猫初始 5% 概率破甲",
     "僵尸猫暗伤 15→25",
     "魂爆半径基础 +2m，每层 +1.5m",
     "图腾猫 HP 调整；回血变慢；不再叠加（同时只吃 1 个图腾奶）",
   ]},
   {"cls":"Stage","zh":"关卡","items":[
     "Boss 战开传送门时全队回满血",
   ]},
   {"cls":"Runes","zh":"符文","items":[
     "巨大欲望基础 20%→15%（每层 +5%）",
     "巨大贪婪基础 20%→15%（每层 +15%）",
   ]},
   {"cls":"Upgrades","zh":"升级","items":[
     "单排：背水一战（Clutch or Kick）与献祭羔羊不再出现在商店",
     "第三定律：拳法师格挡也触发（反弹固定 50%）；新增范围光环显示",
     "狂战士之魂拆分为近战/远程两版",
     "狂战士之魂（近战）代价由移速改为自然回复 -50%",
     "狂战士之魂（远程）代价由移速改为弹道扩散 +2%",
   ]},
  ]},
]
