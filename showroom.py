class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def sorted(self, data):

        new_node = Node(nextNode=None, prevNode=None, data=data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        if data.price < self.head.data.price:
            new_node.nextNode = self.head
            self.head.prevNode = new_node
            self.head = new_node
            return

        current = self.head
        while current.nextNode and current.nextNode.data.price <= data.price:
            current = current.nextNode
        new_node.nextNode = current.nextNode
        new_node.prevNode = current

        if current.nextNode:
            current.nextNode = new_node

        else:
            self.tail = new_node
        
        current.nextNode = new_node

    def find(self, identification):
       current = self.head
       while current:
           if current.data.identification == identification:
               return current
           current = current.nextNode
        

class Car:
    def __init__(self, identification:int, name:str, brand:str, price:int, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    
    for car in cars:
        db.sorted(car)


def add(car):
    
    db.sorted(car)

def updateName(identification, name):
    node = db.find(identification)
    if node:
        node.data.name = name


def updateBrand(identification, brand):
    node = db.find(identification)
    if node:
        node.data.brand = brand


def activateCar(identification):
    node = db.find(identification)
    if node:
        node.data.active = True


def deactivateCar(identification):
    node = db.find(identification)
    if node:
        node.data.active = False


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    price = 0
    current = db.head
    while current:
        if current.data.active == True:
            price += current.data.price
        current = current.nextNode
    return price

def clean():
    db.head = None
    db.tail = None
    return db



