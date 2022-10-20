#!/usr/bin/python3
"""Contains all regions and items for the game"""
from models.region import Region
from models.item import Item


"""Forest Items"""
oak_leaf = Item("OakLeaf", "Leaf")
pebble = Item("Pebble", "Rock")
water = Item("Water", "Water")
tree_bark = Item("TreeBark", "Wood")
fern = Item("Fern", "Leaf")
acorn = Item("Acorn", "Seed")
mushroom = Item("Mushroom", "Mushroom")
deer_antler = Item("DeerAntler", "Deer")
squirrel_fur = Item("SquirrelFur", "Squirrel")

"""Plains Items"""
grass = Item("Grass", "Plant")
rabbit_fur = Item("RabbitFur", "Rabbit")
clover = Item("Clover", "Plant")
four_leaf_clover = Item("4LeafClover", "LuckyClover")
feather = Item("Feather", "Feather")
hazelnut = Item("Hazelnut", "Nut")
clay = Item("Clay", "Clay")
frog_leg = Item("FrogLeg", "Frog")
dragonfly_wing = Item("DragonflyWing", "Dragonfly")
salamander_tail = Item("SalamanderTail", "Salamander")
butterfly = Item("Butterfly", "Butterfly")
fox_fur = Item("FoxFur", "Fox")
lilypad = Item("Lilypad", "Plant")

"""Desert Items"""
sand = Item("Sand", "Sand")
snake_skin = Item("SnakeSkin", "Snake")
cactus = Item("Cactus", "Cactus")
oasis_water = Item("OasisWater", "Water")
date = Item("Date", "Fruit")
pyramid_stone = Item("PyramidStone", "Rock")
hieroglyph_tablet = Item("HieroglyphTablet", "Hieroglyph")
anubis_mask = Item("AnubisMask", "Anubis")
enchanted_beetle = Item("EnchantedBeetle", "Magic")
snake_egg = Item("SnakeEgg", "Egg")

"""Enchanted Forest Items"""
blue_fern = Item("BlueFern", "Leaf")
firefly = Item("Firefly", "Firefly")
glowing_mushroom = Item("GlowingMushroom", "Mushroom")
twisted_magic_wood = Item("TwistedMagicWood", "Magic")
golden_apple = Item("GoldenApple", "Fruit")
mandrake = Item("Mandrake", "Plant")
sage = Item("Sage", "Leaf")
bamboo = Item("Bamboo", "Bamboo")
tea_leaf = Item("TeaLeaf", "Leaf")
peacock_feather = Item("PeacockFeather", "Feather")
moth = Item("Moth", "Moth")
fairy_dust = Item("FairyDust", "Magic")
lotus_leaf = Item("LotusLeaf", "Leaf")
lotus_flower = Item("LotusFlower", "Flower")

"""Volcano Items"""
lava = Item("Lava", "Lava")
volcano_rock = Item("VolcanoRock", "Rock")
diamond = Item("Diamond", "Diamond")
ash = Item("Ash", "Ash")
fire_dragon_scale = Item("FireDragonScale", "FireDragon")
fire_dragon_egg = Item("FireDragonEgg", "Egg")
black_sand = Item("BlackSand", "Sand")
sulfur = Item("Sulfur", "Sulfur")
burnt_wood = Item("BurntWood", "Wood")
fire_dragon_claw = Item("FireDragonClaw", "FireDragon")
phoenix_feather = Item("PhoenixFeather", "Phoenix")

"""Island Items"""
fish = Item("Fish", "Fish")
coconut = Item("Coconut", "Coconut")
exotic_fruit = Item("ExoticFruit", "Fruit")
white_sand = Item("WhiteSand", "Sand")
bottle_in_the_sea = Item("BottleInTheSea", "Glass")
crab_claw = Item("CrabClaw", "Crab")
salt_water = Item("SaltWater", "Water")
palm_leaf = Item("PalmLeaf", "Leaf")
driftwood = Item("Driftwood", "Wood")
turtle_egg = Item("TurtleEgg", "Egg")

"""Mountain Items"""
eagle_egg = Item("EagleEgg", "Egg")
chamois_fur = Item("ChamoisFur", "Chamois")
icy_water = Item("IcyWater", "Water")
snow = Item("Snow", "Snow")
snow_dragon_feather = Item("SnowDragonFeather", "SnowDragon")
snow_dragon_egg = Item("SnowDragonEgg", "Egg")
snow_dragon_claw = Item("SnowDragonClaw", "SnowDragon")
ice = Item("Ice", "Ice")

"""Cave Items"""
bat_wing = Item("BatWing", "Bat")
geode = Item("Geode", "Geode")
rock_dragon_claw = Item("RockDragonClaw", "RockDragon")
rock_dragon_egg = Item("RockDragonEgg", "Egg")
rock_dragon_scale = Item("RockDragonScale", "RockDragon")
cut_stone = Item("CutStone", "Rock")
bear_fur = Item("BearFur", "Bear")

"""Item lists"""
forest_items = [oak_leaf, pebble, water, tree_bark, fern, acorn, mushroom, deer_antler, squirrel_fur]
plains_items = [grass, rabbit_fur, clover, four_leaf_clover, feather, hazelnut, clay, frog_leg, dragonfly_wing, salamander_tail, butterfly, fox_fur]
desert_items = [sand, snake_egg, snake_skin, cactus, oasis_water, date, pyramid_stone, hieroglyph_tablet, anubis_mask, enchanted_beetle]
enchanted_forest_items = [blue_fern, firefly, glowing_mushroom, twisted_magic_wood, golden_apple, mandrake, sage, bamboo, tea_leaf, peacock_feather, moth, fairy_dust, lotus_flower, lotus_leaf]
volcano_items = [lava, volcano_rock, diamond, ash, fire_dragon_claw, fire_dragon_egg, fire_dragon_scale, black_sand, sulfur, burnt_wood, phoenix_feather]
island_items = [fish, coconut, exotic_fruit, white_sand, bottle_in_the_sea, crab_claw, salt_water, palm_leaf, driftwood, turtle_egg]
mountain_items = [eagle_egg, chamois_fur, icy_water, snow, snow_dragon_claw, snow_dragon_egg, snow_dragon_feather, ice]
cave_items = [bat_wing, geode, rock_dragon_claw, rock_dragon_egg, rock_dragon_scale, cut_stone, bear_fur]

"""Regions"""
forest = Region("Forest", forest_items)
plains = Region("Plains", plains_items)
desert = Region("Desert", desert_items)
enchanted_forest = Region("EnchantedForest", enchanted_forest_items)
volcano = Region("Volcano", volcano_items)
island = Region("Island", island_items)
mountain = Region("Mountain", mountain_items)
cave = Region("Cave", cave_items)
