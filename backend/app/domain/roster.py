from dataclasses import dataclass, field
from app.domain.player import Player, Position

STARTING_SLOTS = ["QB", "RB1", "RB2", "WR1", "WR2", "TE", "FLEX", "DST", "K"]

ELIGIBLE_SLOTS: dict[Position, list[str]] = {
    Position.QB: ["QB"],
    Position.RB: ["RB1","RB2","FLEX"],
    Position.WR: ["WR1","WR2","FLEX"],
    Position.TE: ["TE","FLEX"],
    Position.DST: ["DST"],
    Position.K: ["K"],
}

@dataclass
class Roster:
    """
    A participant's fantasy roster: 9 fixed starting slots 
    """

    slots: dict[str, Player | None] = field(default_factory=lambda: {name: None for name in STARTING_SLOTS})

    def eligible_slots_for(self, player: Player) -> list[str]:
        avaliable_positions = ELIGIBLE_SLOTS[player.position].copy()
        for pos, play in self.slots.items():
            if pos in avaliable_positions and play is not None:
                avaliable_positions.remove(pos)
        return avaliable_positions
    
    def assign(self, player: Player, slot: str) -> None:
        if slot not in self.slots.keys():
            raise ValueError
        if self.slots[slot] is not None:
            raise ValueError
        if slot not in self.eligible_slots_for(player):
            raise ValueError
        self.slots[slot] = player
    
    def is_full(self) -> bool:
        return not None in self.slots.values()
    
    def total_points(self) -> float:
        sum = 0
        for player in self.slots.values():
            if player is None:
                continue
            sum += player.fantasy_points
        return sum