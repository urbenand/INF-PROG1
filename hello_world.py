class Kaffee:
    def __init__(self, name, origin, intensity):
        self.name = name
        self.origin = origin
        self.intensity = intensity
        
coffee1 = Kaffee("Arabica", "Madagascar", 3);
coffee2 = Kaffee("Java", "Indonesia", 2);
coffee3 = Kaffee("Oeppis", "Schweiz", 6);
coffee = [coffee1, coffee2, coffee3]

coffee4 = input()

print("Input: ",coffee4)

for c in coffee:
    print(c.name)
    print(c.origin)
    print(c.intensity,"/10")
    print("---")