# Python code quality

Resources for online course `Python code quality` created in 2024 for [Skillmea.sk](https://skillmea.sk) portal.

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

# Tools covered

## Project management

- Pipenv
- Poetry
- Hatch
- Pdm
- Uv
- Rye

## Linting

- Pylint
- Ruff
- Flake8

## Typing

- Pyright
- Mypy
- Pyre
- Dataclass
- Pydantic

## Formátování

- Black
- Autopep8
- Yapf
- Isort

## Bezpečnost

- Bandit
- Safety

## Testování

- Unittest
- Pytest
- Doctest
- Coverage

## Dokumentace

- Sphinx
- Pdoc

## Automatizace

- Make
- Just
- Task
- Poe the poet
- Tox
- Nox
- Pre-commit
- SonarQube

## HW náročnost

- Cprofile
- Snakeviz
- Pyinstrument
- Guppy3
- Numba
- Nuitka
- Codon
- PyO3
- Cython
- Line-profiler
- Memory-profiler
- Tracemalloc
- Gc
- Timeit

## Složitost

- Radon
- Cognitive-complexity
