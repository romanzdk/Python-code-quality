import nox


@nox.session
def lint(session):
    session.run("ruff", "check")

@nox.session
def type_check(session):
    session.run("mypy", ".")

@nox.session
def format(session):
    session.run("isort","--check-only", ".")
    session.run("black", "--check", ".")

@nox.session
def cq(session):
    for session_instance in (lint, type_check, format):
        try:
            session_instance(session)
        except:
            pass

@nox.session
def test(session):
    session.run("pytest", ".")
