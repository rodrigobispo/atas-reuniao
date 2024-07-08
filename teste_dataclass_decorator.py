from dataclasses import dataclass

@dataclass
class Person:
    name: str
    address: str

def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)

if __name__ == "__main__":
    main()