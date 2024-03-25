# docstr-coverage

- `poetry add docstr-coverage`

# pyreverse

- `poetry add pylint`

# pdoc

- `poetry add pdoc`

# Sphinx

1. Install sphinx

- `poetry add sphinx`

2. Initialize

- `sphinx-quickstart`

3. Configure

- add following code to the `conf.py`:
  ```python
  import sys,os
  sys.path.append(os.path.abspath('dokumentace'))
  extensions = ['sphinx.ext.autodoc']
  ```

4. Generate the HTML documentation

- `sphinx-apidoc -o docs/source dokumentace`
- `make html`

# FastAPI

1. Install

- `poetry add fastapi uvicorn`

2. Run

- `uvicorn --port 8889 api:app --reload`
