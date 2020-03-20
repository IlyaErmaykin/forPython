import copy;
import CommonModule;
import HolstedMetricsModule;
import MathAnalysisModule;
import glob;

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

#TestPath = "D:\\Projects\\forPython\\AppPython\\_temp\\_.txt";
#TestPath_2 = "D:\\Projects\\forPython\\AppPython\\_temp\\help.py";
OperatorsFileName = "D:\\Projects\\forPython\\AppPython\\_temp\\operators.txt";
OutputFile = "D:\\Projects\\forPython\\AppPython\\_temp\\output.txt";

path = "D:\\Projects\\forPython\\AppPython\\test\\";

Files = CommonModule.SerachFiles(path);
print("Количество фаайлов в выбранной директории: " + str(len(Files)));

for file in Files:
    print("Обработка файла: " + file);
    
    with open(file, "r") as inf:
       Inf = CommonModule.ReadFile(inf);

    CommonModule.StringCountModule(Inf);
    CommonModule.CommenStringOnesCountModule(Inf);    
    #CommonModule.CommenStringOtherCountModule(inf);
    #--------------------    

    with open(OperatorsFileName) as f:
        Operators = HolstedMetricsModule.CreateOperatorsDictionary(f);

    with open(file) as f:
        Operators, Operands = HolstedMetricsModule.CreateOperandsDictionary(Operators, f);

    n1, N1, n2, N2 = 0, 0, 0, 0
    n1, N1, n2, N2 = HolstedMetricsModule.PtintFunction(Operators, Operands);

    HolstedMetricsModule.CountMetrics(n1, N1, n2, N2, OutputFile)

MathAnalysisModule.getKohonenNetworkAnalysis(OutputFile);

print("");  
    