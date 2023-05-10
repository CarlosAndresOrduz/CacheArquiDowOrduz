from typing import Dict, List, Tuple

class RAM:
    class Address:
        def _init_(self, address: int, value: int = 0) -> None:
            self.address = address
            self.value = value
        
        def _repr_(self) -> str:
            return f"{self.address:08X} {self.value:08X}"
        
        def _lt_(self, other: 'RAM.Address') -> bool:
            return self.address < other.address
    
    def _init_(self) -> None:
        self.memory: List[RAM.Address] = []
        
    def _repr_(self) -> str:
        return "\n".join([str(address) for address in sorted(self.memory)])
        
    def write(self, address: int, value: int) -> None:
        for addr in self.memory:
            if addr.address == address:
                addr.value = value
                return
        self.memory.append(RAM.Address(address, value))
        self.memory.sort()
        
    def read(self, address: int) -> int:
        for addr in self.memory:
            if addr.address == address:
                return addr.value
        return 0
    