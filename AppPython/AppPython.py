s = str(input());
d = len(s);
c = 1;
r = "";
for i in range(d):
        if (d - i == 1):
            print(s[i] + str(c), end="");
            continue;
        if(s[i] != s[i + 1]):
            print(s[i] + str(c), end="");
            c = 1;
        elif(s[i] == s[i + 1]):
            r = s[i] + str(c);
            c += 1;
        else:
            print(r);
            r = "";
            c = 1;