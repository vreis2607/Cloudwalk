import re
from collections import OrderedDict

# Regex match start game
start_regex = re.compile(r".*InitGame:.*")

# Regex match kill lines of log
kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")

# Function to parse games, kills, players
def parse_game_kills(logfile, show_weapon=False):
    """
    Get logfile and parse results into OrderedDict
    """
    game_match_count = 1
    key_map = "game_{}"
    parsed_game_matches = OrderedDict()
    with open(logfile, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            if start_regex.match(line):
                key = key_map.format(game_match_count)
                if show_weapon:
                    parsed_game_matches[key] = {
                        "total_kills": 0,
                        "players": [],
                        "kills": {},
                        "kills_by_means": {}
                    }
                else:
                    parsed_game_matches[key] = {
                        "total_kills": 0,
                        "players": [],
                        "kills": {},
                    }
                game_match_count += 1

            if kill_regex.match(line):
                parse_kill_line(line, parsed_game_matches[key], show_weapon)
    return parsed_game_matches

# Function to parse players kills and weapon means of death
def parse_kill_line(line, game_match, show_weapon=False):
    """
    Specific parse to kill line
    """
    m = kill_regex.match(line)
    player_alive = m.group(1).strip()
    player_dead = m.group(2).strip()

    game_match["total_kills"] += 1
    if (player_alive != "<world>" and player_alive
            not in game_match["players"]):
        game_match["players"].append(player_alive)

    if player_dead not in game_match["players"]:
        game_match["players"].append(player_dead)

    if player_alive != "<world>":
        if player_alive in game_match["kills"].keys():
            game_match["kills"][player_alive] += 1
        else:
            game_match["kills"][player_alive] = 1
    else:
        if player_dead in game_match["kills"].keys():
            game_match["kills"][player_dead] -= 1
        else:
            game_match["kills"][player_dead] = -1

    if show_weapon:
        weapon = m.group(3).strip()
        if weapon in game_match["kills_by_means"].keys():
            game_match["kills_by_means"][weapon] += 1
        else:
            game_match["kills_by_means"][weapon] = 1