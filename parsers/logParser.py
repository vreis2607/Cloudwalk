import re

# Regex match start game
start_regex = re.compile(r".*InitGame:.*")

# Regex match kill lines of log
kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")

# Function to parse games, kills, players
def parse_game_kills(logfile, show_weapon=False):
    """Get logfile and parse results into OrderedDict"""
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