class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        if not self.a:
            root = -self.c / self.b
        else:
            d = pow(self.b, 2) - 4 * self.a * self.c
            if not d:
                root = -self.b / (2 * self.a)
                print(f"Roots are real and equal and is : {root}")
            elif d > 0:
                root1 = (-self.b + pow(d, 0.5)) / (2 * self.a)
                root2 = (-self.b - pow(d, 0.5)) / (2 * self.a)
                print(f"Roots are real and distinct = {root1} and {root2}")
            else:
                rp = -self.b / (2 * self.a)
                ip = pow(abs(d), 0.5) / (2 * self.a)
                print(f"Roots are imaginary and is = {rp}+{ip}i and {rp}-{ip}i")

def main():
    a, b, c = map(int, input("Enter a, b and c values: ").split())
    q = Quadratic(a, b, c)
    q.roots()

if __name__ == "__main__":
    main()
