#*operator
#*args


def sum(*args):
    total=0
    for i in args:
        total+=i
    return total
print(sum(1,2,3,4,5,6,7,8,9))


#use of *args(this operation is done by only * , we can use any name instead of agrs)(this operation returns a tuple)
def all_total(*args):
    print(args)
    print(type(args))

all_total(1,2,3,4,5)
