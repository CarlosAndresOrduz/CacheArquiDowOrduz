from typing import Dict, List, Tuple
import ram
    
class Cache:
    class Block:
        def _init_(self, tag: int, data: List[int], valid: bool = False, dirty: bool = False, age: int = 0):
            self.tag = tag
            self.data = data
            self.valid = valid
            self.dirty = dirty
            self.age = age
        
        def _repr_(self):
            return f"tag: {self.tag:X}, data: {self.data}, valid: {self.valid}, dirty: {self.dirty}, age: {self.age}"
    
    def _init_(self, ram: RAM):
        self.ram = ram
        self.block_size = 8
        self.set_size = 2
        self.num_sets = 16
        self.blocks_per_set = self.set_size
        self.num_blocks = self.num_sets * self.blocks_per_set
        self.cache: Dict[int, List[Cache.Block]] = {set_num: [Cache.Block(0, [0] * self.block_size) for _ in range(self.blocks_per_set)] for set_num in range(self.num_sets)}
    
    def read(self, address: int) -> int:
        tag, set_num, offset = self._decode_address(address)
        for block in self.cache[set_num]:
            if block.valid and block.tag == tag:
                block.age = 0
                return block.data[offset]
        block = self._find_empty_block(set_num)
        if block is None:
            block = self._find_oldest_block(set_num)
            if block.dirty:
                self._write_back(block)
        block.tag = tag
        block.data = self.ram.read_block(address, self.block_size)
        block.valid = True
        block.dirty = False
        block.age = 0
        return block.data[offset]
    
    def write(self, address: int, value: int) -> None:
        tag, set_num, offset = self._decode_address(address)
        for block in self.cache[set_num]:
            if block.valid and block.tag == tag:
                block.data[offset] = value
                block.dirty = True
                block.age = 0
                return
        block = self._find_empty_block(set_num)
        if block is None:
            block = self._find_oldest_block(set_num)
            if block.dirty:
                self._write_back(block)
        block.tag = tag
        block.data = self.ram.read_block(address, self.block_size)
        block.data[offset] = value
        block.valid = True
        block.dirty = True
        block.age = 0
    
    def _decode_address(self, address: int) -> Tuple[int, int, int]:
        offset = address % self.block_size
        set_num = (address // self.block_size) % self.num_sets
        tag = address // (self.block_size * self.num_sets)
        return tag, set_num, offset
    
    def _find_empty_block(self, set_num: int) -> Cache.Block:
        for block in self.cache[set_num]:
            if not block.valid:
                return block
        return None
    
    def _find_oldest_block(self, set_num: int) -> Cache.Block:
        oldest_block = None
        for block in self.cache[set_num]:
            if oldest_block is None or block.age > oldest_block.age:
                oldest_block = block
            block.age += 1
        return oldest_block
    
    def _write_back(self, block: Cache.Block) -> None:
        address = (block.tag * self.num_sets + self.cache.index(block)) * self.block_size
        self.ram.write_block(address, block.data)
        block.dirty = False

    def read_block(self, address: int, size: int) -> List[int]:
        block_address = address // self.block_size * self.block_size
        block_data = []
        for i in range(size):
            block_data.append(self.read(block_address + i))
        return block_data
    
    def write_block(self, address: int, data: List[int]) -> None:
        block_address = address // self.block_size * self.block_size
        for i, value in enumerate(data):
            self.write(block_address + i, value)