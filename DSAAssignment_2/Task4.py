class Node:
   def __init__(self, data):
       self.data = data
       self.next = None


class SinglyLinkedList:
   def __init__(self):
       self.head = None
       # keeps track of the do operations
       self.do_list_operation = []
       # keeps track of the undo values
       self.do_list_values = []
       self.redo_list_operation = []
       self.redo_list_values = []
       # keeps track of the undo operations
       self.listundo = []
       self.valuesundo = []
       # counter of number of undo's done
       self.counter = 0
       # checks if the insert is normal insert
       self.insertcounter = 1


   def printlist(self):
       val = self.head
       while val is not None:
           print(val.data)
           val = val.next

   def insert(self, data):
       addval = Node(data)
       val = self.head
       if self.insertcounter == 1:
           self.redo_list_operation.clear()
           self.redo_list_values.clear()

       while val.next is not None:
           if val.next.data >= addval.data:
               temp = val.next
               addval.next = temp
               val.next = addval
               if self.counter == 0:
                   self.do_list_operation.append("insert")
                   self.do_list_values.append(data)
               # else:
               #     self.redo_list_operation.append("delete")
               #     self.redo_list_values.append(data)
               #     self.counter+=1
               return
           val = val.next
           # if val.next.next = None
       val.next = addval
       if self.counter == 0:
           self.do_list_operation.append("insert")
           self.do_list_values.append(data)
       # else:
       #     self.redo_list_operation.append("delete")
       #     self.redo_list_values.append(data)
   def delete(self, data):
       delval = data
       beginval = self.head
       if beginval is not None:
           if beginval.data == delval:
               self.head = beginval.next
               beginval = None
               if self.counter == 0:
                   self.do_list_operation.append("delete")
                   self.do_list_values.append(data)
               return
       while beginval is not None:
           if beginval.data == delval:
               break
           prev = beginval
           beginval = beginval.next

       if (beginval == None):
           if self.counter == 0:
               self.do_list_operation.append("delete")
               self.do_list_values.append(data)
           return

       prev.next = beginval.next
       beginval = None
       if self.counter == 0:
           self.do_list_operation.append("delete")
           self.do_list_values.append(data)

   def undoFunc(self):

       # last operation stored in the variable
       lastop = self.do_list_operation.pop(-1)
       lastval = self.do_list_values.pop(-1)
       # self.redo_list_operation.append(lastop)
       # self.redo_list_values.append(lastval)
       self.counter += 1
       if lastop == "delete":
           self.insertcounter = 0
           self.insert(lastval)
           self.listundo.append("insert")
           self.valuesundo.append(lastval)
           self.insertcounter = 1
       else:
           self.delete(lastval)
           self.listundo.append("delete")
           self.valuesundo.append(lastval)

       return

   def redoFunc(self):
       lastop = self.listundo.pop(-1)
       lastval = self.valuesundo.pop(-1)
       if self.counter == 0 or len(self.redo_list_values) == 0:
           print("Need To First Undo an operation before redo")
           return

       else:
           if lastop == "delete":
               self.insert(lastval)
           else:
               self.delete(lastval)
       self.counter-=1
       return
list1 = SinglyLinkedList()
list1.head = Node(1)
n2 = 7
list1.insert(n2)
list1.insert(19)
list1.insert(10)

# list1.insert(10)
# list1.insert(19)
# list1.printlist()
list1.insert(6)
list1.printlist()
print(list1.do_list_operation)
# print(list1.undo_list_operation)
list1.undoFunc()
list1.printlist()

# list1.insert(45)
list1.printlist()
list1.undoFunc()
list1.printlist()
list1.undoFunc()
list1.printlist()
list1.redoFunc()
# # list1.insert(45)
# list1.delete(7)
# list1.printlist()
# print(list1.redo_list_values)
# list1.redoFunc()
# list1.printlist()
# list1.undoFunc()
# list1.printlist()
print(list1.listundo)
print(list1.valuesundo)
# list1.redoFunc()
# list1.printlist()
