#python program for count number of words in a file, where "sample.txt" is the text file  

number_of_words = 0
d=open('sample.txt', 'r') # change the file sample.txt into your file name 
data=d.read()
lines = data.split()
for word in lines:
    if not word.isnumeric():
        number_of_words += 1
print("Number of Words:",number_of_words)
