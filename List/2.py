#Reverse a list without using .reverse() or slicing.
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list

    
    def multi_reverse_list(self):
        list_reversed=[]
        for i in range(len(self.num_list)):
            list_reversed.append(self.num_list[-(i+1)])
        return list_reversed

    def reverse_list(self):
        start=0
        end=len(self.num_list)-1
        while start<end:
            self.num_list[start],self.num_list[end]=self.num_list[end],self.num_list[start]
            start+=1
            end-=1
        return self.num_list
            


numbers=[6,5,4,3,2,1]
print(numbers)
obj=Lists(numbers)
#print(obj.multi_reverse_list())
print(obj.reverse_list())