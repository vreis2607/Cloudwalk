# Function to format text
def report(parsed_game_matches):

    message = ""
    for game_match, values in parsed_game_matches.items():
        # import ipdb; ipdb.set_trace()
        players = ", ".join(values['players'])
        total_kills = values['total_kills']
        kills = values['kills']

        message += "\n\n{}{}{}\n\n".format("-~"*20, game_match, "-~"*20)
        message += "Total kills: \n- {}\n\n".format(total_kills)
        message += "Players: \n- {}\n\n".format(players)
        message += "Kills:\n"

        for player_name, kills in kills.items():
            message += "- {}: {}\n".format(player_name, kills)

        if 'kills_by_means' in values.keys():
            message += "Weapons - Means of death:\n"
            kills_by_means = values['kills_by_means']

            for weapon_name, kills in kills_by_means.items():
                message += "- {}: {}\n".format(weapon_name, kills)

    return message