import re

# Regex match start game
start_regex = re.compile(r".*InitGame:.*")

# Regex match kill lines of log
kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")