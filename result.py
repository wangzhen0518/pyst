from typing import TypeVar, Generic, Union

T = TypeVar("T")
E = TypeVar("E")


class Ok(Generic[T, E]):
    def __init__(self, value: T) -> None:
        self.value = value


class Err(Generic[T, E]):
    def __init__(self, error: E) -> None:
        self.error = error


Result = Union[Ok[T, E], Err[T, E]]
