from tkinter import *

def cryptageCesar(x,k):#x c'est le nombre a crypter et k c'est la clé
	return (x+k)

def decryptageCesar(x,k):#----------------################-----------
	return (x-k)

def cryptage(sentence,key):#Crypter un mot/une phrase/une texte
	sentence = my_entry.get()
	sentencesCrypted = []
	asci = []
	for letter in sentence:	
		asci.append(ord(letter))
	for x in asci:
		if x == 32:
			value = 32
		else:
			asciBeta = x-65
			asciCrypted = cryptageCesar(asciBeta,key)
			value = asciCrypted+65	
		sentencesCrypted.append(chr(value))
	sentencesCrypted = "".join(sentencesCrypted)
	return sentencesCrypted


def attackDeCesar(sentence):#Je crée ici un équivalent d'une BRUTE FORCE
	for k in range(26):
		print("Clé numero {} :".format(k))
		cryptage(sentence,-k)

def decryptage(sentence,k):#C'est l'inverse de la fonction cryptage!
	sentence1 = my_entry1.get()
	sentenceDecrypted = []
	asci = []
	for letter in sentence1:
		asci.append(ord(letter))
	for y in asci:
		if y == 32:
			value = 32
		else:
			numberCrypted = y-65
			numberDecrypted = decryptageCesar(numberCrypted,k)
			value = numberDecrypted+65
		sentenceDecrypted.append(chr(value))
	sentenceDecrypted = "".join(sentenceDecrypted)
	return sentenceDecrypted

def btn():
	Ckey = int(keyEntry.get())
	my_sortie.delete(0,END)
	my_sortie.insert(0,cryptage(sentence,Ckey))

def btn1():
	Dkey = int(keyEntry1.get())
	my_sortie1.delete(0,END)
	my_sortie1.insert(0,decryptage(sentence1,Dkey))

def renitialize():
	my_sortie.delete(0,END)
	my_entry.delete(0,END)
	keyEntry.delete(0,END)

def renitialize1():
	my_sortie1.delete(0,END)
	my_entry1.delete(0,END)
	keyEntry1.delete(0,END)

root = Tk()
root.title("Cryptographie")
root.geometry("720x460")
root.resizable(False,False)
sentence = StringVar()
sentence1= StringVar()
Ckey = StringVar()
Dkey = StringVar()

label1 = Label(root,text="Entree")
label2 = Label(root,text="Sortie")
label3 = Label(root,text="Key")
label4 = Label(root,text="Entree")
label5 = Label(root,text="Sortie")
label6 = Label(root,text="Key")
label7 = Label(root,text="Crée par Odie",pady=130)

my_entry = Entry(root,width=70,textvariable=sentence)
my_entry1= Entry(root,width=70,textvariable=sentence1)
my_sortie = Entry(root,width=70,bg="DimGray",fg="white")
my_sortie1= Entry(root,width=70,bg="grey",fg="white")
keyEntry = Entry(root,width=5,textvariable=Ckey)
keyEntry1 = Entry(root,width=5,textvariable=Dkey)
button = Button(root,text="crypter",width=30,command=btn)
button1 = Button(root,text="Decrypter",width=30,command=btn1)
renitialize = Button(root,text="Réinitialiser",width=30,command=renitialize)
renitialize1 = Button(root,text="Réinitialiser",width=30,command=renitialize1)


my_entry.grid(column=1,row=0,padx=2,pady=20)
my_entry1.grid(column=1,row=5,padx=2,pady=20)
keyEntry.grid(column=3,row=0)
keyEntry1.grid(column=3,row=5)
my_sortie.grid(column=1,row=1)
my_sortie1.grid(column=1,row=6)
renitialize.grid(column=1,row=3)
renitialize1.grid(column=1,row=8)
button.grid(column=1,row=2)
button1.grid(column=1,row=7)

label1.grid(column=0,row=0)
label2.grid(column=0,row=1)
label3.grid(column=2,row=0)
label4.grid(column=0,row=5)
label5.grid(column=0,row=6)
label6.grid(column=2,row=5)
label7.grid(column=1,row=12)

mainloop()