1. Install dependencies

- `poetry add black yapf autopep8 isort`

2. Format using black

- `cat formatting.py | black - > formatting_black.py`

3. Format using yapf

- `yapf formatting.py > formatting_yapf.py`

4. Format using autopep8

- `autopep8 formatting.py > formatting_autopep.py`

5. Format using isort

- `isort -d formatting.py > formatting_isort.py`
