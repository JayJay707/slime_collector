#!/usr/bin/python3
"""Contains all monsters and drops for the game"""
from models.monster import Monster
from models.item import Item
from models.regions_items import *


"""Drops"""
magic_wand = Item("MagicWand", "Magic")
potion = Item("Potion", "Potion")
venom = Item("Venom", "Poison")
bear_claw = Item("BearClaw", "Bear")
snake_fang = Item("SnakeFang", "Snake")
energy_sphere = Item("EnergySphere", "Energy")
mushroom_spore = Item("MushroomSpore", "Mushroom")
fire_gem = Item("FireGem", "Fire")
plant_gem = Item("PlantGem", "Plant")
water_gem = Item("WaterGem", "Water")
ice_gem = Item("IceGem", "Ice")
mummy = Item("Mummy", "Mummy")
ectoplasm = Item("Ectoplasm", "Ghost")
cursed_wood = Item("CursedWood", "Wood")
leviathan_scale = Item("LeviathanScale", "Leviathan")
leviathan_fang = Item("LeviathanFang", "Leviathan")
tentacle = Item("Tentacle", "Squid")
ink = Item("Ink", "Ink")
scorpion_stinger = Item("ScorpionStinger", "Scorpion")
cerberus_fang = Item("CerberusFang", "Cerberus")
cerberus_fur = Item("CerberusFur", "Cerberus")
siren_scale = Item("SirenScale", "Siren")
sphynx_claw = Item("SphynxClaw", "Sphynx")
sphynx_fur = Item("SphynxFur", "Sphynx")
stone = Item("Stone", "Rock")

"""General Monsters"""
energy_orb = Monster("EnergyOrb", 30, 10, 10, 10, energy_sphere)
ghost = Monster("Ghost", 10, 5, 10, 5, ectoplasm)
cursed_tree = Monster("CursedTree", 30, 30, 20, 15, cursed_wood)

"""Forest Monsters"""
evil_mushroom = Monster("EvilMushroom", 20, 5, 10, 15, mushroom_spore)
shroombird = Monster("Shroombird", 40, 25, 30, 20, mushroom, mushroom_spore)
not_a_deer = Monster("NotADeer", 30, 15, 20, 15, deer_antler)
plant_imp = Monster("PlantImp", 10, 5, 10, 5, plant_gem)

"""Plains Monsters"""
water_imp = Monster("WaterImp", 10, 5, 10, 5, water_gem)
fox_statue = Monster("FoxStatue", 30, 15, 25, 15, stone)

"""Volcano Monsters"""
fire_dragon = Monster("FireDragon", 150, 40, 30, 50, fire_dragon_claw, fire_dragon_scale)
fire_imp = Monster("FireImp", 10, 5, 10, 5, fire_gem)
burnt_statue = Monster("BurntStatue", 30, 15, 25, 15, stone)

"""Cave Monsters"""
rock_dragon = Monster("RockDragon", 150, 40, 30, 50, rock_dragon_claw, rock_dragon_scale)
bear = Monster("Bear", 50, 20, 30, 20, bear_fur, bear_claw)
cerberus = Monster("Cerberus", 100, 25, 30, 30, cerberus_fang, cerberus_fur)

"""Mountain Monsters"""
snow_dragon = Monster("SnowDragon", 150, 40, 30, 50, snow_dragon_claw, snow_dragon_feather)
ice_imp = Monster("IceImp", 10, 5, 10, 5, ice_gem)

"""Enchanted Forest Monsters"""
elf = Monster("Elf", 120, 20, 30, 40, magic_wand, potion)
elf_statue = Monster("ElfStatue", 30, 15, 25, 15, stone)

"""Desert Monsters"""
giant_snake = Monster("GiantSnake", 75, 25, 20, 30, snake_skin, venom, snake_fang)
half_living_mummy = Monster("HalfLivingMummy", 90, 15, 20, 40, mummy)
scorpion_king = Monster("ScorpionKing", 40, 20, 30, 20, scorpion_stinger, venom)
sphynx = Monster("Sphynx", 50, 20, 30, 20, sphynx_claw, sphynx_fur)
pharaoh_statue = Monster("PharaohStatue", 30, 15, 25, 15, stone)

"""Island Monsters"""
leviathan = Monster("Leviathan", 200, 50, 40, 70, leviathan_fang, leviathan_scale)
kraken = Monster("Kraken", 150, 40, 30, 50, tentacle, ink)
komodo_dragon = Monster("KomodoDragon", 40, 20, 20, 30, venom)
siren = Monster("Siren", 30, 15, 20, 15, siren_scale)

"""Monsters by region"""
forest_monsters = [evil_mushroom, shroombird, plant_imp, not_a_deer, energy_orb, ghost, cursed_tree]
plains_monsters = [water_imp, energy_orb, ghost, cursed_tree, fox_statue]
desert_monsters = [giant_snake, half_living_mummy, energy_orb, ghost, scorpion_king, sphynx, pharaoh_statue]
enchanted_forest_monsters = [elf, energy_orb, ghost, cursed_tree, elf_statue]
volcano_monsters = [fire_dragon, fire_imp, energy_orb, ghost, burnt_statue]
island_monsters = [leviathan, kraken, komodo_dragon, energy_orb, ghost, cursed_tree, siren]
mountain_monsters = [snow_dragon, ice_imp, energy_orb, ghost]
cave_monsters = [rock_dragon, bear, energy_orb, ghost, cerberus]