from . import settings
import pandas as pd
import os

def read_class(class_name):
    # print(settings.classes_path + '/' + class_name + '.csv')
    data = pd.read_csv(settings.classes_path + '/' + class_name + '.csv',encoding=settings.encoding,on_bad_lines='skip')
    data_list=[]
    for index, row in data.iterrows():
        data_dict={}
        for column in data.columns:
            data_dict[column]=row[column]
        data_list.append(data_dict)
    # print(data_list)
    return data_list

def mark(student_list):
    files = os.listdir(settings.labs_path)
    for student in student_list:
        student['diem']=10
    for file in files:
        data = pd.read_excel(settings.labs_path + '/' + file)
        id_set = set()
        for index, row in data.iterrows():
            try:
                id_set.add(row[data.columns[1]].upper().replace('.','').replace(' ',''))
            except:
                pass
        print(id_set)
        for student in student_list:
            if student['MSV'].upper().replace('.','').replace(' ','') not in id_set:
                student['diem']-=1
    return student_list
        

def write_class(class_name,data_list):
    data = pd.DataFrame(data_list)
    data.to_csv(settings.output_path + '/' + class_name + '.csv',index=False,encoding=settings.encoding)

def __main__():
    print("Nhap nhom lop:")
    class_name = input()
    class_member=read_class(class_name)
    write_class(class_name,mark(class_member))
    

__main__()