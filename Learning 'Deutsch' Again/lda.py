# WorkPath:C:\Users\Kev1\Projets\Programmation\Python\Learning 'Deutsch' Again
from tkinter import*
from tkinter import ttk
from random import choice, randint
import webbrowser
import winsound
from time import sleep

def _exit_this():
	winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
	app.quit()

def _about_application():
	app_about_application = Toplevel(app)
	app_about_application.title("À propos de l'application")
	app_about_application.geometry("400x200")
	app_about_application.config(bg=background_color)
	app_about_application.resizable(width=0, height=0)
	text_final_release = Label(app_about_application, text="Sortie final: 15 Décembre")
	label_main_text = Label(app_about_application, text="Learning Deutsch Again (LDA); Bêta:1.0", font=("New Times Roman", 13), fg='Black', relief='solid', bg='#686a6d')
	label_secondary_text = Label(app_about_application, text="L'application, est une  application afin de \npermettre d'améliorer son l'Allemand.\n \nLa version suivante est actuellement prévus pour \nfin Septembre. Comprendra plus de vocabulaire, \ncorrection d'eventuels bugs.",font=("Arial", 12), justify='left', bg='#646d7c' , fg='white', relief='groove')
	label_main_text.place(y=7, x=50)
	label_secondary_text.pack(expand=True)
	menu_contact = Menu(app_about_application)
	menu_contact_list = Menu(menu_contact, tearoff=False)
	menu_contact_list.add_command(label="Facebook", command=_see_project_on_fb)
	# menu_contact_list.add_command(label="GitHub", command=_see_project_on_github)  
	menu_contact.add_cascade(label="Contacte",menu=menu_contact_list)
	app_about_application.config(menu=menu_contact)

def _redefine_vars():
	global counter, life, text_player_data, text_welcome
	text_welcome.set("Bienvenu, vous pouvez naviguer avec la barre principal")
	counter = list_of_data_rule[0]
	life = list_of_data_rule[1]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _pass_question():
	global text_result, counter, life
	text_result.set("Quizz passait")
	if quizz_type==0:
		_quizz_color()
	elif quizz_type==1:
		_quizz_pronom()
	elif quizz_type==2:
		_quizz_number()
	elif quizz_type==3:
		_quizz_number_cardinals()
	counter -= 1
	life -= 1
	entry_answer_quizz.delete(0,END)

def _validate_answer(event=None):
	global quizz_started,list_of_data_rule,text_player_data,text_result, counter, life, quizz_type
	answer = entry_answer_quizz.get().lower()
	if len(answer)!=0:
		if quizz_started==True:
			if answer != "stop" and answer != "exit" and answer != "show":
				if answer == "pass":
					if life > 0 and counter > 0:
						_pass_question()
					elif counter == 1:
						text_result.set("Session terminée")
						question_text.set("Ici, s'affiche la question")
						quizz_started = False
						_redefine_vars()
					elif life == 1:
						text_result.set("Session terminée")
						question_text.set("Ici, s'affiche la question")
						quizz_started = False
						_redefine_vars()
				elif answer == quizz.lower(): 
					label_quizz_result.config(fg='#19760b')
					if counter>1 and life>1:
						text_result.set("Génial!!!")
						if quizz_type==0:
							_quizz_color()
						elif quizz_type==1:
							_quizz_pronom()
						elif quizz_type==2:
							_quizz_number()
						elif quizz_type==3:
							_quizz_number_cardinals()
						counter -= 1
					elif life==1:
						text_result.set("Session terminée")
						question_text.set("Ici, s'affiche la question")
						quizz_started = False
						_redefine_vars()
					elif counter == 1:
						text_result.set("Session terminée")
						quizz_started = False
						question_text.set("Ici, s'affiche la question")
						_redefine_vars()
					else:
						question_text.set("La session à était termiée")
						quizz_started = False
						sleep(0.3)
						_redefine_vars()
						question_text.set("Ici, s'affiche la question")
					entry_answer_quizz.delete(0,END)
				else:
					label_quizz_result.config(fg='#852d2d')
					if life>1:
						life -= 1
						text_result.set("Faux!!!")
					else:
						text_result.set("Session terminée")
						question_text.set("Ici, s'affiche la question")
						quizz_started = False
						_redefine_vars()
			elif answer == "exit":
				entry_answer_quizz.delete(0,END)
				text_result.set("Bye")
				sleep(0.6)
				app.quit()
			elif answer == "stop":
				text_result.set("Session terminée")
				text_welcome.set("Bienvenu,vous pouvez naviguer avec la barre principal")
				question_text.set("Ici, s'affiche la question")
			elif answer == "show":
				text_result.set(quizz)
			else:
				text_result.set("Quizz non démarrer!")
				sleep(0.6)
				label_quizz_result.config(fg="black")
				text_result.set("Ici, s'affiche le résultat")
	else:
		entry_answer_quizz.delete(0,END)
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _see_project_on_fb():
	webbrowser.open_new("https://www.facebook.com/profile.php?id=100019892982300")

