class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other.data:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    
    def issubset(self, other):
        a = self.intersection(other)
        if (self.data == a.data):
            return print(self.data, 'is subset of',other.data,'and', self.data, 'is included',other.data)
        else: 
            return print(self.data, 'is not subset of',other.data,'and', self.data, 'is not included',other.data)
    
    def issuperset(self, other):
        a = self.intersection(other)
        if (self.data == a.data):
            return print(other.data, 'is superset of',self.data, 'and', other.data,'is not included', self.data)
        else: 
            for i in other.data:
                if i not in self.data:
                    self.data.append(i)
            return print(other.data, 'is not superset of',self.data, 'and', sorted(other.data),'is included', self.data)
        
    def __le__(self, other):
        count=0
        for x in self.data:
            if x in other.data:
                count +=1
        if count == len(self.data):
            return True
        else: return False
        
    def __lt__(self, other):
        count=0
        for x in self.data:
            if x in other.data:
                count +=1
        if count == len(self.data):
            return True
        else: return False
    
    def __ge__(self, other):
        count=0
        for x in other.data:
            if x in self.data:
                count +=1
        if count == len(other.data):
            return True
        else: return False
    
    def __gt__(self,other):
        count=0
        for x in other.data:
            if x in self.data:
                count +=1
        if count == len(other.data):
            return True
        else: return False
    
    def intersection_update(self, other) :
        a = []
        for i in self.data:
            if i in other:
                a.append(i)
        self = Set(a)
        return self
    
    def difference_update(self, other):
        a = []
        for i in self.data:
            if i not in other:
                a.append(i)
        self = Set(a)
        return self
    
    def symmetric_difference_update(self, other):
        a = self.data + other.data
        b = self.intersection_update(other)
        c = []
        for x in a:
            if x not in b:
                c.append(x)
        c= Set(c)
        self = c
        return self
    
    def add(self, other):
        a = []
        for x in other.data:
            if not x in self.data:
                a.append(x)
        b = Set(self.data + a)
        self = b
        return self
    
    def remove(self, other):
        for x in self.data:
            if x in other:
                self.data.remove(x)
        return self

    
x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x.concat(y))
print(x & y, x | y)
print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))   # convert to list because x is iterable

x = Set([1,2,3,5,6])
y = Set([1,6])
x.issubset(y)
print(x<=y)
print(x<y)

x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
x.issuperset(y)
print(x,y)
print(x>=y)
print(x>y)


# In[351]:


x = Set([1,7,2,4,3])
y = Set([1,3,5,7])
print('intersection_update:',x.intersection_update(y))

x = Set([1,7,2,4,3])
y = Set([1,3,5,7])
print('difference_update:',x.difference_update(y))

x = Set([1,7,2,4,3])
y = Set([1,3,5,7])
print('symmetric_difference_update:',x.symmetric_difference_update(y))

x = Set([1,7,2,4,3])
y = Set([1,3,5,7])
print('add:',x.add(y))

x = Set([1,7,2,4,3])
y = Set([1,3,5,7])
print('remove:',x.remove(y))


# In[ ]:




