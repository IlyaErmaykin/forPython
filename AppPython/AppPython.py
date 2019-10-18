s = str(input());
sL = s.lower();
strNum = 0;
res = 0;
n = 0;
for i in sL:
    strNum = strNum + 1;

n = sL.count("c") + sL.count("g");
res = float((n / strNum) * 100);
print(res);     

