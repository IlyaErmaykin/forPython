a = float(input());
b = float(input());
op = str(input());
if(op == "+"):
    res = ((a) + (b));
elif (op == "-"):
    res = ((a) - (b));
elif (op == "*"):
    res = ((a) * (b));
elif (op == "/") and (b != 0.0):
    res = ((a) / (b));
elif (op == "mod") and (b != 0.0):
    res = ((a) % (b));
elif (op == "pow"):
    res = ((a) ** (b));
elif (op == "div") and (b != 0.0):
    res = ((a) // (b));
else:
    res = "Деление на 0!";
print(res);
