# -*- coding: utf-8 -*-
# Ecliptica 数据 Part 8a: 符文 / 符文诅咒 / 神器 完整数据（来自英文 wiki Runes/Artifacts 页）
# 符文：局外装备（Penumbral/Antumbral 槽位，demo 只能装 2 个，每个激活附赠随机诅咒×层数）
# phase 值：每阶段（Penumbral→Antumbral→Eclipse）效果增长

RUNES_FULL = [
 {"id":"r_focus","zh":"专注成长","en":"Focus Growth","effect":"暴击率 +10%（每阶段 +10%）","stat":{"critchance":10},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_cleaning","zh":"净化成长","en":"Cleaning Growth","effect":"获得对负面状态的小幅抗性（每阶段提升）","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_recovery","zh":"恢复成长","en":"Recovery Growth","effect":"辅助技能冷却速率 -15%（每阶段 -15%）","stat":{"utilitycd":-15},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_power","zh":"力量成长","en":"Power Growth","effect":"总伤害 +10%（每阶段 +10%）","stat":{"damage":10},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_dexterity","zh":"灵巧成长","en":"Dexterity Growth","effect":"攻击速度 +30%（每阶段 +30%）","stat":{"attackspeed":30},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_precision","zh":"精准成长","en":"Precision Growth","effect":"暴击伤害 +15%（每阶段 +15%）","stat":{"critdmg":15},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_health","zh":"生命成长","en":"Health Growth","effect":"最大生命 +15（每阶段 +15）","stat":{"maxhp":15},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_satieity","zh":"饱食成长","en":"Satieity Growth","effect":"受疗 +10%（每阶段 +10%）","stat":{"healingrecv":10},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_defense","zh":"防御成长","en":"Defense Growth","effect":"总防御 +5%（每阶段 +5%）","stat":{"defense":5},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_rejuvenating","zh":"再生成长","en":"Rejuvenating Growth","effect":"自然回复 +150%（每阶段 +150%）","stat":{"regen":150},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_skybound","zh":"天空之跃","en":"Skybound","effect":"额外跳跃 +1（每阶段 +1）","stat":{"jumpheight":0},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_turtle","zh":"龟之道","en":"Way of the Turtle","effect":"最大生命 +20、总防御 +10%、移动速度 -20%（每阶段 +10 HP / +10% 防 / -20% 速）","stat":{"maxhp":20,"defense":10,"movespeed":-20},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_activeguard","zh":"主动守护","en":"Active Guard","effect":"使用辅助技能有 5% 概率获得坚守（RESILIENCE）状态（每阶段 +2%）","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_manicgambit","zh":"疯狂赌局","en":"Manic Gambit","effect":"献祭的神器获得其 300% 属性（每阶段 +100%）；每阶段 Token 获取 -1","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_greedy","zh":"贪婪","en":"Big and Greedy","effect":"发现额外 Token 概率 +15%（每阶段 +15%）","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_needy","zh":"需求","en":"Big and Needy","effect":"购买普通升级后返还 Token 概率 +15%（每阶段 +5%）","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_picky","zh":"挑剔","en":"Big and Picky","effect":"升级选择时额外 +1 选项；重掷次数 +1（每阶段 +1 重掷）","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
 {"id":"r_insured","zh":"保险","en":"Big and Insured","effect":"开局获得 1 Token（Antumbral+ 阶段每阶段 +1）；重掷次数 +1","stat":{},"curse":"随机 1 种符文诅咒 ×1"},
]

# 符文诅咒（Runic Curses，14 种，激活符文时随机获得，可重复叠层）
CURSES_FULL = [
 {"id":"c_fragility","zh":"脆弱","en":"Fragility","effect":"物理防御 -9%/层"},
 {"id":"c_smolder","zh":"阴燃","en":"Smolder","effect":"火元素防御 -9%/层"},
 {"id":"c_fever","zh":"高热","en":"Fever","effect":"冰元素防御 -9%/层"},
 {"id":"c_conductor","zh":"导体","en":"Conductor","effect":"电元素防御 -9%/层"},
 {"id":"c_profane","zh":"亵渎","en":"Profane","effect":"圣光防御 -9%/层"},
 {"id":"c_divine","zh":"神圣","en":"Divine","effect":"暗影防御 -9%/层"},
 {"id":"c_rot","zh":"腐败","en":"Rot","effect":"毒元素防御 -9%/层"},
 {"id":"c_tremor","zh":"震颤","en":"Tremor","effect":"弹道散布 +2.5%/层"},
 {"id":"c_drain","zh":"汲取","en":"Drain","effect":"最大生命 -10/层"},
 {"id":"c_shedding","zh":"蜕皮","en":"Shedding","effect":"总防御 -5%/层"},
 {"id":"c_anaemia","zh":"贫血","en":"Anaemia","effect":"自然回复 -150%/层"},
 {"id":"c_hypoxia","zh":"缺氧","en":"Hypoxia","effect":"受疗 -10%/层"},
 {"id":"c_light","zh":"轻盈","en":"Light","effect":"受到击退 +15%/层"},
 {"id":"c_asthma","zh":"哮喘","en":"Asthma","effect":"辅助冷却速率 +15%/层"},
]

# 神器（Artifacts，7 种，局内收集献给祭坛，全员加成；★为 wiki 推荐度）
ARTIFACTS_FULL = [
 {"id":"a_archive","zh":"加密档案","en":"Encrypted Archive","effect":"辅助冷却速率 -5%、移动速度 +5%","star":3,"stat":{"utilitycd":-5,"movespeed":5}},
 {"id":"a_sun","zh":"太阳圣杯","en":"Goblet of the Sun","effect":"圣光伤害 +8%、暗影防御 +8%","star":1,"stat":{"damage":0}},
 {"id":"a_armor","zh":"HC 装甲板","en":"HC Armor Plating","effect":"物理防御 +7%（最终 Boss 为 Jim C. Bringer，物防几乎必定有用）","star":2,"stat":{"defense":7}},
 {"id":"a_cinders","zh":"余烬之心","en":"Heart of Cinders","effect":"元素防御 +6%（后期 Boss 高元素伤害）","star":2,"stat":{"elemdefense":6}},
 {"id":"a_malice","zh":"恶意精华","en":"Essence of Malice","effect":"暗影伤害 +6%、圣光防御 +6%","star":2,"stat":{"damage":0}},
 {"id":"a_wheel","zh":"轮回之轮","en":"Wheel of Reincarnation","effect":"受疗 +3%、最大生命 +5","star":3,"stat":{"healingrecv":3,"maxhp":5}},
 {"id":"a_megium","zh":"封印宝石","en":"Sealed Megium","effect":"总伤害 +3%（无视职业，几乎总是好选择）","star":3,"stat":{"damage":3}},
]
