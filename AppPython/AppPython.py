import copy;
import CommonModule;
import HolstedMetricsModule;
# 1. Читать файл;
# 2. Получить количество строк;
# 3. Получить количество строк с однострочными комментариями;

Inf = "";

TestPath = "D:\\Projects\\forPython\\_.txt";
with open(TestPath, "r") as inf:
   Inf = CommonModule.ReadFile(inf);

CommonModule.StringCountModule(Inf);
CommonModule.CommenStringOnesCountModule(Inf);    
#CommonModule.CommenStringOtherCountModule(inf);
    
    #HolstedMetricsModule.CheckUniqueProgramOperands();
    #HolstedMetricsModule.CheckUniqueProgramOperators();
    #HolstedMetricsModule.TotalCountOperands();
    #HolstedMetricsModule.TotalCountOperators();
    #HolstedMetricsModule.ProgramDictionary();
    #HolstedMetricsModule.ProgramLenth();
    #HolstedMetricsModule.ProgramVolume();