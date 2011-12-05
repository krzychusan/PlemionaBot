import re
import os
import pickle

from config import *
from farm import *

def save_to_file(text, name):
    with open(name, 'w+') as f:
        f.write(text)


class InputManager:
    def __init__(self, connector):
        self.c = connector

    def parse_commands(self):
        while True:
            command = raw_input('Polecenie: ')
            if command == 'help':
                cmd_help()
            elif command == 'status':
                cmd_status(self.c)
            elif command == 'armia':
                cmd_units(self.c)
            elif command == 'farma':
                cmd_farm()
            elif command == 'farma manager':
                cmd_manage_farm()
            elif command == 'exit':
                break
            else:
                print 'Unknown command'


def cmd_help():
    print 'Pomoc'
    print '     - status - status aktualnej wioski'
    print '     - armia - status armii w aktualnej wiosce'
    print '     - farma - status wiosek farmionych'
    print '     - farma manager - edycja wiosek do farmienia'
    print '     - exit - zamyka polaczenie z gra'


def get_farm_class():
    if not os.path.exists(DATA_FILE):
        obj = FarmManager()
        pickle.dump(obj, open(DATA_FILE, 'w'))
    return pickle.load(file(DATA_FILE))


def cmd_farm():
    #pickle.dump(obj, file)
    f = get_farm_class()
    f.show()

def cmd_manage_farm():
    f = get_farm_class()
    f.handle_input()

def cmd_status(c):
    if not c.server_ingame:
        print 'Nie mozna wykonac komendy nie bedac w grze'
        return
    resp = c.get_url('http://pl'+str(c.server)+'.plemiona.pl/game.php?screen=overview&intro')
    print '\n'
    cmd_resources(resp)
    cmd_production(resp)
    print '\n'


def cmd_resources(resp):
    #save_to_file(resp, 'resp')
    wood = re.search(wood_amount_regexp, resp).group(1)
    stone = re.search(stone_amount_regexp, resp).group(1)
    iron = re.search(iron_amount_regexp, resp).group(1)
    storage = re.search(storage_amount_regexp, resp).group(1)
    pop = re.search(population_amount_regexp, resp).groups()
    population = pop[0]
    max_population = pop[1]
    print '------ SUROWCE -------------'
    print 'WOOD         ' + wood
    print 'STONE        ' + stone
    print 'IRON         ' + iron
    print 'STORAGE      ' + storage
    print 'POPULATION   ' + population + ' / ' + max_population
    print '----------------------------'

def cmd_production(resp):
    wood = re.search(wood_production_regexp, resp).group(1)
    stone = re.search(stone_production_regexp, resp).group(1)
    iron = re.search(iron_production_regexp, resp).group(1)
    print '--------- PRODUKCJA --------'
    print 'WOOD         ' + wood
    print 'STONE        ' + stone
    print 'IRON         ' + iron
    print '----------------------------'


def cmd_units(c):
    if not c.server_ingame:
        print 'Nie mozna wykonac komendy nie bedac w grze'
        return
    resp = c.get_url('http://pl58.plemiona.pl/game.php?screen=barracks')
    save_to_file(resp, 'resp')
    spear, max_spear = re.search(spear_amount_regexp, resp, re.DOTALL).groups()
    sword, max_sword = re.search(sword_amount_regexp, resp, re.DOTALL).groups()
    axe, max_axe = re.search(axe_amount_regexp, resp, re.DOTALL).groups()
    archer, max_archer = re.search(archer_amount_regexp, resp, re.DOTALL).groups()

    print '\n'
    print '------ UNITS -----------'
    print 'SPEAR    ' + spear  + ' / ' + max_spear
    print 'SWORD    ' + sword  + ' / ' + max_sword
    print 'AXE      ' + axe    + ' / ' + max_axe
    print 'ARCHER   ' + archer + ' / ' + max_archer
    print '------------------------'
    print '\n'
