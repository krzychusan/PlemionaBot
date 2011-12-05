
LOGIN = ''
PASSWORD = ''
SERVER = 58



############### Adresy podstron ###############
village_main_page = "http://pl%s.plemiona.pl/game.php?village=%s&screen=overview"
village_barracks_page = "http://pl%s.plemiona.pl/game.php?village=%s&screen=barracks"
village_townhall_page = "http://pl%s.plemiona.pl/game.php?village=%s&screen=main"






################ Wyrazenia regularne do parsowania strony #################

server_list_regexp = """<p style=\\"margin: 5px; margin-left: 0px; margin-bottom: 10px; font-weight:bold;\\">Na kt\\u00f3rym \\u015bwiecie chcesz si\\u0119 zalogowa\\u0107?<\/p>"""

wood_amount_regexp = """<td class="box-item"><span id="wood" title="\d+" class=".*?">(\d+)</span></td>"""
stone_amount_regexp = """<td class="box-item"><span id="stone" title="\d+" class=".*?">(\d+)</span></td>"""
iron_amount_regexp = """<td class="box-item"><span id="iron" title="\d+" class=".*?">(\d+)</span></td>"""
storage_amount_regexp = """<td class="box-item"><span id="storage">(\d+)</span></td>"""
population_amount_regexp = """<span id="pop_current_label">(\d+)</span>/<span id="pop_max_label">(\d+)</span>"""

village_number_regexp = "/game.php\?village=(\d+)&amp;screen=overview_villages"

wood_production_regexp = """<span class="icon header wood"> </span> Drewno\s*</td>\s*<td>\s*<strong> (\d+)</strong> na godzin"""
stone_production_regexp = """<span class="icon header stone"> </span> Glina\s*</td>\s*<td>\s*<strong> (\d+)</strong> na godzin"""
iron_production_regexp = """<span class="icon header iron"> </span> .{2}elazo\s*</td>\s*<td>\s*<strong> (\d+)</strong> na godzin"""


spear_amount_regexp = """<img src="http://cdn.tribalwars.net/graphic/unit/unit_spear.png\?1" alt="" />\s*?Pikinier.*?<td>\d+:\d+:\d+</td>\s+<td>(\d+)/(\d+)</td>"""
sword_amount_regexp = """<img src="http://cdn.tribalwars.net/graphic/unit/unit_sword.png\?1" alt="" />\s*?Miecznik.*?<td>\d+:\d+:\d+</td>\s+<td>(\d+)/(\d+)</td>"""
axe_amount_regexp = """<img src="http://cdn.tribalwars.net/graphic/unit/unit_axe.png\?1" alt="" />\s*?Topornik.*?<td>\d+:\d+:\d+</td>\s+<td>(\d+)/(\d+)</td>"""
archer_amount_regexp = """<img src="http://cdn.tribalwars.net/graphic/unit/unit_archer.png\?1" alt="" />\s*?.{2}ucznik.*?<td>\d+:\d+:\d+</td>\s+<td>(\d+)/(\d+)</td>"""

townhall_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/main.png\?1" title="Ratusz" alt="" /> Ratusz</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
barracks_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/barracks.png\?1" title="Koszary" alt="" /> Koszary</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
church_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/church.png\?1" title=".*?" alt="" /> .*?</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
smith_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/smith.png\?1" title="Ku.{2}nia" alt="" /> Ku.{2}nia</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
place_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/place.png\?1" title="Plac" alt="" /> Plac</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
statue_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/statue.png\?1" title="Piedesta.{2}" alt="" /> Piedesta.{2}</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
market_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/market.png\?1" title="Rynek" alt="" /> Rynek</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
woodhouse_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/wood.png\?1" title="Tartak" alt="" /> Tartak</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
stonehouse_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/stone.png\?1" title="Cegielnia" alt="" /> Cegielnia</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
ironhouse_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/iron.png\?1" title="Huta .{2}elaza" alt="" /> Huta .{2}elaza</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
farm_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/farm.png\?1" title="Zagroda" alt="" /> Zagroda</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
storage_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/storage.png\?1" title="Spichlerz" alt="" /> Spichlerz</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
hide_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/hide.png\?1" title="Schowek" alt="" /> Schowek</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
wall_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/wall.png\?1" title="Mur obronny" alt="" /> Mur obronny</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
stable_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/stable.png\?1" title="Stajnia" alt="" /> Stajnia</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
garage_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/garage.png\?1" title="Warsztat" alt="" /> Warsztat</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""
palace_level_regexp = """<img src="http://cdn.tribalwars.net/graphic/buildings/snob.png\?1" title="Pa.{2}ac" alt="" /> Pa.{2}ac</a>\s*<span class="nowrap">\s*\(Poziom (\d+)\)\s*</span>"""



main_page_string = """<title>Plemiona - gra online</title>"""
