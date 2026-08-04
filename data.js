// Ecliptica 日蚀攻略站 数据层 (v0.51, 2026-08-03)
// 自动生成自 data_part*.py 数据分片，请勿手改。
const ECLIPTICA_DATA = {
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
   "X @ruralistvevo / @mantibro"
  ]
 },
 "shops": [
  {
   "id": "perseverance",
   "en": "Crystal of Perseverance",
   "zh": "忍耐之晶",
   "jp": "忍耐のクリスタル",
   "theme": "生存：最大HP/防御/回复",
   "skills": [
    {
     "id": "fluffy",
     "en": "Fluffy",
     "jp": "ふわふわ",
     "zh": "毛茸茸",
     "rarity": "Common",
     "desc": "Max HP: +10 (+10 per stack)",
     "descZh": "最大生命 +10（每层+10）",
     "stack": "Linear",
     "tags": [
      "hp"
     ],
     "base": 70,
     "notes": "最通用的生存向堆叠技能；后期 HP 溢出时可适量补。坦位（Fistmage/Shield Mage）核心堆叠项。"
    },
    {
     "id": "gluttonous",
     "en": "Gluttonous",
     "jp": "大食漢",
     "zh": "大胃王",
     "rarity": "Common",
     "desc": "Received Healing +5% (+5% per stack)",
     "descZh": "受到治疗 +5%（每层+5%）",
     "stack": "Linear",
     "tags": [
      "healing"
     ],
     "base": 55,
     "notes": "受疗加成（含奶妈给的奶），自身自然回血不受影响；对依赖治疗的坦/输出都有价值。"
    },
    {
     "id": "sacrificial_lamb",
     "en": "Sacrificial Lamb",
     "jp": "生贄の羊",
     "zh": "献祭羔羊",
     "rarity": "Common",
     "desc": "Upon dying, heal every other party member by 15 HP (+15 HP per stack)",
     "descZh": "死亡时治疗其他队友 15 HP（每层+15）",
     "stack": "Linear",
     "tags": [
      "healing"
     ],
     "base": 20,
     "notes": "单排（solo）不会出现；仅死亡收益，常规局价值低，除非有自爆/送死流。"
    },
    {
     "id": "swarm_enforcer",
     "en": "Swarm Enforcer",
     "jp": "群れの用心棒",
     "zh": "群聚保镖",
     "rarity": "Common",
     "desc": "Gain +1.5% Defense for each enemy within 32 meters of you (+1.5% per stack)",
     "descZh": "32 米内每名敌人提供 +1.5% 防御（每层+1.5%）",
     "stack": "Linear",
     "tags": [
      "defense"
     ],
     "base": 45,
     "notes": "小怪波次收益极高，boss 战仅 1 个目标时收益低；清怪快的队伍收益有限。"
    },
    {
     "id": "vitality",
     "en": "Vitality",
     "jp": "活力",
     "zh": "活力",
     "rarity": "Common",
     "desc": "Health Regeneration: +80% (+80% per stack)",
     "descZh": "自然回复 +80%（每层+80%）",
     "stack": "Linear",
     "tags": [
      "regen"
     ],
     "base": 65,
     "notes": "自然回血是全体通用恢复手段；对坦与持续战斗职业价值最高，配合 Big and Lazy 效果翻倍。"
    },
    {
     "id": "vital_drain",
     "en": "Vital Drain",
     "jp": "バイタルドレイン",
     "zh": "生命虹吸",
     "rarity": "Common",
     "desc": "Critical strikes recover 2 HP (+2 HP per stack)",
     "descZh": "暴击回复 2 HP（每层+2）",
     "stack": "Linear",
     "tags": [
      "lifesteal",
      "crit"
     ],
     "base": 50,
     "notes": "不吃受疗加成；高频攻击/暴击流职业收益高，法系与枪手价值高。"
    },
    {
     "id": "adrenaline_fiend",
     "en": "Adrenaline Fiend",
     "jp": "アドレナリン中毒者",
     "zh": "肾上腺素成瘾",
     "rarity": "Rare",
     "desc": "Using your Utility skill recovers 6 (+6 per stack) HP; Utility Cooldown Rate +7% (+7% per stack); Received Healing -15% (-15% per stack)",
     "descZh": "使用位移/辅助技能回 6 HP（每层+6）；辅助技能 CD 速率 +7%（每层+7%）；受疗 -15%（每层-15%）",
     "stack": "Linear",
     "tags": [
      "healing",
      "utility"
     ],
     "base": 40,
     "notes": "需要频繁使用 Utility 的职业收益高；受疗 -15% 会稀释 Gluttonous，注意平衡。"
    },
    {
     "id": "big_and_lazy",
     "en": "Big and Lazy",
     "jp": "巨大な怠惰",
     "zh": "巨大且懒惰",
     "rarity": "Rare",
     "desc": "When standing still for at least 1 second, gain 200% (+50% per stack) extra Health Regeneration. When moving, set Health Regeneration to 0%.",
     "descZh": "站立 1 秒以上获得额外 200%（每层+50%）自然回复；移动时自然回复归零。",
     "stack": "Multiplicative Linear",
     "tags": [
      "regen"
     ],
     "base": 80,
     "notes": "盾奶（Shield Mage）核心技能（build 必备 1-3 层）：原地站桩时回复翻倍，移动时归零；对站桩输出/坦价值极高。移动输入才触发归零，惯性滑行不算。"
    },
    {
     "id": "big_and_round",
     "en": "Big and Round",
     "jp": "大きな柱",
     "zh": "巨大且圆润",
     "rarity": "Rare",
     "desc": "Knockback Resistance +50% (+50% per stack); Max HP +30 (+30 per stack); Jump Height -10% (-10% per stack); Movement Speed -10% (-10% per stack)",
     "descZh": "击退抗性 +50%（每层+50%）；最大生命 +30（每层+30）；跳跃高度 -10%（每层-10%）；移速 -10%（每层-10%）",
     "stack": "Hyperbolic/Linear",
     "tags": [
      "hp",
      "knockback"
     ],
     "base": 55,
     "notes": "坦向堆叠；击退抗性过高会降低利用击退位移的能力，移速 -10% 对 Spellhammer 冲锋有影响。盾奶后期 HP 调节可选。"
    },
    {
     "id": "cold_blooded",
     "en": "Cold Blooded",
     "jp": "冷血",
     "zh": "冷血",
     "rarity": "Rare",
     "desc": "Reduce FREEZING stacks taken by X (X per stack); FROST Defense +15% (+15% per stack); FIRE Defense -15% (-15% per stack)",
     "descZh": "减少冰冻层数；冰抗 +15%（每层+15%）；火抗 -15%（每层-15%）",
     "stack": "Linear",
     "tags": [
      "res_frost"
     ],
     "base": 35,
     "notes": "针对冰冻地图/冰 boss 的抗性装；火抗 -15% 是代价。按对局敌人类型选。"
    },
    {
     "id": "conductive_armor",
     "en": "Conductive Armor",
     "jp": "コンダクティブ・アーマー",
     "zh": "导电护甲",
     "rarity": "Rare",
     "desc": "PHYSICAL Defense +20% (+20% per stack); Reduce BLEEDING stacks by X (+X per stack); ELEMENTAL Defense -5% (-5% per stack)",
     "descZh": "物理防御 +20%（每层+20%）；减少出血层数；元素防御 -5%（每层-5%）",
     "stack": "Linear",
     "tags": [
      "defense",
      "res_bleed"
     ],
     "base": 60,
     "notes": "物理伤害为主的环境收益极高；盾奶 build 推荐 1-2 层。元素防御 -5% 代价较小。"
    },
    {
     "id": "holy_blessing",
     "en": "Holy Blessing",
     "jp": "聖なる祝福",
     "zh": "圣光祝福",
     "rarity": "Rare",
     "desc": "Falling to LOW HP causes a large explosion dealing 275 (+X per stack) LUMINOUS damage with 100% WEAKENED chance. LUMINOUS Defense +15%; SHADOW Defense +15%; Overall Damage -10% per stack",
     "descZh": "进入低血量时引发大爆炸，造成 275（每层+X）圣光伤害并 100% 施加虚弱；圣/暗抗 +15%；总伤害 -10%（每层）",
     "stack": "Linear",
     "tags": [
      "defense",
      "dmg"
     ],
     "base": 45,
     "notes": "低血量保底反制技能；总伤害 -10% 是代价，输出职业慎选。盾奶可选 1 层（build 推荐）。"
    },
    {
     "id": "iron_skin",
     "en": "Iron Skin",
     "jp": "アイアンスキン",
     "zh": "铁皮",
     "rarity": "Rare",
     "desc": "Defense +8% (+8% per stack); Movement Speed -3% (-3% per stack); Overall Damage -2% (-2% per stack)",
     "descZh": "防御 +8%（每层+8%）；移速 -3%（每层-3%）；总伤害 -2%（每层-2%）",
     "stack": "Linear",
     "tags": [
      "defense"
     ],
     "base": 50,
     "notes": "盾奶 build 明确不建议（'いらない'）：移速与伤害代价高，防御收益一般。坦克可选少量。"
    },
    {
     "id": "last_stand",
     "en": "Last Stand",
     "jp": "最後の抵抗",
     "zh": "背水一战",
     "rarity": "Rare",
     "desc": "Upon taking damage which leaves you at 1 HP, receive X stacks of INVINCIBLE",
     "descZh": "受到伤害降至 1 HP 时获得 X 层无敌",
     "stack": "Linear",
     "tags": [
      "survival"
     ],
     "base": 75,
     "notes": "保命神技，与 Volatile Tenacity（不安定な執念）相性极佳（日文 wiki 明确推荐搭配）。盾奶/坦必带 1 层。"
    },
    {
     "id": "life_leech",
     "en": "Life Leech",
     "jp": "ライフリーチ",
     "zh": "生命汲取",
     "rarity": "Rare",
     "desc": "Restore 1 (+1 per stack) HP upon dealing damage. Overall Damage -10% (-10% per stack); Health Regeneration -50% (-50% per stack); Received Healing -20% (-20% per stack)",
     "descZh": "造成伤害回 1 HP（每层+1）；总伤害 -10%（每层）；自然回复 -50%（每层）；受疗 -20%（每层）",
     "stack": "Linear",
     "tags": [
      "lifesteal"
     ],
     "base": 30,
     "notes": "代价极大：伤害、自然回复、受疗全降。仅高频攻击自保流可选，普通局不推荐。"
    },
    {
     "id": "masochist",
     "en": "Masochist",
     "jp": "マゾヒスト",
     "zh": "受虐狂",
     "rarity": "Rare",
     "desc": "Reduce PARALYZED stacks taken by X (X per stack); ELECTRIC Defense +15% (+15% per stack); PHYSICAL Defense -10% (-15% per stack)",
     "descZh": "减少麻痹层数；电抗 +15%（每层+15%）；物理防御 -10%（每层-15%）",
     "stack": "Linear",
     "tags": [
      "res_electric"
     ],
     "base": 30,
     "notes": "针对电属性环境（如雷 boss）；物理抗性代价明显。"
    },
    {
     "id": "natures_gift",
     "en": "Nature's Gift",
     "jp": "ヒーリングオーラ",
     "zh": "自然馈赠",
     "rarity": "Rare",
     "desc": "Spawn up to 3 (+1 per level) personal Healing Auras at random locations every 10 seconds, healing 20 HP each",
     "descZh": "每 10 秒在随机位置生成最多 3（每层+1）个治疗光环，每个回 20 HP",
     "stack": "Linear",
     "tags": [
      "regen"
     ],
     "base": 25,
     "notes": "位置随机，实战价值有限；站桩坦偶尔能吃到。"
    },
    {
     "id": "benison_purification",
     "en": "Benison of Purification",
     "jp": "清めの祝福",
     "zh": "净化祝福",
     "rarity": "Legendary",
     "desc": "Periodically fire a projectile dealing 25 (+X per stack) LUMINOUS damage at closest enemy within 64m. SHADOW Defense +10%; Overall Defense -5% per stack",
     "descZh": "周期性向 64 米内最近敌人发射 25（每层+X）圣光弹；暗抗 +10%；总防御 -5%（每层）",
     "stack": "Linear",
     "tags": [
      "dmg",
      "defense"
     ],
     "base": 60,
     "notes": "免费白嫖输出 + 暗抗；盾奶 build 推荐 1 层。总防御 -5% 轻微代价。"
    },
    {
     "id": "big_and_wrathful",
     "en": "Big and Wrathful",
     "jp": "巨大な憤怒",
     "zh": "巨大且暴怒",
     "rarity": "Legendary",
     "desc": "Damage dealt at LOW HP +50%; Raise LOW HP threshold by 10%; Defense at LOW HP -25%",
     "descZh": "低血量时伤害 +50%；低血量阈值 +10%；低血量防御 -25%",
     "stack": "Linear/Hyperbolic",
     "tags": [
      "dmg",
      "lowhp"
     ],
     "base": 65,
     "notes": "狂暴流核心：配合 Nekomancer 的 Necropact（死之契约）等低血量机制极佳（日文 wiki 推荐）。坦克慎用。"
    },
    {
     "id": "curse_of_wrath",
     "en": "Curse of Wrath",
     "jp": "憤怒の呪い",
     "zh": "愤怒诅咒",
     "rarity": "Legendary",
     "desc": "Periodically fire a projectile dealing 25 (+X per stack) SHADOW damage at closest enemy within 32m. LUMINOUS Defense -20% (-20% per stack)",
     "descZh": "周期性向 32 米内最近敌人发射 25（每层+X）暗影弹；圣光防御 -20%（每层）",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 55,
     "notes": "免费输出；圣光防御 -20% 在圣光 boss 局（如 Jim 圣光攻击）代价高。"
    },
    {
     "id": "glass_cannon",
     "en": "Glass Cannon",
     "jp": "ガラスキャノン",
     "zh": "玻璃大炮",
     "rarity": "Legendary",
     "desc": "Damage +30% (+30% per stack); Health -50 (-50 per stack)",
     "descZh": "伤害 +30%（每层+30%）；生命 -50（每层-50）",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 70,
     "notes": "输出核心；每层 -50 HP 代价极大，一般 1-2 层。盾奶 build 用它调节过高的 HP（'HP 太高就用玻璃炮降'）。"
    },
    {
     "id": "healthy_guard",
     "en": "Healthy Guard",
     "jp": "ヘルシーガード",
     "zh": "健康守护",
     "rarity": "Legendary",
     "desc": "After being at FULL HP for 15 seconds (-X seconds per stack), next instance of damage reduced by 50% (+50% per stack)",
     "descZh": "满血 15 秒（每层-X 秒）后，下一次受到的伤害降低 50%（每层+50%）",
     "stack": "Linear/Hyperbolic",
     "tags": [
      "survival"
     ],
     "base": 65,
     "notes": "对紫（贯穿）攻击也有效，且能降低复活队友的 50% HP 代价至 25%（日文 wiki 实测）。奶妈/坦克 1 层。"
    },
    {
     "id": "mass_aspect",
     "en": "Mass Aspect",
     "jp": "集積の様相",
     "zh": "质量面相",
     "rarity": "Legendary",
     "desc": "Health +75 (+75 per stack); Movement Speed -30% (-30% per stack)",
     "descZh": "生命 +75（每层+75）；移速 -30%（每层-30%）",
     "stack": "Linear",
     "tags": [
      "hp"
     ],
     "base": 45,
     "notes": "高 HP 高代价；坦克 1 层即可，移速 -30% 对需要走位的职业伤害大。"
    },
    {
     "id": "volatile_tenacity",
     "en": "Volatile Tenacity",
     "jp": "不安定な執念",
     "zh": "不稳定韧性",
     "rarity": "Legendary",
     "desc": "Upon taking lethal damage when above LOW HP, survive with 1 HP. 150s cooldown (+25% cooldown rate per stack)",
     "descZh": "高于低血量阈值时受到致命伤害不会死，保留 1 HP。冷却 150 秒（每层冷却速率+25%）",
     "stack": "Linear",
     "tags": [
      "survival"
     ],
     "base": 90,
     "notes": "最强保命技，日文 wiki 多职业 build 必带 1 层；与 Last Stand 组合可形成免死链。注意持续伤害/多段攻击仍会打死。"
    }
   ]
  },
  {
   "id": "mobility",
   "en": "Crystal of Mobility",
   "zh": "机动之晶",
   "jp": "モビリティのクリスタル",
   "theme": "机动：移速/攻速/辅助CD",
   "skills": [
    {
     "id": "athletic",
     "en": "Athletic",
     "jp": "アスレチック",
     "zh": "运动健将",
     "rarity": "Common",
     "desc": "Movement Speed: +8% (+8% per stack)",
     "descZh": "移动速度 +8%（每层+8%）",
     "stack": "Linear",
     "tags": [
      "movespeed"
     ],
     "base": 65,
     "notes": "移速软上限 150%、硬上限 200%。Thaumaturge build 目标 MS 140 附近（含符文/加速等来源），堆到软上限后收益骤降。"
    },
    {
     "id": "eagle_eye",
     "en": "Eagle Eye",
     "jp": "イーグルアイ",
     "zh": "鹰眼",
     "rarity": "Common",
     "desc": "Projectile Speed +35% (+35% per stack)",
     "descZh": "弹速 +35%（每层+35%）",
     "stack": "Linear",
     "tags": [
      "projectile"
     ],
     "base": 50,
     "notes": "远程/法系核心（弹速软上限 250%）。Thaumaturge build 必须 5 层以上（配合 IQ 太高了 的弹速惩罚）。近战职业价值低。"
    },
    {
     "id": "hawkeye",
     "en": "Hawkeye",
     "jp": "ホークアイ",
     "zh": "隼眼",
     "rarity": "Common",
     "desc": "Projectile Distance +10 M (+10 M per stack); Projectile Spread -1% (-1% per stack)",
     "descZh": "射程 +10 米（每层+10）；弹道扩散 -1%（每层-1%）",
     "stack": "Linear",
     "tags": [
      "projectile"
     ],
     "base": 40,
     "notes": "射程与扩散；对狙击/远程流价值高，Thaumaturge 0-2 层即可。近战基本无用。"
    },
    {
     "id": "quick_breath",
     "en": "Quick Breath",
     "jp": "迅息",
     "zh": "急促呼吸",
     "rarity": "Common",
     "desc": "Utility Cooldown Rate: +10% (+10% per stack)",
     "descZh": "辅助技能冷却速率 +10%（每层+10%）",
     "stack": "Linear",
     "tags": [
      "utility"
     ],
     "base": 50,
     "notes": "Utility CD 软上限 200% 硬上限 300%；依赖位移/辅助技能的职业（Spellsword/Spellhammer/Gunmancer）价值高。"
    },
    {
     "id": "springfoot",
     "en": "Springfoot",
     "jp": "跳躍力",
     "zh": "弹簧脚",
     "rarity": "Common",
     "desc": "Jump Height: +20% (+20% per stack)",
     "descZh": "跳跃高度 +20%（每层+20%）",
     "stack": "Linear",
     "tags": [
      "jump"
     ],
     "base": 45,
     "notes": "Spellhammer 核心（Jump Smash 伤害随跳跃高度缩放）、Twinmage 空中流派；其他职业一般。"
    },
    {
     "id": "swift_hands",
     "en": "Swift Hands",
     "jp": "俊敏の手",
     "zh": "迅捷之手",
     "rarity": "Common",
     "desc": "Attack Speed: +15% (+15% per stack)",
     "descZh": "攻击速度 +15%（每层+15%）",
     "stack": "Linear",
     "tags": [
      "attackspeed"
     ],
     "base": 75,
     "notes": "攻速软上限 250% 硬上限 400%。几乎所有输出职业的核心堆叠；B站社区：光法攻速拉到 200% 就够（再往上暴击率递减）。"
    },
    {
     "id": "leg_day",
     "en": "Leg Day",
     "jp": "今日は脚の集中トレーニング！",
     "zh": "练腿日！",
     "rarity": "Rare",
     "desc": "Reduces HEAVY stacks taken by X; Movement Speed +5% (+5% per stack); Jump Height +10% (+10% per stack)",
     "descZh": "减少沉重层数；移速 +5%（每层+5%）；跳高 +10%（每层+10%）",
     "stack": "Linear",
     "tags": [
      "movespeed",
      "jump"
     ],
     "base": 40,
     "notes": "移速+跳高双收益，数值不高但无副作用；Spellhammer 可用。"
    },
    {
     "id": "reactive_panic",
     "en": "Reactive Panic",
     "jp": "反射的パニック",
     "zh": "应激恐慌",
     "rarity": "Rare",
     "desc": "Taking damage grants 1 (+1 per stack) stack of FRENZIED",
     "descZh": "受到伤害获得 1（每层+1）层狂乱",
     "stack": "Linear",
     "tags": [
      "frenzy"
     ],
     "base": 50,
     "notes": "狂乱提供攻速/移速；受伤触发，站在伤害地板上可快速叠层（日文 wiki 实测）。Twinmage/输出流可用。"
    },
    {
     "id": "smell_the_roses",
     "en": "Smell the Roses",
     "jp": "バラの香り",
     "zh": "闻闻花香",
     "rarity": "Rare",
     "desc": "Falling to low HP grants 7 (+2 per stack) stacks of HASTE with a 30s cooldown",
     "descZh": "进入低血量获得 7（每层+2）层急速，30 秒冷却",
     "stack": "Linear",
     "tags": [
      "haste"
     ],
     "base": 40,
     "notes": "低血量保命跑路技；对脆皮输出有价值。"
    },
    {
     "id": "thunder_aura",
     "en": "Thunder Aura",
     "jp": "サンダーオーラ",
     "zh": "雷霆光环",
     "rarity": "Rare",
     "desc": "Every second inflict 25 (+X per stack) ELECTRIC damage to enemies in radius. Overall Damage -10% (-X% per stack); Movement Speed -5% (-X% per stack)",
     "descZh": "每秒对周围敌人造成 25（每层+X）电伤害；总伤害 -10%（每层）；移速 -5%（每层）",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 45,
     "notes": "AOE 蹭伤害；总伤害 -10% 是代价。盾奶 build 推荐 1-2 层（补输出+麻痹）。B站'受击雷霆'玩法核心。"
    },
    {
     "id": "berserker_soul_melee",
     "en": "Berserker's Soul (Melee)",
     "jp": "バーサーカーソウル",
     "zh": "狂战士之魂（近战）",
     "rarity": "Legendary",
     "desc": "Main attack damage grants Berserker's Soul stacks (up to X). Each stack: +X% Overall Damage, +X% Attack Speed, -X% Health Regeneration. Taking damage resets. Overall Damage -20% (-20% per stack); Attack Speed -40% (-40% per stack)",
     "descZh": "主手攻击获得狂战士之魂层数（上限约 70 层）。每层 +0.64% 伤害、+1.28% 攻速、-0.71% 自然回复（近战）。受伤清空。自带 总伤害-20% 攻速-40%",
     "stack": "Linear",
     "tags": [
      "dmg",
      "attackspeed"
     ],
     "base": 70,
     "notes": "v0.51 拆分近战/远程版本。满层约 +45% 伤害/+90% 攻速/-50% 自然回复。Dot 伤害不叠层；复取只加副作用。无伤流输出核心，'光法能一直无伤收益很高'（B站）。"
    },
    {
     "id": "berserker_soul_ranged",
     "en": "Berserker's Soul (Ranged)",
     "jp": "バーサーカーソウル",
     "zh": "狂战士之魂（远程）",
     "rarity": "Legendary",
     "desc": "Main attack damage grants Berserker's Soul stacks. Each stack: +X% Overall Damage, +X% Attack Speed, +X% Projectile Spread. Taking damage resets. Overall Damage -10% (-10% per stack); Attack Speed -20% (-20% per stack)",
     "descZh": "主手攻击获得层数。每层 +0.64% 伤害、+1.28% 攻速、+0.02% 弹道扩散（远程）。受伤清空。自带 总伤害-10% 攻速-20%",
     "stack": "Linear",
     "tags": [
      "dmg",
      "attackspeed"
     ],
     "base": 70,
     "notes": "远程版代价更轻（扩散可用 Hawkeye 抵消）。枪手/光法无伤流核心。"
    },
    {
     "id": "big_and_speedy",
     "en": "Big and Speedy",
     "jp": "巨大な休息",
     "zh": "巨大且迅捷",
     "rarity": "Legendary",
     "desc": "Utility Cooldown Rate +50% (+50% per stack); Overall Defense -20% (-20% per stack)",
     "descZh": "辅助技能冷却速率 +50%（每层+50%）；总防御 -20%（每层-20%）",
     "stack": "Linear",
     "tags": [
      "utility"
     ],
     "base": 60,
     "notes": "盾奶 build 推荐 1 层（'巨大な急息'，提高仇恨获取节奏）；防御代价明显，坦克慎多取。"
    },
    {
     "id": "featherweight",
     "en": "Featherweight",
     "jp": "軽い足取り",
     "zh": "轻盈步伐",
     "rarity": "Legendary",
     "desc": "Movement Speed +30% (+30% per stack); Overall Defense -20% (-20% per stack)",
     "descZh": "移速 +30%（每层+30%）；总防御 -20%（每层-20%）",
     "stack": "Linear",
     "tags": [
      "movespeed"
     ],
     "base": 50,
     "notes": "移速大提升但防御代价高；移速软上限 150% 注意溢出。输出/奶妈可选 1 层。"
    },
    {
     "id": "heavy_hand",
     "en": "Heavy Hand",
     "jp": "重撃",
     "zh": "重手",
     "rarity": "Legendary",
     "desc": "Damage +30% (+30% per stack); Attack Speed -40% (-40% per stack)",
     "descZh": "伤害 +30%（每层+30%）；攻速 -40%（每层-40%）",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 60,
     "notes": "与攻速流冲突；单发高伤职业（Spellhammer Chuck/跳砸、Gunmancer 蓄力）价值高。"
    },
    {
     "id": "partial_flight",
     "en": "Partial Flight",
     "jp": "短距離飛行",
     "zh": "短暂飞行",
     "rarity": "Legendary",
     "desc": "Extra Jump: +1 (+1 per stack)",
     "descZh": "额外跳跃 +1（每层+1）",
     "stack": "Linear",
     "tags": [
      "jump"
     ],
     "base": 55,
     "notes": "二段跳极大改善走位与 Spellhammer 跳砸连段；通用强力技。"
    },
    {
     "id": "rapid_fire",
     "en": "Rapid Fire",
     "jp": "早撃ち",
     "zh": "急速射击",
     "rarity": "Legendary",
     "desc": "Attack Speed +50% (+50% per stack); Overall Damage -20% (-20% per stack)",
     "descZh": "攻速 +50%（每层+50%）；总伤害 -20%（每层-20%）",
     "stack": "Linear",
     "tags": [
      "attackspeed"
     ],
     "base": 65,
     "notes": "攻速大户但总伤 -20%；攻速软上限 250% 前收益高，溢出后负收益。B站光法攻略：攻速拉到 200% 即可。"
    },
    {
     "id": "way_of_the_law",
     "en": "Way of the Law",
     "jp": "道路交通法",
     "zh": "交通法规",
     "rarity": "Legendary",
     "desc": "Periodically switch between STOP and GO status. STOP: reduced Movement/Attack Speed, increased Damage. GO: increased Movement/Attack Speed, decreased Damage",
     "descZh": "周期切换 STOP/GO 状态：STOP 降速增伤，GO 增速降伤",
     "stack": "Exponential",
     "tags": [
      "dmg"
     ],
     "base": 35,
     "notes": "节奏不稳定，输出窗口随机；不推荐常规 build。"
    }
   ]
  },
  {
   "id": "chrono",
   "en": "Chrono Wizard",
   "zh": "时空法师",
   "jp": "クロノウィザード",
   "theme": "特殊：伤害/暴击/元素/类专",
   "skills": [
    {
     "id": "full_focus",
     "en": "Full Focus",
     "jp": "集中",
     "zh": "全神贯注",
     "rarity": "Common",
     "desc": "Critical Strike Chance +5% (+5% per stack); Critical Strike Damage +5% (+5% per stack)",
     "descZh": "暴击率 +5%（每层+5%）；暴击伤害 +5%（每层+5%）",
     "stack": "Linear",
     "tags": [
      "crit"
     ],
     "base": 65,
     "notes": "暴击率软上限 40% 硬上限 60%；暴伤硬上限 385%。注意与 Pocket Abacus（爆算盘，暴击率归零）冲突：日文 wiki 实测取 2 层以上 Full Focus 时爆算盘反而降低伤害。"
    },
    {
     "id": "potent_strike",
     "en": "Potent Strike",
     "jp": "強烈な一撃",
     "zh": "强力一击",
     "rarity": "Common",
     "desc": "Critical strikes have 6% (+6% per stack) higher chance to inflict a status effect",
     "descZh": "暴击施加状态异常概率 +6%（每层+6%）",
     "stack": "Linear",
     "tags": [
      "crit",
      "status"
     ],
     "base": 45,
     "notes": "异常流（Twinmage/光法暴击异常）辅助技能。"
    },
    {
     "id": "sorcerers_mastery",
     "en": "Sorcerer's Mastery",
     "jp": "魔導師達の極意",
     "zh": "法师的奥义",
     "rarity": "Common",
     "desc": "ELEMENTAL Damage +8% (+8% per stack)",
     "descZh": "元素伤害 +8%（每层+8%）",
     "stack": "Linear",
     "tags": [
      "elem_dmg"
     ],
     "base": 65,
     "notes": "法系核心堆叠；物理职业（Fistmage/Spellhammer 主物理）价值低。"
    },
    {
     "id": "strength",
     "en": "Strength",
     "jp": "ストレングス",
     "zh": "力量",
     "rarity": "Common",
     "desc": "PHYSICAL Damage +10% (+10% per stack)",
     "descZh": "物理伤害 +10%（每层+10%）",
     "stack": "Linear",
     "tags": [
      "phys_dmg"
     ],
     "base": 60,
     "notes": "物理职业核心；法系价值低。"
    },
    {
     "id": "iq_too_high",
     "en": "An IQ Too High?",
     "jp": "IQが高すぎる？",
     "zh": "智商太高了？",
     "rarity": "Rare",
     "desc": "ELEMENTAL Damage +25% (+25% per stack); Projectile Speed -15% (-15% per stack); Attack Speed -10% (-10% per stack)",
     "descZh": "元素伤害 +25%（每层+25%）；弹速 -15%（每层-15%）；攻速 -10%（每层-10%）",
     "stack": "Linear",
     "tags": [
      "elem_dmg"
     ],
     "base": 70,
     "notes": "法系强力增伤；弹速惩罚用 Eagle Eye 抵消（Thaumaturge build 建议配 4+ Eagle Eye）。取 2 层后用 Swift Hands 补攻速（日文 build）。"
    },
    {
     "id": "clutch_or_kick",
     "en": "Clutch or Kick",
     "jp": "背水の陣",
     "zh": "绝境反扑",
     "rarity": "Rare",
     "desc": "Gain +7% (+7% per stack) Overall Damage for every dead player in the party",
     "descZh": "每名阵亡队友提供 +7%（每层+7%）总伤害",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 30,
     "notes": "单排不出现；正常团战队友很少死，价值低。'背水の陣'。"
    },
    {
     "id": "cutting_edge",
     "en": "Cutting Edge",
     "jp": "鋭利な刃",
     "zh": "锋刃",
     "rarity": "Rare",
     "desc": "Chance to inflict BLEEDING +10% (+10% per stack); PHYSICAL Defense -5% (-5% per stack)",
     "descZh": "施加出血概率 +10%（每层+10%）；物理防御 -5%（每层-5%）",
     "stack": "Linear",
     "tags": [
      "status"
     ],
     "base": 50,
     "notes": "出血流核心（Spellsword 极意配合：出血回血）；物理输出职业收益高。"
    },
    {
     "id": "fire_aspect",
     "en": "Fire Aspect",
     "jp": "火の様相",
     "zh": "火焰面相",
     "rarity": "Rare",
     "desc": "FIRE Defense +15%; FIRE Damage +15%; BURNING chance +5%; FROST Defense -10% per stack",
     "descZh": "火抗 +15%（每层）；火伤 +15%（每层）；灼烧概率 +5%（每层）；冰抗 -10%（每层）",
     "stack": "Linear",
     "tags": [
      "elem_dmg",
      "res_fire"
     ],
     "base": 55,
     "notes": "火系职业（Twinmage 火焰手/火法）核心；火抗提升附带生存收益。"
    },
    {
     "id": "frost_aspect",
     "en": "Frost Aspect",
     "jp": "氷の様相",
     "zh": "寒冰面相",
     "rarity": "Rare",
     "desc": "FROST Defense +15%; FROST Damage +15%; FROZEN chance +5%; FIRE Defense -10% per stack",
     "descZh": "冰抗 +15%（每层）；冰伤 +15%（每层）；冰冻概率 +5%（每层）；火抗 -10%（每层）",
     "stack": "Linear",
     "tags": [
      "elem_dmg",
      "res_frost"
     ],
     "base": 55,
     "notes": "冰系职业核心（Twinmage 冰手）。"
    },
    {
     "id": "greater_focus",
     "en": "Greater Focus",
     "jp": "死中に活",
     "zh": "绝境专注",
     "rarity": "Rare",
     "desc": "Critical Strike Chance at low HP +10% (+10% per stack); Critical Strike Damage +3% (+3% per stack)",
     "descZh": "低血量时暴击率 +10%（每层+10%）；暴伤 +3%（每层+3%）",
     "stack": "Linear",
     "tags": [
      "crit",
      "lowhp"
     ],
     "base": 45,
     "notes": "低血量暴击流（配合 Big and Wrathful/低血量机制）。"
    },
    {
     "id": "luminous_aspect",
     "en": "Luminous Aspect",
     "jp": "聖の様相",
     "zh": "圣光面相",
     "rarity": "Rare",
     "desc": "LUMINOUS Damage +15%; SHADOW Defense +15%; WEAKENED chance +5%; ELEMENTAL Defense -5% per stack",
     "descZh": "圣光伤害 +15%（每层）；暗抗 +15%（每层）；虚弱概率 +5%（每层）；元素防御 -5%（每层）",
     "stack": "Linear",
     "tags": [
      "elem_dmg"
     ],
     "base": 60,
     "notes": "光法（Divine Hand）核心——B站实测光法伤害数值 50 远超其他元素 30，'光法是真的顶'，当前版本最强输出流。"
    },
    {
     "id": "poison_aspect",
     "en": "Poison Aspect",
     "jp": "毒の様相",
     "zh": "剧毒面相",
     "rarity": "Rare",
     "desc": "POISON Damage +15%; POISON Defense +15%; POISONED chance +5%; Received Healing -5% per stack",
     "descZh": "毒伤 +15%（每层）；毒抗 +15%（每层）；中毒概率 +5%（每层）；受疗 -5%（每层）",
     "stack": "Linear",
     "tags": [
      "elem_dmg"
     ],
     "base": 50,
     "notes": "毒奶（书奶 Thaumaturge）辅助；v0.51 受疗 -15%→-5% 缓和，但社区仍不建议书奶抓取（'依旧不太建议抓取'）。"
    },
    {
     "id": "shadow_aspect",
     "en": "Shadow Aspect",
     "jp": "闇の様相",
     "zh": "暗影面相",
     "rarity": "Rare",
     "desc": "SHADOW Damage +15%; BREACHED chance +5%; LUMINOUS Defense -10% per stack",
     "descZh": "暗影伤害 +15%（每层）；破甲概率 +5%（每层）；圣光防御 -10%（每层）",
     "stack": "Linear",
     "tags": [
      "elem_dmg"
     ],
     "base": 55,
     "notes": "暗属性枪手/暗法核心；圣光防御代价在圣光 boss 局注意。"
    },
    {
     "id": "sticky",
     "en": "Sticky",
     "jp": "粘着性",
     "zh": "粘性",
     "rarity": "Rare",
     "desc": "Apply 2 (+2 per stack) additional stacks of status effects against enemies. Negative status effects apply X (+X per stack) additional stacks to you",
     "descZh": "对敌人施加的状态异常额外 +2（每层+2）层；自身受到的负面状态也增加",
     "stack": "Linear",
     "tags": [
      "status"
     ],
     "base": 45,
     "notes": "异常流双刃剑：自身负面层数也增加，需搭配抗性/净化。"
    },
    {
     "id": "charged_strike",
     "en": "Charged Strike",
     "jp": "チャージドストライク",
     "zh": "充能打击",
     "rarity": "Legendary",
     "desc": "Critical Hits cause an explosion dealing X (+X per stack) PHYSICAL damage; Critical Strike Chance -5% (-5% per stack)",
     "descZh": "暴击引发 X（每层+X）物理伤害爆炸；暴击率 -5%（每层-5%）",
     "stack": "Linear",
     "tags": [
      "crit",
      "dmg"
     ],
     "base": 55,
     "notes": "暴击爆炸；暴击率惩罚注意。伤害属性为物理（B站评论区提问确认场景）。"
    },
    {
     "id": "flaming_spirit",
     "en": "Flaming Spirit",
     "jp": "炎の守護霊",
     "zh": "烈焰之灵",
     "rarity": "Legendary",
     "desc": "When at full HP, primary skill fires a fireball dealing 16 (+X per stack) FIRE damage. Received Healing -5%; Health Regeneration -20% per stack",
     "descZh": "满血时使用主手技能发射火球造成 16（每层+X）火伤；受疗 -5%（每层）；自然回复 -20%（每层）",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 60,
     "notes": "**与 Frozen Heart 互斥**（日文 wiki：'どちらかしか取得できない'）。Thaumaturge build 认为满血火球是'回复资源获取最强'技能（必带 1 层）。"
    },
    {
     "id": "frozen_heart",
     "en": "Frozen Heart",
     "jp": "凍てついた心",
     "zh": "寒冰之心",
     "rarity": "Legendary",
     "desc": "When at full HP, primary skill fires an icicle dealing 18 (+X per stack) FROST damage. Received Healing -5%; Health Regeneration -20% per stack",
     "descZh": "满血时使用主手技能发射冰锥造成 18（每层+X）冰伤；受疗 -5%（每层）；自然回复 -20%（每层）",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 55,
     "notes": "**与 Flaming Spirit 互斥**。日文 build 明确'凍てついた心は劣化（降级版）'，冰系可选。"
    },
    {
     "id": "pocket_abacus",
     "en": "Pocket Abacus",
     "jp": "携帯そろばん",
     "zh": "便携算盘",
     "rarity": "Legendary",
     "desc": "Every fifth instance of damage becomes a guaranteed Critical Strike. Critical Strike Damage +10%; Non-Critical Damage -10%; Sets Critical Strike Chance to 0%",
     "descZh": "每第 5 次伤害必暴击；暴伤 +10%（每层）；非暴击伤害 -10%（每层）；暴击率归零",
     "stack": "Linear",
     "tags": [
      "crit",
      "dmg"
     ],
     "base": 60,
     "notes": "稳定暴击流核心；与 Full Focus 冲突（日文 wiki 有详细期望值计算：1 层时 vs 集中收益约 2.97% 提升，2 层集中后收益变差）。高频攻击职业最佳。"
    },
    {
     "id": "third_law",
     "en": "Third Law",
     "jp": "反作用",
     "zh": "第三定律",
     "rarity": "Legendary",
     "desc": "Upon taking damage, deal 150% (+25% per stack) of its RAW value to enemies around you as PHYSICAL damage. On Fistmage's Parry, deal 50% of the damage around you",
     "descZh": "受到伤害时向周围敌人反弹 150%（每层+25%）原始值物理伤害；Fistmage 格挡时反弹 50%",
     "stack": "Linear",
     "tags": [
      "dmg"
     ],
     "base": 55,
     "notes": "v0.51 更新：Fistmage 格挡也触发（反弹固定 50%），并新增范围光环显示。坦克/反伤流核心。"
    },
    {
     "id": "warriors_will",
     "en": "Warrior's Will",
     "jp": "戦士の意志",
     "zh": "战士意志",
     "rarity": "Legendary",
     "desc": "Using your Utility Skill grants 4 (+2 per stack) stacks of EMPOWERED; Utility Cooldown Rate -15% (-15% per stack)",
     "descZh": "使用辅助技能获得 4（每层+2）层强力；辅助 CD 速率 -15%（每层-15%）",
     "stack": "Linear",
     "tags": [
      "utility"
     ],
     "base": 55,
     "notes": "Spellsword 短 CD 位移（Quick Dash）可常驻强力（日文 wiki 推荐），Gunmancer/其他频繁 Utility 职业也可用。"
    }
   ]
  }
 ],
 "classes": [
  {
   "id": "spellsword",
   "en": "Spellsword",
   "jp": "スペルソード",
   "zh": "剑术家",
   "role": "ATTACK",
   "roleZh": "攻击",
   "hp": "中等",
   "desc": "Agile close to mid-range fighter, able to dash in and out of combat.",
   "descZh": "灵活的近中距离战士，靠位移技能进出战场。",
   "skills": [
    {
     "type": "Primary",
     "en": "Telekinetic Strike",
     "zh": "念力斩",
     "desc": "近战主手，命中 2.5% 概率叠狂乱（v0.51）。"
    },
    {
     "type": "Secondary",
     "en": "Piercing Strike",
     "zh": "穿刺打击",
     "desc": "可蓄力的远程突刺，满蓄力可发射旋风（配旋风升级）。"
    },
    {
     "type": "Utility",
     "en": "Quick Dash",
     "zh": "快速冲刺",
     "desc": "短 CD 位移，可触发 Burst 攻速爆发、复活减免等机制。"
    }
   ]
  },
  {
   "id": "twinmage",
   "en": "Twinmage",
   "jp": "ツインメイジ",
   "zh": "双法师",
   "role": "ATTACK",
   "roleZh": "攻击",
   "hp": "低",
   "desc": "Versatile dual element user specialising in status ailments.",
   "descZh": "双元素施法者，专精状态异常。左右手可各选一种元素。",
   "skills": [
    {
     "type": "Hand",
     "en": "Flaming Hand / Ice Hand / Electric Hand / Wind Blade / Divine Hand / Profane Hand",
     "zh": "火焰手/寒冰手/雷电手/风刃/圣光手/暗影手",
     "desc": "六种元素手任选其二（左右手）。其中 Divine Hand（圣光手）为当前版本最强输出——B站实测伤害数值 50，远超其他元素 30。"
    },
    {
     "type": "Utility",
     "en": "Quickwarp",
     "zh": "快速传送",
     "desc": "位移技，配合 Wicked Sign 可触发全 buff。"
    }
   ]
  },
  {
   "id": "gunmancer",
   "en": "Gunmancer",
   "jp": "ガンマンサー",
   "zh": "枪术士",
   "role": "ATTACK",
   "roleZh": "攻击",
   "hp": "低",
   "desc": "Powerful long-range marksman focused on heavy damage.",
   "descZh": "强力远程射手，专注重火力。",
   "skills": [
    {
     "type": "Primary",
     "en": "VA-11 Blast Cannon",
     "zh": "VA-11 爆能炮",
     "desc": "光束主手（hit-scan，不吃弹速）。"
    },
    {
     "type": "Primary",
     "en": "Kinetic Fletchette",
     "zh": "动能箭",
     "desc": "弹道型主手。"
    },
    {
     "type": "Secondary",
     "en": "Firebomb / Photon Condenser / Antimatter Accelerator",
     "zh": "爆炎弹/光子凝聚器/反物质加速器",
     "desc": "三种副手武器：火AOE、蓄力散射（圣光）、暗属性枪。"
    },
    {
     "type": "Utility",
     "en": "Airblast",
     "zh": "空气冲击",
     "desc": "位移+短暂滞空，蓄力射击需在空中完成。"
    }
   ]
  },
  {
   "id": "fistmage",
   "en": "Fistmage",
   "jp": "フィストメイジ",
   "zh": "拳法师",
   "role": "HEAVY",
   "roleZh": "重型",
   "hp": "高",
   "desc": "Bulky close-range berserker able to parry incoming damage.",
   "descZh": "高血量近战狂战士，可以格挡（Parry）伤害。",
   "skills": [
    {
     "type": "Primary",
     "en": "Aura Fist",
     "zh": "光环拳",
     "desc": "蓄力近战拳。"
    },
    {
     "type": "Secondary",
     "en": "Deflecting Swipe",
     "zh": "格挡挥击",
     "desc": "核心机制：格挡成功触发大量升级效果（回血、buff、攻速、反弹）。"
    },
    {
     "type": "Utility",
     "en": "Super Endurance",
     "zh": "超级耐力",
     "desc": "位移/减伤。"
    }
   ]
  },
  {
   "id": "spellhammer",
   "en": "Spellhammer",
   "jp": "スペルハンマー",
   "zh": "法锤士",
   "role": "HEAVY",
   "roleZh": "重型",
   "hp": "150",
   "desc": "Dextrous and durable warrior, dealing swift and heavy hits.",
   "descZh": "敏捷耐久的战士，快速重击。基础 HP 150。",
   "skills": [
    {
     "type": "Primary",
     "en": "Pummel",
     "zh": "锤击",
     "desc": "挥锤 90 物理伤害（v0.51 由 110 下调）+ 击退；挥击期间移速×2（受移速影响，v0.51 改为不再受攻速影响）。"
    },
    {
     "type": "Secondary",
     "en": "Jump Smash",
     "zh": "跳砸",
     "desc": "跳跃后砸地 130+ 物理伤害，踩头顶可弹起连段；伤害随跳跃高度缩放。"
    },
    {
     "type": "Secondary",
     "en": "Chuck",
     "zh": "投掷",
     "desc": "蓄力投掷锤，伤害 38-150+ 随蓄力提升；落地爆炸（v0.51 熟练升级附加爆炸伤害）。"
    },
    {
     "type": "Utility",
     "en": "Disperse",
     "zh": "爆散",
     "desc": "130 物理伤害爆炸+后跳；空中可充能但更慢（v0.51）。"
    }
   ]
  },
  {
   "id": "shieldmage",
   "en": "Shield Mage",
   "jp": "シールドメイジ",
   "zh": "盾法师",
   "role": "HEAVY",
   "roleZh": "重型",
   "hp": "高",
   "desc": "Frontline defender able to block incoming strikes.",
   "descZh": "前线防御者，格挡来袭攻击（紫攻击除外）。",
   "skills": [
    {
     "type": "Primary",
     "en": "Offensive Strike",
     "zh": "进攻打击",
     "desc": "盾击输出。"
    },
    {
     "type": "Secondary",
     "en": "Defensive Stance",
     "zh": "防御姿态",
     "desc": "举盾格挡：红圈/弹丸/爆风可挡，紫攻击不可挡。"
    },
    {
     "type": "Utility",
     "en": "Evasive Maneuver",
     "zh": "离脱战术",
     "desc": "大范围护罩（保护队友）+ 紫伤减免；v0.51 盾冲 CD 恢复 4 秒。"
    }
   ]
  },
  {
   "id": "thaumaturge",
   "en": "Thaumaturge",
   "jp": "サウマタージ",
   "zh": "咒术师（书奶）",
   "role": "SUPPORT",
   "roleZh": "辅助",
   "hp": "中",
   "desc": "Healer which converts dealt damage into health for allies.",
   "descZh": "通过造成伤害转化为队友生命值的治疗者。",
   "skills": [
    {
     "type": "Passive",
     "en": "Life Energy",
     "zh": "生命能量",
     "desc": "造成伤害积攒生命能量（25% 消耗释放治疗）。"
    },
    {
     "type": "Primary",
     "en": "Foul Pustule",
     "zh": "腐化脓疱",
     "desc": "远程弹，命中可对敌伤害/对队友治疗。"
    },
    {
     "type": "Secondary",
     "en": "Pain Exchange",
     "zh": "痛苦交换",
     "desc": "核心治疗技：消耗生命能量治疗目标（可对自己）。"
    },
    {
     "type": "Utility",
     "en": "Soulborne",
     "zh": "灵魂出窍",
     "desc": "位移/保命。"
    }
   ]
  },
  {
   "id": "nekomancer",
   "en": "Nekomancer",
   "jp": "ネコマンサー",
   "zh": "猫术士（猫奶）",
   "role": "SUPPORT",
   "roleZh": "辅助",
   "hp": "低",
   "desc": "Summoner commanding a troop of undead cats.",
   "descZh": "指挥亡灵猫大军的召唤师。",
   "skills": [
    {
     "type": "Passive",
     "en": "Souls",
     "zh": "灵魂",
     "desc": "击杀敌人收集灵魂，用于召唤/强化猫。"
    },
    {
     "type": "Primary",
     "en": "Staff of Feline Mortality",
     "zh": "猫之必灭法杖",
     "desc": "远程法杖攻击。"
    },
    {
     "type": "Secondary",
     "en": "Call of the Undead",
     "zh": "亡灵召唤",
     "desc": "召唤僵尸猫/图腾猫（图腾猫提供治疗光环，v0.51 调整了回血速率与叠加规则）。"
    },
    {
     "type": "Utility",
     "en": "Spirit Drift",
     "zh": "灵魂漂移",
     "desc": "位移。"
    }
   ]
  }
 ],
 "class_upgrades": {
  "spellsword": [
   {
    "id": "ss_proficiency",
    "en": "Spellsword: Proficiency",
    "jp": "スペルソード：熟練",
    "zh": "剑术家：熟练",
    "rarity": "Common",
    "desc": "Piercing Strike range +4M (+4M per stack); Primary hits have 2.5% chance to grant FRENZIED (+? per stack)",
    "descZh": "穿刺打击射程 +4 米（每层+4）；主手命中 2.5% 概率获得狂乱（v0.51 新增）",
    "stack": "Linear",
    "tags": [
     "range"
    ],
    "base": 65,
    "notes": "v0.51：主手命中 2.5% 概率叠狂乱（最大 5 层，加算时长）。后期需要拉距离，尽量取。"
   },
   {
    "id": "ss_mastery",
    "en": "Spellsword: Mastery",
    "jp": "スペルソード：極意",
    "zh": "剑术家：奥义",
    "rarity": "Rare",
    "desc": "Bleeding damage heals 2 HP (+? per stack); Health Regeneration -100% (-?% per stack)",
    "descZh": "出血伤害回 2 HP（每层+1→v0.51 改为 1→2）；自然回复 -100%（v0.51 新增）",
    "stack": "Linear",
    "tags": [
     "lifesteal",
     "status"
    ],
    "base": 75,
    "notes": "v0.51 改动：回血 1→2，新增自然回复 -100%。配 Cutting Edge 出血流；取 3 层左右，对多个敌人挂出血回复可观。Boss 战小伤恢复也有用。"
   },
   {
    "id": "ss_burst",
    "en": "Spellsword: Burst",
    "jp": "スペルソード：バースト",
    "zh": "剑术家：爆发",
    "rarity": "Rare",
    "desc": "Using Utility skill grants +50% Attack Speed for 3 seconds (+50% per stack); Utility Cooldown +20% (+20% per stack)",
    "descZh": "使用位移技能后 3 秒攻速 +50%（每层+50%）；位移 CD +20%（每层+20%）",
    "stack": "Linear",
    "tags": [
     "attackspeed"
    ],
    "base": 60,
    "notes": "强力但代价大；可与攻速上限叠加（Frenzied/Burst 可突破攻速上限）。"
   },
   {
    "id": "ss_swift_stab",
    "en": "Spellsword: Swift Stab",
    "jp": "スペルソード：素早い一突き",
    "zh": "剑术家：迅捷突刺",
    "rarity": "Legendary",
    "desc": "Piercing Strike damage +35% (+35% per stack) multiplied by Movement Speed over 100%",
    "descZh": "穿刺打击伤害按超过 100% 的移速比例 +35%（每层+35%）乘算",
    "stack": "Linear",
    "tags": [
     "dmg",
     "movespeed"
    ],
    "base": 80,
    "notes": "无副作用，移速越高收益越大；剑术家核心输出升级，优先取。"
   },
   {
    "id": "ss_shieldbreaker",
    "en": "Spellsword: Shieldbreaker",
    "jp": "スペルソード：シールドブレイカー",
    "zh": "剑术家：破盾者",
    "rarity": "Legendary",
    "desc": "Piercing Strike deals 25% damage to BLOCKING enemies (+?%); Telekinetic Strike base damage +25% (+?%)",
    "descZh": "穿刺对格挡敌人造成 25% 伤害（每层+X）；念力斩基础伤害 +25%（v0.51 新增）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 50,
    "notes": "v0.51 新增：若为念力斩则追加 25% 伤害。目前会完全格挡的 boss 不多，日文 wiki 评价'微妙'。"
   },
   {
    "id": "ss_whirlwind",
    "en": "Spellsword: Whirlwind",
    "jp": "スペルソード：旋風",
    "zh": "剑术家：旋风",
    "rarity": "Legendary",
    "desc": "Full-charge Piercing Strike fires a spherical whirlwind dealing continuous PHYSICAL damage, piercing enemies; Piercing Strike charge time +10% (+10% per stack)",
    "descZh": "满蓄力穿刺发射球状旋风，穿透敌人持续物理伤害；蓄力时间 +10%（每层+10%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 85,
    "notes": "彻底改变玩法的远程化升级：约 0.1 秒一跳，大型敌人伤害爆炸；继承出血概率（配极意极强）；旋风暴击判定无效（暴击流不适用）。v0.51 后出血回血翻倍使其更强。"
   }
  ],
  "twinmage": [
   {
    "id": "tm_sinistra",
    "en": "Twinmage: Sinistra",
    "jp": "ツインメイジ：シニストラ",
    "zh": "双法师：左手（Sinistra）",
    "rarity": "Common",
    "desc": "Left hand damage +5% (+5% per stack); Left hand attack speed +5%; Right hand damage -3%; Right hand attack speed -3%",
    "descZh": "左手伤害/攻速 +5%（每层+5%）；右手伤害/攻速 -3%（每层-3%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 55,
    "notes": "左右手取舍：主手（常用元素）强化。计算组 B（与普通增伤乘算）。"
   },
   {
    "id": "tm_dextra",
    "en": "Twinmage: Dextra",
    "jp": "ツインメイジ：デクストラ",
    "zh": "双法师：右手（Dextra）",
    "rarity": "Common",
    "desc": "Right hand damage +5% (+5% per stack); Right hand attack speed +5%; Left hand damage -3%; Left hand attack speed -3%",
    "descZh": "右手伤害/攻速 +5%（每层+5%）；左手伤害/攻速 -3%（每层-3%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 55,
    "notes": "与 Sinistra 对应：双元素流时取舍。光法（Divine Hand）走右手则 Dextra。"
   },
   {
    "id": "tm_proficiency",
    "en": "Twinmage: Proficiency",
    "jp": "ツインメイジ：熟練",
    "zh": "双法师：熟练",
    "rarity": "Common",
    "desc": "Quickwarp distance +3M (+3M per stack)",
    "descZh": "瞬移距离 +3 米（每层+3）",
    "stack": "Linear",
    "tags": [
     "utility"
    ],
    "base": 50,
    "notes": "位移距离提升；双法师 CD 略长，一次瞬移更远有价值。"
   },
   {
    "id": "tm_rush",
    "en": "Twinmage: Rush",
    "jp": "ツインメイジ：ラッシュ",
    "zh": "双法师：疾冲",
    "rarity": "Common",
    "desc": "Inflicting a status effect grants 4 (+2 per stack) stacks of HASTE",
    "descZh": "施加状态异常获得 4（每层+2）层急速",
    "stack": "Linear",
    "tags": [
     "haste",
     "status"
    ],
    "base": 45,
    "notes": "异常触发不稳定（异常有冷却且概率低），日文 wiki 评价'评价難しい'。"
   },
   {
    "id": "tm_guarded",
    "en": "Twinmage: Guarded",
    "jp": "ツインメイジ：守護",
    "zh": "双法师：守护",
    "rarity": "Rare",
    "desc": "Inflicting a status effect grants 4 (+2 per stack) stacks of GUARDED",
    "descZh": "施加状态异常获得 4（每层+2）层守护",
    "stack": "Linear",
    "tags": [
     "status",
     "defense"
    ],
    "base": 45,
    "notes": "异常触发不稳定，同 Rush。"
   },
   {
    "id": "tm_mastery",
    "en": "Twinmage: Mastery",
    "jp": "ツインメイジ：極意",
    "zh": "双法师：奥义",
    "rarity": "Rare",
    "desc": "Dealing skill damage triggers an explosion dealing 25% damage in radius ?M (+?M per stack)",
    "descZh": "技能伤害触发 25% 伤害爆炸（半径每层+X）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 80,
    "notes": "简单强力的 +25% 增伤；2 层以上收益薄（日文 wiki 注意）。核心输出升级。"
   },
   {
    "id": "tm_wicked_sign",
    "en": "Twinmage: Wicked Sign",
    "jp": "ツインメイジ：邪悪な兆",
    "zh": "双法师：凶兆",
    "rarity": "Rare",
    "desc": "Using Utility skill has 6.7% (+?% per stack) chance to grant 7 stacks of EMPOWERED/GUARDED/HASTE/FRENZIED. 100% chance at 67 HP",
    "descZh": "使用位移技能 6.7%（每层+X%）概率获得强力/守护/急速/狂乱各 7 层；HP 为 67 时 100%",
    "stack": "Linear",
    "tags": [
     "utility"
    ],
    "base": 70,
    "notes": "离谱 buff 池；主动触发需放弃位移 CD 的应急价值。上限 67 HP 机制特殊。"
   },
   {
    "id": "tm_retaliation",
    "en": "Twinmage: Retaliation",
    "jp": "ツインメイジ：報復",
    "zh": "双法师：报复",
    "rarity": "Legendary",
    "desc": "Taking damage of the same element as your skill grants 3 stacks of EMPOWERED",
    "descZh": "受到与技能同属性的伤害时获得 3 层强力",
    "stack": "Linear",
    "tags": [
     "defense"
    ],
    "base": 40,
    "notes": "需要挨打触发，收益一般，日文 wiki 评价'必要性薄い'。"
   }
  ],
  "gunmancer": [
   {
    "id": "gm_overcharged",
    "en": "Gunmancer: Overcharged (VA-11 Blast Cannon)",
    "jp": "ガンマンサー：オーバーチャージ（VA-11ブラスト砲）",
    "zh": "枪术士：过载（VA-11 爆能炮）",
    "rarity": "Common",
    "desc": "Projectile size +5% (+5% per stack); ELECTRIC damage +15% (+15% per stack)",
    "descZh": "弹体大小 +5%（每层+5%）；电伤害 +15%（每层+15%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 55,
    "notes": "电枪（VA-11）强化；弹体变大更易命中。"
   },
   {
    "id": "gm_prof_firebomb",
    "en": "Gunmancer: Proficiency (Firebomb)",
    "jp": "ガンマンサー：熟練（爆炎弾）",
    "zh": "枪术士：熟练（爆炎弹）",
    "rarity": "Common",
    "desc": "Explosion radius +1M (+1M per stack); FIRE damage +7% (+7% per stack)",
    "descZh": "爆炸半径 +1 米（每层+1）；火伤 +7%（每层+7%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 55,
    "notes": "喷子（爆炎弹）流强化。"
   },
   {
    "id": "gm_prof_photon",
    "en": "Gunmancer: Proficiency (Photon Condenser)",
    "jp": "ガンマンサー：熟練（フォトン・コンデンサー）",
    "zh": "枪术士：熟练（光子凝聚器）",
    "rarity": "Common",
    "desc": "Charged shot fires +2 projectiles (+2 per stack); LUMINOUS damage +7% (+7% per stack)",
    "descZh": "蓄力射击弹数 +2（每层+2，v0.51 由 +1 改 +2）；圣光伤害 +7%（每层+7%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 70,
    "notes": "v0.51 加强（+1→+2）；注意弹数加成只对'使用位移技能后的蓄力射击'生效。光枪（VA-11/光子）流核心。"
   },
   {
    "id": "gm_prof_antimatter",
    "en": "Gunmancer: Proficiency (Antimatter Accelerator)",
    "jp": "ガンマンサー：熟練（アンチマター・アクセラレーター）",
    "zh": "枪术士：熟练（反物质加速器）",
    "rarity": "Common",
    "desc": "Projectiles +1 (+1 per stack); SHADOW damage +7% (+7% per stack)",
    "descZh": "弹数 +1（每层+1）；暗影伤害 +7%（每层+7%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 65,
    "notes": "暗枪（反物质）流强化。"
   },
   {
    "id": "gm_sidestep",
    "en": "Gunmancer: Sidestep",
    "jp": "ガンマンサー：サイドステップ",
    "zh": "枪术士：侧步",
    "rarity": "Common",
    "desc": "Using Airblast grants 2 stacks of HASTE",
    "descZh": "使用空气冲击获得 2 层急速",
    "stack": "Linear",
    "tags": [
     "haste"
    ],
    "base": 55,
    "notes": "2 层可常驻 buff；3 层以上几乎无收益（时长加算上限 5 层）。"
   },
   {
    "id": "gm_marksman",
    "en": "Gunmancer: Marksman (VA-11 Blast Cannon)",
    "jp": "ガンマンサー：マークスマン（VA-11ブラスト砲）",
    "zh": "枪术士：神射手（VA-11 爆能炮）",
    "rarity": "Legendary",
    "desc": "Every 10s a coin is thrown; shooting it with VA-11 fires an explosion with 400% damage toward nearby enemies (coin size +10%)",
    "descZh": "每 10 秒投掷硬币，用 VA-11 射击硬币向附近敌人释放 400% 伤害爆炸（硬币大小 +10%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 60,
    "notes": "机制特殊：本体弹被硬币吸收，实际收益约 1.66 倍（弹+爆炸）；换技能打硬币会空耗。光枪玩家可玩。"
   },
   {
    "id": "gm_mastery",
    "en": "Gunmancer: Mastery",
    "jp": "ガンマンサー：極意",
    "zh": "枪术士：奥义",
    "rarity": "Legendary",
    "desc": "Charged shot damage +50% (+50% per stack)",
    "descZh": "蓄力射击伤害 +50%（每层+50%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 75,
    "notes": "蓄力射击指位移技能后高空'シャキン'音效后使用的主/副手技能；光枪核心输出。"
   }
  ],
  "fistmage": [
   {
    "id": "fm_proficiency",
    "en": "Fistmage: Proficiency",
    "jp": "フィストメイジ：熟練",
    "zh": "拳法师：熟练",
    "rarity": "Common",
    "desc": "Successful parry heals 2 HP (+2 per stack) and creates an aura healing allies for half",
    "descZh": "格挡成功回 2 HP（每层+2）并产生光环治疗周围队友一半",
    "stack": "Linear",
    "tags": [
     "lifesteal",
     "healing"
    ],
    "base": 70,
    "notes": "格挡流核心；自回+团队光环。"
   },
   {
    "id": "fm_mach_punch",
    "en": "Fistmage: Mach Punch",
    "jp": "フィストメイジ：マッハパンチ",
    "zh": "拳法师：马赫拳",
    "rarity": "Rare",
    "desc": "PHYSICAL damage increased by 25% of Movement Speed over 100%",
    "descZh": "超过 100% 的移速按 25% 比例增加物理伤害",
    "stack": "Linear",
    "tags": [
     "dmg",
     "movespeed"
    ],
    "base": 65,
    "notes": "移速流增伤；配 Athletic/Featherweight。"
   },
   {
    "id": "fm_mastery",
    "en": "Fistmage: Mastery",
    "jp": "フィストメイジ：極意",
    "zh": "拳法师：奥义",
    "rarity": "Rare",
    "desc": "Successful parry grants +1 (+1 per stack) stack of EMPOWERED and GUARDED",
    "descZh": "格挡成功获得强力/守护各 1（每层+1）层",
    "stack": "Linear",
    "tags": [
     "status"
    ],
    "base": 65,
    "notes": "格挡后 buff；叠层越多越强。"
   },
   {
    "id": "fm_rage",
    "en": "Fistmage: Rage",
    "jp": "フィストメイジ：激昂",
    "zh": "拳法师：激昂",
    "rarity": "Rare",
    "desc": "Successful parry grants 100% Attack Speed for 4s and 3 (+1 per stack) HASTE. Max 10 (+2 per stack) stacks",
    "descZh": "格挡成功 4 秒攻速 +100% 并获得 3（每层+1）层急速；急速上限 10（每层+2，v0.51 改动）",
    "stack": "Linear",
    "tags": [
     "attackspeed"
    ],
    "base": 75,
    "notes": "v0.51：急速最大 10 层起，每升级 +2。攻速×激昂乘算，爆发极高。拳法师核心。"
   },
   {
    "id": "fm_runner",
    "en": "Fistmage: Runner",
    "jp": "フィストメイジ：ランナー",
    "zh": "拳法师：跑者",
    "rarity": "Rare",
    "desc": "While charging primary, Movement Speed gradually increases",
    "descZh": "蓄力主手时移速逐渐提升（v0.51 叠乘倍率下调）",
    "stack": "Linear",
    "tags": [
     "movespeed"
    ],
    "base": 50,
    "notes": "v0.51 削弱（倍率降低）。"
   },
   {
    "id": "fm_apply_force",
    "en": "Fistmage: Apply Force",
    "jp": "フィストメイジ：力の付与",
    "zh": "拳法师：施加力量",
    "rarity": "Legendary",
    "desc": "Successful parry grants 1 (+? per stack) Apply Force stack. While stacked, charged primary fires a PHYSICAL projectile consuming 1 stack. Parry cooldown +30% (+?%)",
    "descZh": "格挡成功获得 1（每层+X）层力量；有层时蓄力主手发射物理投射物消耗 1 层；格挡 CD +30%",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 70,
    "notes": "格挡→远程投射物；核心输出升级，代价是格挡 CD。"
   }
  ],
  "spellhammer": [
   {
    "id": "sh_prof_jump",
    "en": "Spellhammer: Proficiency (Jump Smash)",
    "jp": "スペルハンマー：熟練（ジャンプスマッシュ）",
    "zh": "法锤士：熟练（跳砸）",
    "rarity": "Common",
    "desc": "Knockback Force +10% (+10% per stack); Jump Smash Strength +5% (+5% per stack)",
    "descZh": "击退力 +10%（每层+10%）；跳砸强度 +5%（每层+5%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 55,
    "notes": "跳砸流基础强化。"
   },
   {
    "id": "sh_prof_chuck",
    "en": "Spellhammer: Proficiency (Chuck)",
    "jp": "スペルハンマー：熟練（投擲）",
    "zh": "法锤士：熟练（投掷）",
    "rarity": "Common",
    "desc": "Knockback Force +10%; Chucked Hammer Gravity Drop -10%; Additional explosion damage +8% (+8% per stack, v0.51)",
    "descZh": "击退力 +10%；投掷锤重力衰减 -10%；额外爆炸伤害 +8%（每层+8%，v0.51 新增）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 65,
    "notes": "v0.51 新增爆炸伤害：锤本体+爆炸 2 段伤害。落锤（Chuck）流核心。"
   },
   {
    "id": "sh_boosted",
    "en": "Spellhammer: Boosted",
    "jp": "スペルハンマー：ブースト",
    "zh": "法锤士：强化",
    "rarity": "Rare",
    "desc": "Disperse Blast Strength +10%; Disperse Blast Damage +10%",
    "descZh": "爆散（位移）强度 +10%；伤害 +10%",
    "stack": "Linear",
    "tags": [
     "utility",
     "dmg"
    ],
    "base": 50,
    "notes": "位移技能（爆散）伤害与击退强化。"
   },
   {
    "id": "sh_mastery_jump",
    "en": "Spellhammer: Mastery (Jump Smash)",
    "jp": "スペルハンマー：極意（ジャンプスマッシュ）",
    "zh": "法锤士：奥义（跳砸）",
    "rarity": "Rare",
    "desc": "Landing Jump Smash on an enemy reduces its cooldown by 25% (X% per stack)",
    "descZh": "跳砸命中敌人头顶时 CD -25%（每层+X%）",
    "stack": "Hyperbolic",
    "tags": [
     "dmg"
    ],
    "base": 60,
    "notes": "踩头减 CD 连段流核心；操作要求高。"
   },
   {
    "id": "sh_mastery_chuck",
    "en": "Spellhammer: Mastery (Chuck)",
    "jp": "スペルハンマー：極意（投擲）",
    "zh": "法锤士：奥义（投掷）",
    "rarity": "Rare",
    "desc": "Chucked Hammer bounces toward nearest enemy 1 time (+1 per stack); Gravity Drop -5%",
    "descZh": "投掷锤着弹后向最近敌人弹跳 1 次（每层+1）；重力衰减 -5%",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 70,
    "notes": "弹跳期间主/副手进入 CD；核爆锤玩法重要组件。"
   },
   {
    "id": "sh_concussion_jump",
    "en": "Spellhammer: Concussion (Jump Smash)",
    "jp": "スペルハンマー：脳震盪（ジャンプスマッシュ）",
    "zh": "法锤士：震荡（跳砸）",
    "rarity": "Legendary",
    "desc": "High-power Jump Smash deals additional ELECTRIC damage with 50% chance to PARALYZE",
    "descZh": "高威力跳砸附加电伤害，50% 概率麻痹",
    "stack": "Hyperbolic",
    "tags": [
     "dmg"
    ],
    "base": 60,
    "notes": "麻痹控制流。"
   },
   {
    "id": "sh_concussion_chuck",
    "en": "Spellhammer: Concussion (Chuck)",
    "jp": "スペルハンマー：脳震盪（投擲）",
    "zh": "法锤士：震荡（投掷）",
    "rarity": "Legendary",
    "desc": "On successful hit, spawn an AoE dealing ELECTRIC damage with 50% chance to PARALYZE",
    "descZh": "命中生成电伤害范围，50% 概率麻痹",
    "stack": "Hyperbolic",
    "tags": [
     "dmg"
    ],
    "base": 65,
    "notes": "AOE 电伤+麻痹。"
   },
   {
    "id": "sh_juggernaut_jump",
    "en": "Spellhammer: Juggernaut (Jump Smash)",
    "jp": "スペルハンマー：ジャガーノート（ジャンプスマッシュ）",
    "zh": "法锤士：主宰（跳砸）",
    "rarity": "Legendary",
    "desc": "High-power Jump Smash grants brief ENFORCED; max 5 stacks (+2 per upgrade)",
    "descZh": "高威力跳砸获得短暂坚守；上限 5 层（每升级+2，v0.51 限制）",
    "stack": "Linear",
    "tags": [
     "defense"
    ],
    "base": 65,
    "notes": "v0.51 限制最大 5 层。跳砸流生存核心。"
   },
   {
    "id": "sh_juggernaut_chuck",
    "en": "Spellhammer: Juggernaut (Chuck)",
    "jp": "スペルハンマー：ジャガーノート（投擲）",
    "zh": "法锤士：主宰（投掷）",
    "rarity": "Legendary",
    "desc": "Full-power throw grants brief EMPOWERED; max 5 stacks of EMPOWERED (+2 per upgrade)",
    "descZh": "满蓄力投掷获得短暂强力；强力上限 5 层（每升级+2）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 70,
    "notes": "核爆锤核心：蓄力投掷→强力增伤；配合重手/玻璃炮伤害爆炸。B站'一锤一锤核爆锤'。"
   }
  ],
  "shieldmage": [
   {
    "id": "sm_proficiency",
    "en": "Shieldmage: Proficiency",
    "jp": "シールドメイジ：熟練",
    "zh": "盾法师：熟练",
    "rarity": "Common",
    "desc": "Defensive Stance shield range increased +?% (+?% per stack)",
    "descZh": "防御姿态护盾范围 +?%（每层+?%）",
    "stack": "Linear",
    "tags": [
     "defense"
    ],
    "base": 70,
    "notes": "盾范围提升极大降低格挡难度；build 建议 2-3 层。10 层以上范围仍扩但收益低（日文实测）。"
   },
   {
    "id": "sm_unbreakable",
    "en": "Shieldmage: Unbreakable",
    "jp": "シールドメイジ：不壊",
    "zh": "盾法师：不坏",
    "rarity": "Common",
    "desc": "Purple damage -5% (-?% per stack); Evasive Maneuver purple reduction +10% (+?%); max reduction 75% including barrier",
    "descZh": "紫伤害 -5%（每层）；离脱战术紫减免 +10%；含屏障最大减免 75%",
    "stack": "Linear",
    "tags": [
     "defense"
    ],
    "base": 85,
    "notes": "盾法师核心（build 必须 8-10 层）：紫攻击无法格挡只能靠减免。'不壊'。"
   },
   {
    "id": "sm_ice_burst",
    "en": "Shieldmage: Ice Burst",
    "jp": "シールドメイジ：アイスバースト",
    "zh": "盾法师：寒冰爆发",
    "rarity": "Rare",
    "desc": "Ice Burst charge gain increased +? (+? per stack)",
    "descZh": "冰爆充能获取 +?（每层+?）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 45,
    "notes": "格挡充能→冰爆输出；需操作时机，build 推荐 1 层。"
   },
   {
    "id": "sm_mastery",
    "en": "Shieldmage: Mastery",
    "jp": "シールドメイジ：熟練（離脱戦術）",
    "zh": "盾法师：奥义（离脱战术）",
    "rarity": "Rare",
    "desc": "Evasive Maneuver shield size +50% (+?% per stack)",
    "descZh": "离脱战术护罩范围 +50%（每层+?%）",
    "stack": "Linear",
    "tags": [
     "defense"
    ],
    "base": 50,
    "notes": "只保护队友的护罩扩大；太大易被敌人进入，勿多取。"
   },
   {
    "id": "sm_rally_up",
    "en": "Shieldmage: Rally Up",
    "jp": "シールドメイジ：結束",
    "zh": "盾法师：集结",
    "rarity": "Legendary",
    "desc": "Using Evasive Maneuver grants EMPOWERED stacks to self and allies within 35m",
    "descZh": "使用离脱战术给自己与 35 米内队友强力",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 60,
    "notes": "团队 DPS 提升；配 Warden 时范围 bug 变为无限（日文 wiki 提及）。"
   },
   {
    "id": "sm_warden",
    "en": "Shieldmage: Warden",
    "jp": "シールドメイジ：番人",
    "zh": "盾法师：守望者",
    "rarity": "Legendary",
    "desc": "Using Evasive Maneuver grants RESTORATION to self and all allies; Utility Cooldown +50% (+?% per stack, v0.51 100%→50%)",
    "descZh": "使用离脱战术给自身与全体队友恢复；辅助 CD +50%（每层+X%，v0.51 由 100% 改 50%）",
    "stack": "Linear",
    "tags": [
     "healing"
    ],
    "base": 55,
    "notes": "v0.51 缓和（CD 惩罚 100%→50%），但日文 build 仍明确'非推奨'（CD+50% 依然太重）。恢复对紫攻击无效。"
   }
  ],
  "thaumaturge": [
   {
    "id": "th_keen_eye",
    "en": "Thaumaturge: Keen Eye",
    "jp": "サウマタージ：鋭い眼",
    "zh": "咒术师：锐眼",
    "rarity": "Common",
    "desc": "Pain Exchange range +15M (+15M per stack)",
    "descZh": "痛苦交换射程 +15 米（每层+15）",
    "stack": "Linear",
    "tags": [
     "range"
    ],
    "base": 80,
    "notes": "书奶 build 必须 7 层（Jim Phase 2/3 远程奶防事故，可妥协 6）。后期敌人击退强，射程不足奶不到。"
   },
   {
    "id": "th_proficiency",
    "en": "Thaumaturge: Proficiency",
    "jp": "サウマタージ：熟練",
    "zh": "咒术师：熟练",
    "rarity": "Common",
    "desc": "Pain Exchange heal +3 HP (+3 per stack); Pain Exchange cooldown -10% (-10% per stack)",
    "descZh": "痛苦交换治疗 +3 HP（每层+3）；CD -10%（每层-10%，v0.51 15%→10%）",
    "stack": "Linear",
    "tags": [
     "healing"
    ],
    "base": 85,
    "notes": "书奶 build 必须 7 层（v0.51 削弱 15%→10%，但仍核心）：奶量+CD 双收益。CD 有上限（-100% 封顶）。"
   },
   {
    "id": "th_mastery",
    "en": "Thaumaturge: Mastery",
    "jp": "サウマタージ：極意",
    "zh": "咒术师：奥义",
    "rarity": "Rare",
    "desc": "Pain Exchange energy cost -3% (-3% per stack)",
    "descZh": "痛苦交换消耗能量 -3%（每层-3%；24% 硬上限，8 层封顶）",
    "stack": "Linear",
    "tags": [
     "healing"
    ],
    "base": 90,
    "notes": "书奶核心（'見かけたら必ず取っておこう'）：能量消耗降低=更多治疗循环。硬上限 24%（8 层）。"
   },
   {
    "id": "th_splitshot",
    "en": "Thaumaturge: Splitshot",
    "jp": "サウマタージ：スプリットショット",
    "zh": "咒术师：分裂射击",
    "rarity": "Rare",
    "desc": "Foul Pustule fires +1 projectile (+1 per stack); spread +2.5% (+2.5%, v0.51 fixed); damage -30% (-30% per stack)",
    "descZh": "主手弹数 +1（每层+1）；扩散 +2.5%（每层，v0.51 修正）；伤害 -30%（每层-30%）",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 25,
    "notes": "**书奶 build 明确'1 层都别取'**：变成近战喷子，交火距离骤降。扩散可用 Hawkeye 部分抵消（日文有完整期望值计算）。"
   },
   {
    "id": "th_doping",
    "en": "Thaumaturge: Doping",
    "jp": "サウマタージ：ドーピング",
    "zh": "咒术师：兴奋剂",
    "rarity": "Legendary",
    "desc": "Pain Exchange grants target 5 (+5 per stack) stacks of GUARDED; Pain Exchange cooldown +15% (+?% per stack, v0.51 silent change)",
    "descZh": "痛苦交换为目标附加 5（每层+5）层守护；CD +15%（每层，v0.51 新增）；自我施加上限 3 层",
    "stack": "Linear",
    "tags": [
     "healing",
     "defense"
    ],
    "base": 95,
    "notes": "书奶最强技能（'いわずとしれた強パーク'）：奶+守护双效。v0.51 限制：自我 buff 最大 3 层、守护有上限、CD+15%。没抽到可考虑转生重来。队友满血无法作为目标——需要'故意不满血'卡时机。"
   },
   {
    "id": "th_everlife",
    "en": "Thaumaturge: Everlife",
    "jp": "永遠の命",
    "zh": "咒术师：永生",
    "rarity": "Legendary",
    "desc": "Revive MORTAL CURSED players using 100% Life Energy; self gets BREACHED 42s (-7s) and WEAKENED 48s (-8s), -25 Max HP for the round; Life Energy gain -10% (-10% per stack)",
    "descZh": "消耗 100% 生命能量复活被致命诅咒的队友；自身获得 42 秒破甲/48 秒虚弱，本局最大 HP -25；生命能量获取 -10%（每层）",
    "stack": "Linear",
    "tags": [
     "healing"
    ],
    "base": 40,
    "notes": "书奶 build 明确'不要'（'負けないようにするのがコンセプト'）：复活代价太大，约 50 秒无法有效治疗。高难局若治疗资源充足可考虑，重复取不划算。"
   },
   {
    "id": "th_splashback",
    "en": "Thaumaturge: Splashback",
    "jp": "サウマタージ：スプラッシュバック",
    "zh": "咒术师：溅射反冲",
    "rarity": "Legendary",
    "desc": "Pain Exchange target location spawns a POISON explosion dealing 75 damage",
    "descZh": "痛苦交换目标点生成 75 伤害毒爆",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 55,
    "notes": "无代价附加毒伤；近战多的队伍收益高。书奶 build'可有可无'。"
   }
  ],
  "nekomancer": [
   {
    "id": "nk_proficiency",
    "en": "Nekomancer: Proficiency",
    "jp": "ネコマンサー：熟練",
    "zh": "猫术士：熟练",
    "rarity": "Common",
    "desc": "Killed enemies drop souls +5% (+?%); random soul appearance +25% (+?%)",
    "descZh": "击杀掉魂概率 +5%（每层+X）；随机魂出现率 +25%（每层+X）",
    "stack": "Linear",
    "tags": [
     "summon"
    ],
    "base": 80,
    "notes": "猫术士核心（'キティが本体'）：没有足够的魂什么都干不了。4 层不保证常驻随机魂（基础概率倍率）。"
   },
   {
    "id": "nk_death_blossom",
    "en": "Nekomancer: Death Blossom",
    "jp": "ネコマンサー：デスブロッサム",
    "zh": "猫术士：死亡绽放",
    "rarity": "Rare",
    "desc": "Totem Kitty heal rate +10%; Totem Kitty effect range +1M; Overall Damage -3% per stack",
    "descZh": "图腾猫治疗速率 +10%（每层）；范围 +1 米（每层）；总伤害 -3%（每层）",
    "stack": "Linear",
    "tags": [
     "healing",
     "summon"
    ],
    "base": 60,
    "notes": "奶猫强化；-3% 总伤代价小，'見かけたら取ろう'（日文）。"
   },
   {
    "id": "nk_mastery",
    "en": "Nekomancer: Mastery",
    "jp": "ネコマンサー：極意",
    "zh": "猫术士：奥义",
    "rarity": "Rare",
    "desc": "Each soul held grants +2% Overall Damage (+?%); Health Regeneration +20% (+?%)",
    "descZh": "每持有 1 魂 +2% 总伤害（每层+X）；自然回复 +20%（每层+X）",
    "stack": "Linear",
    "tags": [
     "dmg",
     "summon"
    ],
    "base": 55,
    "notes": "与 Necropact（死之契约）相性极差（低血量机制冲突，日文 wiki 明确）。"
   },
   {
    "id": "nk_soul_detonation",
    "en": "Nekomancer: Soul Detonation",
    "jp": "ネコマンサー：ソウルデトネーション",
    "zh": "猫术士：灵魂引爆",
    "rarity": "Rare",
    "desc": "When Kitty dies, explode for ? SHADOW damage in 2m (+1.5m per stack) radius with 50% BREACHED chance",
    "descZh": "猫死亡时 2 米（每层+1.5 米）范围暗影爆炸，50% 破甲",
    "stack": "Linear",
    "tags": [
     "dmg"
    ],
    "base": 50,
    "notes": "v0.51 爆炸半径改动；需要猫死在敌人身边，操作要求高。图腾猫配合更可行。"
   },
   {
    "id": "nk_necropact",
    "en": "Nekomancer: Necropact",
    "jp": "ネコマンサー：死の契約",
    "zh": "猫术士：死亡契约",
    "rarity": "Legendary",
    "desc": "While a Kitty is summoned, damage taken at LOW HP increased 600% and redirected to the Kitty",
    "descZh": "召唤猫时，低血量受到的伤害增加 600% 并由猫承担",
    "stack": "Linear",
    "tags": [
     "survival"
    ],
    "base": 75,
    "notes": "低血量免死（猫扛伤）；与极意相性差（自然回复会脱离低血量）；配巨大且暴怒（Big and Wrathful）极佳（日文 wiki）。猫术士初始 HP 低，低血量前可能先死。"
   }
  ]
 },
 "builds": [
  {
   "classId": "spellsword",
   "archetypeId": "codex",
   "archetype": "综合构筑（图鉴站）",
   "patch": "v0.51",
   "title": "近战攻击手：高机动+可观物理输出",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：输出=迅捷之手、全力专注、力量、应激恐慌、熟练/爆发/破盾/旋风/极意、战意昂扬；生存=不屈韧性、最后一搏、铁皮、导电护甲、又大又圆、生命汲取、雷霆光环；节奏=快速呼吸、运动健将。可选：输出=绝境翻盘、充能打击；生存=蓬蓬、贪食者、质量之相；节奏=练腿日。",
   "must": [
    {
     "id": "strength",
     "count": 9,
     "reason": "物理伤害 +10%/层（构筑核心输出）"
    },
    {
     "id": "full_focus",
     "count": 5,
     "reason": "暴击率+暴伤；获得袖珍算盘时可节省点数"
    },
    {
     "id": "swift_hands",
     "count": 5,
     "reason": "攻速 +15%/层"
    },
    {
     "id": "quick_breath",
     "count": 4,
     "reason": "战术冷却 +10%/层"
    },
    {
     "id": "conductive_armor",
     "count": 1,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "big_and_round",
     "count": 1,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "低血量无敌保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "致命伤害存活"
    },
    {
     "id": "warriors_will",
     "count": 1,
     "reason": "战术技能叠赋能"
    },
    {
     "id": "athletic",
     "count": 1,
     "reason": "移速 +8%"
    },
    {
     "id": "reactive_panic",
     "count": 1,
     "reason": "受伤叠狂怒"
    },
    {
     "id": "ss_proficiency",
     "count": 1,
     "reason": "穿刺射程+狂怒叠层"
    },
    {
     "id": "ss_burst",
     "count": 1,
     "reason": "战术后攻速爆发"
    },
    {
     "id": "ss_mastery",
     "count": 1,
     "reason": "出血回血（代价自然回复-100%）"
    },
    {
     "id": "ss_shieldbreaker",
     "count": 1,
     "reason": "穿刺/斩击 +25% 伤害"
    },
    {
     "id": "ss_whirlwind",
     "count": 1,
     "reason": "满蓄力旋风持续伤害"
    }
   ],
   "nice": [
    {
     "id": "clutch_or_kick",
     "reason": "可选输出：绝境翻盘"
    },
    {
     "id": "charged_strike",
     "reason": "可选输出：充能打击"
    },
    {
     "id": "fluffy",
     "reason": "可选生存：蓬蓬"
    },
    {
     "id": "gluttonous",
     "reason": "可选生存：贪食者"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "leg_day",
     "reason": "可选节奏：练腿日"
    },
    {
     "id": "life_leech",
     "reason": "构筑常规提及：生命汲取（可换雷霆光环）"
    },
    {
     "id": "thunder_aura",
     "reason": "构筑常规提及：雷霆光环"
    }
   ],
   "avoid": [],
   "playstyle": "近战攻击手：高机动同时拥有可观的物理输出。构筑由中文图鉴站生成，未验证是否达到推荐水准，因游戏存在随机性，请根据实际情况合理取舍、灵活构筑。",
   "reroll": ""
  },
  {
   "classId": "twinmage",
   "archetypeId": "codex",
   "archetype": "综合构筑（图鉴站）",
   "patch": "v0.51",
   "title": "左手强化元素输出流",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：输出=左势、极意、光辉之相、智力过高、法师精通、全力专注；生存=不屈韧性、最后一搏、铁皮、导电护甲、又大又圆、生命汲取、护佑；节奏=迅捷之手、鹰眼、运动健将、疾驰。可选：输出=充能打击+袖珍算盘、狂战士之魂（远程）、烈焰之魂、冰封之心；生存=蓬蓬、贪食者、健康守卫、质量之相；节奏=快速呼吸、练腿日、应激恐慌。",
   "must": [
    {
     "id": "tm_sinistra",
     "count": 9,
     "reason": "左手伤害/攻速 +5%/层（右手-3%）——主手元素强化核心"
    },
    {
     "id": "swift_hands",
     "count": 6,
     "reason": "攻速 +15%/层"
    },
    {
     "id": "full_focus",
     "count": 5,
     "reason": "暴击率+暴伤；配袖珍算盘可节省"
    },
    {
     "id": "vital_drain",
     "count": 3,
     "reason": "暴击回血"
    },
    {
     "id": "iq_too_high",
     "count": 3,
     "reason": "元素伤害 +25%/层（配鹰眼抵消弹速惩罚）"
    },
    {
     "id": "eagle_eye",
     "count": 2,
     "reason": "弹速 +35%/层"
    },
    {
     "id": "conductive_armor",
     "count": 1,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "big_and_round",
     "count": 1,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "luminous_aspect",
     "count": 1,
     "reason": "光耀伤害 +15%（光辉之相）"
    },
    {
     "id": "athletic",
     "count": 1,
     "reason": "移速 +8%"
    },
    {
     "id": "tm_guarded",
     "count": 1,
     "reason": "施加状态异常获得强化防御（护佑）"
    }
   ],
   "nice": [
    {
     "id": "charged_strike",
     "reason": "可选：充能打击+袖珍算盘组合"
    },
    {
     "id": "pocket_abacus",
     "reason": "可选：袖珍算盘（配充能打击）"
    },
    {
     "id": "berserker_soul_ranged",
     "reason": "可选：狂战士之魂（远程）"
    },
    {
     "id": "flaming_spirit",
     "reason": "可选：烈焰之魂"
    },
    {
     "id": "frozen_heart",
     "reason": "可选：冰封之心"
    },
    {
     "id": "fluffy",
     "reason": "可选生存：蓬蓬"
    },
    {
     "id": "gluttonous",
     "reason": "可选生存：贪食者"
    },
    {
     "id": "healthy_guard",
     "reason": "可选生存：健康守卫"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "quick_breath",
     "reason": "可选节奏：快速呼吸"
    },
    {
     "id": "leg_day",
     "reason": "可选节奏：练腿日"
    },
    {
     "id": "reactive_panic",
     "reason": "可选节奏：应激恐慌"
    },
    {
     "id": "tm_mastery",
     "reason": "构筑常规：极意（技能伤害爆炸）"
    },
    {
     "id": "sorcerers_mastery",
     "reason": "构筑常规：法师精通（元素伤害）"
    }
   ],
   "avoid": [],
   "playstyle": "主左手元素强化路线（左势×9 投入巨大，需明确主手元素）。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。💡 光法（右手 Divine Hand 圣光手）路线参考——B站实测：'主要还是拉攻速，拉到200%就可以了；暴击异常可以小点几手；白蓝两个异常给buff都可以拿，金的道中可拿，对策Jim可带右手物法'（光法带飞视频评论区）；走光法时把左势换成右势（Dextra）、光之相（光辉之相）为核心。",
   "reroll": ""
  },
  {
   "classId": "gunmancer",
   "archetypeId": "codex",
   "archetype": "综合构筑（图鉴站）",
   "patch": "v0.51",
   "title": "攻速暴击重炮流",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：输出=熟练（光子）、迅捷之手、全力专注、智力过高、法师精通；生存=不屈韧性、最后一搏、铁皮、导电护甲、又大又圆、生命汲取；节奏=快速呼吸、运动健将、侧步。可选：输出=充能打击+袖珍算盘、法师精通、绝境翻盘、光辉之相、狂战士之魂（远程）；生存=蓬蓬、健康守卫、质量之相；节奏=快速呼吸、练腿日、应激恐慌。",
   "must": [
    {
     "id": "swift_hands",
     "count": 12,
     "reason": "攻速 +15%/层（构筑最大投入，蓄力/连射核心）"
    },
    {
     "id": "full_focus",
     "count": 5,
     "reason": "暴击率+暴伤"
    },
    {
     "id": "athletic",
     "count": 5,
     "reason": "移速 +8%/层"
    },
    {
     "id": "iq_too_high",
     "count": 4,
     "reason": "元素伤害 +25%/层"
    },
    {
     "id": "gm_sidestep",
     "count": 3,
     "reason": "气爆破冲刺获得加速（侧步）"
    },
    {
     "id": "conductive_armor",
     "count": 2,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "big_and_round",
     "count": 2,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    }
   ],
   "nice": [
    {
     "id": "gm_prof_photon",
     "reason": "构筑常规：熟练（光子凝聚器）——光枪路线核心"
    },
    {
     "id": "sorcerers_mastery",
     "reason": "构筑常规/可选：法师精通"
    },
    {
     "id": "charged_strike",
     "reason": "可选：充能打击+袖珍算盘"
    },
    {
     "id": "pocket_abacus",
     "reason": "可选：袖珍算盘"
    },
    {
     "id": "clutch_or_kick",
     "reason": "可选：绝境翻盘"
    },
    {
     "id": "luminous_aspect",
     "reason": "可选：光辉之相（圣光伤害）"
    },
    {
     "id": "berserker_soul_ranged",
     "reason": "可选：狂战士之魂（远程）"
    },
    {
     "id": "fluffy",
     "reason": "可选生存：蓬蓬"
    },
    {
     "id": "healthy_guard",
     "reason": "可选生存：健康守卫"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "quick_breath",
     "reason": "可选节奏：快速呼吸"
    },
    {
     "id": "leg_day",
     "reason": "可选节奏：练腿日"
    },
    {
     "id": "reactive_panic",
     "reason": "可选节奏：应激恐慌"
    }
   ],
   "avoid": [],
   "playstyle": "攻速+暴击+元素伤害重炮流。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。",
   "reroll": ""
  },
  {
   "classId": "gunmancer",
   "archetypeId": "bililightgun",
   "archetype": "光枪流（B站）",
   "patch": "v0.51 (2026-07-29)",
   "title": "光属性重炮：Luminous 277% 实测天赋",
   "source": "B站《光枪沉浸式输出三分半狂打20w+，到底是谁在诋毁光枪啊！》（UP 灵芝dayo，2026-07-12）+ 评论区天赋图与机制讨论",
   "must": [
    {
     "id": "swift_hands",
     "count": 10,
     "reason": "攻速 +15%/层，实机 192% 攻速——光枪 DPS 核心"
    },
    {
     "id": "iq_too_high",
     "count": 4,
     "reason": "全属性 +25%（评论：光枪熟练才 +7~8%，被 IQ 拉爆，是替代光枪熟练的正解）"
    },
    {
     "id": "luminous_aspect",
     "count": 3,
     "reason": "光属性形态核心——实机 Luminous Damage 277%，打暗弱点怪 20w+ 输出的来源"
    },
    {
     "id": "conductive_armor",
     "count": 3,
     "reason": "实机 Physical Defense 296%，站桩输出的生存保障"
    },
    {
     "id": "fluffy",
     "count": 2,
     "reason": "生命 +10/层，配合站桩输出防暴毙"
    },
    {
     "id": "glass_cannon",
     "count": 1,
     "reason": "总伤害 +35%（配高攻速收益最大）"
    },
    {
     "id": "sorcerers_mastery",
     "count": 1,
     "reason": "元素伤害 +8%"
    },
    {
     "id": "berserker_soul_ranged",
     "count": 1,
     "reason": "远程狂战魂：攻速大幅提升（站桩打法）"
    },
    {
     "id": "eagle_eye",
     "count": 1,
     "reason": "弹速提升，光枪手感"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "一血保命"
    },
    {
     "id": "life_leech",
     "count": 1,
     "reason": "吸血续航"
    },
    {
     "id": "big_and_round",
     "count": 1,
     "reason": "击退抗性 +50%，站桩不被推走"
    },
    {
     "id": "warriors_will",
     "count": 1,
     "reason": "伤害 +25%（战士意志）"
    },
    {
     "id": "clutch_or_kick",
     "count": 1,
     "reason": "随机高收益大天赋"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "不稳定韧性保命"
    },
    {
     "id": "vitality",
     "count": 1,
     "reason": "生命 +25"
    },
    {
     "id": "pocket_abacus",
     "count": 1,
     "reason": "点数计算/暴击联动"
    }
   ],
   "nice": [],
   "avoid": [
    {
     "id": "gm_prof_antimatter",
     "reason": "光枪熟练不加：shift 飞天太慢反而降 DPS，属性伤害 +7~8% 被 IQ 太高（+25%）完爆（评论区 yohane_bili 机制分析）"
    }
   ],
   "playstyle": "站桩光炮流：核心是 Luminous 光属性伤害（实机 277%）+ 攻速（192%）——天赋图来源玩家实测 3 分半狂打 20w+ 输出。注意点：不点光枪熟练（shift 空中射击降 DPS）、暴击率仅 2%（不堆暴击，纯光伤碾压）；配 4 件神器：加密档案×3、轮回之轮×6、HC 装甲板×2、太阳圣杯×1（天赋图右下，跨小局累积）。来源：B站 灵芝dayo 光枪输出视频 + 评论区天赋图（灵芝dayo 分享，2026-07-13）。",
   "reroll": ""
  },
  {
   "classId": "gunmancer",
   "archetypeId": "bilidualgun",
   "archetype": "双枪流（B站）",
   "patch": "v0.51 (2026-07-29)",
   "title": "镭射+散弹双枪流",
   "source": "B站评论区 JO丁 实测分享（《最终BOSS通关建议》视频评论区）",
   "note": "玩家实测：双枪bug——按住左键，然后蓄力右键，只松右键可以镭射散弹一起打出。加点：散弹+3、有乌鸦点乌鸦、没乌鸦就点属性伤害+8、异常增加点出2、补攻速到150以上、战士的意志1级、暴击叠到27、暴击会爆炸的词条、不怂可以拿玻璃大炮/重击。实战数据：打弱暗的大螃蟹一颗散弹60、暴击100（战士意志1.25倍+易伤1.25倍），射手技能可给一次双倍伤害射击。光法数值偏低且最终不弱圣，前期弱圣怪少。",
   "must": [
    {
     "id": "gm_prof_firebomb",
     "count": 3,
     "reason": "散弹＋3（核心输出词条）"
    },
    {
     "id": "iq_too_high",
     "count": 2,
     "reason": "有乌鸦点乌鸦（元素伤害+25%/层）"
    },
    {
     "id": "sorcerers_mastery",
     "count": 3,
     "reason": "没乌鸦就点属性伤害＋8（法师精通）"
    },
    {
     "id": "swift_hands",
     "count": 8,
     "reason": "补攻速到 150 以上"
    },
    {
     "id": "warriors_will",
     "count": 1,
     "reason": "战士的意志 1 级（1.25倍伤害buff）"
    },
    {
     "id": "full_focus",
     "count": 5,
     "reason": "暴击叠到 27（全力专注约5层）"
    },
    {
     "id": "charged_strike",
     "count": 1,
     "reason": "暴击会爆炸的词条"
    },
    {
     "id": "gm_mastery",
     "count": 1,
     "reason": "射手技能可以给一次双倍伤害的射击（奥义）"
    }
   ],
   "nice": [
    {
     "id": "glass_cannon",
     "count": 1,
     "reason": "不怂可以拿玻璃大炮"
    },
    {
     "id": "heavy_hand",
     "count": 1,
     "reason": "重击（单发高伤流适配）"
    },
    {
     "id": "sticky",
     "count": 1,
     "reason": "异常增加点出 2（粘着性/异常词条）"
    },
    {
     "id": "potent_strike",
     "count": 1,
     "reason": "异常增加点出 2（强烈一击，暴击流可用）"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "conductive_armor",
     "count": 1,
     "reason": "生存补强"
    }
   ],
   "avoid": [
    {
     "id": "luminous_aspect",
     "reason": "光法数值偏低且最终不弱圣，前期弱圣怪很少（JO丁实测）"
    },
    {
     "id": "springfoot",
     "reason": "枪手跳跃流收益低"
    }
   ],
   "playstyle": "双枪：按住左键蓄力右键，只松右键可镭射+散弹同时打出（当前版本bug/技巧）。散弹+3 为主输出，攻速150+保证频率，暴击27%触发爆炸词条。单发高伤+战士意志+易伤构成爆发。",
   "reroll": "优先商店找散弹熟练/乌鸦/攻速；传说找战士意志/充能打击/玻璃炮/重手。"
  },
  {
   "classId": "fistmage",
   "archetypeId": "codex",
   "archetype": "综合构筑（图鉴站）",
   "patch": "v0.51",
   "title": "格挡狂怒爆发流",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：输出=力量、应激恐慌、狂怒、熟练、极意；生存=不屈韧性、最后一搏、又大又圆、导电护甲、铁皮；节奏=快速呼吸、疾跑、运动健将。可选：输出=绝境翻盘、施力；生存=蓬蓬、贪食者、生命力、质量之相；节奏=练腿日、又大又快。",
   "must": [
    {
     "id": "strength",
     "count": 10,
     "reason": "物理伤害 +10%/层（核心输出）"
    },
    {
     "id": "athletic",
     "count": 7,
     "reason": "移速 +8%/层（联动音速拳增伤）"
    },
    {
     "id": "fm_proficiency",
     "count": 4,
     "reason": "格挡回血+治疗光环"
    },
    {
     "id": "conductive_armor",
     "count": 2,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "big_and_round",
     "count": 2,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "fm_runner",
     "count": 2,
     "reason": "蓄力期间移速提升（疾跑）"
    },
    {
     "id": "fm_rage",
     "count": 2,
     "reason": "格挡后攻速 +100% 4秒+加速（狂怒）"
    },
    {
     "id": "fm_mach_punch",
     "count": 2,
     "reason": "超过100%移速按25%增伤（音速拳）"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "reactive_panic",
     "count": 1,
     "reason": "受伤叠狂怒"
    },
    {
     "id": "fm_mastery",
     "count": 1,
     "reason": "格挡获得赋能+强化防御（极意）"
    }
   ],
   "nice": [
    {
     "id": "clutch_or_kick",
     "reason": "可选输出：绝境翻盘"
    },
    {
     "id": "fm_apply_force",
     "reason": "可选输出：施力（格挡发射投射物）"
    },
    {
     "id": "fluffy",
     "reason": "可选生存：蓬蓬"
    },
    {
     "id": "gluttonous",
     "reason": "可选生存：贪食者"
    },
    {
     "id": "vitality",
     "reason": "可选生存：生命力"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "leg_day",
     "reason": "可选节奏：练腿日"
    },
    {
     "id": "big_and_speedy",
     "reason": "可选节奏：又大又快"
    }
   ],
   "avoid": [],
   "playstyle": "格挡是核心：熟练回血、狂怒爆发、极意叠buff；移速联动音速拳增伤。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。",
   "reroll": ""
  },
  {
   "classId": "spellhammer",
   "archetypeId": "codex",
   "archetype": "跃击流（图鉴站）",
   "patch": "v0.51",
   "title": "跃击（Jump Smash）高机动输出流",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：输出=迅捷之手、力量、熟练（跃击）、极意（跃击）、巨力（跃击）、震荡（跃击）；生存=不屈韧性、最后一搏、又大又圆、导电护甲、铁皮；节奏=弹簧足、练腿日。可选：输出=熟练（跃击）、力量、全力专注；生存=蓬蓬、贪食者、质量之相；节奏=弹簧足、快速呼吸。",
   "must": [
    {
     "id": "strength",
     "count": 7,
     "reason": "物理伤害 +10%/层"
    },
    {
     "id": "swift_hands",
     "count": 6,
     "reason": "攻速 +15%/层。法锤普攻（Pummel）挥锤期间移速×2（随移速缩放）——攻速=挥锤/突进频率，空中快速机动与连段全靠它（wiki 机制）"
    },
    {
     "id": "springfoot",
     "count": 5,
     "reason": "跳跃高度 +20%/层（跃击伤害随高度缩放）"
    },
    {
     "id": "sh_prof_jump",
     "count": 5,
     "reason": "击退力度+跃击强度（熟练·跃击）"
    },
    {
     "id": "athletic",
     "count": 2,
     "reason": "移速 +8%"
    },
    {
     "id": "leg_day",
     "count": 2,
     "reason": "移速+跳高（练腿日）"
    },
    {
     "id": "sh_mastery_jump",
     "count": 2,
     "reason": "踩头顶跃击冷却 -25%（极意·跃击）"
    },
    {
     "id": "conductive_armor",
     "count": 1,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "big_and_round",
     "count": 1,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "sh_juggernaut_jump",
     "count": 1,
     "reason": "高功率跃击获得强化防御（巨力）"
    },
    {
     "id": "sh_concussion_jump",
     "count": 1,
     "reason": "高功率跃击附加雷电+50%麻痹（震荡）"
    }
   ],
   "nice": [
    {
     "id": "sh_prof_chuck",
     "reason": "可选：熟练（投掷）"
    },
    {
     "id": "full_focus",
     "reason": "可选：全力专注"
    },
    {
     "id": "fluffy",
     "reason": "可选生存：蓬蓬"
    },
    {
     "id": "gluttonous",
     "reason": "可选生存：贪食者"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "springfoot",
     "reason": "可选节奏：弹簧足（可继续加）"
    },
    {
     "id": "quick_breath",
     "reason": "可选节奏：快速呼吸"
    }
   ],
   "avoid": [],
   "playstyle": "跃击流：弹簧足+熟练（跃击）堆高度与强度，极意踩头减CD连段，巨力/震荡提供生存与控制。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。注：抛锤（Chuck）核爆流暂缺权威加点参考。",
   "reroll": ""
  },
  {
   "classId": "spellhammer",
   "archetypeId": "bilichuck",
   "archetype": "抛锤核爆流（B站）",
   "patch": "v0.51 (2026-07-29)",
   "title": "蓄力投掷核爆流",
   "source": "B站视频《一锤一锤核爆锤》（落羽松_Taxod 08-02 实机）+ 评论区 JO丁 实测评价",
   "note": "实机经验（视频口述 ASR）：玩锤主要都要点移速；丢锤不太需要跳高但需要弹速（丢进去的物体速度）；'丢垂一般叠一个三四个就够用，主玩丢垂几乎不（普攻）要叠四五六个'；跳锤对移速和跳高都需要。评论区：'跳锤扔锤各有各的好，扔锤在尾王也能打输出，跳锤伤害高但尾王会被肘飞，只能打罐子；扔锤可以自己处理空中单位'。核爆玩法：白嫖符文互叠起爆符，白拿至少 6 个力量（视频简介）；本局下砸伤害上限约 1550。",
   "must": [
    {
     "id": "sh_prof_chuck",
     "count": 3,
     "reason": "投掷熟练 3-4 个就够用（视频实测：'丢垂一般叠一个三四个就够用'）"
    },
    {
     "id": "eagle_eye",
     "count": 2,
     "reason": "丢锤需要弹速（丢进去的物体速度），不太需要跳高（视频实测）"
    },
    {
     "id": "athletic",
     "count": 3,
     "reason": "玩锤主要肯定要点移速（视频实测：'玩垂主要不然拿两个方法他都是要玩那个家移速的'）"
    },
    {
     "id": "sh_juggernaut_chuck",
     "count": 1,
     "reason": "满蓄力投掷→强力 buff；核爆核心（上限 5 层+2/升级）"
    },
    {
     "id": "sh_mastery_chuck",
     "count": 1,
     "reason": "弹跳+1 次；核爆玩法组件"
    },
    {
     "id": "heavy_hand",
     "count": 1,
     "reason": "单发高伤适配（投掷不吃攻速流）；评论区推荐拿重手"
    },
    {
     "id": "glass_cannon",
     "count": 1,
     "reason": "不怂可以拿玻璃大炮（JO丁 枪手同思路，单发流通用）"
    }
   ],
   "nice": [
    {
     "id": "strength",
     "count": null,
     "reason": "物理伤害核心"
    },
    {
     "id": "sh_concussion_chuck",
     "count": 1,
     "reason": "投掷命中 AOE 电伤+麻痹"
    },
    {
     "id": "smell_the_roses",
     "count": 1,
     "reason": "低血量保命"
    },
    {
     "id": "partial_flight",
     "count": 1,
     "reason": "二段跳走位"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    }
   ],
   "avoid": [
    {
     "id": "rapid_fire",
     "reason": "攻速流与投掷蓄力流冲突"
    },
    {
     "id": "swift_hands",
     "reason": "蓄力投掷不吃攻速"
    },
    {
     "id": "way_of_the_law",
     "reason": "节奏随机"
    }
   ],
   "playstyle": "蓄力投掷为主（满蓄力准星变红出手）：尾王也能打输出、可自理空中单位；核爆锤玩法：起爆符符文互叠白嫖力量。跳锤（跃击流）伤害更高但尾王会被肘飞，仅清罐子用（JO丁 实测对比）。",
   "reroll": "红找重手/玻璃炮/投掷系；蓝绿补物理伤害与移速弹速。"
  },
  {
   "classId": "shieldmage",
   "archetypeId": "codex",
   "archetype": "守望机动坦（图鉴站）",
   "patch": "v0.51",
   "title": "战术冷却+团队支援坦",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：生存=导电护甲、铁皮、不破、又大又圆、不屈韧性、最后一搏；团队=守望、集结、熟练、极意；节奏=快速呼吸、运动健将。可选：生存=贪食者、蓬蓬、质量之相；节奏=又大又快、练腿日。",
   "must": [
    {
     "id": "quick_breath",
     "count": 10,
     "reason": "战术冷却 +10%/层（护盾/机动频率核心）"
    },
    {
     "id": "sm_unbreakable",
     "count": 8,
     "reason": "紫攻击伤害 -5%/层+护盾额外减免（不破）"
    },
    {
     "id": "athletic",
     "count": 4,
     "reason": "移速 +8%/层"
    },
    {
     "id": "conductive_armor",
     "count": 3,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "sm_proficiency",
     "count": 3,
     "reason": "防御姿态盾范围扩大（熟练）"
    },
    {
     "id": "iron_skin",
     "count": 2,
     "reason": "防御 +8%"
    },
    {
     "id": "big_and_round",
     "count": 2,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "sm_rally_up",
     "count": 1,
     "reason": "护盾给全队赋能（集结）"
    },
    {
     "id": "sm_warden",
     "count": 1,
     "reason": "护盾给全队韧性可挡一次（守望，代价战术CD+50%）"
    }
   ],
   "nice": [
    {
     "id": "gluttonous",
     "reason": "可选生存：贪食者"
    },
    {
     "id": "fluffy",
     "reason": "可选生存：蓬蓬"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "big_and_speedy",
     "reason": "可选节奏：又大又快"
    },
    {
     "id": "leg_day",
     "reason": "可选节奏：练腿日"
    }
   ],
   "avoid": [],
   "playstyle": "战术冷却流：快速呼吸×10 让护盾/机动几乎常驻；守望+集结提供团队支援。注意守望战术CD+50%的代价已被快速呼吸部分抵消。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。",
   "reroll": ""
  },
  {
   "classId": "shieldmage",
   "archetypeId": "jpwiki",
   "archetype": "站桩坦流（日文wiki）",
   "patch": "v0.50 (2026-07-08)",
   "title": "站桩坦克（相信队友）",
   "source": "日文wiki build页（シールドメイジビルド）",
   "note": "以通关为前提的 build 方案。必须：大且懒1-3、生命力10、不破8-10、熟练2-3、最后抵抗1、不稳定韧性1、巨大且迅捷1；准必须：HP 150-250（多了用玻璃炮回调）、净化祝福1、雷霆光环1-2、导电护甲1-2、冰爆1；非推荐：守望者（CD+50%太重）。",
   "must": [
    {
     "id": "big_and_lazy",
     "count": 3,
     "reason": "站桩自然回复翻倍（1-3 层），坦度核心"
    },
    {
     "id": "vitality",
     "count": 10,
     "reason": "自然回复是坦主要恢复源（按大且懒取得度调整）"
    },
    {
     "id": "sm_unbreakable",
     "count": 9,
     "reason": "紫攻击减免+钉住敌人（8-10 层）"
    },
    {
     "id": "sm_proficiency",
     "count": 3,
     "reason": "盾范围扩大（2-3 层）"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "事故保险"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "同上"
    },
    {
     "id": "big_and_speedy",
     "count": 1,
     "reason": "辅助CD加快=仇恨节奏（防御-20%注意）"
    }
   ],
   "nice": [
    {
     "id": "fluffy",
     "count": null,
     "reason": "HP 补到 150-250；太高可用玻璃炮回调"
    },
    {
     "id": "big_and_round",
     "count": null,
     "reason": "HP+击退抗性（别堆满击退抗性）"
    },
    {
     "id": "benison_purification",
     "count": 1,
     "reason": "免费输出+虚弱减伤"
    },
    {
     "id": "thunder_aura",
     "count": 2,
     "reason": "免费AOE+麻痹"
    },
    {
     "id": "conductive_armor",
     "count": 2,
     "reason": "物理抗性+出血抗性"
    },
    {
     "id": "sm_ice_burst",
     "count": 1,
     "reason": "格挡转输出"
    }
   ],
   "avoid": [
    {
     "id": "sm_warden",
     "reason": "辅助CD +50% 代价太重（v0.51 缓和后仍重）"
    }
   ],
   "playstyle": "杂鱼战保护后排仇恨；门卫战拉仇恨到角落站桩成为掩体；紫攻击必须开护罩/躲。站得住就赢。",
   "reroll": "大且懒+不坏是硬目标；Eclipse 难度前还没拿到大且懒→考虑转生重开。"
  },
  {
   "classId": "thaumaturge",
   "archetypeId": "codex",
   "archetype": "综合构筑（图鉴站）",
   "patch": "v0.51",
   "title": "攻速移速综合奶",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：输出=熟练、极意、锐眼、潜能激发、永命、迅捷之手；生存=不屈韧性、最后一搏、铁皮、导电护甲、又大又圆、蓬蓬、应激恐慌；节奏=运动健将。可选：输出=充能打击、集中、烈焰之魂、冰封之心、毒素之相、智力过高；生存=质量之相、健康守卫；节奏=轻羽、快速呼吸。可选路线：烈焰/冰封——抽到烈焰之魂/冰封之心后放弃全力专注，继续升级迅捷之手；充能打击——抽到充能打击后放弃迅捷之手，走纯暴击伤害路线升级全力专注。",
   "must": [
    {
     "id": "swift_hands",
     "count": 7,
     "reason": "攻速 +15%/层（治疗节奏核心）"
    },
    {
     "id": "athletic",
     "count": 7,
     "reason": "移速 +8%/层"
    },
    {
     "id": "th_mastery",
     "count": 5,
     "reason": "痛楚交换能量消耗 -3%/层（加算，8层降至1%）"
    },
    {
     "id": "conductive_armor",
     "count": 2,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "big_and_round",
     "count": 2,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "th_keen_eye",
     "count": 2,
     "reason": "痛楚交换射程 +15米/层"
    },
    {
     "id": "th_proficiency",
     "count": 2,
     "reason": "治疗量+3、冷却-10%/层"
    },
    {
     "id": "fluffy",
     "count": 1,
     "reason": "最大生命 +10（蓬蓬）"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "hawkeye",
     "count": 1,
     "reason": "弹道距离+散布（猎鹰之眼）"
    },
    {
     "id": "eagle_eye",
     "count": 1,
     "reason": "弹速 +35%（鹰眼）"
    },
    {
     "id": "reactive_panic",
     "count": 1,
     "reason": "受伤叠狂怒"
    },
    {
     "id": "th_doping",
     "count": 1,
     "reason": "痛楚交换目标获得强化防御（潜能激发，自身最多3层）"
    },
    {
     "id": "th_everlife",
     "count": 1,
     "reason": "可复活致命诅咒队友（永命，代价-25HP/本局）"
    }
   ],
   "nice": [
    {
     "id": "charged_strike",
     "reason": "可选输出：充能打击（走纯暴击路线时）"
    },
    {
     "id": "full_focus",
     "reason": "可选输出：集中（烈焰/冰封路线则放弃）"
    },
    {
     "id": "flaming_spirit",
     "reason": "可选：烈焰之魂"
    },
    {
     "id": "frozen_heart",
     "reason": "可选：冰封之心"
    },
    {
     "id": "poison_aspect",
     "reason": "可选：毒素之相"
    },
    {
     "id": "iq_too_high",
     "reason": "可选：智力过高"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "healthy_guard",
     "reason": "可选生存：健康守卫"
    },
    {
     "id": "featherweight",
     "reason": "可选节奏：轻羽"
    },
    {
     "id": "quick_breath",
     "reason": "可选节奏：快速呼吸"
    }
   ],
   "avoid": [],
   "playstyle": "攻速移速双修的综合奶：迅捷之手×7 加快治疗频率，极意×5 降低能量消耗。注意可选路线：抽到烈焰/冰封之魂改堆攻速；抽到充能打击改堆暴击。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。",
   "reroll": ""
  },
  {
   "classId": "thaumaturge",
   "archetypeId": "biliheal",
   "archetype": "奶妈进阶流（B站）",
   "patch": "v0.51 (2026-07-29)",
   "title": "攻速奶+分裂弹输出流",
   "source": "B站视频《书奶（毒奶）玩法指导》（A_Soulsoul 07-21）+ 评论区 JohnUmane7 / JO丁 实测",
   "note": "视频口述（ASR转写）：通过造成伤害积累生命能量，伤害高低决定奶量效率——攻速是奶妈第一属性。分裂射击推荐点 1 个绝对不要 1 个以上（1弹140% / 2弹120%）；鹰眼 2 个抵消分裂散射；重手 1 个配分裂（双弹丸伤害×2）；永命 1 个就够；极意拿 3-6 层降消耗。评论补充（JohnUmane7）：攻速叠到 200，智商太高必拿有多少选多少，永恒生命看到必拿，火球必拿（点燃+中毒持续回蓝），大食汉多拿抵消负面，+50攻速传说和+75生命传说必拿。JO丁修正：弹速 3-4 级、射程 2-3 级、毒 1-2 级、强烈一击不拿（除非暴击符文）。",
   "must": [
    {
     "id": "swift_hands",
     "count": 10,
     "reason": "攻速叠到 200% 左右（JohnUmane7：'攻速手叠到200层就够'；视频：输出达标线=攻速200%+弹丸合计80伤害）"
    },
    {
     "id": "th_proficiency",
     "count": 3,
     "reason": "增加回复量并减少回复CD，越多越好（视频：'继援相关词条决定了奶距离和奶CD'）"
    },
    {
     "id": "th_keen_eye",
     "count": 3,
     "reason": "提升奶人手短距离，等级越高奶人距离越长；'一定要多拿距离！'（评论区）"
    },
    {
     "id": "th_mastery",
     "count": 6,
     "reason": "减少体力消耗，难出，看到优先拿；'点了三个满花板可以拿六磁降低消耗'（24%硬上限=8层）"
    },
    {
     "id": "th_splitshot",
     "count": 1,
     "reason": "**点 1 个绝对不要 1 个以上**：1弹伤害140%，2弹120%负收益（视频+JO丁一致）"
    },
    {
     "id": "eagle_eye",
     "count": 2,
     "reason": "弹速 3-4 级（JO丁）；鹰眼本身附带降低分裂散射，保中远距离命中"
    },
    {
     "id": "heavy_hand",
     "count": 1,
     "reason": "配分裂后双弹丸伤害直接变 200%，提升巨大；但不建议点多（-40%攻速需快手补回）"
    },
    {
     "id": "th_doping",
     "count": 1,
     "reason": "为被奶队友施加强谷（守护），点一次就够，多点提升BUFF时间"
    },
    {
     "id": "th_everlife",
     "count": 1,
     "reason": "复活黑骷髅队友的大级手段，看到必拿（JohnUmane7：'优先级比子弹还高'）；多个只减负面时间所以一个就够"
    },
    {
     "id": "iq_too_high",
     "count": 3,
     "reason": "智商太高了加 25 属性，奶妈打异常跟属性有关，'看到必拿，有多少选多少'（JohnUmane7）"
    },
    {
     "id": "flaming_spirit",
     "count": 1,
     "reason": "看见火球一定要拿：凤凰火的点燃会和中毒一起给你持续回蓝（评论区）"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "最后一波+不稳定韧性两个同时最好，只拿不稳定韧性也足够（视频）"
    }
   ],
   "nice": [
    {
     "id": "last_stand",
     "reason": "配不稳定韧性：一血吸给击秒无敌（视频推荐双保险）"
    },
    {
     "id": "poison_aspect",
     "count": 1,
     "reason": "毒素项位可不点，最多 1 个（-15%被回复量难恢复；视频：'不推荐点，这度点一个'）"
    },
    {
     "id": "sticky",
     "count": 1,
     "reason": "抽到兴奋剂可以选，4秒守护扩到8秒无限叠加（JohnUmane7）"
    },
    {
     "id": "reactive_panic",
     "count": 1,
     "reason": "受伤加速，毒奶打近身有用，后期选（JohnUmane7）"
    },
    {
     "id": "benison_purification",
     "count": 1,
     "reason": "自动锁敌能喂奶充能，所有职业可用，推荐（JohnUmane7）"
    },
    {
     "id": "gluttonous",
     "count": null,
     "reason": "抵消负面状态（毒/乌鸦减回复），可以多拿（JohnUmane7）"
    },
    {
     "id": "rapid_fire",
     "count": 1,
     "reason": "+50 攻速传说看到必拿（JohnUmane7）"
    },
    {
     "id": "mass_aspect",
     "count": 1,
     "reason": "+75 生命传说必拿，能少拿几个锁；拿到永命后专门多点HP词条（视频）"
    },
    {
     "id": "frozen_heart",
     "count": 1,
     "reason": "拿到传说白虎（冰封景象）可选，增加冰冻异常概率（JohnUmane7）"
    },
    {
     "id": "hawkeye",
     "count": 2,
     "reason": "射程 2-3 级（JO丁：为弥补分裂带来的散射）"
    },
    {
     "id": "fluffy",
     "count": null,
     "reason": "拿到永命后多点提升HP的词条（视频）"
    },
    {
     "id": "smell_the_roses",
     "count": 1,
     "reason": "最终Boss超大AOE没有加速就必须保障能跑出范围（视频）"
    },
    {
     "id": "th_splashback",
     "count": 1,
     "reason": "治疗队友产生毒爆，可拿（JohnUmane7）"
    }
   ],
   "avoid": [
    {
     "id": "potent_strike",
     "reason": "强烈一击是暴击才会增加异常概率，可以不拿（除非有暴击符文）（JO丁）"
    },
    {
     "id": "big_and_speedy",
     "reason": "巨大急吸很强但必须补够防御，不然被锁定两三拳被打死（JO丁）"
    }
   ],
   "playstyle": "攻速奶：通过攻速快速叠生命能量→高频治疗。分裂弹1层+重手1层构成输出（双弹丸200%），鹰眼保证命中。双书奶才是完全体：一书奶负责奶人、一书奶负责输出，互不冲突（视频）。",
   "reroll": "一般3个商店都有奶妈能用的；中间/死神商店没刷好就看功能商店有没有攻速，优先推荐拿攻速（JohnUmane7）"
  },
  {
   "classId": "thaumaturge",
   "archetypeId": "jpwiki",
   "archetype": "稳定奶（日文wiki）",
   "patch": "v0.51 (2026-07-29)",
   "title": "稳定型远程奶妈（书奶）",
   "source": "日文wiki build页（サウマタージビルド）",
   "note": "必须：锐眼7、熟练7、兴奋剂1、烈焰之灵1、鹰眼5、隼眼0-2、运动健将（MS140附近）；准必须：极意（见必拿）、溅射反冲、不稳定韧性/最后抵抗/健康守护、HP约200（导电护甲全拿、铁皮不要）、智力过高2；不要：分裂射击、永生。",
   "must": [
    {
     "id": "th_keen_eye",
     "count": 7,
     "reason": "Jim Phase2/3 远程奶防事故的必需射程；妥协可 6"
    },
    {
     "id": "th_proficiency",
     "count": 7,
     "reason": "奶量+CD 双核心（v0.51 CD缩短被削 15%→10%，更需要堆）"
    },
    {
     "id": "th_doping",
     "count": 1,
     "reason": "最强守护奶技，没抽到可考虑转生；v0.51 自我上限 3 层、CD+15%"
    },
    {
     "id": "flaming_spirit",
     "count": 1,
     "reason": "满血火球=回复资源获取最强（与寒冰之心互斥，冰版是降级）"
    },
    {
     "id": "eagle_eye",
     "count": 5,
     "reason": "弹速抵消智力过高惩罚；4 层保底"
    },
    {
     "id": "athletic",
     "count": null,
     "reason": "移速堆到 140 附近（含暗号记录/其他来源），别开局多拿"
    }
   ],
   "nice": [
    {
     "id": "th_mastery",
     "count": null,
     "reason": "能量消耗 -3%/层，24% 硬上限=8 层封顶；见必拿"
    },
    {
     "id": "th_splashback",
     "count": null,
     "reason": "无代价 75 毒伤爆炸；近战队伍更赚"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命；配最后抵抗"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "配不稳定韧性；怕死选它"
    },
    {
     "id": "healthy_guard",
     "count": 1,
     "reason": "满血减伤+复活成本降半"
    },
    {
     "id": "conductive_armor",
     "count": null,
     "reason": "物理防御+出血抗性（全拿）"
    },
    {
     "id": "iq_too_high",
     "count": 2,
     "reason": "元素 +25%/层；取 2 后补 1 迅捷之手"
    },
    {
     "id": "hawkeye",
     "count": null,
     "reason": "0-2 层，鹰眼同用途"
    }
   ],
   "avoid": [
    {
     "id": "th_splitshot",
     "reason": "1 层都别取：近战化+扩散，生存崩盘"
    },
    {
     "id": "th_everlife",
     "reason": "复活代价=50秒废人+永久-25HP；理念冲突"
    },
    {
     "id": "poison_aspect",
     "reason": "v0.51 受疗惩罚缓解但仍不建议"
    }
   ],
   "playstyle": "鹰眼+锐眼让你边打边看全场；痛苦交换的时机与目标选择是核心，差插奶的瞄准+血量判断能力要求高。",
   "reroll": "先看蓝（忍耐）绿（机动）→ 最后看红（时空）。红只在有必须传奇/奥义时才取；红只出伤害系就 reroll。必须项拿完前手动 reroll 只给红。青绿看到必须/准必须直接拿；拿完青绿必要数量后，红公共系补到需要数量再 reroll。伤害系多且必须项拿完→留 token 下轮。后期 HP 不稳可用绿 reroll。"
  },
  {
   "classId": "nekomancer",
   "archetypeId": "codex",
   "archetype": "召唤奶流（图鉴站）",
   "patch": "v0.51",
   "title": "灵魂召唤+生存强化流",
   "source": "Ecliptica Codex 中文图鉴站构筑（36点规划）",
   "note": "常规：节奏=熟练、死之花、运动健将、练腿日；生存=不屈韧性、最后一搏、又大又圆、导电护甲、铁皮、蓬蓬、死灵契约。可选：输出/增益=冰封之心、烈焰之魂、怒焰诅咒、极意；生存=质量之相、健康守卫。",
   "must": [
    {
     "id": "athletic",
     "count": 8,
     "reason": "移速 +8%/层"
    },
    {
     "id": "nk_proficiency",
     "count": 8,
     "reason": "掉魂概率+随机灵魂生成（召唤核心）"
    },
    {
     "id": "fluffy",
     "count": 5,
     "reason": "最大生命 +10/层（猫灵师血量低，蓬蓬堆HP）"
    },
    {
     "id": "big_and_round",
     "count": 3,
     "reason": "击退抗性+最大生命"
    },
    {
     "id": "nk_death_blossom",
     "count": 3,
     "reason": "图腾猫治疗速度+范围（死之花，代价伤害-3%）"
    },
    {
     "id": "conductive_armor",
     "count": 2,
     "reason": "物理防御+出血抗性"
    },
    {
     "id": "shadow_aspect",
     "count": 2,
     "reason": "暗影伤害 +15%（暗影之相，配猫暗伤）"
    },
    {
     "id": "iron_skin",
     "count": 1,
     "reason": "防御 +8%"
    },
    {
     "id": "last_stand",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "volatile_tenacity",
     "count": 1,
     "reason": "保命"
    },
    {
     "id": "leg_day",
     "count": 1,
     "reason": "移速+跳高（练腿日）"
    },
    {
     "id": "nk_necropact",
     "count": 1,
     "reason": "低血量伤害转嫁猫（死灵契约）"
    }
   ],
   "nice": [
    {
     "id": "frozen_heart",
     "reason": "可选输出/增益：冰封之心"
    },
    {
     "id": "flaming_spirit",
     "reason": "可选输出/增益：烈焰之魂"
    },
    {
     "id": "curse_of_wrath",
     "reason": "可选输出/增益：怒焰诅咒（愤怒诅咒）"
    },
    {
     "id": "nk_mastery",
     "reason": "可选输出/增益：极意（每魂+伤害）"
    },
    {
     "id": "mass_aspect",
     "reason": "可选生存：质量之相"
    },
    {
     "id": "healthy_guard",
     "reason": "可选生存：健康守卫"
    }
   ],
   "avoid": [],
   "playstyle": "召唤奶流：熟练×8 保证灵魂产出，死之花强化图腾猫治疗；死灵契约+高HP构成生存底线。构筑由中文图鉴站生成，未验证，按实际情况灵活调整。",
   "reroll": ""
  }
 ],
 "icons": {
  "fluffy": "icons/fluffy.png",
  "gluttonous": "icons/gluttonous.png",
  "sacrificial_lamb": "icons/sacrificial_lamb.png",
  "swarm_enforcer": "icons/swarm_enforcer.png",
  "vitality": "icons/vitality.png",
  "vital_drain": "icons/vital_drain.png",
  "adrenaline_fiend": "icons/adrenaline_fiend.png",
  "big_and_lazy": "icons/big_and_lazy.png",
  "big_and_round": "icons/big_and_round.png",
  "cold_blooded": "icons/cold_blooded.png",
  "conductive_armor": "icons/conductive_armor.png",
  "holy_blessing": "icons/holy_blessing.png",
  "iron_skin": "icons/iron_skin.png",
  "last_stand": "icons/last_stand.png",
  "life_leech": "icons/life_leech.png",
  "masochist": "icons/masochist.png",
  "natures_gift": "icons/natures_gift.png",
  "benison_purification": "icons/benison_purification.png",
  "big_and_wrathful": "icons/big_and_wrathful.png",
  "curse_of_wrath": "icons/curse_of_wrath.png",
  "glass_cannon": "icons/glass_cannon.png",
  "healthy_guard": "icons/healthy_guard.png",
  "mass_aspect": "icons/mass_aspect.png",
  "volatile_tenacity": "icons/volatile_tenacity.png",
  "athletic": "icons/athletic.png",
  "eagle_eye": "icons/eagle_eye.png",
  "hawkeye": "icons/hawkeye.png",
  "quick_breath": "icons/quick_breath.png",
  "springfoot": "icons/springfoot.png",
  "swift_hands": "icons/swift_hands.png",
  "leg_day": "icons/leg_day.png",
  "reactive_panic": "icons/reactive_panic.png",
  "smell_the_roses": "icons/smell_the_roses.png",
  "thunder_aura": "icons/thunder_aura.png",
  "berserker_soul_melee": "icons/berserker_soul_melee.png",
  "berserker_soul_ranged": "icons/berserker_soul_ranged.png",
  "big_and_speedy": "icons/big_and_speedy.png",
  "featherweight": "icons/featherweight.png",
  "heavy_hand": "icons/heavy_hand.png",
  "partial_flight": "icons/partial_flight.png",
  "rapid_fire": "icons/rapid_fire.png",
  "way_of_the_law": "icons/way_of_the_law.png",
  "full_focus": "icons/full_focus.png",
  "potent_strike": "icons/potent_strike.png",
  "sorcerers_mastery": "icons/sorcerers_mastery.png",
  "strength": "icons/strength.png",
  "iq_too_high": "icons/iq_too_high.png",
  "clutch_or_kick": "icons/clutch_or_kick.png",
  "cutting_edge": "icons/cutting_edge.png",
  "fire_aspect": "icons/fire_aspect.png",
  "frost_aspect": "icons/frost_aspect.png",
  "greater_focus": "icons/greater_focus.png",
  "luminous_aspect": "icons/luminous_aspect.png",
  "poison_aspect": "icons/poison_aspect.png",
  "shadow_aspect": "icons/shadow_aspect.png",
  "sticky": "icons/sticky.png",
  "charged_strike": "icons/charged_strike.png",
  "flaming_spirit": "icons/flaming_spirit.png",
  "frozen_heart": "icons/frozen_heart.png",
  "pocket_abacus": "icons/pocket_abacus.png",
  "third_law": "icons/third_law.png",
  "warriors_will": "icons/warriors_will.png",
  "ss_proficiency": "icons/ss_proficiency.png",
  "ss_mastery": "icons/ss_mastery.png",
  "ss_burst": "icons/ss_burst.png",
  "ss_swift_stab": "icons/ss_swift_stab.png",
  "ss_shieldbreaker": "icons/ss_shieldbreaker.png",
  "ss_whirlwind": "icons/ss_whirlwind.png",
  "tm_sinistra": "icons/tm_sinistra.png",
  "tm_dextra": "icons/tm_dextra.png",
  "tm_proficiency": "icons/tm_proficiency.png",
  "tm_rush": "icons/tm_rush.png",
  "tm_guarded": "icons/tm_guarded.png",
  "tm_mastery": "icons/tm_mastery.png",
  "tm_wicked_sign": "icons/tm_wicked_sign.png",
  "tm_retaliation": "icons/tm_retaliation.png",
  "gm_overcharged": "icons/gm_overcharged.png",
  "gm_prof_firebomb": "icons/gm_prof_firebomb.png",
  "gm_prof_photon": "icons/gm_prof_photon.png",
  "gm_prof_antimatter": "icons/gm_prof_antimatter.png",
  "gm_sidestep": "icons/gm_sidestep.png",
  "gm_marksman": "icons/gm_marksman.png",
  "gm_mastery": "icons/gm_mastery.png",
  "fm_proficiency": "icons/fm_proficiency.png",
  "fm_mach_punch": "icons/fm_mach_punch.png",
  "fm_mastery": "icons/fm_mastery.png",
  "fm_rage": "icons/fm_rage.png",
  "fm_runner": "icons/fm_runner.png",
  "fm_apply_force": "icons/fm_apply_force.png",
  "sh_prof_jump": "icons/sh_prof_jump.png",
  "sh_prof_chuck": "icons/sh_prof_chuck.png",
  "sh_boosted": "icons/sh_boosted.png",
  "sh_mastery_jump": "icons/sh_mastery_jump.png",
  "sh_mastery_chuck": "icons/sh_mastery_chuck.png",
  "sh_concussion_jump": "icons/sh_concussion_jump.png",
  "sh_concussion_chuck": "icons/sh_concussion_chuck.png",
  "sh_juggernaut_jump": "icons/sh_juggernaut_jump.png",
  "sh_juggernaut_chuck": "icons/sh_juggernaut_chuck.png",
  "sm_proficiency": "icons/sm_proficiency.png",
  "sm_unbreakable": "icons/sm_unbreakable.png",
  "sm_ice_burst": "icons/sm_ice_burst.png",
  "sm_mastery": "icons/sm_mastery.png",
  "sm_rally_up": "icons/sm_rally_up.png",
  "sm_warden": "icons/sm_warden.png",
  "th_keen_eye": "icons/th_keen_eye.png",
  "th_proficiency": "icons/th_proficiency.png",
  "th_mastery": "icons/th_mastery.png",
  "th_splitshot": "icons/th_splitshot.png",
  "th_doping": "icons/th_doping.png",
  "th_everlife": "icons/th_everlife.png",
  "th_splashback": "icons/th_splashback.png",
  "nk_proficiency": "icons/nk_proficiency.png",
  "nk_death_blossom": "icons/nk_death_blossom.png",
  "nk_mastery": "icons/nk_mastery.png",
  "nk_soul_detonation": "icons/nk_soul_detonation.png",
  "nk_necropact": "icons/nk_necropact.png"
 },
 "stats": [
  {
   "id": "maxhp",
   "zh": "最大生命",
   "en": "Max Health",
   "desc": "各职业基础不同；低于 20%（低血量）屏幕变暗、回血声音变小。",
   "soft": null,
   "hard": null
  },
  {
   "id": "regen",
   "zh": "自然回复",
   "en": "Health Regeneration",
   "desc": "基础每 2 秒回 1 HP；受伤延迟 5 秒（受自然回复影响）。",
   "soft": null,
   "hard": null
  },
  {
   "id": "attackspeed",
   "zh": "攻击速度",
   "en": "Attack Speed",
   "desc": "影响主手与多数副手技能频率；攻速越高状态异常触发率略降但总触发更多。",
   "soft": 250,
   "hard": 400,
   "unit": "%"
  },
  {
   "id": "projectilespeed",
   "zh": "弹道速度",
   "en": "Projectile Speed",
   "desc": "影响弹道型技能与升级弹；不影响 hit-scan（VA-11 爆能炮）。",
   "soft": 250,
   "hard": 400,
   "unit": "%"
  },
  {
   "id": "movespeed",
   "zh": "移动速度",
   "en": "Movement Speed",
   "desc": "基础 7m/s；同时提升部分位移技能距离；Haste 可突破上限。",
   "soft": 150,
   "hard": 200,
   "unit": "%"
  },
  {
   "id": "jumpheight",
   "zh": "跳跃高度",
   "en": "Jump Height",
   "desc": "基础 1 米；提升 Spellhammer 跳砸等技能强度。",
   "soft": null,
   "hard": null
  },
  {
   "id": "healingrecv",
   "zh": "受疗",
   "en": "Healing Received",
   "desc": "影响所有来源的治疗（不含自然回复）。",
   "soft": null,
   "hard": 200,
   "unit": "%"
  },
  {
   "id": "critchance",
   "zh": "暴击率",
   "en": "Critical Strike Chance",
   "desc": "暴击时按暴伤倍率结算。",
   "soft": 40,
   "hard": 60,
   "unit": "%"
  },
  {
   "id": "critdmg",
   "zh": "暴击伤害",
   "en": "Critical Strike Damage",
   "desc": "暴击倍率。",
   "soft": null,
   "hard": 385,
   "unit": "%"
  },
  {
   "id": "utilitycd",
   "zh": "辅助技能冷却速率",
   "en": "Utility Cooldown Rate",
   "desc": "影响位移/辅助技能 CD 恢复速度。",
   "soft": 200,
   "hard": 300,
   "unit": "%"
  },
  {
   "id": "defense",
   "zh": "总防御",
   "en": "Overall Defense",
   "desc": "全伤害类型减免，与元素防御乘算；Tank Buster（紫攻击）无视。",
   "soft": 200,
   "hard": null,
   "unit": "%"
  },
  {
   "id": "elemdefense",
   "zh": "元素防御",
   "en": "Elemental Defense",
   "desc": "对应元素伤害减免，与总防御乘算；紫攻击无视。",
   "soft": 200,
   "hard": null,
   "unit": "%"
  },
  {
   "id": "damage",
   "zh": "总伤害",
   "en": "Overall Damage",
   "desc": "所有技能与升级伤害倍率。",
   "soft": null,
   "hard": null
  },
  {
   "id": "knockbackres",
   "zh": "击退抗性",
   "en": "Knockback Resistance",
   "desc": "按比例减少被击退距离。",
   "soft": null,
   "hard": null
  }
 ],
 "status_effects": [
  {
   "en": "BURNING",
   "zh": "灼烧",
   "zh2": "火属性持续伤害"
  },
  {
   "en": "BLEEDING",
   "zh": "出血",
   "zh2": "物理持续伤害"
  },
  {
   "en": "FROZEN / FREEZING",
   "zh": "冰冻",
   "zh2": "冰属性控制/减速"
  },
  {
   "en": "PARALYZED",
   "zh": "麻痹",
   "zh2": "电属性控制"
  },
  {
   "en": "POISONED",
   "zh": "中毒",
   "zh2": "毒持续伤害"
  },
  {
   "en": "BREACHED",
   "zh": "破甲",
   "zh2": "暗属性，防御降低"
  },
  {
   "en": "WEAKENED",
   "zh": "虚弱",
   "zh2": "圣光施加，减伤"
  },
  {
   "en": "FRENZIED",
   "zh": "狂乱",
   "zh2": "攻速/移速提升"
  },
  {
   "en": "HASTE",
   "zh": "急速",
   "zh2": "移速大幅提升"
  },
  {
   "en": "EMPOWERED",
   "zh": "强力",
   "zh2": "伤害提升"
  },
  {
   "en": "GUARDED",
   "zh": "守护",
   "zh2": "减伤"
  },
  {
   "en": "ENFORCED",
   "zh": "坚守",
   "zh2": "防御提升"
  },
  {
   "en": "RESTORATION",
   "zh": "恢复",
   "zh2": "治疗/护盾"
  },
  {
   "en": "INVINCIBLE",
   "zh": "无敌",
   "zh2": "免疫伤害"
  },
  {
   "en": "STOP / GO",
   "zh": "停/行",
   "zh2": "交通法规切换状态"
  },
  {
   "en": "HEAVY",
   "zh": "沉重",
   "zh2": "减速"
  },
  {
   "en": "MORTAL CURSE",
   "zh": "致命诅咒",
   "zh2": "倒地后复活附加；召唤 boss 时移除一次"
  },
  {
   "en": "WEAKENED",
   "zh": "虚弱",
   "zh2": "减伤"
  }
 ],
 "runes": [
  {
   "id": "r_focus",
   "zh": "专注成长",
   "en": "Focus Growth",
   "effect": "暴击率 +10%（每阶段 +10%）",
   "stat": {
    "critchance": 10
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_cleaning",
   "zh": "净化成长",
   "en": "Cleaning Growth",
   "effect": "获得对负面状态的小幅抗性（每阶段提升）",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_recovery",
   "zh": "恢复成长",
   "en": "Recovery Growth",
   "effect": "辅助技能冷却速率 -15%（每阶段 -15%）",
   "stat": {
    "utilitycd": -15
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_power",
   "zh": "力量成长",
   "en": "Power Growth",
   "effect": "总伤害 +10%（每阶段 +10%）",
   "stat": {
    "damage": 10
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_dexterity",
   "zh": "灵巧成长",
   "en": "Dexterity Growth",
   "effect": "攻击速度 +30%（每阶段 +30%）",
   "stat": {
    "attackspeed": 30
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_precision",
   "zh": "精准成长",
   "en": "Precision Growth",
   "effect": "暴击伤害 +15%（每阶段 +15%）",
   "stat": {
    "critdmg": 15
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_health",
   "zh": "生命成长",
   "en": "Health Growth",
   "effect": "最大生命 +15（每阶段 +15）",
   "stat": {
    "maxhp": 15
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_satieity",
   "zh": "饱食成长",
   "en": "Satieity Growth",
   "effect": "受疗 +10%（每阶段 +10%）",
   "stat": {
    "healingrecv": 10
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_defense",
   "zh": "防御成长",
   "en": "Defense Growth",
   "effect": "总防御 +5%（每阶段 +5%）",
   "stat": {
    "defense": 5
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_rejuvenating",
   "zh": "再生成长",
   "en": "Rejuvenating Growth",
   "effect": "自然回复 +150%（每阶段 +150%）",
   "stat": {
    "regen": 150
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_skybound",
   "zh": "天空之跃",
   "en": "Skybound",
   "effect": "额外跳跃 +1（每阶段 +1）",
   "stat": {
    "jumpheight": 0
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_turtle",
   "zh": "龟之道",
   "en": "Way of the Turtle",
   "effect": "最大生命 +20、总防御 +10%、移动速度 -20%（每阶段 +10 HP / +10% 防 / -20% 速）",
   "stat": {
    "maxhp": 20,
    "defense": 10,
    "movespeed": -20
   },
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_activeguard",
   "zh": "主动守护",
   "en": "Active Guard",
   "effect": "使用辅助技能有 5% 概率获得坚守（RESILIENCE）状态（每阶段 +2%）",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_manicgambit",
   "zh": "疯狂赌局",
   "en": "Manic Gambit",
   "effect": "献祭的神器获得其 300% 属性（每阶段 +100%）；每阶段 Token 获取 -1",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_greedy",
   "zh": "贪婪",
   "en": "Big and Greedy",
   "effect": "发现额外 Token 概率 +15%（每阶段 +15%）",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_needy",
   "zh": "需求",
   "en": "Big and Needy",
   "effect": "购买普通升级后返还 Token 概率 +15%（每阶段 +5%）",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_picky",
   "zh": "挑剔",
   "en": "Big and Picky",
   "effect": "升级选择时额外 +1 选项；重掷次数 +1（每阶段 +1 重掷）",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  },
  {
   "id": "r_insured",
   "zh": "保险",
   "en": "Big and Insured",
   "effect": "开局获得 1 Token（Antumbral+ 阶段每阶段 +1）；重掷次数 +1",
   "stat": {},
   "curse": "随机 1 种符文诅咒 ×1"
  }
 ],
 "curses": [
  {
   "id": "c_fragility",
   "zh": "脆弱",
   "en": "Fragility",
   "effect": "物理防御 -9%/层"
  },
  {
   "id": "c_smolder",
   "zh": "阴燃",
   "en": "Smolder",
   "effect": "火元素防御 -9%/层"
  },
  {
   "id": "c_fever",
   "zh": "高热",
   "en": "Fever",
   "effect": "冰元素防御 -9%/层"
  },
  {
   "id": "c_conductor",
   "zh": "导体",
   "en": "Conductor",
   "effect": "电元素防御 -9%/层"
  },
  {
   "id": "c_profane",
   "zh": "亵渎",
   "en": "Profane",
   "effect": "圣光防御 -9%/层"
  },
  {
   "id": "c_divine",
   "zh": "神圣",
   "en": "Divine",
   "effect": "暗影防御 -9%/层"
  },
  {
   "id": "c_rot",
   "zh": "腐败",
   "en": "Rot",
   "effect": "毒元素防御 -9%/层"
  },
  {
   "id": "c_tremor",
   "zh": "震颤",
   "en": "Tremor",
   "effect": "弹道散布 +2.5%/层"
  },
  {
   "id": "c_drain",
   "zh": "汲取",
   "en": "Drain",
   "effect": "最大生命 -10/层"
  },
  {
   "id": "c_shedding",
   "zh": "蜕皮",
   "en": "Shedding",
   "effect": "总防御 -5%/层"
  },
  {
   "id": "c_anaemia",
   "zh": "贫血",
   "en": "Anaemia",
   "effect": "自然回复 -150%/层"
  },
  {
   "id": "c_hypoxia",
   "zh": "缺氧",
   "en": "Hypoxia",
   "effect": "受疗 -10%/层"
  },
  {
   "id": "c_light",
   "zh": "轻盈",
   "en": "Light",
   "effect": "受到击退 +15%/层"
  },
  {
   "id": "c_asthma",
   "zh": "哮喘",
   "en": "Asthma",
   "effect": "辅助冷却速率 +15%/层"
  }
 ],
 "artifacts": [
  {
   "id": "a_archive",
   "zh": "加密档案",
   "en": "Encrypted Archive",
   "effect": "辅助冷却速率 -5%、移动速度 +5%",
   "star": 3,
   "stat": {
    "utilitycd": -5,
    "movespeed": 5
   }
  },
  {
   "id": "a_sun",
   "zh": "太阳圣杯",
   "en": "Goblet of the Sun",
   "effect": "圣光伤害 +8%、暗影防御 +8%",
   "star": 1,
   "stat": {
    "damage": 0
   }
  },
  {
   "id": "a_armor",
   "zh": "HC 装甲板",
   "en": "HC Armor Plating",
   "effect": "物理防御 +7%（最终 Boss 为 Jim C. Bringer，物防几乎必定有用）",
   "star": 2,
   "stat": {
    "defense": 7
   }
  },
  {
   "id": "a_cinders",
   "zh": "余烬之心",
   "en": "Heart of Cinders",
   "effect": "元素防御 +6%（后期 Boss 高元素伤害）",
   "star": 2,
   "stat": {
    "elemdefense": 6
   }
  },
  {
   "id": "a_malice",
   "zh": "恶意精华",
   "en": "Essence of Malice",
   "effect": "暗影伤害 +6%、圣光防御 +6%",
   "star": 2,
   "stat": {
    "damage": 0
   }
  },
  {
   "id": "a_wheel",
   "zh": "轮回之轮",
   "en": "Wheel of Reincarnation",
   "effect": "受疗 +3%、最大生命 +5",
   "star": 3,
   "stat": {
    "healingrecv": 3,
    "maxhp": 5
   }
  },
  {
   "id": "a_megium",
   "zh": "封印宝石",
   "en": "Sealed Megium",
   "effect": "总伤害 +3%（无视职业，几乎总是好选择）",
   "star": 3,
   "stat": {
    "damage": 3
   }
  }
 ],
 "stat_effects": {
  "fluffy": {
   "maxhp": 10.0
  },
  "gluttonous": {
   "healingrecv": 5.0
  },
  "swarm_enforcer": {
   "defense": 1.5
  },
  "vitality": {
   "regen": 80.0
  },
  "adrenaline_fiend": {
   "utilitycd": 7.0,
   "healingrecv": -15.0
  },
  "big_and_round": {
   "knockbackres": 50.0,
   "maxhp": 30.0,
   "jumpheight": -10.0,
   "movespeed": -10.0
  },
  "cold_blooded": {
   "defense": -15.0
  },
  "conductive_armor": {
   "defense": 20.0,
   "elemdefense": -5.0
  },
  "holy_blessing": {
   "defense": 15.0,
   "damage": -10.0
  },
  "iron_skin": {
   "defense": 8.0,
   "movespeed": -3.0,
   "damage": -2.0
  },
  "life_leech": {
   "damage": 1.0,
   "regen": -50.0,
   "healingrecv": -20.0
  },
  "masochist": {
   "defense": -15.0
  },
  "benison_purification": {
   "defense": -5.0
  },
  "curse_of_wrath": {
   "defense": -20.0
  },
  "glass_cannon": {
   "damage": 30.0
  },
  "mass_aspect": {
   "movespeed": -30.0,
   "maxhp": 75
  },
  "athletic": {
   "movespeed": 8.0
  },
  "eagle_eye": {
   "projectilespeed": 35.0
  },
  "quick_breath": {
   "utilitycd": 10.0
  },
  "springfoot": {
   "jumpheight": 20.0
  },
  "swift_hands": {
   "attackspeed": 15.0
  },
  "leg_day": {
   "movespeed": 5.0,
   "jumpheight": 10.0
  },
  "thunder_aura": {
   "damage": -10.0,
   "movespeed": -5.0
  },
  "berserker_soul_melee": {
   "damage": -20.0,
   "attackspeed": -40.0
  },
  "berserker_soul_ranged": {
   "damage": -10.0,
   "attackspeed": -20.0
  },
  "big_and_speedy": {
   "utilitycd": 50.0,
   "defense": -20.0
  },
  "featherweight": {
   "movespeed": 30.0,
   "defense": -20.0
  },
  "heavy_hand": {
   "damage": 30.0,
   "attackspeed": -40.0
  },
  "rapid_fire": {
   "attackspeed": 50.0,
   "damage": -20.0
  },
  "full_focus": {
   "critchance": 5.0,
   "critdmg": 5.0
  },
  "sorcerers_mastery": {
   "damage": 8.0
  },
  "strength": {
   "damage": 10.0
  },
  "iq_too_high": {
   "damage": 25.0,
   "projectilespeed": -15.0,
   "attackspeed": -10.0
  },
  "cutting_edge": {
   "defense": -5.0
  },
  "fire_aspect": {
   "defense": -10.0,
   "damage": 15.0
  },
  "frost_aspect": {
   "defense": -10.0,
   "damage": 15.0
  },
  "greater_focus": {
   "critdmg": 3.0
  },
  "luminous_aspect": {
   "damage": 15.0,
   "defense": 15.0,
   "elemdefense": -5.0
  },
  "poison_aspect": {
   "damage": 15.0,
   "defense": 15.0,
   "healingrecv": -5.0
  },
  "shadow_aspect": {
   "damage": 15.0,
   "defense": -10.0
  },
  "charged_strike": {
   "critchance": -5.0
  },
  "flaming_spirit": {
   "healingrecv": -5.0,
   "regen": -20.0
  },
  "frozen_heart": {
   "healingrecv": -5.0,
   "regen": -20.0
  },
  "pocket_abacus": {
   "critdmg": 10.0,
   "damage": -10.0
  },
  "warriors_will": {
   "utilitycd": -15.0,
   "damage": 25
  },
  "ss_mastery": {
   "regen": -100.0
  },
  "ss_burst": {
   "attackspeed": 50.0
  },
  "ss_swift_stab": {
   "damage": 35.0
  },
  "ss_shieldbreaker": {
   "damage": 25.0
  },
  "tm_sinistra": {
   "damage": -3.0,
   "attackspeed": -3.0
  },
  "tm_dextra": {
   "damage": -3.0,
   "attackspeed": -3.0
  },
  "tm_mastery": {
   "damage": 25.0
  },
  "gm_overcharged": {
   "damage": 15.0
  },
  "gm_prof_firebomb": {
   "damage": 7.0
  },
  "gm_prof_photon": {
   "damage": 7.0
  },
  "gm_prof_antimatter": {
   "damage": 7.0
  },
  "gm_marksman": {
   "damage": 400.0
  },
  "gm_mastery": {
   "damage": 50.0
  },
  "fm_rage": {
   "attackspeed": 1.0
  },
  "sh_prof_chuck": {
   "damage": 8.0
  },
  "sh_boosted": {
   "damage": 10.0
  },
  "sm_unbreakable": {
   "damage": -5.0
  },
  "th_splitshot": {
   "damage": -30.0
  },
  "nk_death_blossom": {
   "damage": -3.0
  },
  "nk_mastery": {
   "damage": 2.0,
   "regen": 20.0
  },
  "way_of_the_law": {
   "movespeed": 20
  },
  "hawkeye": {
   "projectilespeed": 10
  },
  "big_and_lazy": {
   "regen": 50
  }
 },
 "changelog": [
  {
   "version": "v0.51",
   "date": "2026-07-29",
   "title": "Ecliptica Demo Playtest Changelog",
   "items": [
    {
     "cls": "Spellsword",
     "zh": "剑术家",
     "items": [
      "熟练：主手命中 2.5% 概率叠狂乱（最大 5 层）",
      "破盾者：念力斩额外 +25% 伤害",
      "奥义：新增自然回复 -100% 代价；出血回血 1→2",
      "熟练：穿刺打击射程 5m→4m"
     ]
    },
    {
     "cls": "Twinmage",
     "zh": "双法师",
     "items": [
      "圣光球基础伤害 50→35"
     ]
    },
    {
     "cls": "Gunmancer",
     "zh": "枪术士",
     "items": [
      "光子凝聚器熟练：蓄力附加弹数 +1→+2"
     ]
    },
    {
     "cls": "Fistmage",
     "zh": "拳法师",
     "items": [
      "激昂：加速最大 10 层起，每升级 +2",
      "跑者：叠乘倍率下调"
     ]
    },
    {
     "cls": "Shield Mage",
     "zh": "盾法师",
     "items": [
      "盾冲 CD 恢复 4 秒",
      "守望者：辅助 CD 惩罚 100%→50%",
      "守望者恢复不再干扰拳法师格挡"
     ]
    },
    {
     "cls": "Spellhammer",
     "zh": "法锤士",
     "items": [
      "投掷熟练：新增附加爆炸伤害（0.5m 起，每层 +0.5m）",
      "主手锤击 110→90",
      "投掷主宰：强力最大 5 层，每升级 +2",
      "主手挥击移速仅受移速影响（不再受攻速）",
      "投掷熟练伤害加成调整",
      "爆散空中可充能（更慢），着地恢复"
     ]
    },
    {
     "cls": "Thaumaturge",
     "zh": "咒术师",
     "items": [
      "毒面相受疗 -15%→-5%",
      "兴奋剂：守护有上限；自我 buff 最大 3 层",
      "（静默）兴奋剂：痛苦交换 CD +15%",
      "熟练：痛苦交换 CD 缩短 15%→10%",
      "自我治疗时 CD 恢复慢 75%",
      "分裂射击扩散修正 +2.5%"
     ]
    },
    {
     "cls": "Nekomancer",
     "zh": "猫术士",
     "items": [
      "僵尸猫初始 5% 概率破甲",
      "僵尸猫暗伤 15→25",
      "魂爆半径基础 +2m，每层 +1.5m",
      "图腾猫 HP 调整；回血变慢；不再叠加（同时只吃 1 个图腾奶）"
     ]
    },
    {
     "cls": "Stage",
     "zh": "关卡",
     "items": [
      "Boss 战开传送门时全队回满血"
     ]
    },
    {
     "cls": "Runes",
     "zh": "符文",
     "items": [
      "巨大欲望基础 20%→15%（每层 +5%）",
      "巨大贪婪基础 20%→15%（每层 +15%）"
     ]
    },
    {
     "cls": "Upgrades",
     "zh": "升级",
     "items": [
      "单排：背水一战（Clutch or Kick）与献祭羔羊不再出现在商店",
      "第三定律：拳法师格挡也触发（反弹固定 50%）；新增范围光环显示",
      "狂战士之魂拆分为近战/远程两版",
      "狂战士之魂（近战）代价由移速改为自然回复 -50%",
      "狂战士之魂（远程）代价由移速改为弹道扩散 +2%"
     ]
    }
   ]
  }
 ],
 "difficulties": [
  {
   "en": "Primal",
   "zh": "原始"
  },
  {
   "en": "Penumbra",
   "zh": "半影"
  },
  {
   "en": "Antumbra",
   "zh": "环影"
  },
  {
   "en": "Umbra",
   "zh": "本影"
  },
  {
   "en": "Eclipse",
   "zh": "日蚀"
  },
  {
   "en": "Eye of the Eclipse",
   "zh": "日蚀之眼"
  }
 ],
 "flow": [
  "选择职业 → 大厅高台全员集合开始 Run",
  "战斗阶段：清理小怪（提示收集 3 个 Token，位置随机）",
  "准备阶段：收集神器献祭给中央祭坛（此阶段获得加速状态，趁机捡 Token）",
  "Boss 阶段：击杀 Boss（v0.51 起开门时全队满血）",
  "休憩阶段（世界狭间）：用 Token 购买升级（3 个商店 + 1 次免费重随）；可花 95% Token 在日蚀处换职业（每 3 轮 1 次）"
 ],
 "game_mechanics": [
  "难度：Primal→Penumbra→Antumbra→Umbra→Eclipse→Eye of the Eclipse；随进度解锁，决定小怪/Boss 池",
  "Token（蓝水晶）：局内拾取（每局固定 3 个，扣除符文增减）；未用完可存留",
  "进度平衡：加入别人房间时会按进度补发 Token",
  "升级购买后商店自动刷新，可重复购买同一技能",
  "单排时：背水一战（Clutch or Kick）与献祭羔羊（Sacrificial Lamb）不会出现",
  "Flaming Spirit 与 Frozen Heart 互斥（二者只能取其一）",
  "倒地（0 HP）：可被队友以 50% 最大生命复活（健康守护可降至 25%）；复活获得致命诅咒（召唤 Boss 时移除一次）"
 ]
};
