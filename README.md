# Python code quality

Resources for online course `Python code quality` created in 2024 for [Skillmea.sk](https://skillmea.sk) portal available at [link](https://skillmea.cz/online-kurzy/python-code-quality)

# Content

```
.
├── Justfile
├── Makefile
├── README.md
├── automatizace
│   ├── README.md
│   ├── cq.sh
│   └── cq_adv.sh
├── bezpecnost
│   ├── README.md
│   └── bezpecnost.py
├── cleanup.sh
├── dokumentace
│   ├── README.md
│   ├── README_example.md
│   ├── __init__.py
│   ├── api.py
│   ├── api_complex.py
│   ├── classes_documentation.png
│   ├── conf.py
│   ├── docstrings.py
│   ├── docstrings_google.py
│   ├── docstrings_numpy.py
│   ├── doctest_priklad.py
│   ├── komentare.py
│   └── uml.py
├── fastapi_demo
│   ├── README.md
│   └── cq.sh
├── formatting
│   ├── README.md
│   ├── formatting.py
│   ├── formatting_autopep.py
│   ├── formatting_black.py
│   ├── formatting_isort.py
│   └── formatting_yapf.py
├── linting
│   ├── README.md
│   └── linting.py
├── noxfile.py
├── performance
│   ├── big_o.py
│   ├── compilers
│   │   ├── README.md
│   │   └── numba_test.py
│   ├── extensions
│   │   ├── README.md
│   │   ├── c_extensions
│   │   │   ├── app.py
│   │   │   ├── build.sh
│   │   │   ├── example.c
│   │   │   └── setup.py
│   │   ├── cython_example
│   │   │   ├── app.py
│   │   │   ├── fib.c
│   │   │   ├── fib.pyx
│   │   │   ├── fib_app.py
│   │   │   ├── lib.c
│   │   │   ├── lib.pyx
│   │   │   └── setup.py
│   │   └── rust_extension
│   │       ├── Cargo.lock
│   │       ├── Cargo.toml
│   │       ├── app.py
│   │       └── src
│   │           └── lib.rs
│   ├── interpreters
│   │   ├── README.md
│   │   ├── codon_test.py
│   │   └── get_interpreter.py
│   ├── profiling
│   │   ├── README.md
│   │   ├── cprofile_test.py
│   │   ├── gc_test.py
│   │   ├── line_profiling_test.py
│   │   ├── mprof_example.py
│   │   ├── run_cprofile.sh
│   │   ├── run_timeit.sh
│   │   ├── scalene_test.py
│   │   └── tracemalloc_test.py
│   └── pythons
│       ├── README.md
│       ├── benchmark.sh
│       ├── concurrency.py
│       ├── cpu.py
│       ├── data.py
│       ├── fib.py
│       ├── io.py
│       ├── mandelbrot.py
│       └── test_file.txt
├── poetry.lock
├── project_management
│   ├── pip
│   │   ├── dev-requirements.txt
│   │   ├── requirements.txt
│   │   └── setup.py
│   ├── pipenv
│   │   ├── Pipfile
│   │   └── Pipfile.lock
│   └── poetry
│       ├── poetry.lock
│       └── pyproject.toml
├── pyproject.toml
├── slozitost
│   ├── README.md
│   └── slozitost.py
├── testy
│   ├── __init__.py
│   ├── complex
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── doctest_example.py
│   │   ├── pytest_example.py
│   │   └── unittest_example.py
│   ├── coverage.sh
│   └── simple
│       ├── __init__.py
│       ├── app.py
│       ├── doctest_example.py
│       ├── pytest_example.py
│       └── unittest_example.py
└── typing
    ├── README.md
    ├── dataclass_example.py
    ├── pydantic_example.py
    └── validators.py

25 directories, 100 files
```

# Odkazy

## Project management

- https://github.com/pypa/pip
- https://github.com/pypa/virtualenv
- https://github.com/pypa/pipenv
- https://github.com/pdm-project/pdm
- https://github.com/pypa/hatch
- https://github.com/astral-sh/rye
- https://github.com/astral-sh/uv
- https://github.com/python-poetry/poetry

- https://packaging.python.org/en/latest/
- https://github.com/pypa

## Linting

- https://github.com/pylint-dev/pylint
- https://github.com/astral-sh/ruff

## Formátování

- https://peps.python.org/pep-0008/
- https://github.com/google/styleguide/blob/gh-pages/pyguide.md
- https://github.com/psf/black
- https://github.com/google/yapf
- https://github.com/hhatto/autopep8
- https://github.com/PyCQA/isort
- https://peps.python.org/pep-0020/

## Typing

- https://peps.python.org/pep-0484/
- https://peps.python.org/pep-0526/

- https://docs.python.org/3/library/typing.html
- https://docs.python.org/3/library/dataclasses.html

- https://github.com/pydantic/pydantic
- https://github.com/python/mypy
- https://github.com/microsoft/pyright
- https://github.com/facebook/pyre-check

## Dokumentace

- https://peps.python.org/pep-0257/
- https://devguide.python.org/documentation/style-guide/#economy-of-expression

- https://docs.python.org/3/library/doctest.html

- https://github.com/sphinx-doc/sphinx
- https://github.com/mitmproxy/pdoc

- https://peps.python.org/pep-0008/#comments

- https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
- https://github.com/abhisheknaiidu/awesome-github-profile-readme
- https://github.com/matiassingers/awesome-readme
- https://github.com/hackergrrl/art-of-readme
- https://www.makeareadme.com/
- https://shields.io/
- https://choosealicense.com/

- https://miro.com/
- https://app.diagrams.net/
- https://www.lucidchart.com/
- https://www.powerdesigner.biz/
- https://sparxsystems.com/

- https://spec.openapis.org/oas/latest.html
- https://learning.postman.com/docs/integrations/available-integrations/working-with-openAPI/

## Testy

- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/doctest.html
- https://github.com/pytest-dev/pytest

- https://coverage.readthedocs.io/en/7.4.4/
- https://github.com/pytest-dev/pytest-cov

## Složitost kódu

- https://github.com/rubik/radon
- https://www.python.org/download/releases/2.3/mro/
- https://github.com/Melevir/flake8-cognitive-complexity

## Zabezpečení

- https://github.com/PyCQA/bandit
- https://github.com/pyupio/safety
- https://github.com/pypa/pip-audit

## HW náročnost

- https://docs.python.org/3/library/profile.html
- https://github.com/pyutils/line_profiler
- https://github.com/joerick/pyinstrument
- https://github.com/pberkes/big_O

- https://github.com/plasma-umass/scalene
- https://github.com/benfred/py-spy

- https://docs.python.org/3/library/tracemalloc.html
- https://docs.python.org/3/library/gc.html
- https://github.com/giampaolo/psutil
- https://github.com/htop-dev/htop
- https://github.com/pythonprofilers/memory_profiler
- https://github.com/zhuyifei1999/guppy3/

- https://wiki.python.org/moin/TimeComplexity

- https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-faster-cpython
- https://docs.python.org/3/whatsnew/3.12.html#asyncio

- https://github.com/modin-project/modin
- https://github.com/dask/dask

- https://github.com/numba/numba
- https://github.com/Nuitka/Nuitka

- https://github.com/exaloop/codon
- https://github.com/micropython/micropython
- https://github.com/RustPython/RustPython

- https://github.com/pola-rs/polars
- https://github.com/duckdb/duckdb
- https://github.com/apache/spark

- https://github.com/PyO3/pyo3
- https://github.com/cython/cython

## Automatizace

- https://github.com/tox-dev/tox
- https://github.com/wntrblm/nox
- https://github.com/cjolowicz/nox-poetry
- https://github.com/nat-n/poethepoet
- https://www.gnu.org/software/make/
- https://github.com/go-task/task
- https://github.com/casey/just
- https://github.com/SonarSource/sonarqube
- https://github.com/pre-commit/pre-commit

- https://docs.github.com/en/actions
- https://docs.gitlab.com/ee/ci/
- https://azure.microsoft.com/en-us/products/devops/pipelines
- https://circleci.com/
- https://www.jenkins.io/

## FastAPI Demo

- https://github.com/tiangolo/fastapi

## Business hledisko

- https://martinfowler.com/articles/is-quality-worth-cost.html

## Souhrn

- http://cleancoder.com
- https://www.martinfowler.com/
- https://www.sonarsource.com/

- https://stackoverflow.blog/2021/10/18/code-quality-a-concern-for-businesses-bottom-lines-and-empathetic-programmers/
- https://martinfowler.com/articles/is-quality-worth-cost.html
- https://docs.gitlab.com/ee/ci/testing/code_quality.html
- https://codescene.com/blog/3-code-health-kpis/
- https://codescene.io/docs/guides/technical/code-health.html
- https://codescene.com/blog/code-biomarkers/

- https://python.cz/
- https://pyvec.org/
- https://europython.eu/
- https://pycoders.com/

- https://linkedin.com/in/romanzdk
- https://romanzdk.com
