class numlist(object):
    def __init__(self):
        self.counter=0
    
    def __iter__(self):
        return self

    def __next__(self):
        self.counter +=1;
        if self.counter >3:
            raise StopIteration()
        return self.counter-1

obj= numlist()
v1=next(obj)
print(v1)
v2=next(obj)
print(v2)
v3=next(obj)
print(v3)

obj2=numlist()
for item in obj2:
    print(item)
