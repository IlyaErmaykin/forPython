a = int(input());

strA = str(a);
lenStrA = int(len(strA) - 1);

if (lenStrA == 0):
    if (a < 1 or 5 <= a <= 9):
        print(strA + " программистов");
    elif (2 <= a <=4):
        print(strA + " программиста");
    else:
        print(strA + " программист");
elif (lenStrA == 1 ):
    if (a % 10 == 1 and (a != 11)):
        print(strA + " программист");
    elif (a != 12 and a != 13 and a != 14 and (a % 10 == 2 or a % 10 == 3 or a % 10 == 4)):
        print(strA + " программиста");
    else:
        print(strA + " программистов");
elif (lenStrA == 2 ):
     if (a != 111 and a != 112 and a != 113 and (a % 10 == 1)):
        print(strA + " программист");
     elif (a % 100 != 11 and a % 100 != 12 and a % 100 != 13 and a % 100 != 14 and (a % 10 == 2 or a % 10 == 3 or a % 10 == 4)):
        print(strA + " программиста");
     else:
        print(strA + " программистов");
else:
    print(strA + " программистов");
