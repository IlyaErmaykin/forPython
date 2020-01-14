n = int(input());
List = [];

for word in range(n):
    List.append(str(input()).lower());
#print(List);

nLine = int(input());
linesList = [];
multitude = set();

for line in range(nLine):
    l = str(input().lower()).split();
    for el in range(len(l)):
        multitude.add(str(l[el]));
#print(linesList);

for el in range(len(List)):
    if (List[el] in multitude):
        multitude.remove(List[el]);
    else:
        continue;

for el in multitude:
    print(el);


