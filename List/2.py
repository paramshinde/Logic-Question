#Reverse a list without using .reverse() or slicing.
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list

    
    def new_list_reverse(self):
        new_list=[]
        for i in range(len(self.num_list)):
            new_list.append(self.num_list[-(i+1)])
        return new_list
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
#print(obj.new_list_reverse())
print(obj.reverse_list())