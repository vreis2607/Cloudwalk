import argparse

from parsers.logParser1 import parse_game_kills
from parsers.logParser2 import report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse log file of quake game matches')
    parser.add_argument('-f', '--logfile',
                        dest='logfile',
                        metavar='logfile',
                        action='store',
                        help='your logfile fullpath',
                        required=True)

    parser.add_argument('-p', dest='plus', action='store_true',
                        help='enable plus mode to show weapons of death')

    parser.add_argument('-r', dest='report', action='store_true',
                        help='print report on finish')

    args = parser.parse_args()
    if args.plus:
        game_matches = parse_game_kills(args.logfile, show_weapon=True)
    else:
        game_matches = parse_game_kills(args.logfile)

    if args.report:
        print(report(game_matches))