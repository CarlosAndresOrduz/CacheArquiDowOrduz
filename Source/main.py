import cache, ram

def main():
    print("Hola mundo")


ram = RAM()
ram.write(0x1000, 0xABCD)
ram.write(0x2000, 0x1234)
ram.write(0x3000, 0x5678)
print(ram)
print(hex(ram.read(0x1000)))
print(hex(ram.read(0x2000)))
print(hex(ram.read(0x3000)))
print(hex(ram.read(0x4000)))