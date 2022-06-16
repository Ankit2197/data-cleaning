# f=open("kanu.txt","a")
# c=f.write("yogi se dur rho")
# f.close()
# f=open("kanu.txt")
# print(f.read())
# def rr2():
#     x=23
#     def rohsha():
#         x=98
#     print(x)
#     rohsha()
#     print(x)
# rr2()
# from array import *
# arr=array('i',[2,3,4,5,6])
# new_arr=array('i',[a*a for a in arr])
# print(new_arr)
# def div(a,b):
#     print(a/b)
# def smart_div(func):
#     def inner(a,b):
#         if a<b :
#             a,b=b,a
#         return func(a,b)
#     return inner
# div=smart_div(div)
# div(2,4)
# class Car:
#     wheels = 4
#     def __init__(self):
#         self.mil=10
#         self.com="BMW"
# c1=Car()
# c1.mil=8
# Car.wheels=6
# print(c1.com,c1.wheels,c1.mil)
# class Pharm():
#     def execute(self):
#         print("c")
#         print("k")
# class Myeditor:
#     def execute(self):
#         print("s")
#         print("c")
#         print("r")
# class Laptop:
#     def code(self,ide):
#         ide.execute()
# ide=Pharm()
# ide=Myeditor()
# lap1=Laptop()
# lap1.code(ide)
# def power(base,exp):
#     assert exp>=0 and int(exp)==exp;'the numbers must be positive and base should not be zero'
#     if exp==0:
#         return 1
#     else :
#         return base * power(base,exp-1)
#
# print(power(4,2.5))
# from array import *
# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     else:
#         return arr[0] * productOfArray(arr[1:])
# x=productOfArray(array('i',[2,3,4]))
# print(x)
#     product=1
#     for k in arr:
#         if k==0:
#             return 0
#         else:
#             product=k*product
#     print(product)
# poa(array('i',[3,6,4]))
# def reverse(string):
#     if len(string)<=1:
#         return string
#     else :
#         return string[len(string)-1]+reverse(string[0:len(string)-1])
# x=reverse("ankit")
# print(x)
#
# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
#
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#
#     return v
#
#
# print(fun(data[0]))

#

# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#
# # print(sum)
# n= int(input("no. of days temperature recorded"))
# list1=[]
# c=0
# for i in range(n):
#     value=int(input("enter the tempertaure"))
#     list1.append(value)
# avg=sum(arr1)/len(arr1)
# print("the input temperatures are: ",arr1)
# print("avg of the temp is: ",avg)
# for i in arr1:
#     if arr1[i]>avg:
#         c+=1
# print("n0. of days temp was above avg temp: ",c)
#
# n=int(input("no. of enteries reqd.:\t"))
# list1=[]
# for k in range(n):
#     y=int(input("enter the numbers:\t"))
#     list1.append(y)
# print(list1)
# x=int(input("enter the target value:\t"))
# for i in list1:
#     for j in list1:
#         if i + j ==x and i!=j:
#             print([i,j])
#         else:
#             continue
# from array import *
# max_prd=0
# arr1=array('i',[3,7,4,6,8,2])
# for i in range(len(arr1)):
#     for j in range(i+1,len(arr1)):
#         if arr1[i]*arr1[j]>arr1[i]*arr1[j-1]:
#             max_prd = arr1[i]*arr1[j]
#             pair=[arr1[i],arr1[j]]
#         else:
#             continue
# print(pair)
# print(max_prd)
# mylist=[2,3,4,54,52,34,56,78,43,6,5]
# def tkae(list):
#     new_lst=[]
#     for i in mylist:
#         if i in new_lst:
#             print(i)
#             return False
#         else:
#             new_lst.append(i)
#     return True
# print(tkae(mylist))
#
# def rotate_matrix(matrix):
#     '''rotates a matrix 90 degrees clockwise'''
#     n = len(matrix)
#     for layer in range(n // 2):
#         first, last = layer, n - layer - 1
#         for i in range(first, last):
#             # save top
#             top = matrix[layer][i]
#
#             # left -> top
#             matrix[layer][i] = matrix[-i - 1][layer]
#
#             # bottom -> left
#             matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
#
#             # right -> bottom
#             matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]
#
#             # top -> right
#             matrix[i][- layer - 1] = top
#     return matrix
#
# matrix = [[1,2,3], [3,4,5],[6,7,8]]
# print(matrix)
# print(rotate_matrix(matrix))

