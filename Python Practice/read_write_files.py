# f=open("e://data//funny.txt","a")
# f.write("hello c++ \n I love python as well")
# f.close()
# f=open("e://data//funny.txt","r")
# f.close()
# f=open("e://data//funny.txt","r")
# print(f.read())
# f.close()

# f = open("e://data//funny.txt", "r")
# f_out=open("e://data//funny_wc.txt","w")
# for line in f:
#     tokens = line.split(' ')
#     f_out.write(line+"word count is "+ str(len(tokens))+"\n")
#     print(len(tokens))
# f.close()
# f_out.close()


with open("e://data//funny_wc.txt","r") as f:
    print(f.read())
    print(f.closed)