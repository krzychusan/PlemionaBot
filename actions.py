import re
import urllib
import string

import connector
from config import *


class Actions:
    def __init__(self, connector):
        self.connector = connector

    def build(self, building):
        url = village_townhall_page % \
                (self.connector.server, self.connector.village)
        page = self.connector.get_url(url)
        h = re.search(build_parameters_regexp, page).group(1)
        
        url = village_build_page % \
                (self.connector.server, self.connector.village, h, building)
        page = self.connector.get_url(url)
        print page

    def attack(self, (px,py), army):
        attr = self._init_attack((px,py), army)
        if attr == False:
            return False
        if not self._send_attack((px,py), army, attr):
            return False
        print "Atak wyslany na wioske %d:%d" % (px,py)
        return True


    def _init_attack(self, (px,py), army):
        params = urllib.urlencode({
                    '4dc3a62ffd110a0eda1bfe': '713c69df4dc3a6',
                    'spear': army[0],
                    'sword': army[1],
                    'axe': army[2],
                    'archer': army[3],
                    'spy': army[4],
                    'light': army[5],
                    'marcher': army[6],
                    'heavy': army[7],
                    'ram': army[8],
                    'catapult': army[9],
                    'knight': army[10],
                    'snob': army[11],
                    'x': px,
                    'y': py,
                    'attack': 'Napad'
                    })
        url = village_attack_request_page % \
                (self.connector.server, self.connector.village)
        
        page = self.connector.get_url(url, params)
        if not string.find(page, attack_request_regexp) > 0:
            print 'Nie mozna zainicjowac ataku'
            return False
        return re.search(attack_parameters_regexp, page, re.DOTALL).groups()


    def _send_attack(self, (px,py), army, attr):
        (h, ch, tx, ty, action) = attr
        params = urllib.urlencode({
                    'attack': True,
                    'ch': ch,
                    'x': px,
                    'y': py,
                    'action_id': action,
                    'spear': army[0],
                    'sword': army[1],
                    'axe': army[2],
                    'archer': army[3],
                    'spy': army[4],
                    'light': army[5],
                    'marcher': army[6],
                    'heavy': army[7],
                    'ram': army[8],
                    'catapult': army[9],
                    'knight': army[10],
                    'snob': army[11]
                })

        url = village_attack_confirm_page % \
                (self.connector.server, self.connector.village, h)
        
        page = self.connector.get_url(url, params)
        if string.find(page, "(%d|%d)" % (px,py)) > 0:
            return True
        else:
            return False
