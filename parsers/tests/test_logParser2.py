import pytest

from parsers.logParser2 import report


class TestLogParser2:
    """
    Run tests on logParser2 report
    """

    @pytest.fixture
    def parsed_game_matches(self):
        return {
            'game_1': {
                'total_kills': 11,
                'kills': {
                    'Mocinha': 1,
                    'Isgalamido': 2
                },
                'players': ['Isgalamido', 'Mocinha']
            },
            'game_2': {
                'total_kills': 4,
                'kills': {'Mocinha': 1},
                'players': ['Isgalamido', 'Mocinha', 'Zeh', 'Dono da Bola']
            }
        }

    @pytest.fixture
    def parsed_game_matches_with_weapons(self):
        return {
            'game_1': {
                'total_kills': 11,
                'kills': {
                    'Mocinha': 1,
                    'Isgalamido': 2
                },
                'players': ['Isgalamido', 'Mocinha'],
                'kills_by_means': {
                    'MOD_ROCKET_SPLASH': 60,
                }
            },
            'game_2': {
                'total_kills': 4,
                'kills': {'Mocinha': 1},
                'players': ['Isgalamido', 'Mocinha', 'Zeh', 'Dono da Bola'],
                'kills_by_means': {
                    'MOD_RAILGUN': 9,
                    'MOD_MACHINEGUN': 4,
                    'MOD_TRIGGER_HURT': 14,
                    'MOD_SHOTGUN': 4,
                    'MOD_ROCKET_SPLASH': 60,
                    'MOD_FALLING': 3,
                    'MOD_ROCKET': 37
                }
            }
        }

    def test_write_correct_report(self, parsed_game_matches):
        msg = report(parsed_game_matches)
        assert "game_2" in msg
        assert "Total kills: \n- 4" in msg
        assert ("Players: \n- "
                "Isgalamido, Mocinha, Zeh, Dono da Bola") in msg
        assert "Kills:\n- Mocinha: 1" in msg

        assert "game_1" in msg
        assert "Total kills: \n- 11" in msg
        assert "Players: \n- Isgalamido, Mocinha" in msg
        assert "Kills:" in msg
        assert "\n- Isgalamido: 2" in msg
        assert "\n- Mocinha: 1" in msg

    def test_write_correct_report_with_weapons(self, parsed_game_matches_with_weapons):
        msg = report(parsed_game_matches_with_weapons)
        assert "game_2" in msg
        assert "Total kills: \n- 4" in msg
        assert ("Players: \n- "
                "Isgalamido, Mocinha, Zeh, Dono da Bola") in msg
        assert "Kills:\n- Mocinha: 1" in msg

        assert "\n- MOD_TRIGGER_HURT: 14" in msg
        assert "\n- MOD_RAILGUN: 9" in msg
        assert "\n- MOD_ROCKET: 37" in msg
        assert "\n- MOD_FALLING: 3" in msg
        assert "\n- MOD_MACHINEGUN: 4" in msg
        assert "\n- MOD_ROCKET_SPLASH: 60" in msg
        assert "\n- MOD_SHOTGUN: 4" in msg

        assert "game_1" in msg
        assert "Total kills: \n- 11" in msg
        assert "Players: \n- Isgalamido, Mocinha" in msg
        assert "Kills:" in msg
        assert "\n- Isgalamido: 2" in msg
        assert "\n- Mocinha: 1" in msg

        assert "\n- MOD_ROCKET_SPLASH: 60" in msg
