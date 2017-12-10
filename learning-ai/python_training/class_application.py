class Calculation:
    value = 0
    def square(self):
        return self.value * self.value

# a = Calculation()
# b = Calculation()
# c = Calculation()
#
# calcs = [a, b, c]

calcs = [Calculation(), Calculation(), Calculation()]


calcs[0].value = 3
calcs[1].value = 5
calcs[2].value = 7

print calcs[0].square()
print calcs[1].square()
print calcs[2].square()

for c in calcs:
    print c.square()