def _see_project_on_github():
	webbrowser.open_new("http://youtube.com//")

def _set_easy_rule():
	global list_of_data_rule, text_player_data
	list_of_data_rule = [7,3,0]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _set_normal_rule():
	global list_of_data_rule, text_player_data
	list_of_data_rule = [7,3,0]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _set_hard_rule():
	global list_of_data_rule, text_player_data
	list_of_data_rule = [10,1]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _quizz_number_cardinals():
	global quizz, list_of_data_rule, quizz_started,text_result, life, counter, quizz_type, last_quizz
	text_welcome.set("Nombre Cardinaux")
	quizz_type = 3
	if quizz_started==True:
		if counter > 0:
			if life > 0:
				while quizz == last_quizz:
					quizz = choice(list_number_cardinal_de)
					question_text.set("{}".format(list_number_cardinal_fr[list_number_cardinal_de.index(quizz)]))
				last_quizz = quizz
		else:
			question_text.set("Ici, s'affiche la question")
			text_result.set("Fin de la session")
			sleep(0.3)
			text_result.set("Ici, s'affiche le résultat")
	else:
		life = list_of_data_rule[1]
		counter = list_of_data_rule[0]
		text_result.set("Session Démarrer")
		quizz_started = True
		_quizz_number()

def _quizz_number():
	global quizz, list_of_data_rule, quizz_started,text_result, life, counter, quizz_type, last_quizz
	text_welcome.set("Nombre")
	quizz_type = 2
	if quizz_started==True:
		if counter > 0:
			if life > 0:
				while quizz == last_quizz:
					quizz = choice(list_number_de)
					question_text.set("{}".format(list_number_fr[list_number_de.index(quizz)]))
				last_quizz = quizz
		else:
			question_text.set("Ici, s'affiche la question")
			text_result.set("Fin de la session")
			sleep(0.3)
			text_result.set("Ici, s'affiche le résultat")
	else:
		life = list_of_data_rule[1]
		counter = list_of_data_rule[0]
		text_result.set("Session Démarrer")
		quizz_started = True
		_quizz_number()

def _quizz_pronom(event=None):
	global quizz, list_of_data_rule, quizz_started,text_result, life, counter, quizz_type, last_quizz
	text_welcome.set("Pronom")
	quizz_type = 1
	if quizz_started==True:
		if counter > 0:
			if life > 0:
				while quizz == last_quizz:
					quizz = choice(list_pronom_de)
					question_text.set("{}".format(list_pronom_fr[list_pronom_de.index(quizz)]))
				last_quizz = quizz
		else:
			question_text.set("Ici, s'affiche la question")
			text_result.set("Fin de la session")
			sleep(0.3)
			text_result.set("Ici, s'affiche le résultat")
	else:
		life = list_of_data_rule[1]
		counter = list_of_data_rule[0]
		text_result.set("Session Démarrer")
		quizz_started = True
		_quizz_pronom()

def _quizz_color(event=None):
	global quizz, list_of_data_rule, quizz_started, text_result, life, counter, last_quizz, quizz_type, text_welcome
	text_welcome.set("Couleur")
	quizz_type = 0
	if quizz_started==True:
		if counter > 0:
			if life > 0:
				quizz = choice(list_color_de)
				while quizz == last_quizz:
					quizz = choice(list_color_de)
				question_text.set(list_color_fr[list_color_de.index(quizz)])
				last_quizz = quizz
	else:
		life = list_of_data_rule[1]
		counter = list_of_data_rule[0]
		text_result.set("Une session démarre")
		quizz_started = True
		_quizz_color()

#Personnalisation des règles, y compris la fenêtre 
def _change_data():
	global list_of_data_rule, text_player_data
	list_of_data_rule[0] = text_count.get()
	list_of_data_rule[1] = text_life.get()
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _rule_hard():
	# global list_of_data_rule, text_player_data
	list_of_data_rule = [10,1]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _rule_easy():
	global list_of_data_rule, text_player_data
	list_of_data_rule = [5,10]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _rule_initial():
	global list_of_data_rule, text_player_data
	list_of_data_rule = [7,3]
	text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))

