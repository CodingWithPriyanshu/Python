import json
FILE = "user.json"

# getting user db
try:
    with open(FILE, 'r') as file:
        user = json.load(file)
except:
    user = []

profile = None

# Account function
def Account(opinion):
    global profile
    if opinion=="create account":
        username = input('Enter username: ')
        password = input("Enter password: ")
        data = {
            "username":username,
            "password":password,
            "todos":[]
        }
        user.append(data)
        save_data()
        profile = data
    elif opinion=="remove account":
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        for account in user:
            if account['username']==username and account['password']==password:
                index_number = user.index(account)
                del user[index_number]
                print('account deleting succesfull.')
                save_data()
                exit()
                break
        else:
            print('account was not found.')
            exit()
        

    elif opinion=="signin account":
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        for account in user:
            if account['username']==username and account['password']==password:
                profile = account
                break
        else:
            print("account was not found.")
            exit()
    else:
        print('Please enter any option sir')

# add task function
def addTask():
    task = input('Enter one task to add: ')
    profile.get('todos').append([task, 'not complete'])
    save_data()

# remove task function 
def removeTask():
    task = int(input('Enter the task number which you have want to delete: '))-1
    del profile.get('todos')[task]
    save_data()
def viewTask():
    task = profile.get('todos')
    for todos in task:
        print(f'{task.index(todos)+1} --> {todos}')

# mark task function
def markTask():
    task_number = int(input('Enter todo number to mark complete or not: '))
    tasks = profile.get('todos')
    if tasks[task_number-1][1] == "not complete":
        tasks[task_number-1][1] = "complete"
        save_data()
    else:
        tasks[task_number-1][1] = "not complete"
        save_data()

def save_data():
    with open(FILE, 'w') as file:
        json.dump(user, file, indent=4)


if __name__ == "__main__":
    opinion = input('What do you want to create account, remove account or sigin account: ')
    Account(opinion)
    print('OPTIONS:-')
    print('1. Add Task')
    print('2. Remove Task')
    print('3. View Task')
    print('4. Mark Task(complete or not)')
    print('5. Exit')
    while True:
        try:
            command = int(input('Enter the option number: '))
            if command==1:
                addTask()
            elif command==2:
                removeTask()
            elif command==3:
                viewTask()
            elif command==4:
                markTask()
            elif command==5:
                break
            else:
                print('please enter any number in option number')
                continue
        except:
            print('Pease Enter only number')
            continue