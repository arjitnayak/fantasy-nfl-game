import random
from dataclasses import dataclass, field
from app.domain.participant import Participant
from app.domain.player import Player

@dataclass
class Game_Engine:
    participants: list[Participant]
    players_by_team: dict[str, list[Player]]
    drafted_player_ids: set[str] = field(default_factory=set)
    current_turn_index: int = 0

    def current_participant(self) -> Participant:
        return self.participants[self.current_turn_index]
    
    def roll_team(self) -> tuple[str, list[Player]]:
        team = random.choice(list(self.players_by_team.keys()))
        return (team, self.players_by_team[team])
        