def _customise_rule():
	global list_of_data_rule, text_life, text_count
	#Création et config de la fenêtre
	app_rule = Toplevel()
	app_rule.title("Paramètrage de la session")
	app_rule.geometry("350x140")
	app_rule.config(bg=background_color)
	#Zone des variables
	text_life = IntVar()
	text_count = IntVar()
	text_count.set(list_of_data_rule[0])
	text_life.set(list_of_data_rule[1])
	#création widget et affichage des widgets
	label_life = Label(app_rule, text="Nombre de vie :", font=("Arial", 17), relief='sunken', bg=background_color, fg='white')
	label_count = Label(app_rule, text="Nombre de quizz :", font=("Arial", 17), relief='sunken', bg=background_color, fg='white')
	spin_life = Spinbox(app_rule,width=15,textvariable=text_life ,font=("Halvetica", 15), from_=1, to=10, command=_change_data)
	spin_count = Spinbox(app_rule, width=15, textvariable=text_count, font=("Halvetica", 15), relief='sunken', from_=1, to=10, command=_change_data)
	# test.set(int(spin_life.get()))
	label_life.pack(fill=X)
	spin_life.pack() 
	label_count.pack(fill=X)
	spin_count.pack()
	#Création du menu de la mini-fenêtre
	menu_app_rule = Menu(app_rule)
	menu_customise_rule = Menu(menu_app_rule, tearoff=False)
	menu_customise_rule.add_command(label="Facile", command=_rule_easy)
	menu_customise_rule.add_command(label="Moyen", command=_rule_initial)
	menu_customise_rule.add_command(label="Dur", command=_rule_hard)
	menu_app_rule.add_cascade(label="Réglage Prédéfinis", menu=menu_customise_rule)
	app_rule.config(menu=menu_app_rule)

#variables quizz
list_color_fr = ["Blanc","Bleu","Gris","Jaune","Marron","Mauve","Orange","Rose","Rouge","Vert","Violet"]
list_color_de = ["Weiß","Blau","Grau","Gelb","Braun","Mauve","Orange","Rosa","Rot","Grün","Lila"]
list_pronom_fr = ["Je","Tu","Il","Elle","Nous","Vous","Ils"]
list_pronom_de = ["Ich","Du","Er","Sie","Wir","Sie","Sie"]
list_pronom_possesion =["ihr"]
list_number_fr = ["un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf","vingt"]
list_number_de = ["ein","zwei","drei","vier","fünf","sechs","sieben","acht","neun","zehn","elf","zwölf","dreizehn","vierzehn","fünfzehn","sechzehn","siebzehn","achtzehn","neunzehn","zwanzig"]
list_number_cardinal_fr = ["premier","second","troisième","quatrième","cinquième","sixième","septième","huitième","neuvième","dixième","onzième","douzième","treizième","quatorzième","quinzième","sezième","dix-septième","dix-huitième","dix-neuvième","vingtième"]
list_number_cardinal_de = ["erste","Sekunde","dritte","vierte","fünfte","fünfte","sechste","siebte","acht","neunte","zehnte","elfte","zwölfte","dreizehnte","vierzehnte","fünfzehnte","sechzehnte","siebzehnte","achtzehnte","neunzehnte","zwanzigten"]


add_text_quizz = 0
quizz = "T"
last_quizz = "T"
quizz_error = 0 
quizz_started = False
quizz_type = -1

"""
variables des règles
le premier élèment est le nombre de quizz d'une session, le second sont les vies
le troisième est le nombre d'erreur durant une partie 
"""
list_of_data_rule = [7,3,0]
counter = 7
life = 3
color_value = 0
background_color = "#343941"
test_new_color = background_color
new_color = ""
length_error = False
test_new_color = ""

#Construction et génération de la fenêtre
app = Tk()
app.title("Learning Deutsch Again")
app.geometry("600x300")
app.iconbitmap("new_icon.ico")
app.config(bg=background_color)
app.maxsize(width=600, height=300)

#frame
frame_main = Frame(app, width=200, height=150, bg=background_color)
frame_left = Frame(frame_main, relief='solid', bg='#686a6d', width=250, height=200)
frame_right = Frame(frame_main, relief='solid', bg='#686a6d', width=250, height=200)

