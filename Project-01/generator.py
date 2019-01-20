def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

gen = reverse('abcd')
print (gen)
print (type(gen))

for char in gen:
    print (char)