# While

cargo = [40,32,4,5,8,9,6,30,41,32,9]
boxCapacity = 90
box = []
i = 0

cargo.sort()
cargo.reverse()
print('Cargo is: ', cargo)

while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1


print('The collected items sum is: ',sum(box))
print('The elements are: ', box)
