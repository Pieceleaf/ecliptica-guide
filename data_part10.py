# -*- coding: utf-8 -*-
# Boss 与敌人图鉴数据（来源：Ecliptica 英文 wiki Miraheze，2026-08-04 抓取）
BOSSES = [
 {
  "id": "maxipuss",
  "name": "Maxipuss",
  "lore": "Maxipuss is the beloved cat of Milean, the humble owner of the Brewsal's famous Milean Restaurant. His namesake comes from his love of eating rats. Very few know of Maxipuss' true form, that being his owner and only a few select patrons of the restaurant. Most bothersome customers leave the restaurant with a hazy memory and a ton of bruises.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n|+\n| colspan=\"3\" |\nMaxipuss\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.7x)\n|-\n|SHADOW\n|WEAK (1.3x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 5300\n|-\n| colspan=\"3\" |Damage: PHYSICAL\n|-\n| colspan=\"3\" |Can inflict: POISONED\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nThe Maxipuss battle consists of 1 phase.\n\nFor close range, Maxipuss has simple punch attacks, as well as an introductory grapple.\n\nFor targets at a distance, Maxipuss may throw a hairball or leap.\n\n== Credits ==\nMade by Have, Scena and Mantibro\n\nMusic:",
  "strategy": "The Maxipuss battle consists of 1 phase.\n\nFor close range, Maxipuss has simple punch attacks, as well as an introductory grapple.\n\nFor targets at a distance, Maxipuss may throw a hairball or leap.\n\n== Credits ==\nMade by Have, Scena and Mantibro\n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.25
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.7
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.3
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "5300",
  "damage": "PHYSICAL",
  "inflicts": "POISONED",
  "phases": "1",
  "desc": "The Rodent Hunter",
  "phase": "Prime",
  "icon": "icons/boss/Maxipuss_Icon.png",
  "zh_mech": "1 阶段。近战：简单拳击 + 起手抓取；远程目标：吐毛球或扑击。",
  "zh_tips": "近战注意抓取起手前摇；远程保持移动闪避毛球与扑击。弱冰（×1.25）、弱暗（×1.3），光属性伤害被抵抗（×0.7），别用光打。",
  "dmg_zh": "物理"
 },
 {
  "id": "darkmouth",
  "name": "Darkmouth",
  "lore": "A species of marsh-dwelling predators, believed to have evolved from burrowing sandworms. The dunes they used to reside in were considered low risk, and as such was used to train rookie mages in the use of gravity magic, taking advantage of the abundance of lightweight sand and soil for easy results.\n\nDue to continuous magic accumulation in the surroundings, the sand became saturated with the gravity particles, and developed a sort of natural levitation. The worms ate it regularly while tunnelling, and become light and lighter, evolving to rely less on raw strength and eventually becoming airborne altogether.\n\nConveniently, this new shape of theirs made them a great opportunity for mages to use as target practice.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Darkmouth\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.5x)\n|-\n|POISON\n|WEAK (1.5x)\n|-\n| colspan=\"3\" |Base HP: 4200\n|-\n| colspan=\"3\" |Damage: PHYSICAL and POISON\n|-\n| colspan=\"3\" |Can inflict: POISONED\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nDarkmouth is a simple flying battle consisting of 2 attacks while it attempts to keep a distance from its opponent. The first is a volley of poisonous projectiles that have a chance to inflict the poison debuff on contact. The other is a charge towards its target dealing significantly more damage. While it most often alternates its attacks it can occasionally change its pattern and timing in an attempt to catch its opponents off guard.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "strategy": "Darkmouth is a simple flying battle consisting of 2 attacks while it attempts to keep a distance from its opponent. The first is a volley of poisonous projectiles that have a chance to inflict the poison debuff on contact. The other is a charge towards its target dealing significantly more damage. While it most often alternates its attacks it can occasionally change its pattern and timing in an attempt to catch its opponents off guard.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.5
   },
   "POISON": {
    "status": "WEAK",
    "mult": 1.5
   }
  },
  "hp": "4200",
  "damage": "PHYSICAL and POISON",
  "inflicts": "POISONED",
  "phases": "1",
  "desc": "Eater of Fields",
  "phase": "Prime",
  "icon": "icons/boss/DarkMouth_Icon.png",
  "zh_mech": "飞行 Boss，1 阶段，2 种招式：毒弹幕（接触几率中毒）与冲锋（显著高伤）。通常交替出招，偶尔改变节奏与时机。",
  "zh_tips": "躲毒弹幕、警惕冲锋变奏；中毒后注意净化或回复。弱冰/弱暗，光被抵抗。",
  "dmg_zh": "物理、毒"
 },
 {
  "id": "kakarot",
  "name": "Kakarot",
  "lore": "The carrot emerges from the soil of its own volition, and stands before the Plantsman. The Plantsman keels down closer to the new sprout, petting it on the leaf.\n\n\"You're smaller than I expected, but this can still work. You see these fields? This is your home. Our home. Storms are brewing, and there are bad things out there that want to hurt out home. I need you to protect it while I'm gone. Can you do this?\"\n\nThe carrot churns, it's fist launching forward and connecting with the Being before it. The Plantsman chuckles loudly. Yes, you will make for a fine keeper.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Kakarot\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|NEUTRAL (1x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 5800\n|-\n| colspan=\"3\" |Damage: PHYSICAL \n|-\n| colspan=\"3\" |Can inflict: -\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nThe Kakarot battle consists of 1 phase.\n\nKakarot will alternate between a powerful forward slam, and a spread of small AoEs around him\n\nFor targets at a distance, Kakarot may throw rocks or leap upwards with low accuracy.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "strategy": "The Kakarot battle consists of 1 phase.\n\nKakarot will alternate between a powerful forward slam, and a spread of small AoEs around him\n\nFor targets at a distance, Kakarot may throw rocks or leap upwards with low accuracy.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "5800",
  "damage": "PHYSICAL",
  "inflicts": "-",
  "phases": "1",
  "desc": "Keeper of the Garden",
  "phase": "Prime",
  "icon": "icons/boss/Kakarot_Icon.png",
  "zh_mech": "1 阶段。交替使用强力前砸与周身小范围 AOE 散开；远程目标会被丢石头或低准度跃起。",
  "zh_tips": "近战注意前砸前摇，别贴脸站桩；远程躲石头即可。查看克制表选择输出属性。",
  "dmg_zh": "物理"
 },
 {
  "id": "nan",
  "name": "NaN",
  "lore": "The Nanite Autonomous Non-Conglomerate is a self-sufficient defense system which is a collection of synergistic nanomachines which form together in arbitrary configurations, able to adapt its combat capabilities actively.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |NaN\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|NEUTRAL (1x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 5300\n|-\n| colspan=\"3\" |Damage: FIRE, FROST, ELECTRIC, LUMINOUS AND SHADOW\n|-\n| colspan=\"3\" |Can inflict: BURNING, FROZEN, PARALYZED, WEAKENED and BREACHED\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nNaN is a machine capable of switching into 4 different modes each presenting their own difficulty and vulnerability.\n\nWhen switching to fire, NaN becomes vulnerable to fire damage and periodically shoots a projectile at its target with a chance to burn them.\n\nWhen switching to frost, NaN becomes vulnerable to frost damage and fires bursts of projectiles at its targets with a chance to freeze them.\n\nWhen switching to electric, NaN becomes vulnerable to electric damage and launches bolts into the sky which crash down in small AOE's with a chance to paralyze its targets.\n\nWhen switching to shadow and light, NaN can fire either a spiral of shadow projectiles applying breach or a line of light projectiles applying weak to its targets. Notably it is not weak to either shadow or light in this form as it adopts both opposing elements.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "strategy": "NaN is a machine capable of switching into 4 different modes each presenting their own difficulty and vulnerability.\n\nWhen switching to fire, NaN becomes vulnerable to fire damage and periodically shoots a projectile at its target with a chance to burn them.\n\nWhen switching to frost, NaN becomes vulnerable to frost damage and fires bursts of projectiles at its targets with a chance to freeze them.\n\nWhen switching to electric, NaN becomes vulnerable to electric damage and launches bolts into the sky which crash down in small AOE's with a chance to paralyze its targets.\n\nWhen switching to shadow and light, NaN can fire either a spiral of shadow projectiles applying breach or a line of light projectiles applying weak to its targets. Notably it is not weak to either shadow or light in this form as it adopts both opposing elements.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "5300",
  "damage": "FIRE, FROST, ELECTRIC, LUMINOUS AND SHADOW",
  "inflicts": "BURNING, FROZEN, PARALYZED, WEAKENED and BREACHED",
  "phases": "1",
  "desc": "An Elemental Machine",
  "phase": "Prime",
  "icon": "icons/boss/NaN_Icon.png",
  "zh_mech": "元素机器，可切换 4 种模式，各模式对应不同弱点与攻击：火模式弱火（周期射弹、几率灼烧）；冰模式弱冰（弹幕、几率冻结）；电模式弱电（发射闪电）；光/暗模式对应光/暗攻击。",
  "zh_tips": "注意模式切换——当前模式即弱点（用对应属性打），同时躲避对应弹幕与异常。",
  "dmg_zh": "火、冰、雷、光、暗"
 },
 {
  "id": "beelzebub",
  "name": "Beelzebub",
  "lore": "Beelzebub The Astonishing.\n\nAn incredible evolution from the Peltapod sub-species which generally are made to fly and live a short life, this specimen appears to be insanely durable and intelligent as it's presence is made very clear as it descends and mimics what appears to be some sort of human opera song.\n\nIt is said that when encountering the Peltapod Queen near this specimen it will mimic human flexing poses and show off it's massive arm muscles, while its legs may appear feeble this creature can close distances between targets in a short amount of time and channel a deadly beam of light to incinerate its prey.\n\nFlies are, in almost all cases, destined to die. The turbulence of dimensional instability often sends flies into places they're just not able to survive in. In almost every dimension, even the lowest of creatures can capture and consume the flies for a sweet treat. However, in exceptionally rare cases, luck may grace a fly with a fighting chance.\n\nBeelzebub was one very lucky fly. Tossed into a realm of Abundance, it was allowed to feast and grow strong without any competition whatsoever. With his newfound strength, he seeks what no other fly has sought out before, to rule.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Beelzebub\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.5x)\n|-\n|POISON\n|RESIST (0.5x)\n|-\n| colspan=\"3\" |Base HP: 5200\n|-\n| colspan=\"3\" |Damage: PHYSICAL and POISON\n|-\n| colspan=\"3\" |Can inflict: POISONED\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nThe Beelzebub battle consists of 1 phase.\n\nBeelzebub is able to summon flies to help him in battle. At 50% HP,  flies will spawn automatically. \n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "strategy": "The Beelzebub battle consists of 1 phase.\n\nBeelzebub is able to summon flies to help him in battle. At 50% HP,  flies will spawn automatically. \n\n== Credits ==\nMade by Have and Mantibro\n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.5
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.5
   }
  },
  "hp": "5200",
  "damage": "PHYSICAL and POISON",
  "inflicts": "POISONED",
  "phases": "1",
  "desc": "Lord of the Flies",
  "phase": "Prime",
  "icon": "icons/boss/BeelzebubIcon.png",
  "zh_mech": "1 阶段。可召唤苍蝇助战；50% HP 时自动开始刷苍蝇。",
  "zh_tips": "50% 血量后留意苍蝇骚扰，留 AOE/清怪手段处理。弱冰/弱暗。",
  "dmg_zh": "物理、毒"
 },
 {
  "id": "buff_noob",
  "name": "Buff Noob",
  "lore": "He was small. Thin as can be. Even smaller than you. Or even I.\n\nThey mocked him. Pointed fingers at him. Called him a Noob.\n\nHe had enough.\n\nHe curled iron. He honed his muscles. He grew very strong.\n\nIn mere seconds.\n\nHe was huge. Shredded as can be. Even larger that you. And even I.\n\nSteel sharpens steel. He seeks them out. Weak creatures all around.\n\nCan you lift?\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Buff Noob\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.25x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.5x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 4800\n|-\n| colspan=\"3\" |Damage: PHYSICAL \n|}\n\n== Strategy ==\nThe Buff Noob fight is the first to introduce purple attacks in the form of powerful ass claps that pierce his opponents defenses. He focuses on getting close to his enemies and delivering several blows to take them down. When around 40% HP he will consume one of his two items: Pizza or Bloxy Cola, healing him and granting him either enforced or empowered respectively. He will do this action again when reaching the HP threshold, consuming whichever item remains.\n\n== Credits ==\nMade by Mantibro\n\nMusic: \n\nBuff Noob is from ROBLOX\n\n== Statistics ==\nBase HP: 4800\n\nDamage: PHYSICAL\n\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity !! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n| PHYSICAL|| NEUTRAL (1x)\n|-\n| FIRE|| NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.25x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.5x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "strategy": "The Buff Noob fight is the first to introduce purple attacks in the form of powerful ass claps that pierce his opponents defenses. He focuses on getting close to his enemies and delivering several blows to take them down. When around 40% HP he will consume one of his two items: Pizza or Bloxy Cola, healing him and granting him either enforced or empowered respectively. He will do this action again when reaching the HP threshold, consuming whichever item remains.\n\n== Credits ==\nMade by Mantibro\n\nMusic: \n\nBuff Noob is from ROBLOX\n\n== Statistics ==\nBase HP: 4800\n\nDamage: PHYSICAL\n\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity !! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n| PHYSICAL|| NEUTRAL (1x)\n|-\n| FIRE|| NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.25x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.5x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "WEAK",
    "mult": 1.25
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.5
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "4800",
  "damage": "PHYSICAL",
  "inflicts": "",
  "phases": "",
  "desc": "Can You Lift?",
  "phase": "Prime",
  "icon": "icons/boss/Buff_Noob_Icon.png",
  "zh_mech": "首个拥有紫色攻击的 Boss：强力拍击无视防御。倾向贴近连续击打。约 40% HP 时吃道具回血（披萨=Enforced 强制增伤 / 可乐=Empowered 强化），同一阈值再吃剩下一个。",
  "zh_tips": "看到紫色蓄力立刻远离（无视防御）；40% 附近注意他会回血，别放松输出。",
  "dmg_zh": "物理"
 },
 {
  "id": "vesra",
  "name": "Vesra",
  "lore": "The Queen and protector of the Peltapod Colony. Having been exiled from their home habitat due to dimensional instability, Vesra has grown extremely territorial and violently protective of her offspring. Due to the harsh conditions brought about by being a species of dimensional interlopers, Queen Vesra's body has adapted into a more combat-focused form, with sleek body parts.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Vesra\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.5x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|RESIST (0.5x)\n|-\n| colspan=\"3\" |Base HP: 4800\n|-\n| colspan=\"3\" |Damage: PHYSICAL \n|-\n| colspan=\"3\" |Can inflict: BLEEDING\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nThe Vesra battle consists of 2 sub-phases, a regular form and a cocooned form. Vesra will become immune to all damage while within the cocoon.\n\nIn her regular form, Vesra will alternate between a grounded and airborne moveset. At 50% HP, Vesra will transfer into her cocoon state, spawning a single Peltapod Guard and then spawning regular peltapods in set intervals. Once the Peltapod Guard is slain, she will exit the cocoon and return to her regular form.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic: \n\n== Fun Facts ==\nVesra was named after one of the contributors for Ecltipica: VesraVampire",
  "strategy": "The Vesra battle consists of 2 sub-phases, a regular form and a cocooned form. Vesra will become immune to all damage while within the cocoon.\n\nIn her regular form, Vesra will alternate between a grounded and airborne moveset. At 50% HP, Vesra will transfer into her cocoon state, spawning a single Peltapod Guard and then spawning regular peltapods in set intervals. Once the Peltapod Guard is slain, she will exit the cocoon and return to her regular form.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic: \n\n== Fun Facts ==\nVesra was named after one of the contributors for Ecltipica: VesraVampire",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.5
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.5
   }
  },
  "hp": "4800",
  "damage": "PHYSICAL",
  "inflicts": "BLEEDING",
  "phases": "1",
  "desc": "Grand Matriarch of Peltapods",
  "phase": "Late Prime",
  "icon": "icons/boss/Vesra_Icon.png",
  "zh_mech": "2 子阶段：常规形态 + 结茧形态（茧内对全部伤害免疫）。常规形态交替使用地面/空中招式；50% HP 进入结茧，召唤 1 只 Peltapod Guard 并定期刷 Peltapod；击杀 Guard 后破茧回到常规形态。",
  "zh_tips": "50% 后优先集火 Peltapod Guard 破茧，别把输出浪费在免疫的茧上。",
  "dmg_zh": "物理"
 },
 {
  "id": "pride",
  "name": "Pride",
  "lore": "Pride himself, while not notably strong in combat prowess, has an incredibly potent magical aura that lingers long after he has visited a realm. This magical aura is not damaging in any way, and has actually been shown to drastically increase one's mood. While this may seem like a good thing, some leading scholars and magical minds believe it's some sort of mind control. Whether or not this is true has never been confirmed, as Pride always escapes questioning by flying away with his umbrella.\n\nThe combat abilities he does possess don't actually deal any physical damage to it's target, rather they cause an unfathomably intense rush of endorphins. This effect is far stronger than any illicit substances you can find in the market, unless you know a guy.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Pride\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.25x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|RESIST (0.5x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 4600\n|-\n| colspan=\"3\" |Damage: PHYSICAL and LUMINOUS\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and WEAKENED\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nPride mainly focuses on presenting to the area around him rather than an individual target. Many of his attacks spawn heart projectiles which circle around him while he preforms his move set, catching his opponents off guard. He also has the ability to preform 2 different types of beams, one that he summons in front of him and another that comes from his umbrella.\n\nAt any point Pride can decide to fly into the air spawning a swarm of heart projectiles and firing more at his opponents on the ground, following them at a close distance.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by Scena \n\nMusic:",
  "strategy": "Pride mainly focuses on presenting to the area around him rather than an individual target. Many of his attacks spawn heart projectiles which circle around him while he preforms his move set, catching his opponents off guard. He also has the ability to preform 2 different types of beams, one that he summons in front of him and another that comes from his umbrella.\n\nAt any point Pride can decide to fly into the air spawning a swarm of heart projectiles and firing more at his opponents on the ground, following them at a close distance.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by Scena \n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "WEAK",
    "mult": 1.25
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "RESIST",
    "mult": 0.5
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "4600",
  "damage": "PHYSICAL and LUMINOUS",
  "inflicts": "BLEEDING and WEAKENED",
  "phases": "1",
  "desc": "Prideful of Power",
  "phase": "Late Prime",
  "icon": "icons/boss/Pride_Icon.png",
  "zh_mech": "以自身周围 AOE 为主而非单体。多数招式附带环绕心形弹幕；两种光束（面前召唤 / 从伞发射）；可随时飞空撒大量心形弹幕并继续对地射击。",
  "zh_tips": "注意环绕心弹别被蹭到；两种光束前摇不同需分别辨认；飞空阶段保持移动。",
  "dmg_zh": "物理、光"
 },
 {
  "id": "steven",
  "name": "Steven",
  "lore": "Have you ever noticed how often inanimate objects are there for you? Your bed has never gotten up and ran away, your sword will never try to escape your hand, and your mug will always hold your drink. While some may just call this common sense, it comes across different to some. Steven, in his darkest hour, had an epiphany. Pancakes had always been there for him. For his hunger, for his bad nights, and if he just needed someone to talk to. The pancakes never abandoned him. And so Steven adorned Michael, his favorite pancake, upon his face, and swore to protect the place where he belongs.\n\nSteven has no elevated abilities, no combat training, no abnormal magical attunement beyond the norm, nothing. The most likely conclusion we can draw here is that the pancake named Michael is itself, magical, and is channeling its power through Steven. Beyond any logic, it seems the will of the pancakes gives him the strength that rivals that of intermediate combat parties. Knight Major Jerosh suggested training dungeon delving troops under similar \"pancake conditions\", and was dishonorably discharged.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Steven\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.75x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.5x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 8600\n|-\n| colspan=\"3\" |Damage: PHYSICAL and FIRE\n|-\n| colspan=\"3\" |Can inflict: BLEEDING, STICKY and BURNING\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Steven battle consists of 2 sub-phases, a regular form and an enflamed form.\n\nWhile in regular form, Steven will throw out high damaging slashes, as well as deploying puddles of syrup. Standing in the Syrup will apply stacks of the Sticky debuff.\n\nAt 50% HP, Steven will transition into his enflamed state, enhancing all of his moves with additional Fire damage and a chance to proc the Burn debuff. His syrup move also shoots many more puddles.\n\n== Credits ==\nMade by Mr. Nobody, Scena and Mantibro \n\nVoiced by Ace45677 \n\nMusic:",
  "strategy": "The Steven battle consists of 2 sub-phases, a regular form and an enflamed form.\n\nWhile in regular form, Steven will throw out high damaging slashes, as well as deploying puddles of syrup. Standing in the Syrup will apply stacks of the Sticky debuff.\n\nAt 50% HP, Steven will transition into his enflamed state, enhancing all of his moves with additional Fire damage and a chance to proc the Burn debuff. His syrup move also shoots many more puddles.\n\n== Credits ==\nMade by Mr. Nobody, Scena and Mantibro \n\nVoiced by Ace45677 \n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.75
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.25
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.5
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "8600",
  "damage": "PHYSICAL and FIRE",
  "inflicts": "BLEEDING, STICKY and BURNING",
  "phases": "2",
  "desc": "Protector of the Pancakes",
  "phase": "Penumbra",
  "icon": "icons/boss/Steven_Icon.png",
  "zh_mech": "2 子阶段：常规 + 火焰形态。常规：高伤斩击 + 糖浆池（踩中叠 Sticky 粘滞）。50% HP 转火焰形态：全部招式附加火伤并几率灼烧，糖浆数量大增。",
  "zh_tips": "别踩糖浆（粘滞减速）；50% 后注意灼烧与更大范围糖浆。",
  "dmg_zh": "物理、火"
 },
 {
  "id": "kodama",
  "name": "Kodama",
  "lore": "A curse Incarnate. They say that the forests are alive. The trees and animals are alive of course, but the larger whole is alive as well. The forest enjoys the lushness of life at dawn, but by dusk, it works. To seek out and remove any poison infecting its roots, so that the day may be ever brighter. To those who wander into these systems after nightfall, pray that your spirit is clean. For if it is not, it shall be.\nThose who are lost should be wary, for the forest gives and takes what it can without asking why.\n\nAn abomination made out of the souls of children who were lost in the forest, the compound spirit is far beyond a spirit and has become a potent curse that seeks those who wish to exchange the soul of a living being for the soul of a dead child.\n\nIt appears that it's natural habitat is in the upper floors of the dungeon, mimicking the sounds of laughter of children and tricking adventurers into a false sense of security before trapping them in the trees and taking their bodies.\n\n\"If you hear the sound of kids playing in the dungeon, go the other way unless you want your soul taken\"\n\n- Axiol Morah, second in command of the Oak Guild.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Kodama\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|RESIST (0.5x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|WEAK (1.5x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 6500\n|-\n| colspan=\"3\" |Damage: SHADOW\n|-\n| colspan=\"3\" |Can inflict: BLEEDING, BREACHED, DECAYED and HEAVY\n|-\n| colspan=\"3\" |Phases: 1\n|-\n| colspan=\"3\" |This boss is Stationary, meaning it doesn't move when spawned.\n|}\n\n== Strategy ==\nKodama is a stationary boss with a ring of shadow around the arena that constantly deal damage. He attacks with large AOE blasts and tentacles that he summons in various patterns, capable of applying bleed, breached, decay and heavy.\n\n== Credits ==\nMade by Have and Mantibro \n\nMusic:",
  "strategy": "Kodama is a stationary boss with a ring of shadow around the arena that constantly deal damage. He attacks with large AOE blasts and tentacles that he summons in various patterns, capable of applying bleed, breached, decay and heavy.\n\n== Credits ==\nMade by Have and Mantibro \n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "RESIST",
    "mult": 0.5
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.5
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "6500",
  "damage": "SHADOW",
  "inflicts": "BLEEDING, BREACHED, DECAYED and HEAVY",
  "phases": "1",
  "desc": "A Curse Incarnate",
  "phase": "Penumbra",
  "icon": "icons/boss/Kodama_Icon.png",
  "zh_mech": "站桩 Boss，场地边缘暗环持续造成伤害；大范围 AOE 爆 + 多种触手模式，可施加出血/破甲/衰减/沉重。",
  "zh_tips": "保持移动远离边缘暗环与触手；带异常净化的队友或道具应对 debuff。",
  "dmg_zh": "暗"
 },
 {
  "id": "the_gravetender",
  "name": "The Gravetender",
  "lore": "A demon known as the Gravetender; born from the angel who wished for an eternal rest.\n\nIts agony has caused it to lose its sense of self. The demon grew in size due to its roots, transforming itself into a worm-like creature with hundreds of arms making up its body, digging through the soil and burrowing itself with the goal of locating the corpse of its creator, for only the destruction of it would put an end to the demon's suffering.\n\nIt mourns all who fall before it, ensuring they are properly memorialized; though, it may just be a way to mark where it has already been searched.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |The Gravetender\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.5x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|WEAK (1.25x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 6500\n|-\n| colspan=\"3\" |Damage: PHYSICAL and SHADOW\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and BREACHED\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nThe Gravetender fight consists of 1 phase.\n\nThe Gravetender is a semi-stationary boss which occasionally burrows around the arena below players to move around. The Gravetender will occasionally shoot out a Gravity Well, a slow moving orb which will pull in all players within it's radius, it cannot be killed and will only go away with time.\n\n== Credits ==\nMade by Beyond\n\nMusic: \n\nThe Gravetender is from .\n\n== Statistics ==\nBase HP: 7800\n\nDamage: PHYSICAL and SHADOW\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity\n! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.5x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|WEAK (1.25x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "strategy": "The Gravetender fight consists of 1 phase.\n\nThe Gravetender is a semi-stationary boss which occasionally burrows around the arena below players to move around. The Gravetender will occasionally shoot out a Gravity Well, a slow moving orb which will pull in all players within it's radius, it cannot be killed and will only go away with time.\n\n== Credits ==\nMade by Beyond\n\nMusic: \n\nThe Gravetender is from .\n\n== Statistics ==\nBase HP: 7800\n\nDamage: PHYSICAL and SHADOW\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity\n! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.5x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|WEAK (1.25x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.5
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.25
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.25
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "6500",
  "damage": "PHYSICAL and SHADOW",
  "inflicts": "BLEEDING and BREACHED",
  "phases": "1",
  "desc": "The Aperture's Demon",
  "phase": "Penumbra",
  "icon": "icons/boss/Gravetender_Icon.png",
  "zh_mech": "半站桩 Boss，偶尔钻地移动。会发射重力井（慢速球体，吸附范围内所有玩家；不可击杀，随时间消失）。",
  "zh_tips": "看见重力井立刻远离其吸力范围，等它自然消失。",
  "dmg_zh": "物理、暗"
 },
 {
  "id": "the_black_lily",
  "name": "The Black Lily",
  "lore": "CODE: BLACK LILY Report\n\nAn unidentified entity has been confirmed at ████/███/██ in sector ████.\n\nThe entity attempted to establish control over the surrounding environment by commanding multiple species of smaller entities in a manner similar to a queen bee directing its swarm.\n\nFurthermore, substances produced by both the entity and its servants have been found to possess severe mind-corrupting properties. Reports indicate that exposed individuals suffered intense confusion and hallucinations, often describing the sensation as though the thoughts of other people had become mixed with their own.\n\nThe white spherical structures attached to the entity have been designated as \"Cores.\" These Cores are capable of recording the informational composition of matter and reproducing it.\n\nIt has been determined that these Cores allow the entity to generate servants in effectively limitless quantities. As such, the entity’s capacity to influence and overwrite its surroundings has been assessed as catastrophic. Immediate extermination is required upon discovery.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |The Black Lily\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.25x)\n|-\n|SHADOW\n|RESIST (0.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 6500\n|-\n| colspan=\"3\" |Damage: LUMINOUS and SHADOW\n|-\n| colspan=\"3\" |Can inflict: BLEEDING, WEAKENED, BREACHED and DECAYED\n|-\n| colspan=\"3\" |Phases: 1\n|-\n| colspan=\"3\" |This boss is Stationary, meaning it doesn't move when it spawns.\n|}\n\n== Strategy ==\nThe Black Lily is a stationary boss that summons up to 3 Black Lily Tokens at any given time. It begins with only 2 attacks before reaching 50% HP where it has access to a few additional, much more devastating moves ranging from puddles that can apply the decay status effect to a large laser damaging an entire half of the battlefield. Many of Black Lily's attacks provide little to no indicator, forcing its opponents to pay close attention to it as well as its minions less they be caught off guard.\n\n== Credits ==\nMade by BAKAME, Mantibro and CosMicz \n\nMusic: \n\n== Statistics ==\nBase HP: 11000\n\nThis boss does not deviate from its spawn point.\n\nDamage: LUMINOUS and SHADOW\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity\n! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.25x)\n|-\n|SHADOW\n|RESIST (0.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "strategy": "The Black Lily is a stationary boss that summons up to 3 Black Lily Tokens at any given time. It begins with only 2 attacks before reaching 50% HP where it has access to a few additional, much more devastating moves ranging from puddles that can apply the decay status effect to a large laser damaging an entire half of the battlefield. Many of Black Lily's attacks provide little to no indicator, forcing its opponents to pay close attention to it as well as its minions less they be caught off guard.\n\n== Credits ==\nMade by BAKAME, Mantibro and CosMicz \n\nMusic: \n\n== Statistics ==\nBase HP: 11000\n\nThis boss does not deviate from its spawn point.\n\nDamage: LUMINOUS and SHADOW\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity\n! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.25x)\n|-\n|SHADOW\n|RESIST (0.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.25
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.25
   },
   "SHADOW": {
    "status": "RESIST",
    "mult": 0.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "6500",
  "damage": "LUMINOUS and SHADOW",
  "inflicts": "BLEEDING, WEAKENED, BREACHED and DECAYED",
  "phases": "1",
  "desc": "A Swarming Illuminate",
  "phase": "Late Penumbra",
  "icon": "icons/boss/Black_Lily_Icon.png",
  "zh_mech": "站桩 Boss，同时维持最多 3 个黑百合 Token。50% HP 前仅 2 种攻击；50% 后解锁数种毁灭性招式：衰减地面池、覆盖半场的大型激光等。多数攻击几乎没有前摇提示。",
  "zh_tips": "全程紧盯本体与小怪动作（提示极少），50% 后警惕地面衰减池与半场激光。",
  "dmg_zh": "光、暗"
 },
 {
  "id": "nx-obsidian",
  "name": "NX-Obsidian",
  "lore": "A war machine, advanced by our standards but primitive in its home dimension. As war in said dimension escalated, weapons and tactics evolved, leading to the creation of NX Constructs. Obsidian, one of the early NX models was ultimately abandoned when newer units were made. Now they are simply to rot and be forgotten in a warehouse filled with other machines much like NX-Obsidian, each carrying a single hard-coded directive: Kill.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |NX-Obsidian\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|WEAK (1.25x)\n|-\n|FIRE\n|RESIST (0.75x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|RESIST (0.75x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 8400\n|-\n| colspan=\"3\" |Damage: PHYSICAL and FIRE\n|-\n| colspan=\"3\" |Can inflict: BURNING\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nThe NX-Obsidian fight consists of 1 phase.\n\nNX-Obsidian possesses a high damage moveset, as well as an unparryable purple explosive attack. Players will need to be wary of powerful lasers which inflict heavy burn on survivors.\n\nHowever, NX-Obsidian is a unique case and is weak to Physical. \n\n== Credits ==\nMade by MelonTM and Mantibro \n\nVoiced by MelonTM\n\nArt and Design by Kejun Wang. \n\nMusic:",
  "strategy": "The NX-Obsidian fight consists of 1 phase.\n\nNX-Obsidian possesses a high damage moveset, as well as an unparryable purple explosive attack. Players will need to be wary of powerful lasers which inflict heavy burn on survivors.\n\nHowever, NX-Obsidian is a unique case and is weak to Physical. \n\n== Credits ==\nMade by MelonTM and Mantibro \n\nVoiced by MelonTM\n\nArt and Design by Kejun Wang. \n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.75
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.75
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "8400",
  "damage": "PHYSICAL and FIRE",
  "inflicts": "BURNING",
  "phases": "1",
  "desc": "STATUS SET: DESTROY",
  "phase": "Late Penumbra",
  "icon": "icons/boss/NX_Obsidian_Icon.png",
  "zh_mech": "1 阶段。高伤招式 + 不可格挡的紫色爆炸攻击；强力激光会给幸存者挂重灼烧。",
  "zh_tips": "紫爆不可格挡必须躲；激光躲开后及时处理灼烧。特殊点：它是唯一弱物理的 Boss，物理输出收益最高。",
  "dmg_zh": "物理、火"
 },
 {
  "id": "middleman",
  "name": "Middleman",
  "lore": "A long, long time ago, humanity discovered a heavenly relic, and used its angelic power to create a great ship to explore vastness the cosmos. The colossal vessel, nicknamed \"Babel,\" carried humanity far, far past their homestead, allowing them to colonize other planets and expand their reach to an intergalactic extent.\n\nEventually, humanity managed to find the edge of the universe. There, their feeble minds, unequipped to handle the realm before them, entered what they could only call \"Heaven.\" An innocuous being then invades the heavenly realm, and comes across an entity of a higher power, an Angel. The being makes a wish, which the Angel then grants. The wish manifests a dark, insidious mass of power, with a destructive potential of a universal scale. A power which corrupts and decays anything and everything it contacts.\n\nThe power of Megium.\n\nHumanity's colossal vessel is then destroyed alongside nearly half of the heavenly realm. Fragments of heaven scatter themselves across the universe, falling into the hands of many of humanity's intergalactic colonies, giving them access to the vastness of angelic power. The ERNA organization was formed as a means to collect and claim the many pieces of heaven yet to be discovered, as well as recruit those blessed with heavenly power to their ranks.\n\nDuring ERNA's early foundation, with access to few angelic resources, the faction made conscripted human soldiers undergo heavy cybernetic enhancements, turning them into robotic super-warriors with little of their humanity still intact. The first constructed series, aiming to give ERNA direction for its future, was built with the said theme in mind; \"Direction.\" Thus, a unit of seven mechanical soldiers began to serve among ERNA's elite ranks. It consisted of: The Frontman, The Backman, The Leftman, The Rightman, The Upman, The Downman, and lastly, The Middleman.\n\nThrough the years, the seven units were swept back as ERNA was able to utilize the scavenged heavenly fragments to make use of their power to construct a massive army which far outclassed the cybernetic soldiers. By then, ERNA either did not notice, or simply did not care when the seven solders rebelled against the faction, going down their own paths as their contempt and hatred of ERNA only grew.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Middleman\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.5x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|RESIST (0.75x)\n|-\n| colspan=\"3\" |Base HP: 7800\n|-\n| colspan=\"3\" |Damage: PHYSICAL and ELECTRIC\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and PARALYZING\n|-\n| colspan=\"3\" |Phases: 1\n|}\n\n== Strategy ==\nMiddle Man is the first fast paced boss, constantly charging and slashing at his opponents with his twin swords. Throughout his fight he jumps high into the air and chooses to either fly back down for a kick or fire a piercing laser at his opponents. Specializing in close range combat, the majority of Middleman's attacks cause him to lunge at his opponent allowing him to close distances quickly.\n\n== Credits ==\nMade by Scena and Mantibro\n\nCharacter and Design by MR COWBOY\n\nVoiced by DarkGrey\n\nMusic: Ecliptica Sound Team - The Middleman",
  "strategy": "Middle Man is the first fast paced boss, constantly charging and slashing at his opponents with his twin swords. Throughout his fight he jumps high into the air and chooses to either fly back down for a kick or fire a piercing laser at his opponents. Specializing in close range combat, the majority of Middleman's attacks cause him to lunge at his opponent allowing him to close distances quickly.\n\n== Credits ==\nMade by Scena and Mantibro\n\nCharacter and Design by MR COWBOY\n\nVoiced by DarkGrey\n\nMusic: Ecliptica Sound Team - The Middleman",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "WEAK",
    "mult": 1.5
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.75
   }
  },
  "hp": "7800",
  "damage": "PHYSICAL and ELECTRIC",
  "inflicts": "BLEEDING and PARALYZING",
  "phases": "1",
  "desc": "The Power of Megium",
  "phase": "Late Penumbra",
  "icon": "icons/boss/Middleman_Icon.png",
  "zh_mech": "首个快节奏 Boss：双剑冲锋斩击；跳至高空后二选一——俯冲踢击或贯穿激光。多数招式带突进，擅长快速拉近距离。",
  "zh_tips": "保持距离防突进；看他跳起后辨认俯冲/激光再闪避。",
  "dmg_zh": "物理、雷"
 },
 {
  "id": "melgor_johnson",
  "name": "Melgor Johnson",
  "lore": "Forcefully pulled through a portal, Melgor Johnson is a Y-Style automaton able to shift the shape of his body for comedic effect, along with further questioning he gave the answers to how he works:\n\nQ - \"What is your name?\"\n\nA - \"My name'a Melon\"\n\nQ - \"Why do you become Buff?\"\n\nA - \"Because I can\"\n\nQ - \"How do your powers work?\"\n\nA - \"Mountain Dew Voltage...\"\n\nQ - \"Where did you come from?\"\n\nA - \"My house...\"\n\nQ - \"Who are you?\"\n\nA - \"The Creator of... uh... um... theres these cool games named-\"\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Melgor Johnson\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|WEAK (1.5x)\n|-\n|ELECTRIC\n|RESIST (0.5x)\n|-\n|LUMINOUS\n|NEUTRAL (1x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 10000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and ELECTRIC\n|-\n| colspan=\"3\" |Can inflict: PARALYZING\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Melgor Johnson battle consists of 2 phases. In Phase 2, his moveset is enhanced with extra damage and more electrical attacks.\n\nAt any health in Phase 2, Melgor Johnson may clap his cheeks, emitting a massive purple shockwave.\n\n== Credits ==\nMade by MelonTM and Mantibro\n\nVoiced by MelonTM\n\nMusic Phase 1: \n\nMusic Phase 2:",
  "strategy": "The Melgor Johnson battle consists of 2 phases. In Phase 2, his moveset is enhanced with extra damage and more electrical attacks.\n\nAt any health in Phase 2, Melgor Johnson may clap his cheeks, emitting a massive purple shockwave.\n\n== Credits ==\nMade by MelonTM and Mantibro\n\nVoiced by MelonTM\n\nMusic Phase 1: \n\nMusic Phase 2:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.5
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.5
   },
   "LUMINOUS": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "10000",
  "damage": "PHYSICAL and ELECTRIC",
  "inflicts": "PARALYZING",
  "phases": "2",
  "desc": "The Fallen Employee",
  "phase": "Antumbra",
  "icon": "icons/boss/Melon_Icon.png",
  "zh_mech": "2 阶段。P2 招式增强：额外伤害 + 更多电属性攻击；P2 任意血量都可能拍掌释放巨型紫色震波。",
  "zh_tips": "P2 全程警惕紫色震波（无视防御），看到蓄力就远离。",
  "dmg_zh": "物理、雷"
 },
 {
  "id": "amaziah",
  "name": "Amaziah",
  "lore": "Anger made flesh.\n\nAn imprisoned soul of the dungeon said to hold immense corrosion powers. Its anger could be felt through the air around it as it stomped near the gate to pummel anyone who stood close to it, scouts were able to listen closely and described its constant screaming and rambling of rage to be tied to a specific name \"Bae’Bijonn.\" researchers have found no creatures or individuals within and outside the dungeon that match this name or title but one thing is certain, this gate guardian appears to hold an immense grudge against said name to an unfathomable degree as the sheer mention of the name has proven to earn combat mage teams a quick death as the entity rabidly leapt towards the one mentioning said name to test its reaction.\n\nThe being is said to wander the halls of an ancient palace in the middle layer of the dungeon, stomping and fuming eternally until someone challenges it or happens to enter its sight, to this day we are unsure as to what its true purpose for being this enraged is, and what could cause such a thing to come into existence.\n\n\"KILL YOU KILL YOU KILL YOU!\"\n\n- Amaziah\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Amaziah\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.75x)\n|-\n|FROST\n|WEAK (1.5x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|RESIST (0.5x)\n|-\n| colspan=\"3\" |Base HP: 15000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and POISON\n|-\n| colspan=\"3\" |Can inflict: POISONED\n|-\n| colspan=\"3\" |Phases: 1\n|-\n| colspan=\"3\" |KILL YOU KILL YOU KILL YOU KILL YOU KILL YOU *INCOHERENT BABBLING*\n|}\n\n== Strategy ==\nAmaziah is a poison based boss who primarily uses close ranged attacks, all of which shoot an additional poisonous projectile. When reaching 60% HP Amaziah's move set is expanded allowing him to perform much larger and deadlier jumps, lunge at opponents in the sky, and fire beams from his face.\n\n== Credits ==\nMade by Have and Mantibro\n\nVoiced by BimpChooks\n\nMusic: Ecliptica Sound Team - KILL YOU",
  "strategy": "Amaziah is a poison based boss who primarily uses close ranged attacks, all of which shoot an additional poisonous projectile. When reaching 60% HP Amaziah's move set is expanded allowing him to perform much larger and deadlier jumps, lunge at opponents in the sky, and fire beams from his face.\n\n== Credits ==\nMade by Have and Mantibro\n\nVoiced by BimpChooks\n\nMusic: Ecliptica Sound Team - KILL YOU",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.75
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.5
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.5
   }
  },
  "hp": "15000",
  "damage": "PHYSICAL and POISON",
  "inflicts": "POISONED",
  "phases": "1",
  "desc": "KILL YOU KILL YOU KILL YOU",
  "phase": "Antumbra",
  "icon": "icons/boss/AmaziahIcon.png",
  "zh_mech": "毒系近战 Boss，所有近战攻击附带额外毒弹。60% HP 解锁：更大更致命的跳跃、空中突进、面部光束。",
  "zh_tips": "60% 后同时躲近战突进与毒弹；注意中毒状态。",
  "dmg_zh": "物理、毒"
 },
 {
  "id": "jacked_o_lantern",
  "name": "Jacked O' Lantern",
  "lore": "In a dark, peaceful pumpkin patch, a sudden overwhelming presence arrived to shake up the roots. The one they call Bae'Bijonn descended down with a loud smash, unimpressed with the uneventful find.\n\nOut of nothing more than personal amusement, he sprinkled the soil with his magical power, to act as fertilizer of mana for the orange fruits. The invader announced his presence, but his expectations were slim, so he simply left, allowing the plants to grow.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Jacked O' Lantern\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|RESIST (0.75x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|WEAK (1.25x)\n|-\n| colspan=\"3\" |Base HP: 18000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and FIRE\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and BURNING\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Jacked O' Lantern battle consists of 2 sub-phases. In sub-phase 2, all of his basic swings are enhanced with an extra fire projectile, and all slams will leave behind Pillars of fire.\n\nJacked O' Lantern will transition into sub-phase 2 at 35% HP, healing a large chunk of his total HP. In this subphase, he may also choose to Bulk Up, giving himself the Enforced and Empowered status effects for a long duration\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by BimpChooks\n\nMusic:",
  "strategy": "The Jacked O' Lantern battle consists of 2 sub-phases. In sub-phase 2, all of his basic swings are enhanced with an extra fire projectile, and all slams will leave behind Pillars of fire.\n\nJacked O' Lantern will transition into sub-phase 2 at 35% HP, healing a large chunk of his total HP. In this subphase, he may also choose to Bulk Up, giving himself the Enforced and Empowered status effects for a long duration\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by BimpChooks\n\nMusic:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.75
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "WEAK",
    "mult": 1.25
   }
  },
  "hp": "18000",
  "damage": "PHYSICAL and FIRE",
  "inflicts": "BLEEDING and BURNING",
  "phases": "2",
  "desc": "Bad Things, Good People",
  "phase": "Antumbra",
  "icon": "icons/boss/JackedOLantern_Icon.png",
  "zh_mech": "2 子阶段。P2 全部基础挥砍附加火弹、砸地留下火焰柱。35% HP 转 P2 并回复大量血量；P2 可能 Bulk Up 给自己长时间 Enforced + Empowered。",
  "zh_tips": "35% 转阶段会回血别松懈；Bulk Up 期间伤害大增，优先避战拖过增益。",
  "dmg_zh": "物理、火"
 },
 {
  "id": "despair",
  "name": "Despair",
  "lore": "Folks tell of a great archmage by the name of \"Confidence\" who was blinded by his own power. He was blinded soo much, it would inevitably lead to his demise & haunt him for all of eternity. Or, that's what they thought.\n\nFor the protective sake of their world & the people they love, Confidence's closest relative \"Optimism\" banished him to another realm of reality, isolating him in complete darkness. Confidence grew hopeless in his dimension & hatred began to boil within him, but with that, he discovered something. Something useful.\n\nHe can manifest his own arcane energy through the essence of others emotions, including his own.\n\nUpon breaking out of his isolated dimension, he began fueling off of those to oppose him and brought ruin upon countless worlds & realms. Eventually, including his own. Those who live to tell the tale refuse to call him by his original alias anymore. Some refer to him as the \"Harbinger of the Hopeless.\" Others call him, Despair.\n\n\"I feared this day would manifest into reality, but i refused to see it. I loved him too much to believe such a fate would occur. But power will always blind those who seek for more of it. What happened is my responsibility to fix, & I hold every little accountability for it. I'm truly sorry for not looking out for you sooner, brother...\" ~ Optimism\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Despair\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.15x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|RESIST (0.7x)\n|-\n|LUMINOUS\n|WEAK (1.25x)\n|-\n|SHADOW\n|RESIST (0.85x)\n|-\n|POISON\n|WEAK (1.1x)\n|-\n| colspan=\"3\" |Base HP: 15000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and ELECTRIC\n|-\n| colspan=\"3\" |Can inflict: PARALYZED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nDespair's fight consists of two different phases.\n\nIn his first phase he attacks his opponents with lightning strikes and beams, occasionally side stepping away from his opponents to keep at range. When defeated he will transition into his second phase boasting much more powerful attacks. Larger beams, lightning strikes, and a very large and powerful AOE blast with a chance to activate twice to catch his opponents off guard.\n\n== Credits ==\nMade by CosMicz \n\nMusic Phase 1:  \n\nMusic Phase 2:",
  "strategy": "Despair's fight consists of two different phases.\n\nIn his first phase he attacks his opponents with lightning strikes and beams, occasionally side stepping away from his opponents to keep at range. When defeated he will transition into his second phase boasting much more powerful attacks. Larger beams, lightning strikes, and a very large and powerful AOE blast with a chance to activate twice to catch his opponents off guard.\n\n== Credits ==\nMade by CosMicz \n\nMusic Phase 1:  \n\nMusic Phase 2:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.15
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.25
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.7
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.25
   },
   "SHADOW": {
    "status": "RESIST",
    "mult": 0.85
   },
   "POISON": {
    "status": "WEAK",
    "mult": 1.1
   }
  },
  "hp": "15000",
  "damage": "PHYSICAL and ELECTRIC",
  "inflicts": "PARALYZED",
  "phases": "2",
  "desc": "Harbinger of the Hopeless",
  "phase": "Late Antumbra",
  "icon": "icons/boss/Despair_Icon.png",
  "zh_mech": "2 阶段。P1：闪电打击 + 光束，偶尔侧移拉开距离。P2（击败后转入）：更大的光束、闪电，以及超大 AOE 且几率连续触发两次。",
  "zh_tips": "P2 的 AOE 可能连放两次，躲完别急着回去输出。",
  "dmg_zh": "物理、雷"
 },
 {
  "id": "m-41-d",
  "name": "M-41-D",
  "lore": "An extremely large alloy, M-41-D resides on the 6th floor, acting as the guardian of a large mansion owned by Hapticor’s CEO, Isyel.\n\nM-41-D is the only moving thing in the mansion, patrolling the halls quietly cleaning, all day, all night. Intruders attempting to break into the mansion will likely encounter her, and will likely meet their end. Her massive mechanical broomstick is able to dissolve small objects and dispel flesh and bone with ease due to its intense energy, and her size allows her to easily overpower most that are unprepared for her.\n\nPrior to her activation, she was kept within a very large storage container on the 2nd floor, and was discovered and recovered by Hapticor during a small-scale invasion of the 2nd floor. She was seemingly intended to be used as a weapon against Hapticor, as she had several modifications done to her, including the removal of her mouth, subsumed livers of fallen kin within her arms to allow for various powers and abilities, such as her mastery over energy, and her technology being made to heavily resist OYP interception, a strategy often used by Hapticor to hijack machinery on the 2nd floor.\n\nAfter being recovered, M-41-D was activated by Hapticor, and was quickly conditioned to obey them, particularly Isyel himself, who directly influenced her; ending up becoming something of a father figure to her. Once her conditioning was done, rather than sending her back down to the 2nd floor to be used as a weapon, she was instead sent to reside at Isyel’s old mansion to keep it clean and protected, with a promise that Isyel would return one day to come see her.\n\nThough, that day never came. Isyel could never look at M-41-D without thinking of his lost daughter, and ultimately, M-41-D would remain alone, cleaning the mansion for someone who would never return.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |M-41-D\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.75x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.25x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|RESIST (0.25x)\n|-\n| colspan=\"3\" |Base HP: 13000\n|-\n| colspan=\"3\" |Damage: ELECTRIC\n|-\n| colspan=\"3\" |Can inflict: PARALYZED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe M-41-D fight consists of 2 sub-phases. A standard phase and a Tower phase.\n\nOnce per fight, once M-41-D reaches 40% HP, she will summon 2 Disruption Towers. Each tower will alternate between healing M-41-D, or using a large electric AoE if players are nearby. M-41-D will also become more powerful after this phase transition, increasing the radius of several of her moves.\n\n== Credits ==\nMade by Beyond and Mantibro\n\nMusic Phase 1:  \n\nMusic Phase 2: \n\nFirst appeared in !",
  "strategy": "The M-41-D fight consists of 2 sub-phases. A standard phase and a Tower phase.\n\nOnce per fight, once M-41-D reaches 40% HP, she will summon 2 Disruption Towers. Each tower will alternate between healing M-41-D, or using a large electric AoE if players are nearby. M-41-D will also become more powerful after this phase transition, increasing the radius of several of her moves.\n\n== Credits ==\nMade by Beyond and Mantibro\n\nMusic Phase 1:  \n\nMusic Phase 2: \n\nFirst appeared in !",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.75
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "WEAK",
    "mult": 1.25
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.25
   }
  },
  "hp": "13000",
  "damage": "ELECTRIC",
  "inflicts": "PARALYZED",
  "phases": "2",
  "desc": "The Servant Alloy",
  "phase": "Late Antumbra",
  "icon": "icons/boss/M41D_Icon.png",
  "zh_mech": "2 子阶段：标准 + 塔阶段。每场一次：40% HP 召唤 2 座干扰塔，轮流治疗 M-41-D 或对附近玩家释放大范围电 AOE；转阶段后自身招式半径增大。",
  "zh_tips": "40% 时优先处理干扰塔（阻止治疗与电 AOE）；转阶段后保持更远距离。",
  "dmg_zh": "雷"
 },
 {
  "id": "corus",
  "name": "Corus",
  "lore": "With the combined research and innovation of the Proto Colony alongside Omen, The FOX were close to finding a worthy recreation of the regenerative body of the Onyx Pilot. Their progress eventually landed on self-sufficient nanomachines, which feasted on metal and formed themselves into sentient constructs with the ability to replicate. An experimental batch of the nanobots was deposited into a sealed container to act as a controlled environment for monitoring the activity of the nanomachines, dubbed the Mechanical Biosphere System. After many Gaian days, it was noticed that the containment was slowly, but continuously rising in temperature. A monitoring probe was lowered into the box, and inside, a fully formed construct was seemingly laying dormant, emitting extreme heat and combustible gas. The construct was soon given the name Corus.\n\nAfter further research and refinements, a new strand of nanomachines would be soon created, one which would later be deposited onto a planet which would later be named MBS-02, Mechanical Biosphere System 02. The original containment was eventually also dropped onto the planet, but by then it was treated as merely a way of disposal.\n\nAs the knowledge of the construct spread outside the Proto Colony research team, through hearsay it eventually became a niche legend.\n\n\"A being molded from the star itself, sealed away under a mountain of metal.\"\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Corus\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.5x)\n|-\n|FROST\n|WEAK (1.5x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 12000\n|-\n| colspan=\"3\" |Damage: FIRE\n|-\n| colspan=\"3\" |Can inflict: BURNING\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nCorus' fight consists of two phases. In the first phase he releases constant barrages of fire balls spread throughout the battlefield with every attack. He can also jump high into the air and throw down a larger fireball that leaves a lingering puddle that damages his opponents.\n\nUpon death, he gets engulfed in blue flames and enters his second phase. In this phase the majority of the fireballs he launches leave an addition puddle of fire covering the floor of the battlefield. Additionally, his jump attack leaves a pillar of flames which lingers and grows overtime. Combined with the puddles, Corus leaves his battlefield mostly untraversable allowing little room to avoid his onslaught of attacks when he's close.\n\n== Credits ==\nMade by Beyond and Mantibro \n\nMusic: \n\nFirst appear in !",
  "strategy": "Corus' fight consists of two phases. In the first phase he releases constant barrages of fire balls spread throughout the battlefield with every attack. He can also jump high into the air and throw down a larger fireball that leaves a lingering puddle that damages his opponents.\n\nUpon death, he gets engulfed in blue flames and enters his second phase. In this phase the majority of the fireballs he launches leave an addition puddle of fire covering the floor of the battlefield. Additionally, his jump attack leaves a pillar of flames which lingers and grows overtime. Combined with the puddles, Corus leaves his battlefield mostly untraversable allowing little room to avoid his onslaught of attacks when he's close.\n\n== Credits ==\nMade by Beyond and Mantibro \n\nMusic: \n\nFirst appear in !",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.5
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.5
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "12000",
  "damage": "FIRE",
  "inflicts": "BURNING",
  "phases": "2",
  "desc": "The First Chorus",
  "phase": "Umbra",
  "icon": "icons/boss/Corus_Icon.png",
  "zh_mech": "2 阶段。P1：每招都伴随覆盖战场的火球弹幕；可高空投下大火球并留下持续伤害的火池。死亡后蓝焰转 P2：多数火球落地额外留火池，招式更强。",
  "zh_tips": "全程注意地面火池；P2 火池密度大增，走位空间要留足。",
  "dmg_zh": "火"
 },
 {
  "id": "yuki",
  "name": "Yuki",
  "lore": "Android born from hands of the Ancient Humans, and infused with power of element of ice. Seen as a failed creation from its creator, they locked its power away and then imprisoned it in a domain of ice, never to be released from its shackles.\n\nOne day, an unknown entity took it away from its domain of ice to test its strength against whoever encounters it.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Yuki\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|WEAK (1.25x)\n|-\n|LUMINOUS\n|NEUTRAL (1x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 10000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and FROST\n|-\n| colspan=\"3\" |Can inflict: FROZEN and PARALYZED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Yuki fight consists of 2 phases, a grounded and flying phase.\n\nIn phase 1, Yuki will try to punch and grapple players. At 50% HP, Yuki will be able to pound the ground to emit purple shockwaves.\n\nIn phase 2, Yuki will be permanently in flight. Yuki will gain access to ranged ice attacks. At 50% HP, Yuki will unlock their full moveset, being able to seperate parts of the arena into sections with ice walls, as well as devastating laser attacks.\n\n== Credits ==\nCreated by Voltric [Maruki]\n\nMusic Phase 1:  \n\nMusic Phase 2:",
  "strategy": "The Yuki fight consists of 2 phases, a grounded and flying phase.\n\nIn phase 1, Yuki will try to punch and grapple players. At 50% HP, Yuki will be able to pound the ground to emit purple shockwaves.\n\nIn phase 2, Yuki will be permanently in flight. Yuki will gain access to ranged ice attacks. At 50% HP, Yuki will unlock their full moveset, being able to seperate parts of the arena into sections with ice walls, as well as devastating laser attacks.\n\n== Credits ==\nCreated by Voltric [Maruki]\n\nMusic Phase 1:  \n\nMusic Phase 2:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "WEAK",
    "mult": 1.25
   },
   "LUMINOUS": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "10000",
  "damage": "PHYSICAL and FROST",
  "inflicts": "FROZEN and PARALYZED",
  "phases": "2",
  "desc": "Ice-born Android",
  "phase": "Umbra",
  "icon": "icons/boss/Yuki_Icon.png",
  "zh_mech": "2 阶段：地面 + 飞行。P1 拳击/抓取；50% HP 可砸地释放紫色震波。P2 永久飞行 + 冰系远程；50% 解锁全套招式：冰墙分割场地、毁灭性激光。",
  "zh_tips": "P2 注意冰墙分割（避免被隔开落单）与激光；50% 阈值时防紫震波。",
  "dmg_zh": "物理、冰"
 },
 {
  "id": "cone_head",
  "name": "Cone Head",
  "lore": "The one called the manifestation of man's inner struggle against traffic laws. A warrior always present, but rarely seen. Those, who follow the way of the law will not have the need of witnessing his will. His yellow blade, named Jōdō-tō, is the warning to the offenders, to show but a fraction of the wrath of traffic enforcement. To teach the correct morals, the Urban Samurai unsheathes two more blades, Teirei-tō, and Shinrei-tō, whose blades and red, and green respectively.\n\nThose who learn to follow the way of the law shall be left unscathed.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Cone Head\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.7x)\n|-\n|SHADOW\n|WEAK (1.3x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 20000\n|-\n| colspan=\"3\" |Damage: PHYSICAL\n|-\n| colspan=\"3\" |Can inflict: BLEEDING\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nCone Head's main move set utilizes the traffic light gimmick of moving while the light is green and stopping while the light is red to avoid his attacks. In his first phase he uses one of his three swords to strike at his opponent and occasionally teleporting behind them or covering the majority of the battle field with a traffic light attack, dealing a devastating amount of damage if not followed correctly. Around 30% HP the sword is flung out of his hands and he goes into a melee sub-phase where he chases and punches his opponent until defeated.\n\nOnce defeated he will enter his second phase, unsheathing his remaining two swords and utilizing the traffic light gimmick to its fullest. Now each of his slashes are either red or green and are able to be dodged by not moving or moving respectively. His large traffic light AOE attack now strikes 3 times, forcing his opponents to remember the order of the lights or take a significant amount of damage.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by twui061 (おとぅい)\n\nMusic Phase 1:  \n\nMusic Phase 2: \n\n== Statistics ==\nBase HP: 20000\n\nDamage: PHYSICAL\n\nThis boss is made up of TWO phases\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity\n! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.7x)\n|-\n|SHADOW\n|WEAK (1.3x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "strategy": "Cone Head's main move set utilizes the traffic light gimmick of moving while the light is green and stopping while the light is red to avoid his attacks. In his first phase he uses one of his three swords to strike at his opponent and occasionally teleporting behind them or covering the majority of the battle field with a traffic light attack, dealing a devastating amount of damage if not followed correctly. Around 30% HP the sword is flung out of his hands and he goes into a melee sub-phase where he chases and punches his opponent until defeated.\n\nOnce defeated he will enter his second phase, unsheathing his remaining two swords and utilizing the traffic light gimmick to its fullest. Now each of his slashes are either red or green and are able to be dodged by not moving or moving respectively. His large traffic light AOE attack now strikes 3 times, forcing his opponents to remember the order of the lights or take a significant amount of damage.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by twui061 (おとぅい)\n\nMusic Phase 1:  \n\nMusic Phase 2: \n\n== Statistics ==\nBase HP: 20000\n\nDamage: PHYSICAL\n\nThis boss is made up of TWO phases\n{| class=\"wikitable\" style=\"background:#000; color:#fff; border:1px solid #444;\"\n! style=\"background:#000000; color:#ffffff;\" | Affinity\n! style=\"background:#000000; color:#ffffff;\" | Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.7x)\n|-\n|SHADOW\n|WEAK (1.3x)\n|-\n|POISON\n|NEUTRAL (1x)\n|}",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.7
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.3
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "20000",
  "damage": "PHYSICAL",
  "inflicts": "BLEEDING",
  "phases": "2",
  "desc": "The Urban Samurai",
  "phase": "Umbra",
  "icon": "icons/boss/Cone_Head_Icon.png",
  "zh_mech": "核心机制为红绿灯：绿灯移动、红灯停（否则吃伤害）。P1 用三把剑之一攻击，偶尔瞬移到背后或释放覆盖大半场地的红绿灯攻击（应对错误则巨额伤害）。约 30% 剑脱手进入近战子阶段。",
  "zh_tips": "严格按红绿灯节奏移动；全场地红绿灯时观察灯色再走；30% 后注意近战形态变化。",
  "dmg_zh": "物理"
 },
 {
  "id": "mephiel",
  "name": "Mephiel",
  "lore": "After an unsuccessful attempt to murder his brother Veelch, Mephiel, known as the Corrupt God of Dominion, was imprisoned in a lonely dimension of his brother’s making, which only served to act as a reminder of what drove Mephiel to commit an act of treachery against his family, for it was the ability to reach into the multiverse, an ability which his brother possessed, that the Traitor greatly envied Veelch for. Mephiel, himself blessed with the innate ability to absorb the magical powers of others and use them for himself, was fully prepared to utilize his wicked power against his very own sibling to fuel his own selfish and greedy desires.\n\nAfter hundreds of years of isolation, Mephiel rejoiced as a dimensional interloper, DarkGrey, fell within his grasp. Seeing his one way out of his prison, he manipulated the grey goo creature to do his bidding and defeat his brother in his place. Mephiel’s plan was successful, and after acquiring the ability of dimensional travel he’s seeked for so long, he set out to amass as much power in the multiverse as he could.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Mephiel\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|RESIST (0.75x)\n|-\n|LUMINOUS\n|WEAK (1.5x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 19000\n|-\n| colspan=\"3\" |Damage: SHADOW\n|-\n| colspan=\"3\" |Can inflict: BLEEDING, BREACHED and DECAY\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Mephiel fight consists of 2 phases. Phase 2 has a greatly expanded moveset and previous moves are enhanced.\n\nMephiel is a boss with a bullet-hell focused style, covering with swathes of the arena in hazards. In phase 2, Mephiel will gain the ability to fly, leaving players with a period more focused on surviving rather than damaging the boss.\n\nMephiel possesses a powerful rotating pizza cutter move, requiring players to rotate around.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by WanderBlues\n\nMusic Phase 1: \n\nMusic Phase 2:",
  "strategy": "The Mephiel fight consists of 2 phases. Phase 2 has a greatly expanded moveset and previous moves are enhanced.\n\nMephiel is a boss with a bullet-hell focused style, covering with swathes of the arena in hazards. In phase 2, Mephiel will gain the ability to fly, leaving players with a period more focused on surviving rather than damaging the boss.\n\nMephiel possesses a powerful rotating pizza cutter move, requiring players to rotate around.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by WanderBlues\n\nMusic Phase 1: \n\nMusic Phase 2:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.75
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.5
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "19000",
  "damage": "SHADOW",
  "inflicts": "BLEEDING, BREACHED and DECAY",
  "phases": "2",
  "desc": "The Treacherous",
  "phase": "Late Umbra",
  "icon": "icons/boss/Mephiel_Icon.png",
  "zh_mech": "2 阶段。弹幕地狱型：大面积场地危险区。P2 招式大幅扩充并强化，且获得飞行能力（以生存为主）。招牌：旋转披萨刀（需绕圈走位）。",
  "zh_tips": "披萨刀要绕圈躲；P2 飞行阶段优先保命，伤害其次。",
  "dmg_zh": "暗"
 },
 {
  "id": "irides",
  "name": "Irides",
  "lore": "Forged from jagged black glass and crowned with radiant white wings; the Crystalline Prototype, a failed attempt. Its body reflects no light, only swallowing it into endless darkness, while the orb within pulses with an eerie glow.\n\nBeing far from the monstrous entity it was meant to become, it drifts through ruins of its genesis like a broken god waiting to kill or be killed.\n\nThe Creator is dead.\n\nLight is Strength.\n\nThe World is Bright.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Irides\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|WEAK (1.25x)\n|-\n|FIRE\n|RESIST (0.7x)\n|-\n|FROST\n|WEAK (1.15x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 12500\n|-\n| colspan=\"3\" |Damage: PHYSICAL, ELECTRIC, LUMINOUS and SHADOW\n|-\n| colspan=\"3\" |Can inflict: PARALYZED, WEAKENED, BREACHED and DECAYED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nIrides is a fast paced boss consisting of two phases. In his first he berates his opponents with an entourage of attacks. Slashing at them, firing projectiles, and preforming piercing dashes that go through defenses. Upon death, Irides reaches phase two where he is equipped with more speed and an expanded move set allowing him shoot large lightning bolt, light projectiles, and a thunderous stomp piercing through his foes.\n\nDuring Phase two when below 50% HP Irides can summon three crystals that embed themselves into the ground. While they are active Irides is completely invincible. The crystals target a nearby player as indicated by the lightning emanating from them. The player they target is the only player capable of dealing damage to the crystal. Additionally, the individual crystals can charge and spike attack, forcing all of those in the battle field to jump over it. The crystals can appear a total of 3 times during the battle.\n\n== Credits ==\nMade by MelonTM\n\nDesign by Uno Dos Tres\n\nBased off of Hakita's ULTRAKILL\n\nMusic Phase 1:  \n\nMusic Phase 2:",
  "strategy": "Irides is a fast paced boss consisting of two phases. In his first he berates his opponents with an entourage of attacks. Slashing at them, firing projectiles, and preforming piercing dashes that go through defenses. Upon death, Irides reaches phase two where he is equipped with more speed and an expanded move set allowing him shoot large lightning bolt, light projectiles, and a thunderous stomp piercing through his foes.\n\nDuring Phase two when below 50% HP Irides can summon three crystals that embed themselves into the ground. While they are active Irides is completely invincible. The crystals target a nearby player as indicated by the lightning emanating from them. The player they target is the only player capable of dealing damage to the crystal. Additionally, the individual crystals can charge and spike attack, forcing all of those in the battle field to jump over it. The crystals can appear a total of 3 times during the battle.\n\n== Credits ==\nMade by MelonTM\n\nDesign by Uno Dos Tres\n\nBased off of Hakita's ULTRAKILL\n\nMusic Phase 1:  \n\nMusic Phase 2:",
  "affinity": {
   "PHYSICAL": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.7
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.15
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "12500",
  "damage": "PHYSICAL, ELECTRIC, LUMINOUS and SHADOW",
  "inflicts": "PARALYZED, WEAKENED, BREACHED and DECAYED",
  "phases": "2",
  "desc": "The Crystalline Prototype",
  "phase": "Late Umbra",
  "icon": "icons/boss/Irides_Icon.png",
  "zh_mech": "快节奏 2 阶段。P1 连招 + 弹幕 + 贯穿防御的突刺。击败后转 P2：速度更快、招式扩充（大闪电、光弹、贯穿雷鸣践踏）。P2 50% 以下可召唤 3 个水晶（辅助攻击）。",
  "zh_tips": "P2 躲闪电与践踏；50% 以下注意水晶召唤物。",
  "dmg_zh": "物理、雷、光、暗"
 },
 {
  "id": "golden_grouch",
  "name": "Golden Grouch",
  "lore": "A sentient mascot costume, brought to life with the power of a mysterious entity known as \"The Deity\", an ethereal Soul Weaver. The soul inside the suit is that of an extreme substance abuser.\n\nThrough the help of an unknown third party, this entity was empowered with the Golden Galaxy Gas, giving it the power and means to enact whatever murderous rampage it wishes.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Golden Grouch\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|RESIST (0.55x)\n|-\n|LUMINOUS\n|WEAK (1.5x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|RESIST (0.5x)\n|-\n| colspan=\"3\" |Base HP: 18500\n|-\n| colspan=\"3\" |Damage: PHYSICAL and SHADOW\n|-\n| colspan=\"3\" |Can inflict: BLEEDING, BREACHED, DECAYED, FROZEN and HEAVY\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Golden Grouch battle consists of 2 sub-phases (stances), the sword phase, and the barehanded phase. The sub-phases have fully unique move sets.\nOnce per fight, Golden Grouch will have his sword knocked out of his hand upon falling below 70% HP, switching to the barehanded phase. The sword will be left as a passive entity next to the Gate. During the barehanded phase, Golden Grouch can perform a move which summons 6 Shadow Grouch enemies. This can be done up to 2 times.\n\nShadow Grouch has decaying HP, losing 3% of their MAX HP per second. Every 10 seconds, each Shadow Grouch grants Golden Grouch a small duration of the INVINCIBLE status effect.\n\nAfter falling below 40% HP in the barehanded phase, Golden Grouch will begin to run towards the dropped sword, picking it up and switching back to the sword phase. Golden Grouch in sword phase has an expanded moveset when below 50% HP.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by ruralist\n\nThe Grouch originally from \n\nMusic: \n\n== Fun Facts ==\nGolden Grouch was conceived as a mere joke, a \"What if\" if you will about all the different variations of Five Nights at Freddy's versions of Grouch you could have! Mantibro and ruralist spent the best part of an hour wheezing as they kept listing more off.\n\nAll voice-lines Golden Grouch says, compiled into one video:\n\nhttps://www.youtube.com/watch?v=V9pM73txJ9Y",
  "strategy": "The Golden Grouch battle consists of 2 sub-phases (stances), the sword phase, and the barehanded phase. The sub-phases have fully unique move sets.\nOnce per fight, Golden Grouch will have his sword knocked out of his hand upon falling below 70% HP, switching to the barehanded phase. The sword will be left as a passive entity next to the Gate. During the barehanded phase, Golden Grouch can perform a move which summons 6 Shadow Grouch enemies. This can be done up to 2 times.\n\nShadow Grouch has decaying HP, losing 3% of their MAX HP per second. Every 10 seconds, each Shadow Grouch grants Golden Grouch a small duration of the INVINCIBLE status effect.\n\nAfter falling below 40% HP in the barehanded phase, Golden Grouch will begin to run towards the dropped sword, picking it up and switching back to the sword phase. Golden Grouch in sword phase has an expanded moveset when below 50% HP.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by ruralist\n\nThe Grouch originally from \n\nMusic: \n\n== Fun Facts ==\nGolden Grouch was conceived as a mere joke, a \"What if\" if you will about all the different variations of Five Nights at Freddy's versions of Grouch you could have! Mantibro and ruralist spent the best part of an hour wheezing as they kept listing more off.\n\nAll voice-lines Golden Grouch says, compiled into one video:\n\nhttps://www.youtube.com/watch?v=V9pM73txJ9Y",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.55
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.5
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.5
   }
  },
  "hp": "18500",
  "damage": "PHYSICAL and SHADOW",
  "inflicts": "BLEEDING, BREACHED, DECAYED, FROZEN and HEAVY",
  "phases": "2",
  "desc": "The Forever Trapped",
  "phase": "Late Umbra",
  "icon": "icons/boss/Golden_Grouch_Icon.png",
  "zh_mech": "2 子阶段（架势）：持剑 + 空手，两套招式完全不同。每场一次：70% HP 时剑被打脱进入空手阶段，剑留在 Gate 旁成为被动实体；空手阶段可召唤 6 只 Shadow Grouch（最多 2 次）。",
  "zh_tips": "70% 转空手后警惕 Shadow Grouch 群；两阶段招式差异大需重新熟悉。",
  "dmg_zh": "物理、暗"
 },
 {
  "id": "abaddon",
  "name": "Abaddon",
  "lore": "The Apex mana predator.\nThe manalytes are a species of creatures completely made out of the mana absorbed from dead bodies inside the dimensional gate's dungeon. They are exceptionally aggressive and tend to live short lives due to needing more mana every time they grow. They are found generally in the middle levels of the dungeon resting and prowling around areas with a high concentration of ambient mana crystals.\n\nIt has been observed that during their later stages of evolution the manalytes known as \"elders\" tend to fight between each other and in some cases devour one another to gain greater mass and mana capacity. During the travels of the Sables guild team, a stampede of elder manalytes was observed on the lower layer as if they were running away from something. As the resource collection team of the guild approached the aftermath of the stampede to check on some of the remains, another scout near the main team heard a bunch of screams followed by sudden silence and a crunching sound. When the main team checked on the collection team, they were greeted by a scene of pure gore and viscera accompanied by what appeared to be a building sized monster. After examination from afar, the researcher of the team classified this monster as \"Abaddon\" as it's modus operandi of hunting appeared to be opening cracks in the dungeon to grab other elder manalytes to devour. From a skin sample it was determined that this monster may be more than 20,000 years old and insanely durable.\n\nA later report from the Albatross Kingdom's specialized mage team identified the creature's ability to resist tier 10 spells that could level an entire kingdom in seconds, as if they were a hot shower on tuesday. Holy element mages have been a requirement when accessing the mana crystal supplies on the lower levels as holy magic seemed to drive most of the creatures away and dimished the encounters with the deviant.\n\nNew adventurer teams have been warned to retreat the moment this monster is spotted and to report back to the guild.\n\n\"It appeared out of nowhere, killed and ate like it had been hungry for a thousand years\". \n\n- Sables Guild master, Jeremy.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Abaddon\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.5x)\n|-\n|FROST\n|RESIST (0.5x)\n|-\n|ELECTRIC\n|RESIST (0.5x)\n|-\n|LUMINOUS\n|WEAK (1.75x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|RESIST (0.5x)\n|-\n| colspan=\"3\" |Base HP: 32000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and SHADOW\n|-\n| colspan=\"3\" |Can inflict: BREACHED, DECAYED and HEAVY\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nAbbadon is a massive Manalyte that summons up to 3 Elder Manalytes to fight alongside him. He preforms massive AOE attacks which produce flaming pillars and fireballs alongside orbs of darkness which can apply decay to his opponent.\n\nUpon death, Abbadon sheds his skin and reaches second phase where the maximum amount of Manalytes he can spawn increases to 6. The majority of his attacks now pierce through his opponents defenses with an even larger radius. His most devastating move coming from a shockwave engulfing the majority of the battlefield.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic Phase 1: \n\nMusic Phase 2: \n\nAlso appears in !",
  "strategy": "Abbadon is a massive Manalyte that summons up to 3 Elder Manalytes to fight alongside him. He preforms massive AOE attacks which produce flaming pillars and fireballs alongside orbs of darkness which can apply decay to his opponent.\n\nUpon death, Abbadon sheds his skin and reaches second phase where the maximum amount of Manalytes he can spawn increases to 6. The majority of his attacks now pierce through his opponents defenses with an even larger radius. His most devastating move coming from a shockwave engulfing the majority of the battlefield.\n\n== Credits ==\nMade by Have and Mantibro\n\nMusic Phase 1: \n\nMusic Phase 2: \n\nAlso appears in !",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.5
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.5
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.5
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.75
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.5
   }
  },
  "hp": "32000",
  "damage": "PHYSICAL and SHADOW",
  "inflicts": "BREACHED, DECAYED and HEAVY",
  "phases": "2",
  "desc": "Demon of Destruction",
  "phase": "Eclipse",
  "icon": "icons/boss/AbbadonIcon.png",
  "zh_mech": "巨型 Manalyte，召唤最多 3 只 Elder Manalyte 并肩作战；大 AOE：火焰柱/火球 + 暗球（可挂衰减）。死亡蜕皮转 P2：召唤上限 6 只、多数招式贯穿防御且范围更大，最致命招来自...",
  "zh_tips": "P1 清召唤物控制场面；P2 贯穿 AOE 无法靠防御硬吃，躲开为主。",
  "dmg_zh": "物理、暗"
 },
 {
  "id": "khepri",
  "name": "Khepri",
  "lore": "Amongst the growing hatchlings of Queen Vesra’s offspring, there was one sealed cocoon. As new Peltapod larvae hatched, that one egg simply laid dormant. Not dead, but still growing, over many years, becoming stronger and stronger. Queen Vesra, knowing that she would not be able to protect her colony forever, laid one egg which she coddled to no end, day after day pouring as much magical energy into it as she could allow. If she were to ever fall, the egg would stop receiving her energy, which would then lead it to finally hatch.\n\nQueen Vesra can be at peace, knowing that after her passing, her precious offspring will be protected by a more than worthy successor.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Khepri\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 26000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and FROST\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and FROZEN\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Khepri fight consists of 2 phases. In Phase 2, Khepri will gain greatly increased mobility and the ability to fly.\n\nKhepri is capable of unleashing powerful ice attacks in a pizza cutter shape, these can be chained up to 3 times in a row. If players a far away in Phase 1, he can throw a deadly accurate ice spike which always inflicts the freeze debuff.\n\nIn Phase 2, if players are near Khepri, he may choose to scream. This will freeze everyone caught in the purple radius, and he will instantly transition into flying. While in flight, Khepri has the ability to both grab players and also throw out a shredding spread of ice projectiles, all inflicting a long freeze status.\n\n== Credits ==\nMade by Have, Scena and Mantibro\n\nOriginal Design from Solo Leveling and Chugong\n\nMusic Phase 1: \n\nMusic Phase 2:",
  "strategy": "The Khepri fight consists of 2 phases. In Phase 2, Khepri will gain greatly increased mobility and the ability to fly.\n\nKhepri is capable of unleashing powerful ice attacks in a pizza cutter shape, these can be chained up to 3 times in a row. If players a far away in Phase 1, he can throw a deadly accurate ice spike which always inflicts the freeze debuff.\n\nIn Phase 2, if players are near Khepri, he may choose to scream. This will freeze everyone caught in the purple radius, and he will instantly transition into flying. While in flight, Khepri has the ability to both grab players and also throw out a shredding spread of ice projectiles, all inflicting a long freeze status.\n\n== Credits ==\nMade by Have, Scena and Mantibro\n\nOriginal Design from Solo Leveling and Chugong\n\nMusic Phase 1: \n\nMusic Phase 2:",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "26000",
  "damage": "PHYSICAL and FROST",
  "inflicts": "BLEEDING and FROZEN",
  "phases": "2",
  "desc": "The Ant King",
  "phase": "Eclipse",
  "icon": "icons/boss/Khepri_Icon.png",
  "zh_mech": "2 阶段。P2 机动性大增并获得飞行。冰属性披萨刀攻击（可连发 3 次）；P1 远程必中冰锥（必挂冻结）；P2 近身可能尖叫——紫色半径内全员冻结并立即...",
  "zh_tips": "P1 别离太远（防必中冰锥）；P2 别贴脸（防尖叫冻结），躲披萨刀绕圈。",
  "dmg_zh": "物理、冰"
 },
 {
  "id": "pandora",
  "name": "Pandora",
  "lore": "At the end of the LEGION Project, we created something far beyond what we had intended.\n\nNo—perhaps they were what we truly needed all along. The Cores possessed by entities such as CODE: BLACK LILY were exactly what we had been searching for.\n\nHowever, handling them requires the utmost caution. If even a single specimen escapes containment, this timeline would likely collapse in short order.\n\nThe military power we originally possessed had its limits. Their armor was incredibly resilient, and conventional weaponry proved ineffective against them.\n\nThe conclusion we reached was simple:\n\nTo fight them with the same power.\n\nPandora is the final safeguard against our own arrogance, the last fortress built to contain calamity.\n\nNo matter how late it may be, it will eradicate those accursed monsters and protect hope itself.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Pandora\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.5x)\n|-\n|FROST\n|RESIST (0.3x)\n|-\n|ELECTRIC\n|RESIST (0.8x)\n|-\n|LUMINOUS\n|WEAK (1.1x)\n|-\n|SHADOW\n|RESIST (0.75x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 24000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and FROST\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and FROZEN\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nPandora is a flying boss that utilizes large ice AOE's and quick dashes to attack its opponents. It can create waves of ice shards that need to be jumped over and fire an ice lazer across the battle field.\n\nUpon reaching 50% HP it becomes more agressive, attacking with larger scale, more devastating attacks and soaring through the skies at high speed to deliver larger ice blasts that pierce through defenses.\n\n== Credits ==\nMade by BAKAME, MelonTM and Mantibro\n\nMusic Phase 1: \n\nMusic Phase 2: \n\nFirst appeared in !",
  "strategy": "Pandora is a flying boss that utilizes large ice AOE's and quick dashes to attack its opponents. It can create waves of ice shards that need to be jumped over and fire an ice lazer across the battle field.\n\nUpon reaching 50% HP it becomes more agressive, attacking with larger scale, more devastating attacks and soaring through the skies at high speed to deliver larger ice blasts that pierce through defenses.\n\n== Credits ==\nMade by BAKAME, MelonTM and Mantibro\n\nMusic Phase 1: \n\nMusic Phase 2: \n\nFirst appeared in !",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.5
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.3
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.8
   },
   "LUMINOUS": {
    "status": "WEAK",
    "mult": 1.1
   },
   "SHADOW": {
    "status": "RESIST",
    "mult": 0.75
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "24000",
  "damage": "PHYSICAL and FROST",
  "inflicts": "BLEEDING and FROZEN",
  "phases": "2",
  "desc": "The Arrogance Safeguard",
  "phase": "Eclipse",
  "icon": "icons/boss/Pandora_Icon.png",
  "zh_mech": "飞行 Boss：大型冰 AOE + 快速突进；冰刃波（需跳跃躲避）+ 覆盖战场的冰激光。50% HP 后更激进：更大规模毁灭性攻击，高速俯冲释放贯穿防御的大冰爆。",
  "zh_tips": "冰刃波用跳跃躲；激光横向闪避；50% 后警惕贯穿冰爆。",
  "dmg_zh": "物理、冰"
 },
 {
  "id": "bravera",
  "name": "Bravera",
  "lore": "Created as the most efficient centralized processor for the Opton Empire, O-O1000 \"Bravera\" exists purely to calculate thousands of operations in any given moment while fully connected to every automaton of the Opton Empire. All of this to fulfill the unreversible prime directive, to eliminate the FOX Empire. As the most powerful automaton in the universe, Commander Bravera is equipped with terrifying combat capabilities, ones which are rarely displayed due to the efficiency of the automatons' operations.\n\nHaving a hybrid power source consisting of both Opton energy as well as the Rift Energy which drives FOX Pilots he was instructed to eliminate, the Commander strikes a perfect balance between tremendous power and energy output, as well as pure, uninhibited computational efficiency. Unhampered by the burden of sapience and conscience abundant within the FOX, Bravera is easily able to exterminate one FOX Colony after another, while actively planning the extermination of hundreds more.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Bravera\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|RESIST (0.5x)\n|-\n|ELECTRIC\n|RESIST (0.5x)\n|-\n|LUMINOUS\n|RESIST (0.5x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|WEAK (1.25x)\n|-\n| colspan=\"3\" |Base HP: 28000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and ELECTRIC\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and PARALYZED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Bravera fight consists of 2 phases. In Phase 1, Bravera will spawn with 2 Opton Guards. The Opton Guards will seek out the player in the lobby with the lowest HP, and constantly harass them. The guards are not required to be killed to hurt Bravera, so its up to the team to decide who to go after.\n\nIn Phase 1, once Bravera reaches 50% HP, he will unlock 2 new moves. He can now use his Corkscrew Leap to cover long distances, and may end his lunges in a powerful, single striking Pizza-cutter.\n\nOnce Phase 2 begins, Bravera will unlock a new moveset. This moveset is much more agile than the first, with intense melee combos and the ability to sprint, making Bravera is very difficult to escape from without teammate support. At 50% HP in Phase 2, Bravera will be able to use an enhanced version of his previous Pizza-cutter, now striking twice, and also being useable at any point.\n\n== Credits ==\nMade by Mantibro\n\nMusic Phase 1: \n\nMusic Phase 2: \n\n also appears in Terrors of Nowhere",
  "strategy": "The Bravera fight consists of 2 phases. In Phase 1, Bravera will spawn with 2 Opton Guards. The Opton Guards will seek out the player in the lobby with the lowest HP, and constantly harass them. The guards are not required to be killed to hurt Bravera, so its up to the team to decide who to go after.\n\nIn Phase 1, once Bravera reaches 50% HP, he will unlock 2 new moves. He can now use his Corkscrew Leap to cover long distances, and may end his lunges in a powerful, single striking Pizza-cutter.\n\nOnce Phase 2 begins, Bravera will unlock a new moveset. This moveset is much more agile than the first, with intense melee combos and the ability to sprint, making Bravera is very difficult to escape from without teammate support. At 50% HP in Phase 2, Bravera will be able to use an enhanced version of his previous Pizza-cutter, now striking twice, and also being useable at any point.\n\n== Credits ==\nMade by Mantibro\n\nMusic Phase 1: \n\nMusic Phase 2: \n\n also appears in Terrors of Nowhere",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.5
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.5
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.5
   },
   "SHADOW": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "POISON": {
    "status": "WEAK",
    "mult": 1.25
   }
  },
  "hp": "28000",
  "damage": "PHYSICAL and ELECTRIC",
  "inflicts": "BLEEDING and PARALYZED",
  "phases": "2",
  "desc": "The Opton Commander",
  "phase": "Late Eclipse",
  "icon": "icons/boss/Bravera_Icon.png",
  "zh_mech": "2 阶段。P1 开场带 2 名 Opton Guard：锁定全队当前最低 HP 的玩家持续骚扰；Guard 不必击杀即可伤害 Bravera。50% 解锁 2 新招：开瓶钻跳跃（远距离位移）与突进收尾的强力披萨刀。",
  "zh_tips": "Guard 会追最低血队友，团队需决定先清 Guard 还是直接打 Boss；50% 后防远距跳跃突进。",
  "dmg_zh": "物理、雷"
 },
 {
  "id": "o-one",
  "name": "O-One",
  "lore": "O-OOOO1 was constructed as a prototype automaton, sent to the planet MBS-02 to act as a surveyor and a test of the Operative Automaton design. After cutting contact with the Opton overlord, the lone prototype was left to explore the planet and form his own directives, on his own terms. On the planet, he became the closest comrade of Sir Alux, a legendary figure within the FOX, the one who was to protect and serve the King directly, and the one who gifted the disposable soldier with the name \"O-One.\" After the planet’s liberation, the mercenary known on the planet as The Smiling Opton managed to escape the planet as one of its very few survivors, scarred after witnessing the agonizing death of Alux caused by the planet’s infectious nanomachines. After years of exploration and a period of strength conditioning to learn to overclock his body’s energy output at the expense of its longevity, O-One isolated himself to the existence of a hermit, unconvinced in being able to find any purpose, now wielding an exact replica of Sir Alux’s longsword which he had trained to be proficient with through remembering the fighting style of his old comerade, also adorned with a hat closely resembling that which Alux used to wear.\n\nAs the Opton War against the FOX Empire raged on and the tales of his existence spread, it was inevitable for him to be eventually found and admired as a survivor of the MBS Incident, and asked to assist with the conflict. While his unyielding self found no drive to assist an intergalactic Empire, he did decide to swear upon himself a solemn vow. He was to live for just as long as the Empire he was born with, no more, no less. Perhaps it was his intrigue and and the questions Alux left him with which eventually made him eager to learn about the \"beings of conscience\" which his comrade was adamant in deeply respecting.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |O-One\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|WEAK (1.25x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 16000\n|-\n| colspan=\"3\" |Damage: PHYSICAL\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and PARALYZED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nO-One's battle has two phases.\n\nIn the first he wields a small battle axe with a pistol. He typically circles around his opponents firing shots at them and occasionally dashes in to strike them with his axe. He mostly repeats this cycle of staying far to shoot and coming in to slash with his high speeds.\n\nOnce his health reaches 40% he will change out his weapons for a single sword and attack his opponents at close range with even more speed and new attacks.\n\n== Credits ==\nMade by Mantibro\n\nVoiced by Mapleveins\n\nMusic Phase 1: \n\nMusic Phase 2: \n\n== Additional Information ==\n\nLikes Shawarma.",
  "strategy": "O-One's battle has two phases.\n\nIn the first he wields a small battle axe with a pistol. He typically circles around his opponents firing shots at them and occasionally dashes in to strike them with his axe. He mostly repeats this cycle of staying far to shoot and coming in to slash with his high speeds.\n\nOnce his health reaches 40% he will change out his weapons for a single sword and attack his opponents at close range with even more speed and new attacks.\n\n== Credits ==\nMade by Mantibro\n\nVoiced by Mapleveins\n\nMusic Phase 1: \n\nMusic Phase 2: \n\n== Additional Information ==\n\nLikes Shawarma.",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FROST": {
    "status": "WEAK",
    "mult": 1.25
   },
   "ELECTRIC": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "16000",
  "damage": "PHYSICAL",
  "inflicts": "BLEEDING and PARALYZED",
  "phases": "2",
  "desc": "The First Opton",
  "phase": "Late Eclipse",
  "icon": "icons/boss/O_One_Icon.png",
  "zh_mech": "2 阶段。P1 小战斧 + 手枪：绕圈射击、偶尔突进斧击，高速循环远近。40% HP 换单剑近战：速度更快 + 新招式。",
  "zh_tips": "P1 防枪线、防突进；40% 后转为近战节奏，注意更快连击。",
  "dmg_zh": "物理"
 },
 {
  "id": "neo_pilot",
  "name": "Neo Pilot",
  "lore": "Having witnessed hundreds of years of death and disfigurement of her closest friends and comrades, and with a terrifying sight of a horrifying scale of destruction of the Temperance Colony still fresh in her mind, the Pilot of Neo chose to absorb herself in a meaningless existence of consumption an indulgence, turning her Neo Colony into a debauched place of endless gluttony, parties, and a way to isolate and disassociate herself from the struggles and tribulations of the FOX Empire. She used her gregarious and bubbly persona as a shield and coping mechanism against the worsening state of the Empire she held a major role in. Even as it was being rapidly exterminated in the Opton War, she was far too broken and hopeless to stand up and fight for her kin. Each new tragedy simply made her isolate even deeper. After the death of the Pilot of Onyx, she was officially titled as the strongest Combat Pilot of the FOX Empire. She was eventually forced to endure a hard wake-up call when the Neo Colony was attacked by the automatons. Without a place of comfort and shelter, Neo Pilot began to sink into the pits of despair she had opened for herself.\n\nAnd yet, as her Empire was nearing the threat of total extermination, she was made to realize her purpose. In spite of how completely hopeless the chances stood for the FOX Empire, and how quickly their inevitable defeat was approaching, the FOX never once thought of giving up, and were fully ready to struggle to the bitter end. The legacy of the long-lost humanity still fully lived on in the spirits of the FOX. It was not something a band of thoughtless automatons had a right to extinguish.\n\nBeing one of the few known to have a fighting chance to overpower Commander Bravera, she knew what had to be done to make things right.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Neo Pilot\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|WEAK (1.25x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|RESIST (0.75x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|WEAK (1.25x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 27000\n|-\n| colspan=\"3\" |Damage: PHYSICAL and ELECTRIC\n|-\n| colspan=\"3\" |Can inflict: BLEEDING and PARALYZED\n|-\n| colspan=\"3\" |Phases: 2\n|}\n\n== Strategy ==\nThe Neo Pilot fight consists of 2 sub-phases. If players enter the air against Neo Pilot, she will leap towards them and attempt to kick them twice. These kicks have a chance to inflict the Heavy status effect.\n\nIn her regular state, Neo Pilot will stick to slashes and strafes. Upon reaching 70% HP, she will start jumping at players from long distances. \n\nOnce per fight, upon reaching 40% HP, Neo Pilot will enter sub-phase 2. She will heal a large portion of health and imbue all of her leaps with electric shockwaves that players must jump over to dodge. Her melee attacks also gain a significant speed boost. Once she reaches 40% HP again, Neo Pilot will unlock two powerful new moves. The first is a forward facing tankbuster that comes out almost instantly, requiring players to keep distance. Her second move is a rapid striking, triple pizza-cutter.\n\n== Credits ==\nMade by Beyond, Honda, Mantibro and THEDAO77\n\nVoiced by JUSTJ3NNY\n\nMusic: \n\nFirst seen in \n\nAlso appears in",
  "strategy": "The Neo Pilot fight consists of 2 sub-phases. If players enter the air against Neo Pilot, she will leap towards them and attempt to kick them twice. These kicks have a chance to inflict the Heavy status effect.\n\nIn her regular state, Neo Pilot will stick to slashes and strafes. Upon reaching 70% HP, she will start jumping at players from long distances. \n\nOnce per fight, upon reaching 40% HP, Neo Pilot will enter sub-phase 2. She will heal a large portion of health and imbue all of her leaps with electric shockwaves that players must jump over to dodge. Her melee attacks also gain a significant speed boost. Once she reaches 40% HP again, Neo Pilot will unlock two powerful new moves. The first is a forward facing tankbuster that comes out almost instantly, requiring players to keep distance. Her second move is a rapid striking, triple pizza-cutter.\n\n== Credits ==\nMade by Beyond, Honda, Mantibro and THEDAO77\n\nVoiced by JUSTJ3NNY\n\nMusic: \n\nFirst seen in \n\nAlso appears in",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "WEAK",
    "mult": 1.25
   },
   "FROST": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.75
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "WEAK",
    "mult": 1.25
   },
   "POISON": {
    "status": "NEUTRAL",
    "mult": 1.0
   }
  },
  "hp": "27000",
  "damage": "PHYSICAL and ELECTRIC",
  "inflicts": "BLEEDING and PARALYZED",
  "phases": "2",
  "desc": "Empress of FOX",
  "phase": "Late Eclipse",
  "icon": "icons/boss/Neo_Pilot_Icon.png",
  "zh_mech": "2 子阶段。玩家跳空会触发她跃起二连踢（几率挂沉重）；常规状态斩击 + 横移；70% 开始远距离跳扑。每场一次 40% 进 P2：回复大量血量且所有跳跃附带强化。",
  "zh_tips": "别随意跳空（吃二连踢）；70% 后防远跳扑；40% 转阶段回血。",
  "dmg_zh": "物理、雷"
 },
 {
  "id": "jim_c._bringer",
  "name": "Jim C. Bringer",
  "lore": "The founder, owner and CEO of the Bringer Company, a centralized corporation specializing in research and manufacturing of heavy weaponry which utilize Min-Max technology from the Meta of the Faction Wars. The company is headquartered in a massive, wedge-shaped floating mothership, The Singularity.\n\nJim himself was a combatant of the Faction Wars, once being a member of the clan IZK, a.k.a Izakia. Under the guidance and mentorship of Bob H. Dee, one of the most knowledgeable and efficient Min-Maxers, he eventually become highly proficient in creating extremely efficient machines of the Meta War. During the war, he created what he dubbed the Triple Entente, which consisted of three highly advanced armored vehicles. The C. Flipper, #REDACTED# and #REDACTED#.\n\nThe first was a wedge-shaped heavily armored tracked vehicle, capable of reaching speeds of up to 130 MPH, being able to accelerate to 100 MPH in less than 5 seconds. Its combat role was to ram itself into enemy tanks to then send them flying, rendering them defenseless.\n\nThe second, a streamlined Main Battle Tank whose turret was shaped like a #REDACTED#. Built as an experiment to attempt to recreate the technology of The Khabib, the most feared and powerful tank belonging to ISA, the Inner Sphere Alliance, a rival faction to IZK. The #REDACTED# was capable of reaching speeds of 300 MPH, with a 0-100 time of less than half a second.\n\nThe third, and most powerful of the Triple Entente, a humongous wedge with an excessively large rotary autocannon, all driven by a single, imbalanced monowheel.\n\nJim was a witness of the covert operation done by Malleus C. Gaming, which allowed IZK to steal The Khabib and expose the alien technology that allowed its armor to have the ability to become completely impermeable to any and all kinetic attacks.\n\nJim, according to his former Meta War peers, is considered \"unapologetically and unfathomably ####### stupid.\" In spite of this, he considers himself to be a mastermind tactician who can easily overwhelm any opponent with his \"perfect plan.\" In reality, the plans and tactics concocted by Jim would be consistently considered tactically nonsensical, usually involving a lot of wasted resources and unnecessary steps, and would be extremely unlikely to bring positive results. However, when the plan is set in motion, any and all weaknesses are easily resolved by Jim's pure brute strength, which in turn leads Jim to believe his tactics were impeccable, further reinforcing his self-perceived intelligence.\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Jim C. Bringer (Phase 1 and 2)\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|NEUTRAL (1x)\n|-\n|FROST\n|NEUTRAL (1x)\n|-\n|ELECTRIC\n|NEUTRAL (1x)\n|-\n|LUMINOUS\n|NEUTRAL (1x)\n|-\n|SHADOW\n|NEUTRAL (1x)\n|-\n|POISON\n|NEUTRAL (1x)\n|-\n| colspan=\"3\" |Base HP: 50000\n|-\n| colspan=\"3\" |Damage: PHYSICAL\n|-\n| colspan=\"3\" |Can inflict: -\n|}\n{| class=\"wikitable\" style=\"background:#000000; color:#ffffff; border:1px solid #444;\"\n| colspan=\"3\" |Jim C. Bringer (Phase 3)\n|-\n| rowspan=\"8\" |\n|Affinity\n|Resistance\n|-\n|PHYSICAL\n|NEUTRAL (1x)\n|-\n|FIRE\n|RESIST (0.75x)\n|-\n|FROST\n|RESIST (0.75x)\n|-\n|ELECTRIC\n|RESIST (0.75x)\n|-\n|LUMINOUS\n|RESIST (0.75x)\n|-\n|SHADOW\n|RESIST (0.75x)\n|-\n|POISON\n|RESIST (0.75x)\n|-\n| colspan=\"3\" |Base HP: 50000\n|-\n| colspan=\"3\" |Damage: PHYSICAL\n|-\n| colspan=\"3\" |Can inflict: BLEEDING\n|}\n\n== Strategy ==\nAll of Jim's direct Melee Attacks will deal PURPLE Damage!\n\nPhase 1: During Phase 1, Jim is neutral to all forms of damage. While attacking, he will throw out powerful, long reaching punches while ignoring any form of attention grabbing abilites, as his aggro is entirely random in all phases of the fight. Upon reaching 70% HP, Jim will unlock more moves, including a long distance leap and his infamously powerful laser. Upon reaching 40% HP, Jim will be able to perform Cataclysm, a long channeling and near arena sized nuke. Standing within the center radius of Cataclysm will instantly kill, but the damage slowly ramps down as you exit and get further from the center. He will be passive for a long time after performing Cataclysm, so it's advised to take this time to restore your team's health and revive any dead players once Cataclysm is over.\n\nAt 70%, 50%, and 30% HP, Jim will pause to summon a Jim's Wedge, a powerful supporting enemy which fires from long distances.\n\nPhase 2: Phase 2 begins with Jim entering the Flipper MK.II Abyssal, which he will remain in for the entire phase. The Flipper is immune to any and all damage, considering any damage as Blocked. It has access to 3 moves. It can ram players at extreme speeds dealing heavy purple damage, it can deploy a Jim's Wedge, and it can launch a barrage of rockets at targets from any distance.\n\nOnce 2 minutes have passed, 4 Signal Towers will drop in each corner of the arena. Players must stand inside these Signal Towers to charge them. Alone, these Signal Towers take 30 seconds to charge, but this duration increases with the lobby's player count. Several players standing under one Signal Tower will increase how quickly it charges. Once all 4 Signal Towers have been charged, an orbital strike will land on the Flipper, destroying it.\n\nPhase 3: Phase 3 consists of 2 sub-phases. Jim will behave similarly to the original Phase 1, however his entire moveset has been powered up. He swings much faster, combos for longer, and unlocks extremely powerful combo chain enders. Jim will also now gain a 0.75x resistance to all elements with the exception of Physical. \n\nUpon reaching 70% HP, Jim will unlock the same moves as before, but once again these moves have been enhanced. His laser is wider and faster, and his leap will deal more damage. Jim may now also teleport to players who are far away, or teleport mid-combo to catch players off guard.\n\nUpon reaching 50% HP, sub-phase 2 will begin. With a long cooldown, a Product Barrel will drop in the arena. The barrel will drop directly opposite to the side of the arena where Jim is standing. Jim will become invincible, and begin jogging towards the barrel. Players must destroy the barrel before Jim reaches it. If Jim reaches the barrel, he will consume it, healing a large portion of HP and granting a long Empowered and Enforced buff. If Jim heals above 50% HP from this, he will not be able to drop any more barrels until he reaches that health threshold again.\n\nJim's moveset will expand one more time, unlocking powerful moves which often effect the whole arena. Nutnado, a powerful tornado which pulls players into the air. Nutdust, an arena wide gravity slam which will only damage players who are airborne, inflicting a lasting Heavy status effect. Tableflip, where Jim will ground himself and target the entire arena in the direction he is facing, dealing damage from both the impact and the wave that follows. Finally, at 40% HP, Jim will once again gain access to Cataclysm.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by MRCOWBOY\n\nMusic Phase 1: \n\nMusic Phase 2: \n\nMusic Phase 3: \n\nOriginal Model Design from Team Fortress 2 by VALVE",
  "strategy": "All of Jim's direct Melee Attacks will deal PURPLE Damage!\n\nPhase 1: During Phase 1, Jim is neutral to all forms of damage. While attacking, he will throw out powerful, long reaching punches while ignoring any form of attention grabbing abilites, as his aggro is entirely random in all phases of the fight. Upon reaching 70% HP, Jim will unlock more moves, including a long distance leap and his infamously powerful laser. Upon reaching 40% HP, Jim will be able to perform Cataclysm, a long channeling and near arena sized nuke. Standing within the center radius of Cataclysm will instantly kill, but the damage slowly ramps down as you exit and get further from the center. He will be passive for a long time after performing Cataclysm, so it's advised to take this time to restore your team's health and revive any dead players once Cataclysm is over.\n\nAt 70%, 50%, and 30% HP, Jim will pause to summon a Jim's Wedge, a powerful supporting enemy which fires from long distances.\n\nPhase 2: Phase 2 begins with Jim entering the Flipper MK.II Abyssal, which he will remain in for the entire phase. The Flipper is immune to any and all damage, considering any damage as Blocked. It has access to 3 moves. It can ram players at extreme speeds dealing heavy purple damage, it can deploy a Jim's Wedge, and it can launch a barrage of rockets at targets from any distance.\n\nOnce 2 minutes have passed, 4 Signal Towers will drop in each corner of the arena. Players must stand inside these Signal Towers to charge them. Alone, these Signal Towers take 30 seconds to charge, but this duration increases with the lobby's player count. Several players standing under one Signal Tower will increase how quickly it charges. Once all 4 Signal Towers have been charged, an orbital strike will land on the Flipper, destroying it.\n\nPhase 3: Phase 3 consists of 2 sub-phases. Jim will behave similarly to the original Phase 1, however his entire moveset has been powered up. He swings much faster, combos for longer, and unlocks extremely powerful combo chain enders. Jim will also now gain a 0.75x resistance to all elements with the exception of Physical. \n\nUpon reaching 70% HP, Jim will unlock the same moves as before, but once again these moves have been enhanced. His laser is wider and faster, and his leap will deal more damage. Jim may now also teleport to players who are far away, or teleport mid-combo to catch players off guard.\n\nUpon reaching 50% HP, sub-phase 2 will begin. With a long cooldown, a Product Barrel will drop in the arena. The barrel will drop directly opposite to the side of the arena where Jim is standing. Jim will become invincible, and begin jogging towards the barrel. Players must destroy the barrel before Jim reaches it. If Jim reaches the barrel, he will consume it, healing a large portion of HP and granting a long Empowered and Enforced buff. If Jim heals above 50% HP from this, he will not be able to drop any more barrels until he reaches that health threshold again.\n\nJim's moveset will expand one more time, unlocking powerful moves which often effect the whole arena. Nutnado, a powerful tornado which pulls players into the air. Nutdust, an arena wide gravity slam which will only damage players who are airborne, inflicting a lasting Heavy status effect. Tableflip, where Jim will ground himself and target the entire arena in the direction he is facing, dealing damage from both the impact and the wave that follows. Finally, at 40% HP, Jim will once again gain access to Cataclysm.\n\n== Credits ==\nMade by Scena and Mantibro\n\nVoiced by MRCOWBOY\n\nMusic Phase 1: \n\nMusic Phase 2: \n\nMusic Phase 3: \n\nOriginal Model Design from Team Fortress 2 by VALVE",
  "affinity": {
   "PHYSICAL": {
    "status": "NEUTRAL",
    "mult": 1.0
   },
   "FIRE": {
    "status": "RESIST",
    "mult": 0.75
   },
   "FROST": {
    "status": "RESIST",
    "mult": 0.75
   },
   "ELECTRIC": {
    "status": "RESIST",
    "mult": 0.75
   },
   "LUMINOUS": {
    "status": "RESIST",
    "mult": 0.75
   },
   "SHADOW": {
    "status": "RESIST",
    "mult": 0.75
   },
   "POISON": {
    "status": "RESIST",
    "mult": 0.75
   }
  },
  "hp": "50000",
  "damage": "PHYSICAL",
  "inflicts": "-",
  "phases": "",
  "desc": "The Man of Many Titles",
  "phase": "HC Armor Plating",
  "icon": "icons/boss/Jim_C._Bringer_Icon.png",
  "zh_mech": "所有直接近战攻击都是紫色伤害（无视防御）！P1 对全部伤害属性中性；攻击为长距离重拳，无视嘲讽（全阶段仇恨完全随机）。70% 解锁更多招式：远距离跳跃 + 著名的激光。40% 可释放 Cataclysm（长时间引导的毁灭技）。",
  "zh_tips": "全阶段仇恨随机，无法靠嘲讽拉稳；近战全是紫伤——看到起手就躲；40% 后 Cataclysm 引导期立即远离/打断。",
  "dmg_zh": "物理"
 }
]
ENEMIES = [
 {
  "id": "fly",
  "name": "Fly",
  "damage": "物理",
  "debuffs": [],
  "mech": [],
  "phase": "Prime",
  "icon": "icons/enemy/Fly.png",
  "tips": "物理小飞虫（Beelzebub 战最多 9 只同时在场）——群攻/范围技能清掉即可。"
 },
 {
  "id": "voltwall",
  "name": "Voltwall",
  "damage": "雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "phase": "Prime",
  "icon": "icons/enemy/Status_Stun.png",
  "tips": "电系远程怪，弹幕可挂麻痹——保持移动躲避；麻痹会强制破盾法格挡并瘫痪，T 位建议出麻痹抗性（社区实测）。"
 },
 {
  "id": "frost_sac",
  "name": "Frost Sac",
  "damage": "冰",
  "debuffs": [
   "冰冻"
  ],
  "mech": [],
  "phase": "Prime",
  "icon": "icons/enemy/Status_Frozen.png",
  "tips": "冰弹幕怪，可挂冰冻——保持移动，被冻后让队友/净化处理。"
 },
 {
  "id": "peltapod",
  "name": "Peltapod",
  "damage": "物理",
  "debuffs": [
   "出血"
  ],
  "mech": [
   "正面格挡"
  ],
  "phase": "Prime",
  "icon": "icons/enemy/Status_Bleed.png",
  "tips": "正面格挡近战攻击——绕到侧面或背后输出，正面硬刚会被挡下。弱暗（社区实测暗属性散弹一颗 60+）。"
 },
 {
  "id": "acolyte",
  "name": "Acolyte",
  "damage": "物理、毒",
  "debuffs": [
   "中毒"
  ],
  "mech": [],
  "phase": "Late Primal",
  "icon": "icons/enemy/Status_Poison.png",
  "tips": "物理+毒，可挂中毒——别站毒池，中毒后及时回复/净化。"
 },
 {
  "id": "lava_sac",
  "name": "Lava Sac",
  "damage": "火",
  "debuffs": [
   "灼烧"
  ],
  "mech": [],
  "phase": "Late Primal",
  "icon": "icons/enemy/Status_Fire.png",
  "tips": "火弹幕怪，可挂灼烧——保持移动，别站火池。"
 },
 {
  "id": "too_tired",
  "name": "Too Tired",
  "damage": "物理",
  "debuffs": [],
  "mech": [],
  "phase": "Late Primal",
  "icon": "icons/enemy/TooTired.png",
  "tips": "物理——无特殊机制，常规输出。"
 },
 {
  "id": "cone_bomber",
  "name": "Cone Bomber",
  "damage": "物理",
  "debuffs": [],
  "mech": [
   "紫色攻击（无视防御）"
  ],
  "phase": "Penumbra",
  "icon": "icons/enemy/ConeBomber.png",
  "tips": "物理+紫色攻击——紫色攻击无视防御但一定有蓄力提示（社区实测），看到紫蓄力立即远离。"
 },
 {
  "id": "cone_enforcer",
  "name": "Cone Enforcer",
  "damage": "物理",
  "debuffs": [],
  "mech": [
   "红绿灯机制（红灯停）",
   "红绿灯机制（绿灯行"
  ],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Stop.png",
  "tips": "红绿灯机制：红灯时停下别动（移动会吃伤害），绿灯时再移动/输出；与 Cone Head Boss 同机制，观察灯色再走。"
 },
 {
  "id": "ice_squid",
  "name": "Ice Squid",
  "damage": "冰",
  "debuffs": [
   "冰冻"
  ],
  "mech": [],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Frozen.png",
  "tips": "冰系，可挂冰冻——移动躲冰弹。"
 },
 {
  "id": "black_lily_token",
  "name": "Black Lily Token",
  "damage": "光",
  "debuffs": [
   "虚弱"
  ],
  "mech": [],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Weak.png",
  "tips": "光系，可挂虚弱——虚弱削减输出，优先清掉（Boss 战最多同时 3 个）。"
 },
 {
  "id": "black_lily_token",
  "name": "Black Lily Token",
  "damage": "光",
  "debuffs": [
   "虚弱"
  ],
  "mech": [],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Weak.png",
  "tips": "光系，可挂虚弱——虚弱削减输出，优先清掉（Boss 战最多同时 3 个）。"
 },
 {
  "id": "carnie",
  "name": "Carnie",
  "damage": "火、毒",
  "debuffs": [
   "中毒"
  ],
  "mech": [
   "紫色攻击（无视防御）"
  ],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Fire.png",
  "tips": "火+毒双属性，区域攻击全是紫色（无视防御）——躲开地面火/毒区域，紫蓄力时远离。"
 },
 {
  "id": "curious_creature",
  "name": "Curious Creature",
  "damage": "物理",
  "debuffs": [
   "出血"
  ],
  "mech": [
   "正面格挡"
  ],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Bleed.png",
  "tips": "同 Peltapod：正面格挡，绕侧/背后攻击。"
 },
 {
  "id": "voltwalker",
  "name": "Voltwalker",
  "damage": "雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "phase": "Penumbra",
  "icon": "icons/enemy/Status_Stun.png",
  "tips": "电系怪，可挂麻痹——同 Voltwall：躲弹幕，T 位备麻痹抗性。"
 },
 {
  "id": "lizord",
  "name": "Lizord",
  "damage": "火",
  "debuffs": [
   "灼烧"
  ],
  "mech": [],
  "phase": "Late Penumbra",
  "icon": "icons/enemy/Status_Fire.png",
  "tips": "火系，灼烧——移动躲避火球。"
 },
 {
  "id": "manalyte",
  "name": "Manalyte",
  "damage": "暗",
  "debuffs": [
   "破甲"
  ],
  "mech": [],
  "phase": "Late Penumbra",
  "icon": "icons/enemy/Status_Breach.png",
  "tips": "暗系，可挂破甲——破甲后防御降低，被挂破甲时别硬吃大伤害。"
 },
 {
  "id": "ash_horn",
  "name": "Ash Horn",
  "damage": "火",
  "debuffs": [
   "灼烧"
  ],
  "mech": [],
  "phase": "Antumbra",
  "icon": "icons/enemy/Status_Fire.png",
  "tips": "火系，灼烧——同 Lizord。"
 },
 {
  "id": "concrete_revanent",
  "name": "Concrete Revanent",
  "damage": "物理",
  "debuffs": [],
  "mech": [],
  "phase": "Antumbra",
  "icon": "icons/enemy/Concrete_Golem.png",
  "tips": "物理——常规输出，注意近战距离。"
 },
 {
  "id": "mother_sac",
  "name": "Mother Sac",
  "damage": "火、冰",
  "debuffs": [
   "冰冻"
  ],
  "mech": [],
  "phase": "Antumbra",
  "icon": "icons/enemy/Status_Fire.png",
  "tips": "火+冰双属性弹幕，可挂灼烧与冰冻——移动躲避，异常及时处理。"
 },
 {
  "id": "volt_buster",
  "name": "Volt Buster",
  "damage": "雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "phase": "Antumbra",
  "icon": "icons/enemy/Status_Stun.png",
  "tips": "电系怪，麻痹 debuff——躲闪电，T 位备麻痹抗性。"
 },
 {
  "id": "aspiopod",
  "name": "Aspiopod",
  "damage": "物理",
  "debuffs": [],
  "mech": [
   "正面格挡"
  ],
  "phase": "Umbra",
  "icon": "icons/enemy/Aspiopod.png",
  "tips": "正面格挡，绕侧/背后攻击。"
 },
 {
  "id": "black_virtue",
  "name": "Black Virtue",
  "damage": "光",
  "debuffs": [
   "衰减"
  ],
  "mech": [],
  "phase": "Umbra",
  "icon": "icons/enemy/Status_Weak.png",
  "tips": "光系，虚弱+衰减——优先清，别让它持续叠 debuff。"
 },
 {
  "id": "big_sigma",
  "name": "Big Sigma",
  "damage": "光",
  "debuffs": [
   "衰减"
  ],
  "mech": [],
  "phase": "Umbra",
  "icon": "icons/enemy/Status_Weak.png",
  "tips": "光系，虚弱+衰减——同 Black Virtue，优先清。"
 },
 {
  "id": "cloud_dragonkin",
  "name": "Cloud Dragonkin",
  "damage": "火、雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "phase": "Umbra",
  "icon": "icons/enemy/Status_Fire.png",
  "tips": "火+雷，灼烧+麻痹——移动躲弹幕，麻痹注意（破格挡）。"
 },
 {
  "id": "elder_manalyte",
  "name": "Elder Manalyte",
  "damage": "暗",
  "debuffs": [
   "破甲"
  ],
  "mech": [],
  "phase": "Umbra",
  "icon": "icons/enemy/Status_Breach.png",
  "tips": "暗系，可挂破甲（Abaddon 战召唤）——优先处理召唤物或躲开破甲弹。"
 },
 {
  "id": "shamanic_compound",
  "name": "Shamanic Compound",
  "damage": "物理、毒",
  "debuffs": [
   "衰减"
  ],
  "mech": [],
  "phase": "Umbra",
  "icon": "icons/enemy/Status_Poison.png",
  "tips": "物理+毒，中毒+衰减——别站毒池，清 debuff 优先。"
 },
 {
  "id": "eclipse_warden",
  "name": "Eclipse Warden",
  "damage": "光",
  "debuffs": [
   "衰减"
  ],
  "mech": [],
  "phase": "Late Umbra",
  "icon": "icons/enemy/Status_Weak.png",
  "tips": "光系，虚弱+衰减——保持距离输出，debuff 及时处理。"
 },
 {
  "id": "peltapod_guard",
  "name": "Peltapod Guard",
  "damage": "物理",
  "debuffs": [],
  "mech": [
   "可自增益（强力+坚守）",
   "自增益：强力",
   "自增益：坚守"
  ],
  "phase": "Eclipse",
  "icon": "icons/enemy/Status_Empower.png",
  "tips": "破武器后自增益（强力+坚守）——在其武器被破坏前尽快击杀；Vesra 战击杀它可破茧。"
 },
 {
  "id": "nightwalker",
  "name": "Nightwalker",
  "damage": "暗",
  "debuffs": [
   "破甲"
  ],
  "mech": [],
  "phase": "Eclipse",
  "icon": "icons/enemy/Status_Breach.png",
  "tips": "暗系，可挂破甲——同 Manalyte。"
 },
 {
  "id": "black_chimera",
  "name": "Black Chimera",
  "damage": "光",
  "debuffs": [
   "衰减"
  ],
  "mech": [],
  "phase": "Late Eclipse",
  "icon": "icons/enemy/Status_Weak.png",
  "tips": "光系，虚弱+衰减——高阶段怪，保持距离，debuff 及时净化。"
 }
]
BOSS_ENEMIES = [
 {
  "id": "fly",
  "name": "Fly",
  "damage": "物理",
  "debuffs": [],
  "mech": [],
  "boss": "Beelzebub Fight",
  "icon": "icons/enemy/FlyBeelze.png"
 },
 {
  "id": "peltapod",
  "name": "Peltapod",
  "damage": "物理",
  "debuffs": [
   "出血"
  ],
  "mech": [],
  "boss": "Vesra Fight",
  "icon": "icons/enemy/Status_Bleed.png"
 },
 {
  "id": "peltapod_guard",
  "name": "Peltapod Guard",
  "damage": "物理",
  "debuffs": [],
  "mech": [
   "可自增益（强力+坚守）",
   "自增益：强力",
   "自增益：坚守"
  ],
  "boss": "Vesra Fight",
  "icon": "icons/enemy/Status_Empower.png"
 },
 {
  "id": "black_lily_tokens",
  "name": "Black Lily Tokens",
  "damage": "光",
  "debuffs": [
   "虚弱"
  ],
  "mech": [],
  "boss": "The Black Lily Fight",
  "icon": "icons/enemy/Status_Weak.png"
 },
 {
  "id": "disruption_tower",
  "name": "Disruption Tower",
  "damage": "雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "boss": "M-41-D Fight",
  "icon": "icons/enemy/Status_Stun.png"
 },
 {
  "id": "idol_crystal",
  "name": "Idol Crystal",
  "damage": "雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "boss": "Irides Fight",
  "icon": "icons/enemy/Status_Stun.png"
 },
 {
  "id": "shadow_grouch",
  "name": "Shadow Grouch",
  "damage": "",
  "debuffs": [],
  "mech": [],
  "boss": "Golden Grouch Fight",
  "icon": "icons/enemy/Status_Invincible.png"
 },
 {
  "id": "elder_manalytes",
  "name": "Elder Manalytes",
  "damage": "暗",
  "debuffs": [
   "破甲"
  ],
  "mech": [],
  "boss": "Abaddon Fight",
  "icon": "icons/enemy/Status_Breach.png"
 },
 {
  "id": "opton_guards",
  "name": "Opton Guards",
  "damage": "物理、雷",
  "debuffs": [
   "麻痹"
  ],
  "mech": [],
  "boss": "Bravera Fight",
  "icon": "icons/enemy/Status_Bleed.png"
 },
 {
  "id": "jims_wedge",
  "name": "Jim's Wedge",
  "damage": "物理",
  "debuffs": [],
  "mech": [],
  "boss": "Jim C. Bringer Fight",
  "icon": "icons/enemy/Wedge.png"
 },
 {
  "id": "the_flipper_mk._ii",
  "name": "The Flipper Mk. II",
  "damage": "物理、火",
  "debuffs": [
   "灼烧"
  ],
  "mech": [],
  "boss": "Jim C. Bringer Fight",
  "icon": "icons/enemy/Status_Fire.png"
 }
]
