# a = ["hey", "bro", "good morning"]
# itr = iter(a)
# print(next(itr))
# print(dir(itr))
# it = reversed(a)
# print(next(it))

class RemoteControl :
    def __init__(self):
        self.channels = ["Zee", "Star", "Sun", "Moon"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1;
        if(self.index == len(self.channels)):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControl()
itr = iter(r);
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))