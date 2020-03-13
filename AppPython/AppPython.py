import copy;
import CommonModule;
import HolstedMetricsModule;

# + 1. Читать файл;
# + 2. Получить количество строк;
# + 3. Получить количество строк с однострочными комментариями;
# 4. Получить количество строк с многострочными комментариями;
#--------------------
# + 5. Читать файл операторов;
# + 6. Создать словарь операторов;


Inf = "";
Files = [];
Operators = {};
Operands = {};

TestPath = "D:\\Projects\\forPython\\AppPython\\_temp\\_.txt";
TestPath_2 = "D:\\Projects\\forPython\\AppPython\\_temp\\help.py";
OperatorsFileName = "D:\\Projects\\forPython\\AppPython\\_temp\\operators.txt";

path = "D:\\Projects\\forPython\\AppPython\\_temp\\";

Files = CommonModule.SerachFiles(path);

for file in Files:
    print(file);

with open(TestPath_2, "r") as inf:
   Inf = CommonModule.ReadFile(inf);

CommonModule.StringCountModule(Inf);
CommonModule.CommenStringOnesCountModule(Inf);    
#CommonModule.CommenStringOtherCountModule(inf);
#--------------------    

with open(OperatorsFileName) as f:
    Operators = HolstedMetricsModule.CreateOperatorsDictionary(f);

with open(TestPath_2) as f:
    Operators, Operands = HolstedMetricsModule.CreateOperandsDictionary(Operators, f);

n1, N1, n2, N2 = 0, 0, 0, 0
n1, N1, n2, N2 = HolstedMetricsModule.PtintFunction(Operators, Operands);

HolstedMetricsModule.CountMetrics(n1, N1, n2, N2)
print("");  
#HolstedMetricsModule.CheckUniqueProgramOperands();
#HolstedMetricsModule.CheckUniqueProgramOperators();
#HolstedMetricsModule.TotalCountOperands();
#HolstedMetricsModule.TotalCountOperators();
#HolstedMetricsModule.ProgramDictionary();
#HolstedMetricsModule.ProgramLenth();
#HolstedMetricsModule.ProgramVolume();