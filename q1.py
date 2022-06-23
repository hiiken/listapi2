f = float(input())
e = float(input())
y = float(input())

def vox(f, e, y):
    valorvox = (f * e**2 * y**3)/(f + e + y)
    return valorvox

valorvox = vox(f, e, y)

print("vox = {:.2f}".format(valorvox))