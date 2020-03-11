import copy;
import CommonModule;
import HolstedMetricsModule;
# + 1. Читать файл;
# + 2. Получить количество строк;
# + 3. Получить количество строк с однострочными комментариями;
# 4. Получить количество строк с многострочными комментариями;
#--------------------
# + 5. Читать файл операторов;


Inf = "";
Operators = {}

TestPath = "D:\\Projects\\forPython\\AppPython\\_temp\\_.txt";
OperatorsFileName = "D:\\Projects\\forPython\\AppPython\\_temp\\operators.txt";

#with open(TestPath, "r") as inf:
#   Inf = CommonModule.ReadFile(inf);

#CommonModule.StringCountModule(Inf);
#CommonModule.CommenStringOnesCountModule(Inf);    
#CommonModule.CommenStringOtherCountModule(inf);
#--------------------    

with open(OperatorsFileName) as f:
    Operators = HolstedMetricsModule.CreateOperatorsDictionary(f)
    print(Operators);

#HolstedMetricsModule.CheckUniqueProgramOperands();
#HolstedMetricsModule.CheckUniqueProgramOperators();
#HolstedMetricsModule.TotalCountOperands();
#HolstedMetricsModule.TotalCountOperators();
#HolstedMetricsModule.ProgramDictionary();
#HolstedMetricsModule.ProgramLenth();
#HolstedMetricsModule.ProgramVolume();