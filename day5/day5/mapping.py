class Mapping:
    def __init__(self, destination: int, source: int, range: int) -> None:
        self.destination = destination
        self.source = source
        self.range = range
    
    def __str__(self) -> str:
        return f"Destination: {self.destination}, Source: {self.source}, Range: {self.range}"
    
    def __repr__(self) -> str:
        return f"Destination: {self.destination}, Source: {self.source}, Range: {self.range}"