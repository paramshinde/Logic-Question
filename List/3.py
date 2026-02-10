#Remove duplicate elements from a list without using set()
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list
    
    def remove_duplicate(self):
        unique_list=[]
        for i in self.num_list:
            if i not in unique_list:
                unique_list.append(i)
        return unique_list

numbers=[1,2,3,4,4,5,6,7,8,8,8]
obj=Lists(numbers)
print(obj.remove_duplicate())