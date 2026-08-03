# -*- coding: utf-8 -*-
# Ecliptica 数据 Part 5: 职业定义 (8 职业)

CLASSES = [
 {"id":"spellsword","en":"Spellsword","jp":"スペルソード","zh":"剑术家","role":"ATTACK","roleZh":"攻击",
  "hp":"中等","desc":"Agile close to mid-range fighter, able to dash in and out of combat.","descZh":"灵活的近中距离战士，靠位移技能进出战场。",
  "skills":[
    {"type":"Primary","en":"Telekinetic Strike","zh":"念力斩","desc":"近战主手，命中 2.5% 概率叠狂乱（v0.51）。"},
    {"type":"Secondary","en":"Piercing Strike","zh":"穿刺打击","desc":"可蓄力的远程突刺，满蓄力可发射旋风（配旋风升级）。"},
    {"type":"Utility","en":"Quick Dash","zh":"快速冲刺","desc":"短 CD 位移，可触发 Burst 攻速爆发、复活减免等机制。"},
  ]},
 {"id":"twinmage","en":"Twinmage","jp":"ツインメイジ","zh":"双法师","role":"ATTACK","roleZh":"攻击",
  "hp":"低","desc":"Versatile dual element user specialising in status ailments.","descZh":"双元素施法者，专精状态异常。左右手可各选一种元素。",
  "skills":[
    {"type":"Hand","en":"Flaming Hand / Ice Hand / Electric Hand / Wind Blade / Divine Hand / Profane Hand","zh":"火焰手/寒冰手/雷电手/风刃/圣光手/暗影手","desc":"六种元素手任选其二（左右手）。其中 Divine Hand（圣光手）为当前版本最强输出——B站实测伤害数值 50，远超其他元素 30。"},
    {"type":"Utility","en":"Quickwarp","zh":"快速传送","desc":"位移技，配合 Wicked Sign 可触发全 buff。"},
  ]},
 {"id":"gunmancer","en":"Gunmancer","jp":"ガンマンサー","zh":"枪术士","role":"ATTACK","roleZh":"攻击",
  "hp":"低","desc":"Powerful long-range marksman focused on heavy damage.","descZh":"强力远程射手，专注重火力。",
  "skills":[
    {"type":"Primary","en":"VA-11 Blast Cannon","zh":"VA-11 爆能炮","desc":"光束主手（hit-scan，不吃弹速）。"},
    {"type":"Primary","en":"Kinetic Fletchette","zh":"动能箭","desc":"弹道型主手。"},
    {"type":"Secondary","en":"Firebomb / Photon Condenser / Antimatter Accelerator","zh":"爆炎弹/光子凝聚器/反物质加速器","desc":"三种副手武器：火AOE、蓄力散射（圣光）、暗属性枪。"},
    {"type":"Utility","en":"Airblast","zh":"空气冲击","desc":"位移+短暂滞空，蓄力射击需在空中完成。"},
  ]},
 {"id":"fistmage","en":"Fistmage","jp":"フィストメイジ","zh":"拳法师","role":"HEAVY","roleZh":"重型",
  "hp":"高","desc":"Bulky close-range berserker able to parry incoming damage.","descZh":"高血量近战狂战士，可以格挡（Parry）伤害。",
  "skills":[
    {"type":"Primary","en":"Aura Fist","zh":"光环拳","desc":"蓄力近战拳。"},
    {"type":"Secondary","en":"Deflecting Swipe","zh":"格挡挥击","desc":"核心机制：格挡成功触发大量升级效果（回血、buff、攻速、反弹）。"},
    {"type":"Utility","en":"Super Endurance","zh":"超级耐力","desc":"位移/减伤。"},
  ]},
 {"id":"spellhammer","en":"Spellhammer","jp":"スペルハンマー","zh":"法锤士","role":"HEAVY","roleZh":"重型",
  "hp":"150","desc":"Dextrous and durable warrior, dealing swift and heavy hits.","descZh":"敏捷耐久的战士，快速重击。基础 HP 150。",
  "skills":[
    {"type":"Primary","en":"Pummel","zh":"锤击","desc":"挥锤 90 物理伤害（v0.51 由 110 下调）+ 击退；挥击期间移速×2（受移速影响，v0.51 改为不再受攻速影响）。"},
    {"type":"Secondary","en":"Jump Smash","zh":"跳砸","desc":"跳跃后砸地 130+ 物理伤害，踩头顶可弹起连段；伤害随跳跃高度缩放。"},
    {"type":"Secondary","en":"Chuck","zh":"投掷","desc":"蓄力投掷锤，伤害 38-150+ 随蓄力提升；落地爆炸（v0.51 熟练升级附加爆炸伤害）。"},
    {"type":"Utility","en":"Disperse","zh":"爆散","desc":"130 物理伤害爆炸+后跳；空中可充能但更慢（v0.51）。"},
  ]},
 {"id":"shieldmage","en":"Shield Mage","jp":"シールドメイジ","zh":"盾法师","role":"HEAVY","roleZh":"重型",
  "hp":"高","desc":"Frontline defender able to block incoming strikes.","descZh":"前线防御者，格挡来袭攻击（紫攻击除外）。",
  "skills":[
    {"type":"Primary","en":"Offensive Strike","zh":"进攻打击","desc":"盾击输出。"},
    {"type":"Secondary","en":"Defensive Stance","zh":"防御姿态","desc":"举盾格挡：红圈/弹丸/爆风可挡，紫攻击不可挡。"},
    {"type":"Utility","en":"Evasive Maneuver","zh":"离脱战术","desc":"大范围护罩（保护队友）+ 紫伤减免；v0.51 盾冲 CD 恢复 4 秒。"},
  ]},
 {"id":"thaumaturge","en":"Thaumaturge","jp":"サウマタージ","zh":"咒术师（书奶）","role":"SUPPORT","roleZh":"辅助",
  "hp":"中","desc":"Healer which converts dealt damage into health for allies.","descZh":"通过造成伤害转化为队友生命值的治疗者。",
  "skills":[
    {"type":"Passive","en":"Life Energy","zh":"生命能量","desc":"造成伤害积攒生命能量（25% 消耗释放治疗）。"},
    {"type":"Primary","en":"Foul Pustule","zh":"腐化脓疱","desc":"远程弹，命中可对敌伤害/对队友治疗。"},
    {"type":"Secondary","en":"Pain Exchange","zh":"痛苦交换","desc":"核心治疗技：消耗生命能量治疗目标（可对自己）。"},
    {"type":"Utility","en":"Soulborne","zh":"灵魂出窍","desc":"位移/保命。"},
  ]},
 {"id":"nekomancer","en":"Nekomancer","jp":"ネコマンサー","zh":"猫术士（猫奶）","role":"SUPPORT","roleZh":"辅助",
  "hp":"低","desc":"Summoner commanding a troop of undead cats.","descZh":"指挥亡灵猫大军的召唤师。",
  "skills":[
    {"type":"Passive","en":"Souls","zh":"灵魂","desc":"击杀敌人收集灵魂，用于召唤/强化猫。"},
    {"type":"Primary","en":"Staff of Feline Mortality","zh":"猫之必灭法杖","desc":"远程法杖攻击。"},
    {"type":"Secondary","en":"Call of the Undead","zh":"亡灵召唤","desc":"召唤僵尸猫/图腾猫（图腾猫提供治疗光环，v0.51 调整了回血速率与叠加规则）。"},
    {"type":"Utility","en":"Spirit Drift","zh":"灵魂漂移","desc":"位移。"},
  ]},
]
