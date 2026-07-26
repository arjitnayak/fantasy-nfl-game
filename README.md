# Fantasy NFL Game

A turn-based fantasy football roster-building game. Each turn, a random NFL
team is "rolled" and the active player drafts one player from that team's
roster into an open fantasy slot (QB, RB1, RB2, WR1, WR2, TE, FLEX, D/ST, K).
Highest total fantasy points wins.

## Project structure
- `backend/app/domain/` — core game logic (players, rosters, turn engine)
- `backend/app/api/` — FastAPI routes
- `backend/app/db/` — persistence layer
- `notebooks/` — data exploration
- `frontend/` — React client

## Status
🚧 Early development
