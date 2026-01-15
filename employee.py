
class Employee:
    def __init__(self,id, name, surename, performance):
        self.id = id
        self.name = name
        self.surename = surename
        self.performance = performance

e1 = Employee(12, 'Natasha', 'Romanov' , 233)
e2 = Employee(32, 'Thor', 'Odinson', 430)
e3 = Employee(1,'Steve', 'Rogers', 123)
e4 = Employee(20, 'Anthony', 'Stark', 444)
employees = [e1, e2, e3, e4]

def findBestEmployee(array):
    if array == []:
        return -1
    max = 0
    selected = None
    for i in range(len(array)):
        if array[i].performance > max:
            max = array[i].performance
            selected = array[i]
    return selected.id

def getEmployee(array, id):
    for employee in array:
        if employee.id == id:
            return f"{employee.name} {employee.surename} ({employee.performance})"
    return None
    
def removeEmployee(employees, id):
    array = employees[:]
    for i in range(len(array)):
        if employees[i].id ==  id:
            array.remove(employees[i])
    list = []
    for employee in array:
        list.append(employee)
    return list

def sortEmployees(array):
    if array == []:
        return []
    best = findBestEmployee(array)
    new_array = [getEmployee(array, best)]
    array = removeEmployee(array, best)

    new_array += sortEmployees(array)
    return new_array


def assemble(array, work):
    performance_of_group = 0
    for employee in array:
        performance_of_group += employee.performance
    if performance_of_group < work:
        return True
    return False


def saveThem(array, number):
    new_array = []
    for employee in array:
        if employee.performance > number:
            new_array.append( getEmployee(array, employee.id))
    return new_array
    
    

def deployThem(array1, array2, value):
    array1len = len(array1)
    hard = value / array1len 
    sum_of_new = 0
    new_array1 = []
    ultimate_array = []
    for employee in array1[:]:
        if employee.performance < hard:
            array1[:].remove(employee)
        if employee.performance > hard:
            sum_of_new += employee.performance
            new_array1 += [getEmployee(array1, employee.id)]
    if sum_of_new >= value:
        return new_array1
    else:
        for employee in array2:
            sum_of_new += employee.performance
            if sum_of_new > value:
                new_array1 += [getEmployee(array2, employee.id)]
                return new_array1
    if sum_of_new < value:
        for employee in array1:
            ultimate_array += [getEmployee(array1, employee.id)]
    for employee in array2:
        ultimate_array += [getEmployee(array2, employee.id)]
    return ultimate_array    


            



print(deployThem([e1,e2], [e3,e4],470))




