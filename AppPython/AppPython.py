import copy;
import CommonModule;
import HolstedMetricsModule;
# 1. Читать файл;
# 2. Получить количество строк;

Inf = "";

TestPath = "D:\\Projects\\forPython\\_.txt";
with open(TestPath, "r") as inf:
   Inf = CommonModule.ReadFile(inf);
    
CommonModule.StringCountModule(Inf);
CommonModule.StringCountModule(Inf);
CommonModule.CommenStringOnesCountModule(Inf);    
    
    # TODO
    #CommonModule.CommenStringOtherCountModule(inf);
    
    #HolstedMetricsModule.CheckUniqueProgramOperands();
    #HolstedMetricsModule.CheckUniqueProgramOperators();
    #HolstedMetricsModule.TotalCountOperands();
    #HolstedMetricsModule.TotalCountOperators();
    #HolstedMetricsModule.ProgramDictionary();
    #HolstedMetricsModule.ProgramLenth();
    #HolstedMetricsModule.ProgramVolume();