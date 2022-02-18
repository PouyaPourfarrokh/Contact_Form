import pandas as pd 

class contact:
    def __init__(self,name,number,gender,age):
        self.name=name
        self.number=number
        self.gender=gender
        self.age=age

def update_file(contacts):
    with open('Contacts.txt',mode="w") as file:
        
        for c in contacts:
            name = str(c.name)
            number = str(c.number)
            gender = str(c.gender)
            age = str(c.age)
            line = name + ',' + number + ',' + gender + ',' + age + '\n'
            file.write(line)

def read_file():
    contacts=[]
    with open('Contacts.txt', mode = 'r') as file:
        data = file.read()
        if len(data) != 0:
            data = data.split('\n')
            data2 = data[:len(data)-1]
            for i in range(len(data2)):
                c_info = data2[i].split(',')
                cc = contact(c_info[0],int(c_info[1]),c_info[2],int(c_info[3]))
                contacts.append(cc)
            return contacts
        else:
            return contacts
        
def search(search_phrase):
     for i in range(len(contacts)):
         if contacts[i].name == search_phrase or contacts[i].number == search_phrase:
             return i
         
def sort(contacts):
    
    n = len(contacts)
    for i in range(n):
        for j in range(0,n-i-1):
                  if contacts[j].name > contacts[j+1].name:
                          contacts[j],contacts[j+1] = contacts[j+1],contacts[j]
    
    return contacts




    

contacts = []
while True :
    
    contacts = read_file()
    print("choose an option")
    print("1) Show Contacts")
    print("2) Insert Contact")
    print("3) Delete Contact")
    print("4) Edit Contact")
    print("5) Search")
    print("6) create csv")
    print("0) Exit ")

    option= int(input())

    if option==1:
        sort(contacts)
        for e in contacts :
            print(e.name,e.number,e.gender,e.age)
        update_file(contacts)

    elif option==2:
        print("Inserting Contact")
        print("Contact has 4 arguments: name,number,gender,age")
        name=input("Input name:")
        number=int(input("Input Number:"))
        gender=input("Input Gender:")
        age=int(input("Input Age:"))
        c = contact(name , number , gender , age)
        contacts.append(c)
        update_file(contacts)
        
    elif option == 3:
        search_phrase = input('Input name or number:')
        index = search(search_phrase)
        print('contact:',contacts[index].name,contacts[index].number,contacts[index].gender,contacts[index].age)
        print('Are you sure? y/n: ')
        answer = input('Input y/n:')
        if answer=='y':
            contacts.pop(index)
            update_file(contacts)

    elif option == 4:
        search_phrase = input('Input name or number:')
        index = search(search_phrase)
        print('contact: ', contacts[index].name,contacts[index].number,contacts[index].gender,contacts[index].age)
        print('Input your changes')
        name = input('name:')
        number = input('number:')
        gender = input('gender:')
        age = input('age:')
        if contacts[index].name !=name or contacts[index].number!= number or contacts[index].gender != gender or contacts[index].age != age:
                  contacts[index].name = name.replace(contacts[index].name,name)
                  contacts[index].number = int(number.replace(str(contacts[index].number),number))
                  contacts[index].gender = gender.replace(contacts[index].gender,gender)
                  contacts[index].age = int(age.replace(str(contacts[index].age),age))
           
                  
        update_file(contacts)

    elif option == 5:
        search_phrase = input('Input name or number:')
        index = search(search_phrase)
        print('contact: ', contacts[index].name,contacts[index].number,contacts[index].gender,contacts[index].age)
    
    elif option == 6:
        name = []
        number = []
        gender = []
        age = []
        for e in contacts:
                name.append(e.name)
                number.append(e.number)
                gender.append(e.gender)
                age.append(e.age)
                #print(name,number,gender,age)
        df = pd.DataFrame()
        df['name'] = name
        df['number'] = number
        df['gender'] = gender
        df['age'] = age
        df.to_csv('data.csv')       
        print(df)

    elif option == 0 :
        
        break
    
    else:
        print("Invalid Number of Option")


