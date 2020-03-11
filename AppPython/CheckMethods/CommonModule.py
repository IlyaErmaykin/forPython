# Функция чтения файла;
def ReadFile(inf):
    res = "";
    for line in inf:
        res = res + line;
    return res;    

# Функция возвращает количаство строк в файле;
def StringCountModule(inf):
    res = 0;
    for line in inf.split('\n'):
        if line.strip():
            res = res + 1;
    print("Количество строк в выбранном файле: " + str(res));

# Функция подсчета однострочных комментариев;
def CommenStringOnesCountModule(inf):
    res = 0;
    for line in inf:
        if line.startswith('#'):
            res = res + 1;
    print("Количество строк c однострочными комментариями: " + str(res));

# Функция подсчета многострочных комментариев;
def CommenStringOtherCountModule(inf):
    return True;