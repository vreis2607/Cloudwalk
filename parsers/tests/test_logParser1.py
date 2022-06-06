import os
import pytest

from parsers.logParser1 import parse_game_kills, parse_kill_line


class TestLogParser1:
    """
    Run tests on logParser1 parser
    """
    # Path to the custom logfile "test.log"
    @pytest.fixture
    def task1_logfile(self):
        logfile = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'fixtures',
            'test.log')
        return logfile

    def test_parse_game_kills(self, task1_logfile):
        parsed_dict = dict(parse_game_kills(task1_logfile))
        assert parsed_dict == {
            'game_1': {
                'total_kills': 11,
                'players': ['Isgalamido', 'Mocinha'],
                'kills': {
                    'Isgalamido': -5
                }
            },
            'game_2': {
                'total_kills': 4,
                'players': ['Isgalamido', 'Mocinha', 'Zeh', 'Dono da Bola'],
                'kills': {
                    'Zeh': -2,
                    'Dono da Bola': -1,
                    'Isgalamido': 1
                }
            }
        }

    def test_parse_game_kills_with_show_weapons(self, task1_logfile):
        parsed_dict = dict(parse_game_kills(task1_logfile, show_weapon=True))
        assert parsed_dict == {
            'game_1': {
                'total_kills': 11,
                'kills_by_means': {
                    'MOD_ROCKET_SPLASH': 3,
                    'MOD_TRIGGER_HURT': 7,
                    'MOD_FALLING': 1
                },
                'players': ['Isgalamido', 'Mocinha'],
                'kills': {'Isgalamido': -5}
            },
            'game_2': {
                'total_kills': 4,
                'kills_by_means': {
                    'MOD_FALLING': 1,
                    'MOD_TRIGGER_HURT': 2,
                    'MOD_ROCKET': 1
                },
                'players': ['Isgalamido', 'Mocinha', 'Zeh', 'Dono da Bola'],
                'kills': {
                    'Zeh': -2,
                    'Dono da Bola': -1,
                    'Isgalamido': 1
                }
            }
        }

    def test_parse_kill_line(self):
        game_match = {
            "total_kills": 0,
            "players": [],
            "kills": {}
        }
        line = ("20:54 Kill: 1022 2 22: <world> killed Isgalamido "
                "by MOD_TRIGGER_HURT")
        parse_kill_line(line, game_match)
        assert game_match == {
            'players': ['Isgalamido'],
            'total_kills': 1,
            'kills': {'Isgalamido': -1},
        }

        line = ("22:06 Kill: 2 3 7: Isgalamido killed Mocinha by "
                "MOD_ROCKET_SPLASH")
        parse_kill_line(line, game_match)
        assert game_match == {
            'players': ['Isgalamido', 'Mocinha'],
            'total_kills': 2,
            'kills': {'Isgalamido': 0},
        }

    def test_parse_kill_line_with_show_weapons(self):
        game_match = {
            "total_kills": 0,
            "players": [],
            "kills": {},
            "kills_by_means": {},
        }
        line = ("20:54 Kill: 1022 2 22: <world> killed Isgalamido "
                "by MOD_TRIGGER_HURT")
        parse_kill_line(line, game_match, show_weapon=True)
        assert game_match == {
            'players': ['Isgalamido'],
            'kills_by_means': {
                'MOD_TRIGGER_HURT': 1
            },
            'total_kills': 1,
            'kills': {
                'Isgalamido': -1
            },
        }

        line = ("22:06 Kill: 2 3 7: Isgalamido killed Mocinha by "
                "MOD_ROCKET_SPLASH")
        parse_kill_line(line, game_match, show_weapon=True)
        assert game_match == {
            'players': ['Isgalamido', 'Mocinha'],
            'kills_by_means': {
                'MOD_TRIGGER_HURT': 1,
                'MOD_ROCKET_SPLASH': 1
            },
            'total_kills': 2,
            'kills': {
                'Isgalamido': 0
            }
        }