# def sumDiagonal(a):
#     sum=0
#     for i in range(len(myList2D)):
#         for j in range(len(myList2D)):
#             if i==j:
#                 sum= sum + myList2D[i][j]
#             else:
#                 continue
#     return sum
# myList2D=[[1,2,3],[4,5,6],[7,8,9]]
# print(sumDiagonal(myList2D))
# def firstSecond(a):
#     a.sort()
#     a.reverse()
#     for i in range(len(a)):
#         for j in range(1,len(a)):
#              if a[j]!=a[i]:
#                 return a[0],a[j]
#              else :
#                 continue
# myList=[84,85,86,87,85,87,85,83,23,45,84,1,2,0]
# # print(firstSecond(myList))
# def missingNumber(myList, totalCount):
#     n = totalCount
#     total = (n * (n + 1)) / 2
#     x = sum(myList)
#     mis_num = x - total
#     return mis_num
# print(missingNumber([1, 2, 3, 4, 6], 6))
# def removeDuplicates(myList):
#     new_lst=[]
#     for i in myList:
#         if i not in new_lst :
#             new_lst.append(i)
#     return new_lst
# myList=[1,1,2,2,3,4,5]
# print(removeDuplicates(myList))
# def pairSum(myList, sum):
#     new_lst=[]
#     for i  in range(len(myList)):
#         for j in range(i+1,len(myList)):
#             if myList[i]+myList[j]==sum:
#                 new_lst.append(str(myList[i])+'+'+str(myList[j]))
#             else:
#                 continue
#     return new_lst
# myList=[2,4,3,5,6,-2,4,7,8,9]
# sum=7
# print(pairSum(myList, sum))
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
#
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
#
# print(sum)
# init_tuple = ()
# print (init_tuple.__len__())
# init_tuple = [(0, 1), (1, 2), (2, 3)]
# result = sum(n*n for _, n in init_tuple)
# print(result)
# init_tuple_a = 1, 2
# init_tuple_b = (3, 4)
# for x in [init_tuple_a + init_tuple_b]:
#     print(sum(x))
# init_tuple = [(0, 1), (1, 2), (2, 3)]
# for _, n in init_tuple:
# #   print(_,n)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = 1
#
# class SLinkedList:
#     def __init__(self):
#         self.head = 3
#         self.tail = 4
# ap=SLinkedList()
# node1=Node(1)
# node2=Node(2)
# ap.head=node1
# ap.head.next=node2
# ap.tail=node2
# print([ap.head,node2.value,ap.tail])
#
# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None
# class LL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def __iter__(self):
#         node=self.head
#         while node:
#             yield node
#             if node.next==self.head:
#                 break
#             node=node.next
#     def crCSLL(self,nodevalue):
#         node=Node(nodevalue)
#         node.next=node
#         self.head=node
#         self.tail=node
#     def incsll(self,value,location):
#         if self.head is None:
#             return "the head reference is none"
#         else:
#             newnode=Node(value)
#             if location==0:
#                 newnode.next=self.head
#                 self.head=newnode
#                 self.tail.next=newnode
#             elif location==1:
#                 newnode.next = self.tail.next
#                 self.tail.next = newnode
#                 self.tail=newnode
#             else:
#                 tempnode=self.head
#                 index=0
#                 while index < location-1:
#                     tempnode=tempnode.next
#                     index+=1
#                 nextnode=tempnode.next
#                 tempnode.next=newnode
#                 newnode.next=nextnode
#         return "the linked list is successfully inserted"
#
#     def delcsll(self,location):
#         if self.head is None:
#             print("nodes are not available")
#         elif location==0:
#             if self.head==self.tail:
#                 self.head=None
#                 self.tail=None
#                 self.head.next=None
#             else:
#                 self.head=self.head.next
#                 self.tail.next=self.head
#         elif location==1:
#             if self.head==self.tail:
#                 self.head=None
#                 self.tail=None
#                 node.next=None
#             else:
#                 node=self.head
#                 while node is not None:
#                     if node.next==self.tail:
#                         break
#                     node = node.next
#                 node.next=self.head
#                 self.tail=node
# #         else:
# #             tempnode=self.head
#             index=0
#             while index<location-1:
#                 tempnode=tempnode.next
#                 index+=1
#             nextnode=tempnode.next
#             tempnode.next=nextnode.next
#
# createlist1=LL()
# createlist1.crCSLL(1)
# createlist1.incsll(0,0)
# createlist1.incsll(4,0)
# createlist1.incsll(2,2)
# createlist1.incsll(3,1)
#
# print([node.value for node in createlist1])
#
# createlist1.delcsll(4)
# print([node.value for node in createlist1])
# class Queue:
#     def __init__(self):
#         self.list=[]
#     def __str__(self):
#         values=[str(x) for x in self.list]
#         return '\n'.join(values)
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         return False
#     def enqueue(self,values):
#         self.list.append(values)
#         return "elements inserted"
#     def dequeue(self):
#         if self.isEmpty():
#             return "empty"
#         else:
#             return self.list.pop()
#     def peek(self):
#         if self.isEmpty():
#             return "empty"
#         else:
#             return self.list[0]
#     def delete(self):
#         self.list=None
# letsgo=Queue()
# print(letsgo.isEmpty())
# letsgo.enqueue(5)
# letsgo.enqueue(55)
# letsgo.enqueue(75)
# letsgo.enqueue(53)
# letsgo.enqueue(9)
# print(letsgo)
# print(letsgo.isEmpty())

# linked list queue
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class Linlis:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node=node.next
class Queue:
    def __init__(self):
        self.linlist=Linlis()

    def __str__(self):
        values=[str(x.value) for x in self.linlist]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linlist.head==None:
            return True
        return False
    def enqueue(self,val):
        node=Node(val)
        if self.linlist.head is None:
            self.linlist.head=node
            self.linlist.tail=node
        else:
            self.linlist.tail.next=node
            self.linlist.tail=node
        return "nodes inserted"
    def dequeue(self):
        if self.isEmpty():
            return "empty"
        elif self.linlist.head==self.linlist.tail:
            self.linlist.head=None
        else:
            tempnode=self.linlist.head
            self.linlist.head=self.linlist.head.next
            return tempnode
blaha=Queue()
blaha.enqueue(9)
blaha.enqueue(45)
blaha.enqueue(53)
blaha.enqueue(58)
blaha.enqueue(5)
print(blaha)
blaha.dequeue()
print(blaha)












