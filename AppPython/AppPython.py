import CommonModule;
import HolstedMetricsModule;
# 1. Читать файл;
# 2. Получить количество строк;

TestPath = "D:\\Projects\\forPython\\_.txt";
with open(TestPath, "r") as inf:
    #CommonModule.StringCountModule(inf);
    #CommonModule.CommenStringOnesCountModule(inf);
    
    # TODO
    #CommonModule.CommenStringOtherCountModule(inf);
    
    HolstedMetricsModule.CheckUniqueProgramOperands();
    HolstedMetricsModule.CheckUniqueProgramOperators();
    HolstedMetricsModule.TotalCountOperands();
    HolstedMetricsModule.TotalCountOperators();
    HolstedMetricsModule.ProgramDictionary();
    HolstedMetricsModule.ProgramLenth();
    HolstedMetricsModule.ProgramVolume();