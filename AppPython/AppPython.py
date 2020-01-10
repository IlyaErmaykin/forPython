def count_average_value_user(v1, v2, v3):
    result = (v1 + v2 + v3)/3;
    #print(float(result));
    return result;

def count_average_subject_value(v1, count):
    result = str(v1/count);
    #print(float(result));
    return result;


def finalli_result_function(v1, v2, v3, count):
    
    average_list = " ";

    cres1 = count_average_subject_value(v1, count);
    cres2 = count_average_subject_value(v2, count);
    cres3 = count_average_subject_value(v3, count);
    
    average_list = str(cres1) + " " + str(cres2) + " " +  str(cres3);
    print(average_list);
    #return str(average_list);

List = [];
res_1 = 0;
res_2 = 0;
res_3 = 0;

with open("_.txt", encoding='utf-8') as inf:
    for line in inf:
        List.append(line.replace("\n", ""));
#print(List);

for element in range(len(List)):
    #print(List[element]);
    parce_value = List[element].split(";");
    #print(parce_value[1]);
    average_value = count_average_value_user(int(parce_value[1]), int(parce_value[2]), int(parce_value[3]));
    print(average_value);
    res_1 = res_1 + int(parce_value[1]);
    res_2 = res_2 + int(parce_value[2]);
    res_3 = res_3 + int(parce_value[3]);

    if (element == len(List) - 1):
        finalli_result = finalli_result_function(res_1, res_2, res_3, len(List));
        print(finalli_result);
    else:
        continue;
