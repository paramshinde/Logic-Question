#Find the second largest number in a list.
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list

    def sort_list(self):
        for i in self.num_list:
            for j in self.num_list:
                if i>j:
                    self.num_list[i],self.num_list[j]=self.num_list[j],self.num_list[i]
        return self.num_list
num=[1,2,4,1,5,7,6]
obj=Lists(num)
print(obj.sort_list())