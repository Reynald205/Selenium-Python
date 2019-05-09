fw = open('sample.txt','w')# Opens or creates a new file with (Filename, w(riting)).
fw.write("Writing some stuff in my text file\n")#Allows you to add text to the file
fw.write("I like bacon\n")
fw.close()
fr = open('sample.txt','r')#Opens file and tells the program to r(ead) it.
text = fr.read()
print(text)
fr.close()