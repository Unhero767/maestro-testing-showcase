# Architecture & Taxonomy

## Folder Layout
- `src/main/core/`: Contains fundamental domain business logic.
- `src/main/utils/`: Pure helper functions with zero side effects.
- `src/main/services/`: External adapters, database hooks, and API clients.
- `tests/unit/`: Isolated, fast-running unit tests targeting discrete functions.
- `tests/integration/`: Service and database interaction validations.
