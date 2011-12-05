import sys
import os
import time

import connector
import functions
import actions
from config import *

connection = connector.Connector()
functions = functions.Functions(connection)
actions = actions.Actions(connection)

def polacz(login, password, server):
    global connection
    if not connection.connect():
        sys.exit(1)
    if not connection.login(login, password):
        sys.exit(1)
    if not connection.join_server(server):
        sys.exit(1)

def surowce():
    global functions
    (wood, stone, iron, storage, (population,max_population)) = functions.get_resources()
    print '------ SUROWCE -------------'
    print 'WOOD         ' + wood
    print 'STONE        ' + stone
    print 'IRON         ' + iron
    print 'STORAGE      ' + storage
    print 'POPULATION   ' + population + ' / ' + max_population
    print '----------------------------\n'

def produkcja():
    global functions
    (wood, stone, iron) = functions.get_production()
    print '--------- PRODUKCJA --------'
    print 'WOOD         ' + wood
    print 'STONE        ' + stone
    print 'IRON         ' + iron
    print '----------------------------\n'

def jednostki():
    global functions
    ((spear, max_spear), (sword, max_sword),
    (axe, max_axe), (archer, max_archer),
    (scout, max_scout), (horse_light, max_horse_light),
    (horse_archer, max_horse_archer), (horse_heavy, max_horse_heavy),
    (ram, max_ram), (catapult, max_catapult),
    (knight, max_knight), (noble, max_noble)) = functions.get_units()
    print '------ JEDNOSTKI -----------'
    print 'Jednostki nie odkryte oznaczone sa jako None'
    print 'SPEAR    ' + str(spear)       + ' / ' + str(max_spear)
    print 'SWORD    ' + str(sword)       + ' / ' + str(max_sword)
    print 'AXE      ' + str(axe)         + ' / ' + str(max_axe)
    print 'ARCHER   ' + str(archer)      + ' / ' + str(max_archer)
    print 'SCOUT    ' + str(scout)       + ' / ' + str(max_scout)
    print 'LIGHT    ' + str(horse_light) + ' / ' + str(max_horse_light)
    print 'HARCHER  ' + str(horse_archer)+ ' / ' + str(max_horse_archer)
    print 'HEAVY    ' + str(horse_heavy) + ' / ' + str(max_horse_heavy)
    print 'RAM      ' + str(ram)         + ' / ' + str(max_ram)
    print 'CATAPULT ' + str(catapult)    + ' / ' + str(max_catapult)
    print 'KNIGHT   ' + str(knight)      + ' / ' + str(max_knight)
    print 'NOBLE    ' + str(noble)       + ' / ' + str(max_noble)
    print '----------------------------\n'

def budynki():
    global functions
    (townhall, barracks, church, smith,
        place, statue, market, woodhouse,
        stonehouse, ironhouse, farm, storage,
        hide, wall, stable, garage,
        palace) = functions.get_buildings()
    print '------ BUDYNKI -----------'
    print 'TOWNHALL     ' + str(townhall)
    print 'BARRACKS     ' + str(barracks)
    print 'CHURCH       ' + str(church)
    print 'SMITH        ' + str(smith)
    print 'PLACE        ' + str(place)
    print 'STATUE       ' + str(statue)
    print 'MARKET       ' + str(market)
    print 'WOODHOUSE    ' + str(woodhouse)
    print 'STONEHOUSE   ' + str(stonehouse)
    print 'IRONHOUSE    ' + str(ironhouse)
    print 'FARM         ' + str(farm)
    print 'STORAGE      ' + str(storage)
    print 'HIDE         ' + str(hide)
    print 'WALL         ' + str(wall)
    print 'STABLE       ' + str(stable)
    print 'GARAGE       ' + str(garage)
    print 'PALACE       ' + str(palace)
    print '--------------------------'

def czekaj(czas):
    time.sleep(czas)

def atakuj(enemy, army):
    actions.attack(enemy, army)

def buduj(building):
    actions.build(building)

def usage():
    print 'Uzycie: \n python main.py script.py'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    script = sys.argv[1]
    if not os.path.exists(script):
        print 'Nie znaleziono skryptu.'
        sys.exit(1)
    print 'Uruchamiam skrypt: ', script
    execfile(script)
