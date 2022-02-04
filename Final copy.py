import xlrd

path = "/Users/amritkumarjha/Desktop/Sample Names and IDs.xls"
book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)

N=sheet.nrows               #No of student entries
list_of_dictionaries=[]
branchcode={"A3":"EEE","A7":"CSE","A8":"ENI","B1":"MSc Bio","B3":"MSc Eco"}

for I in range(1,N):
    ID=sheet.cell_value(I,1)
    jyear=ID[0:4]           #Joining Year
    bcode=ID[4:6]           #Branch Code
    dbranch=ID[6:8]         #Dual Branch Code
    ucode=ID[8:12]          #Unique Code
    
    emailid='f'+ jyear + ucode +'@pilani.bits-pilani.ac.in'
    branch=branchcode[bcode]
    if dbranch=="PS":
        fbranch=branch
    else:
        dualbranch=branchcode[dbranch]
        fbranch=f'{branch} + {dualbranch}'

    Dict={'Name':sheet.cell_value(I,0),'BITS ID':ID,'BITS email address':emailid,'Student branch':fbranch}          
    list_of_dictionaries.append(Dict)

print(list_of_dictionaries)  
    
    

