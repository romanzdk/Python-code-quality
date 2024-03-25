cq:
	- @echo "================== LINTING (ruff) =================="
	- ruff check
	- @echo "\n\n================== TYPE CHECK (mypy) =================="
	- mypy .
	- @echo "\n\n================== FORMATTING (isort) =================="
	- isort --check-only . 
	- @echo "\n\n================== FORMATTING (black) =================="
	- black --check .
test:
	pytest