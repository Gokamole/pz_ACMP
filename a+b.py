input_data = open('input.txt', 'r')
data = input_data.read ()

data = data.split()
a = int(data[0])
b = int(data[1])
c = str(a + b)

output_data = open ('output.txt', 'w')
output_data.write(c)

input_data.close()
output_data.close()