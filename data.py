Hand = {
    "gold": 10, # 0
    "hand_axe": 0,  # 손도끼, 1
    "linen_bandage": 0,  # 리넨 붕대, 2
    "stormwind_cheddar": 0,  # 스톰윈드 체더 치즈, 3
    "cute_doll": 0,  # 귀여운 인형, 4
    "shadowy_gem": 0,  # 그림자 보석, 5
    "elixir_of_vigor": 0,  # 재활의 물약, 6
    "potions_of_night": 0,  # 밤의 물약, 7
    "gnomish_shield": 0,  # 노움 방패, 8
    "loyal_pet_whistle": 0,  # 충직의 애완동물 호루라기, 9
    "very_nice_hat": 0,  # 아주 멋진 모자, 10
    "angry_cristal": 0,  # 화난 수정, 11
    "jade_locket": 0,  # 비취 은감 목걸이, 12
    "goblin_fishing_pole": 0,  # 고블린 낚시 도구, 13
    "captivating_pipe": 0,  # 매료의 피리, 14
    "healing_potion": 0,  # 치유 물약, 15
    "iron_dagger": 0,  # , 강철 단검, 16
    "arcane_scroll": 0,  # 비전 두루마리, 17
    "golden_goblet": 0,  # 황금 술잔, 18
    "sapphire_wand": 0,  # 사파이어 마법봉, 19
    "everburning_candle": 0,  # 영원히 타오르는 양초, 20
    "ruby_crown": 0,  # 루비 왕관, 21
    "alliance_mace": 0,  # 얼라이언스 철퇴, 22
    "draught_of_angels": 0,  # 천사의 비약, 23
    "gilneas_dagger": 0,  # 길니아스 단검, 24
    "tiger_amulet": 0,  # 호랑이 부적, 25
    "sphere_of_wisdom": 0,  # 지혜의 구슬, 26
}

# (a : Str, b : Str, c : int)
# ex) 2 "gold" for a "healing potion"

Baloon_Merchant = [
    ("gold", "healing_potion", 2),
    ("hand_axe", "golden_goblet", 5),
    ("linen_bandage", "jade_locket", 2),
    ("stormwind_cheddar", "alliance_mace", 14),
    ("cute_doll", "draught_of_angels", 3),
    ("shadowy_gem", "gilneas_dagger", 2),
    ("elixir_of_vigor", "loyal_pet_whistle", 4),
]
Armor_Vender = [
    ("gold", "iron_dagger", 1),
    ("stormwind_cheddar", "jade_locket", 4),
    ("healing_potion", "golden_goblet", 4),
    ("hand_axe", "ruby_crown", 22),
    ("potions_of_night", "sphere_of_wisdom", 4),
    ("gnomish_shield", "shadowy_gem", 3),
    ("loyal_pet_whistle", "sapphire_wand", 2),
]
Barrens_Blacksmith = [
    ("linen_bandage", "cute_doll", 5),
    ("gold", "hand_axe", 2),
    ("very_nice_hat", "arcane_scroll", 8),
    ("angry_cristal", "draught_of_angels", 1),
    ("jade_locket", "potions_of_night", 5),
    ("goblin_fishing_pole", "everburning_candle", 4),
    ("captivating_pipe", "tiger_amulet", 5),
]

Darkshire_Alchemist = [
    ("gold", "captivating_pipe", 11),
    ("iron_dagger", "gnomish_shield", 12),
    ("golden_goblet", "alliance_mace", 3),
    ("elixir_of_vigor", "linen_bandage", 1),
    ("healing_potion", "gilneas_dagger", 49),
    ("stormwind_cheddar", "potions_of_night", 13),
    ("arcane_scroll", "tiger_amulet", 3),
]

Shady_dealer = [
    ("gold", "arcane_scroll", 25),
    ("hand_axe", "very_nice_hat", 2),
    ("healing_potion", "captivating_pipe", 7),
    ("elixir_of_vigor", "angry_cristal", 20),
    ("sapphire_wand", "gilneas_dagger", 2),
    ("golden_goblet", "sphere_of_wisdom", 10),
    ("stormwind_cheddar", "sapphire_wand", 15),
]

Master_Swordsmith = [
    ("captivating_pipe", "ruby_crown", 3),
    ("gold", "elixir_of_vigor", 3),
    ("hand_axe", "goblin_fishing_pole", 4),
    ("very_nice_hat", "sapphire_wand", 5),
    ("alliance_mace", "everburning_candle", 1),
    ("cute_doll", "angry_cristal", 5),
    ("golden_goblet", "draught_of_angels", 9),
]

Drakkari_Enchanter = [
    ("gold", "stormwind_cheddar", 2),
    ("stormwind_cheddar", "goblin_fishing_pole", 5),
    ("iron_dagger", "loyal_pet_whistle", 7),
    ("elixir_of_vigor", "shadowy_gem", 9),
    ("ruby_crown", "gilneas_dagger", 1),
    ("gnomish_shield", "tiger_amulet", 4),
    ("cute_doll", "alliance_mace", 3),
]

# needed amount
dalaran_mage = {
    "hand_axe": 6,
    "goblin_fishing_pole": 2,
    "angry_cristal": 1,
    "arcane_scroll": 6,
    "sphere_of_wisdom": 3,
}
bloodsail_corsair = {
    "cute_doll": 1,
    "stormwind_cheddar": 10,
    "goblin_fishing_pole": 10,
    "ruby_crown": 4,
    "potions_of_night": 8,
}
violet_apprentice = {
    "linen_bandage": 3,
    "very_nice_hat": 4,
    "draught_of_angels": 1,
    "angry_cristal": 3,
    "cute_doll": 9,
}
silver_hand_knight = {
    "jade_locket": 1,
    "captivating_pipe": 6,
    "ruby_crown": 2,
    "tiger_amulet": 2,
    "sapphire_wand": 10,
}
darnassus_aspirant = {
    "iron_dagger": 3,
    "gilneas_dagger": 1,
    "captivating_pipe": 4,
    "alliance_mace": 5,
    "shadowy_gem": 7,
}
windspeaker = {
    "golden_goblet": 7,
    "elixir_of_vigor": 10,
    "gnomish_shield": 2,
    "alliance_mace": 4,
    "everburning_candle": 7,
}
defender_of_argus = {
    "healing_potion": 8,
    "loyal_pet_whistle": 3,
    "arcane_scroll": 2,
    "gnomish_shield": 7,
    "draught_of_angels": 4,
}

Sellers = [
    Baloon_Merchant,
    Armor_Vender,
    Barrens_Blacksmith,
    Darkshire_Alchemist,
    Shady_dealer,
    Master_Swordsmith,
    Drakkari_Enchanter,
]

Buyers = [
    dalaran_mage,
    bloodsail_corsair,
    violet_apprentice,
    silver_hand_knight,
    darnassus_aspirant,
    windspeaker,
    defender_of_argus,
]
Gold_Amount = [
    [10, 18, 60, 138, 205],
    [18, 25, 120, 92, 240],
    [13, 14, 30, 150, 166],
    [11, 42, 72, 114, 125],
    [6, 70, 50, 125, 166],
    [65, 15, 25, 70, 180],
    [10, 22, 70, 60, 204],
]
