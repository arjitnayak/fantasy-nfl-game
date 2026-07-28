# Necessary Imports
from dataclasses import dataclass
from enum import Enum
import re

class Position(str, Enum):
    """
    The set of roster positions the game supports

    Inherits from str so members compare equal to their raw string value
    Simplifies loading positions from CSV data
    """
    QB = "QB"
    RB = "RB"
    WR = "WR"
    TE = "TE"
    DST = "DST"
    K = "K"

def build_player_id(name: str, position: Position, team: str) -> str:
    """
    Build an id from a player's name, position, and team.

    Args:
        name: The player's display name
        position: The player's Position enum value
        team: The player's NFL team

    Returns:
        A lowercase, underscore-separated id safe for use as a dict key
    """
    slug_name = re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')
    return f"{slug_name}_{position.lower()}_{team.lower()}"

@dataclass(frozen=True)
class Player:
    """
    A NFL player seasonal data

    Immutable (frozen) by design: a Player represents a historical fact, which shouldn't change once loaded
    Id is always generated consistently in create method
    """
    id: str
    name: str
    position: Position
    team: str
    fantasy_points: float

    @classmethod
    def create(cls, name: str, position: Position, team: str, fantasy_points: float) -> "Player":
        """
        Construct a Player, generating its id automatically

        Args:
            name: The player's display name
            position: The player's Position enum value
            team: The player's NFL team
            fantasy_points: Total season fantasy points (PPR)

        Returns:
            A new, fully-constructed Player with an id

        Raises:
            ValueError: if position is a string that doesn't match any Position member
        """
        if isinstance(position, str):
            position = Position(position)
        player_id = build_player_id(name, position, team)
        return cls(id=player_id, name=name, position=position, team=team, fantasy_points=fantasy_points)