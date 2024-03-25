lint:
  - echo "================== LINTING (ruff) =================="
  - ruff check

type_check:
  - echo "\n\n================== TYPE CHECK (mypy) =================="
  - mypy .

format:
  - echo "\n\n================== FORMATTING (isort) =================="
  - isort --check-only .
  - echo "\n\n================== FORMATTING (black) =================="
  - black --check .

cq:
  - just lint
  - just type_check
  - just format
