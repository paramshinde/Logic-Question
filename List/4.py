#Find the second largest number in a list.
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list

    def smallest(self):
        smallest=self.num_list[0]
        for i in self.num_list:
            if i<smallest:
                smallest=i
        return smallest
    def second_smallest(self):
        smallest=self.num_list[0]
        second_smallest=1
        for i in self.num_list:
            if i<smallest:
                second_smallest=smallest
                smallest=i
            elif i!=smallest and i<second_smallest:
                second_smallest=i
        return second_smallest
    
    def largest(self):
        largest=self.num_list[0]
        for i in self.num_list:
            if i>largest:
                largest=i
        return largest
    
    def second_largest(self):
        largest=self.num_list[0]
        second_largest=0
        for i in self.num_list:
            if i>largest:
                second_largest=largest
                largest=i
            elif i!=largest and i<second_largest:
                second_largest=i
        return second_largest

num=[1,2,4,1,5,7,0,6,-1,10]
obj=Lists(num)
print(obj.smallest())
print(obj.second_smallest())
print(obj.largest())
print(obj.second_largest())