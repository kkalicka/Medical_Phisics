import matplotlib.pyplot as plt
import numpy as np

#ilosc analizownych indeksów (max 920)
index = 220
index = index + 50
# wartosc progowa dla local max zaznaczonych zielonymi liniami na wykresie
break_value = 1*10**(-10)
# maksymalna wartosc wyswietlana na wykresie (aby poprawic widocznosc pozostalych danych)
max_y_value = 9*10**(-8)
# min_freq i max_freq napisz w MHz
min_freq = 905
max_freq = 915
# numery indeksow, ktore odpowiadaja danej czestotliwosci
min_freq = int((min_freq-700)/2.5)
max_freq = int((max_freq-700)/2.5)
Amplitudes_x = []
Amplitudes_y = []
file_min = 438
file_max = 472
if_print_all_plots = False

def space_delete(sentence):
    temp = ""
    break_point=0
    for i in sentence:
        if break_point==1:
            temp = temp + i
        if i == ";":
            break_point=1

    #pierwsza cyfra
    temp_value_a = int(temp[0])
    #liczba po przecinku
    if temp[4] == 'E':
        temp_value_b = int(temp[2:4])*10
    elif(temp[3] == 'E'):
        temp_value_b = int(temp[2:3])*100
    else:
        temp_value_b = int(temp[2:5])
    #potega 10
    if int(temp[-2:])>6:
        temp_value_c = int(temp[-2:])
    temp_value_c = int(temp[-3:])
    return (float(temp_value_a+temp_value_b*0.001)*10**(-temp_value_c))

def define_file_names(number1, number2):
    file_name_list = []
    for i in range(number1, number2+1):
        if i != 426 and i!=424 and i != 421 and i!=423 and i != 425 and i!=427 and i != 428 and i!=429  and i != 430 and i!=422:
            basic_name = "E-0007_" + str(i) + "_1.csv"
            file_name_list.append(basic_name)
    return file_name_list

def find_amplitude(min_arg, max_arg, data):
    amplitude_value = data[min_arg-1]
    for i in range(min_arg-1, max_arg):
        if data[i]>amplitude_value:
            amplitude_value = data[i]
    return amplitude_value

def calculate_EX(data):
    EX = 0
    for i in data:
        EX = EX + i
    print(len(data))
    return EX/len(data)

def calculate_STD(data, EX):
    STD = 0
    for i in data:
        STD = STD + (EX-i)*(EX-i)
    STD = STD/(len(data)-1)
    STD = np.sqrt(STD   )
    return STD

# podaj numery pomiarow
file_names = define_file_names(file_min, file_max)

for file_name in file_names:
    # tabela z warto�ciami
    data_x = []
    data_y = []
    # tabela z obszarami pik�w
    rois = []

    with open(file_name, "r") as file:
        line_index = 0
        line_value = 0
        for line in file:
            if line_index > index:
                break
            if line_index > 50:
                # 50 linijek zajmuje obszar przed danymi
                line_value = space_delete(line)
                if line_value>max_y_value:
                    data_y.append(max_y_value)
                else:
                    data_y.append(line_value)
                #data_y.append(line_value)
                data_x.append(700+(2.5*(line_index-50)))
            line_index = line_index + 1
    ROI = []
    for i in range(0, index-50):
        if data_y[i] > break_value:
            ROI.append(i)
    local_max=[]
    local_max_value = []
    ROI_value = []            
    Amplitudes_x.append(file_name[7:-6])
    Amplitudes_y.append(find_amplitude(min_freq, max_freq, data_y))
    '''
    print(local_max)   
    print(local_max_value) 
    '''
    if if_print_all_plots == True:
        plt.plot(data_x, data_y)
        plt.title(file_name[7:-6])
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Value [W/cm^2]")
        plt.show()

    # zapis pliku w formie .png
    """"
    plt.savefig(f"{file_name[:-5]}.png")
    plt.show()
    """

print(Amplitudes_y)
print(calculate_EX(Amplitudes_y))
print(calculate_STD(Amplitudes_y, calculate_EX(data_y)))

fig, ax = plt.subplots()
error = 0.55*3.05*10**(-15)
ax.bar(Amplitudes_x, Amplitudes_y, color = 'r')
ax.bar(x=np.arange(len(Amplitudes_x)), #x-coordinates of bars
       height=Amplitudes_y, #height of bars
       capsize=4) #length of error bar caps
plt.title("Amplitudy dla czestotliwosci od "+ str(700+(2.5*(min_freq)))+ "MHz do " + str(700+(2.5*(max_freq))) + "MHz")
plt.xlabel("Numer pomiaru")
plt.ylabel("Value [W/cm^2]")
plt.ylim(0, (max(Amplitudes_y)*2))
#plt.savefig("pomiary_"+f"{(file_names[0])[7:-6]}"+"_"f"{(file_names[-1])[7:-6]}"+"_czest"+"_"+str(int(700+(2.5*(min_freq))))+"_"+str(int(700+(2.5*(max_freq)))))
plt.show()
exp_data_y_dzwonienie = []
exp_data_y_odbieranie = []
exp_data_x = [0,10,20,30,40,50,60,70,80,100,120,140,160,180,200,360,520]
for x in range(439,473):
    if x%2 == 1:
        exp_data_y_dzwonienie.append(Amplitudes_y[x-439])
    else:
        exp_data_y_odbieranie.append(Amplitudes_y[x-439])
print(len(exp_data_x))
print(len(exp_data_y_dzwonienie))
print(len(exp_data_y_odbieranie))
ax.bar(exp_data_x, exp_data_y_dzwonienie, color = 'r')
ax.bar(x=np.arange(len(exp_data_x)), #x-coordinates of bars
       height=exp_data_y_odbieranie, #height of bars
       capsize=4) #length of error bar caps
plt.title("dzwonienie")
plt.xlabel("Frequency [MHz]")
plt.ylabel("Value [W/cm^2]")
plt.show()
ax.bar(exp_data_x, exp_data_y_odbieranie, color = 'r')
ax.bar(x=np.arange(len(exp_data_x)), #x-coordinates of bars
       height=exp_data_y_odbieranie, #height of bars
       capsize=4) #length of error bar caps
plt.title("odbieranie")
plt.xlabel("Frequency [MHz]")
plt.ylabel("Value [W/cm^2]")
plt.show()
print(exp_data_y_odbieranie)
print(exp_data_y_dzwonienie)
# sprawdzenie czy program do konca sie wykonuje
print("test")
