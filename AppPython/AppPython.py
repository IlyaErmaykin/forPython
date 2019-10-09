f = str(input());
a = 0;
b = 0;
c = 0;
pi = 3.14;
p = 0;
S = 0.0;

if (f == "треугольник"):
    a = int(input());
    b = int(input());
    c = int(input());
    p = (a + b + c) / 2;
    S = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif (f == "прямоугольник"):
    S = (int(input()) * int(input()));
else:
    S = (pi * (int(input()) ** 2));
print(float(S));
