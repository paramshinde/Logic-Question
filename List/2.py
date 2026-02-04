#Reverse a list without using .reverse() or slicing.
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list

    
    def reverse_list(self):
        list_reversed=[]
        for i in range(len(self.num_list)):
            list_reversed.append(self.num_list[-(i+1)])
        return list_reversed


numbers=[5,4,3,2,1]
print(numbers)
obj=Lists(numbers)
print(obj.reverse_list())