from app.domain.roster import Roster
from dataclasses import dataclass, field
@dataclass(frozen=True)
class Participant:
    """
    A single player or AI in the game

    Frozen property is set to true because we don't want 
    any of the other properties to be mutable. Roster is
    always mutable because the frozen property is set to false
    """
    id: str
    name: str
    is_ai: bool
    roster: Roster = field(default_factory=Roster)
