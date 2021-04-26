from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated" and player not in self.players:
            return f"Player {player.name} is in another guild."
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        current_player = [p for p in self.players if p.name == player_name]
        if not player:
            return f"Player {player_name} is not in the guild."
        current_player = current_player[0]
        self.players.remove(current_player)
        current_player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += f"{player.player_info()}\n"
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())