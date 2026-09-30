# AGENTS.md — windsurf-cascade-intent-twin

**Company:** Windsurf
**Domain:** Cloud AI Platform Engineering

## Quick Rules
- **Test command:** `PYTHONPATH=src pytest tests/ -v`
- **Lint:** `ruff check src/ tests/`
- **No drive-by edits** — load the skill first.

## Architecture
- `src/windsurf_cascade_intent_twin/core.py` — Domain logic (Cloud AI Platform Engineering)
- `tests/` — Verified test suite
- `.github/workflows/ci.yml` — Enforced CI pipeline
