from math import log2;

# Функция создания словаря операторов;
def CreateOperatorsDictionary(inf):
    operators = {}
    n1, N1 = 0, 0;

    for op in inf:
        operators[op.replace('\n','')] = 0
    
    return operators;

# Функция получения уникального числа операторов;
def CheckUniqueProgramOperators():
    pass;

# Функция создания словаря операторов;
def CreateOperandsDictionary(operators, f):
    operands = {};
    isAllowed = True;
    n2, N2 = 0, 0;

    for line in f:
        line = line.strip("\n").strip(' ')

        if(line.startswith("/*")):
            isAllowed = False
       
        if((not line.startswith("//")) and isAllowed == True and (not line.startswith('#'))):
            for key in operators.keys():
                operators[key] = operators[key] + line.count(key)
                line = line.replace(key,' ')
            for key in line.split():
                if key in operands:
                    operands[key] = operands[key] + 1
                else:
                    operands[key] = 1

        if(line.endswith("*/")):
            isAllowed = True;

    return operators, operands

def PtintFunction(operators, operands):
    n1, N1, n2, N2 = 0, 0, 0, 0

    print("ОПЕРАТОРЫ:\n");
    for key in operators:
        if(operators[key] > 0):
            if(key not in ")}]"):
                n1, N1 = n1 + 1, N1 + operators[key];
                print("{} = {}".format(key, operators[key]));

    print("\nОПЕРАНДЫ\n");
    for key in operands.keys():
        if(operands[key] > 0):
            n2, N2 = n2 + 1, N2 + operands[key];
            print("{} = {}".format(key, operands[key]));

    return n1, N1, n2, N2;

def CountMetrics(n1, N1, n2, N2):
    val = {"N": N1 + N2, "n": n1 + n2, "V": (N1 + N2) * log2(n1 + n2), "D": n1 * N2 / 2 / n2}
    val['E'] = val['D'] * val['V']
    val['L'] = val['V'] / val['D'] / val['D']
    val['I'] = val['V'] / val['D']
    val['T'] = val['E'] / (18)
    val['N^'] = n1 * log2(n1) + n2 * log2(n2)
    val['L^'] = 2 * n2 / N2 / n1

    unit = {'V': 'Количество бит', 'T': 'Секунды'}
    name = {'N':'Длина программы', 'n':'Словарь программы', 'V':'Объем программы', 'D':'Сложность программы', 'E': 'Нагруженность программы', 'L':'Уровень языка', 'I':'Вычислительная мощность', 'T':'Время выполнения программы   ','N^':'Планируемая длина программф', 'L^':'Планируемый уровень языка'}

    print("\nВывод значений: ")
    for key in val.keys():
        print("{} ({}) = {} {}".format(key,name[key], val[key], unit[key] if key in unit else ''))

    return True;
# Функция получения уникального числа операндов;
def CheckUniqueProgramOperands():
    pass;

# Функция получения количества всех операторов;
def TotalCountOperators():
    pass;

# Функция получения количества всех операндов;
def TotalCountOperands():
    pass;

# Функция получения словаря программы;
def ProgramDictionary():
    pass;

# Функция получения длины программы;
def ProgramLenth():
    pass;

# Функция получения объема программы;
def ProgramVolume():
    pass;