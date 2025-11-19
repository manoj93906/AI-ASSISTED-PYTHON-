from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    """Represents a student with basic bio and marks."""

    name: str
    age: int
    marks: List[float] = field(default_factory=list)

    def details(self) -> None:
        """Print the student's details."""
        print(f"Name: {self.name}, Age: {self.age}")

    def total(self) -> float:
        """Return the total score across all recorded marks."""
        return sum(self.marks)
      
