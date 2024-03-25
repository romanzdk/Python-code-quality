from typing import Any, List, Optional, TypedDict, Union


def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

###############################################################################

def calculate_area(radius: float, pi: float = 3.14) -> float:
    return pi * radius ** 2

print(calculate_area(5))

###############################################################################

def summarize_scores(scores: list[int]) -> dict:
    return {
        "average": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores),
    }

print(summarize_scores(['abc', 'def']))

###############################################################################

def get_user_role(user_id: int | str) -> str:
    if user_id == "admin" or user_id == 1:
        return "Administrator"
    else:
        return "Regular user"

print(get_user_role("admin"))
print(get_user_role(2))
print(get_user_role({'abc':123}))

###############################################################################

class User(TypedDict):
    id: int
    name: str
    email: str

def send_email_to_users(users: list[User]) -> None:
    for user in users:
        print(f"Sending email to {user['name']} at {user['email']}")

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

send_email_to_users(users)

###############################################################################

def process_value(value: Any) -> str:
    match value:
        case int():
            return "Received an integer"
        case str():
            return "Received a string"
        case _:
            return "Received an unknown type"

print(process_value(10))
print(process_value("hello"))
print(process_value([123,12345]))
