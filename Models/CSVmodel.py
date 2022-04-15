from dataclasses import dataclass

@dataclass
class CSV_model:
    header: list[str]
    data: list[list[str]]