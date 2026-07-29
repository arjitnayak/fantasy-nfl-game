# Necessary Imports
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
        """
        Return which of this player's possible slots are currently open

        Args:
            player: The player being considered for a slot

        Returns:
            A list of open slot names that player's
            position is allowed to fill
        """
        avaliable_positions = ELIGIBLE_SLOTS[player.position].copy()
        for pos, play in self.slots.items():
            if pos in avaliable_positions and play is not None:
                avaliable_positions.remove(pos)
        return avaliable_positions
    
    def assign(self, player: Player, slot: str) -> None:
        """
        Place a player into a specific slot

        Args:
            player: The player being drafted onto this roster
            slot: The specific slot name to place them in

        Raises:
            ValueError: if the slot doesn't exist, is already filled,
                or the player isn't eligible for that slot
        """
        if slot not in self.slots.keys():
            raise ValueError(f"'{slot}' is not a valid roster slot")
        if self.slots[slot] is not None:
            raise ValueError(f"Slot '{slot}' is already filled")
        if slot not in self.eligible_slots_for(player):
            raise ValueError(f"{player.name} ({player.position.value}) is not eligible for slot '{slot}'")
        self.slots[slot] = player
    
    def is_full(self) -> bool:
        """
        Returns true if all 9 slots are filled
        """
        return not None in self.slots.values()
    
    def total_points(self) -> float:
        """
        Sum of fantasy_points across all filled slots. Empty slots contribute 0
        """
        sum = 0
        for player in self.slots.values():
            if player is None:
                continue
            sum += player.fantasy_points
        return sum