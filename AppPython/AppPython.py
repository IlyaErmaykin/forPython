import sys;

List = [];

for arg in range(len(sys.argv)):
    List.append(sys.argv[arg]); 

List.pop(0)

for arg in range(len(List)):
    print(List[arg], end=" ");