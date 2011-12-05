import re

import connector
from config import *


class Functions:
    def __init__(self, connector):
        self.connector = connector

    #Returns actual state: (wood, stone, iron, storage, (population, max_population))
    def get_resources(self, page=None):
        if page == None:
            url = village_main_page % (self.connector.server, self.connector.village)
            page = self.connector.get_url(url)

        wood = re.search(wood_amount_regexp, page).group(1)
        stone = re.search(stone_amount_regexp, page).group(1)
        iron = re.search(iron_amount_regexp, page).group(1)
        storage = re.search(storage_amount_regexp, page).group(1)
        pop = re.search(population_amount_regexp, page).groups()
        population = pop[0]
        max_population = pop[1]
        return (wood, stone, iron, storage, (population, max_population))

    #Returns actual production: (wood, stone, iron)
    def get_production(self, page=None):
        if page == None:
            url = village_main_page % (self.connector.server, self.connector.village)
            page = self.connector.get_url(url)

        wood = re.search(wood_production_regexp, page).group(1)
        stone = re.search(stone_production_regexp, page).group(1)
        iron = re.search(iron_production_regexp, page).group(1)
        return (wood, stone, iron)

    def get_units(self, page=None):
        if page == None:
            url = village_barracks_page % (self.connector.server, self.connector.village)
            page = self.connector.get_url(url)

        try:
            spear, max_spear = re.search(spear_amount_regexp, page, re.DOTALL).groups()
        except:
            spear = max_spear = None
        try:
            sword, max_sword = re.search(sword_amount_regexp, page, re.DOTALL).groups()
        except:
            sword = max_sword = None
        try:
            axe, max_axe = re.search(axe_amount_regexp, page, re.DOTALL).groups()
        except:
            axe = max_axe = None
        try:
            archer, max_archer = re.search(archer_amount_regexp, page, re.DOTALL).groups()
        except:
            archer = max_archer = None
        try:
            scout, max_scout = re.search(scout_amount_regexp, page, re.DOTALL).groups()
        except:
            scout = max_scout = None
        try:
            horse_light, max_horse_light = re.search(horse_light_amount_regexp, page, re.DOTALL).groups()
        except:
            horse_light = max_horse_light = None
        try:
            horse_archer, max_horse_archer = re.search(horse_archer_amount_regexp, page, re.DOTALL).groups()
        except:
            horse_archer = max_horse_archer = None
        try:
            horse_heavy, max_horse_heavy = re.search(horse_heavy_amount_regexp, page, re.DOTALL).groups()
        except:
            horse_heavy = max_horse_heavy = None
        try:
            ram, max_ram = re.search(ram_amount_regexp, page, re.DOTALL).groups()
        except:
            ram = max_ram = None
        try:
            catapult, max_catapult = re.search(catapult_amount_regexp, page, re.DOTALL).groups()
        except:
            catapult = max_catapult = None
        try:
            knight, max_knight = re.search(knight_amount_regexp, page, re.DOTALL).groups()
        except:
            knight = max_knight = None
        try:
            noble, max_noble = re.search(noble_amount_regexp, page, re.DOTALL).groups()
        except:
            noble = max_noble = None

        return ((spear, max_spear), (sword, max_sword),
                (axe, max_axe), (archer, max_archer),
                (scout, max_scout), (horse_light, max_horse_light),
                (horse_archer, max_horse_archer), (horse_heavy, max_horse_heavy),
                (ram, max_ram), (catapult, max_catapult),
                (knight, max_knight), (noble, max_noble))

    def get_buildings(self, page=None):
        if page == None:
            url = village_townhall_page % (self.connector.server, self.connector.village)
            page = self.connector.get_url(url)
        try: townhall = re.search(townhall_level_regexp, page, re.DOTALL).group(1)
        except: townhall = None
        try: barracks = re.search(barracks_level_regexp, page, re.DOTALL).group(1)
        except: barracks = None
        try: church = re.search(church_level_regexp, page, re.DOTALL).group(1)
        except: church = None
        try: smith = re.search(smith_level_regexp, page, re.DOTALL).group(1)
        except: smith = None
        try: place = re.search(place_level_regexp, page, re.DOTALL).group(1)
        except: place = None
        try: statue = re.search(statue_level_regexp, page, re.DOTALL).group(1)
        except: statue = None
        try: market = re.search(market_level_regexp, page, re.DOTALL).group(1)
        except: market = None
        try: woodhouse = re.search(woodhouse_level_regexp, page, re.DOTALL).group(1)
        except: woodhouse = None
        try: stonehouse = re.search(stonehouse_level_regexp, page, re.DOTALL).group(1)
        except: stonehouse = None
        try: ironhouse = re.search(ironhouse_level_regexp, page, re.DOTALL).group(1)
        except: ironhouse = None
        try: farm = re.search(farm_level_regexp, page, re.DOTALL).group(1)
        except: farm = None
        try: storage = re.search(storage_level_regexp, page, re.DOTALL).group(1)
        except: storage = None
        try: hide = re.search(hide_level_regexp, page, re.DOTALL).group(1)
        except: hide = None
        try: wall = re.search(wall_level_regexp, page, re.DOTALL).group(1)
        except: wall = None
        try: stable = re.search(stable_level_regexp, page, re.DOTALL).group(1)
        except: stable = None
        try: garage = re.search(garage_level_regexp, page, re.DOTALL).group(1)
        except: garage = None
        try: palace = re.search(palace_level_regexp, page, re.DOTALL).group(1)
        except: palace = None

        return (townhall, barracks, church, smith,
                place, statue, market, woodhouse,
                stonehouse, ironhouse, farm, storage,
                hide, wall, stable, garage,
                palace)
