my_file = open("testfile.txt", 'w')

my_file.write("Hello World\n")
my_file.write("How are you?\n")
my_file.write("Hope you are fine\n")

my_file.close()


my_file2 = open("testfile.txt", 'r')
print(my_file2.readlines(2))
print(my_file2.readlines())
my_file2.close()