#widget
text_keyboard = StringVar()
text_keyboard.set("_________\n|ALT+0223 \n|     ß\n|________\n|U+MAJ+¨\n|     Ü\n_________")
label_keyboard = Label(frame_main, textvariable=text_keyboard, justify='left', bg=background_color, font=("Arial", 10), fg='black')
text_player_data = StringVar()
text_player_data.set("Vie :{} | Durée :{}".format(str(life),str(counter)))
label_player_data = Label(frame_right, textvariable=text_player_data, justify='left', font=("Arial", 15), bg='#686a6d', fg='black')
question_text = StringVar()
question_text.set("Ici, s'affiche la question")
label_question_text = Label(frame_left, textvariable=question_text, width=18, font=("Arial", 17), bg='#686a6d', fg='black', relief='flat')
text_result = StringVar()
text_result.set("Ici, s'affiche le résultat")
label_quizz_result = Label(frame_left, textvariable=text_result, width=17, justify='center', font=("Arial", 17), bg='#686a6d', fg='black')
text_welcome = StringVar()
text_welcome.set("Bienvenu, vous pouvez naviguer avec la barre principal")  
label_welcome = Label(app, textvariable=text_welcome, font=("Arial", 17), bg=background_color, fg='white')
button_stop_quizz = Button(frame_left, text="Arreter", font=("Arial", 8), bg='#686a6d', relief='flat')
button_pass_quizz = Button(frame_left, text="passer", font=("Arial", 8), bg='#686a6d', relief='flat', command=_pass_question)
button_start_quizz = Button(frame_left, text="Démarrer", font=("Arial", 8), bg='#686a6d', relief='flat')
button_change_rule = Button(frame_right, text="Modifier les règles", font=("Comic Sans MS", 12), justify='center', width=15,fg='white' , bg='#646d7c', relief='solid', command=_customise_rule)
button_set_rule_easy = Button(frame_right, text="Facile", font=("Arial", 8), bg='#686a6d', relief='flat', command=_rule_easy)
button_set_rule_normal = Button(frame_right, text="Moyen", font=("Arial", 8), bg='#686a6d', relief='flat', command=_rule_initial)
button_set_rule_hard = Button(frame_right, text="Dur", font=("Arial", 8), bg='#686a6d', relief='flat', command=_rule_hard)


#quizz
entry_answer_quizz = Entry(frame_left, justify='center', width=15, bg='#646d7c', fg='white', font=("Comic Sans MS", 15), relief='solid')
entry_answer_quizz.bind("<Return>", _validate_answer)
entry_answer_quizz.focus()

# Création d'une barre de menu
menu_app = Menu(app)
menu_app_list = Menu(menu_app, tearoff=0)
menu_quizz_list = Menu(menu_app, tearoff=0)
menu_custom_list = Menu(menu_app, tearoff=0)
menu_about_list = Menu(menu_app, tearoff=0)
menu_app_list.add_command(label="Quitter", command=_exit_this)
menu_quizz_list.add_command(label="Couleur", command=_quizz_color)
menu_quizz_list.add_command(label="Nombres", command=_quizz_number)
menu_quizz_list.add_command(label="Nombres Cardinaux", command=_quizz_number_cardinals)
menu_quizz_list.add_command(label="Pronom Personnel", command=_quizz_pronom)
menu_quizz_list.add_command(label="Modifier les règles", command=_customise_rule)
menu_about_list.add_command(label="À propos de l'application", command=_about_application)
menu_app.add_cascade(label="Application", menu=menu_app_list)
menu_app.add_cascade(label="Quizz", menu=menu_quizz_list)
menu_app.add_cascade(label="À propos", menu=menu_about_list)

#Refresh
button_pass_quizz.place(x=5 ,y=98)
# button_pass_quizz.place(x=110, y=98)
button_change_rule.place(x=50 ,y=34)
button_set_rule_easy.place(x=5, y=98)
button_set_rule_normal.place(x=115, y=98)
button_set_rule_hard.place(x=215, y=98)
button_stop_quizz.place(x=200, y=98)
label_keyboard.place(x=265, y=37)
label_welcome.pack()
label_player_data.place(x=5)
label_question_text.place(x=5)
entry_answer_quizz.place(x=25, y=35)
label_quizz_result.place(x=5, y=70)
frame_left.place(x=10,y=30)
frame_right.place(x=340, y=30)
frame_main.pack(fill=X)
app.config(menu=menu_app)
app.mainloop()