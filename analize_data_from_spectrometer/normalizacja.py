import matplotlib.pyplot as plt
import numpy as np

# test = 0 lub 11!!!
test = 11
min_number = 19
max_number = 31
def define_file_names(min_num, max_numb):
    temp_file_name = []
    for i in range(min_num, max_numb+1):
        if i <10:
            j = "0" + str(i)
        else:
            j = str(i)
        temp_file_name.append("DMB0" + j + ".SP")
    return temp_file_name

def space_delete(sentence):
    temp = ""
    for i in sentence:
        if i != " ":
            temp = temp + i
    return int(temp)

def y_data_define(sentence):
    n = 1
    calkowite_str = ""
    milionowe_str = ""
    if_after_coma = False
    if_minus_in_sentence = False
    for i in sentence:
        if i == "-":
            if_minus_in_sentence = True
        if i == " ":
            break
        if n>test:
            if i == ".":
                if_after_coma = True
                continue
            if if_after_coma == False:
                calkowite_str = calkowite_str + i
            if if_after_coma == True:
                milionowe_str = milionowe_str + i
        n = n+1

    if if_minus_in_sentence == False:
        temp = float(calkowite_str)+int(milionowe_str)*0.000001
    if if_minus_in_sentence == True:
        temp = float(calkowite_str)-int(milionowe_str)*0.000001
    return temp


# podaj nazwy plików widmowych 
file_names = define_file_names(min_number, max_number)

index = 695
data_x = []

for x in range(0,640):
    data_x.append(x*0.5 + 380)

for file_name in file_names:
    # tabela z wartosciami
    data_y = []

    with open(file_name, "r") as file:
        line_index = 0
        max_data = 0
        max_data_index = 0
        line_value = 0
        for line in file:
            if line_index > index:
                break
            if line_index > 55:
                data_y.append(y_data_define(line))
            line_index = line_index + 1

    data_tlo = []
    if int(file_name[4:6]) == 3:
        data_tlo = data_y 

    if int(file_name[4:6]) >4:
        if len(data_tlo)>0:
            for i in range(0, len(data_y)):
                if data_tlo[i]>data_y[i]:
                    data_y[i] = data_y[i] - data_tlo[i]
        max_data_y=0
        max_data_y=max(data_y[100:400])
        print(max_data_y)

        for i in range(0, len(data_y)):
            data_y[i] = data_y[i]/max_data_y
    
        plt.xlim([450, 650])
        plt.ylim([0, 1])
        plt.plot(data_x, data_y)
        plt.title(file_name[7:-6])
        plt.xlabel("długość fali [nm]")
        plt.ylabel("ilosc zliczen")

plt.show()