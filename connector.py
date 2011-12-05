import sys
import re
import string
import cookielib
import urllib
import urllib2

from config import *


class Connector:
    def __init__(self):
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        self.server_active = False
        self.server_logged = False
        self.server_ingame = False

    def connect(self):
        resp = self.opener.open('http://www.plemiona.pl')
        resp = resp.read()
        if string.find(resp, main_page_string):
            self.server_active = True
            print 'Plemiona dzialaja'
            return True
        else:
            self.server_active = False
            print 'Plemiona nie dzialaja sorry...'
            return False

    def login(self, login, password):
        self.login = login
        if not self.server_active:
            print 'Nie mozna sie logowac, jak plemiona nie dzialaja'
            self.server_logged = False
            return False
        params = urllib.urlencode({'user': login, 'password': password, 'clear': True})
        resp = self.opener.open('http://www.plemiona.pl/index.php?action=login&server_list=1&show_server_selection=1',params)
        resp = resp.read()
        self.server_logged = string.find(resp, server_list_regexp) > 0
        if not self.server_logged:
            print 'Nie powiodlo sie pobranie listy serwerow'
            return False
        print 'Zalogowano jako ', login
        self.session_key = re.search(r"value=\\\"(.{15,50}?)\\\" \\/>", str(resp)).group(1)
        print 'Zaszyfrowane haslo: ', self.session_key
        return True

    def join_server(self, server):
        self.server = server
        if not self.server_logged:
            print 'Trzeba byc zalogowanym, aby moc polaczyc sie z serwerem'
            return False

        params = urllib.urlencode({'user': self.login, 'password': self.session_key})
        resp = self.opener.open('http://www.plemiona.pl/index.php?action=login&server_pl'+str(server), params)
        resp = resp.read()

        self.village = re.search(village_number_regexp, resp).group(1)
        print 'VILLAGE: ', self.village
        self.server_ingame = True
        return True

    def get_url(self, path, params = None):
        if params is None:
            resp = self.opener.open(path)
        else:
            resp = self.opener.open(path, params)
        return resp.read()

    def change_village(self, new_village):
        pass
