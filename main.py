import random as rng
import numpy as np
import sys
from os import system, name, getcwd
from datetime import date

file_name = 'liste_verbes.txt'

def print_help():
    clear_screen()
    print("\n##################  Aide !  ##################\n")
    print("Ce programme a pour but de permettre à l'utilisateur de reviser ses verbes irregulier en anglais.\n")
    print("Dans le mode entrainement, vous devez completer le tableau comme demandé. Les mots doivent tous être sans accent et correctement orthographiés\n")
    print("Lorsque plusieurs mots sont attendus, il faut les séparer par une virgule. Exemple : 'was,were'\n")
    print("Lorsque tout les mots d'une ligne sont rentrés la correction de cette ligne s'effectue en affichant en rouge les mots faux et leur correction en vert.\n")
    print("Les mots justes restent dans la couleur de base.\n")

    print("\nQuelques bugs connus à corriger : \n")
    print("\t- Certains mots trop longs font bouger le tableau\n")
    print("\t- Les entrées des menus ne sont pas controlées et peuvent donc être hors limites...\n")
    print("\t- J'ajouterai un jour un reset des scores et un affichage de l'heure\n")
    print("\t- Pour ajouter des mots il faut directement modifer le .txt (me demander si besoin)\n")
    print("\t- Les mots à particule (se sentir) risquent de poser problème...\n")

    input("\n\nAppuyez sur 'Entrée' pour continuer...")
    main()

def scores():
    '''Cette fonction affiche les scores lus dans 'scores.txt' '''
    clear_screen()
    print("\n##################  Scores !  ##################\n")
    print("Voici les scores obtenus par date :")
    f = open("scores.txt",'r')
    lines = f.readlines()
    for line in lines:
        line_split = line.strip().split(';')
        date_value = line_split[0]
        score_value = line_split[1]
        max_score_value = line_split[2]
        print("\t{} => {}/{} ({}%)".format(date_value,score_value,max_score_value, round(float(int(score_value)/int(max_score_value)*100),2)))
    f.close()
    input("\n\nAppuyez sur 'Entrée' pour continuer...")
    main()

def menu_entrainement():
    clear_screen()
    print("\n##################  Entrainement !  ##################\n")
    print("Mode d'entrainement:\n\t1. A partir de la traduction francaise\n\t2. A partir de l'infinitif anglais\n\t3. Aléatoire")
    choix_mode = int(input("\nVeuillez taper le chiffre correspondant à votre choix puis faire 'Entrée' : "))
    clear_screen()
    print("\n##################  Entrainement !  ##################\n")
    choix_nombre = int(input("\nVeuillez choisir un nombre de mots sur lesquels s'entrainer (entre 1 et 100): "))
    choix_nombre = max(1, min(choix_nombre, 100))
    if choix_mode == 1:
        entrainement(choix_nombre,connu=3)
    if choix_mode == 2:
        entrainement(choix_nombre,connu=0)
    if choix_mode == 3:
        entrainement(choix_nombre)

def entrainement(nombre_mots_choisis, connu=None):
    '''Cette fonction a pour but de s'entrainer aux verbes irreguliers
    Cette fonction lira le fichier stockant les verbes irréguliers et posera des questions'''
    clear_screen()
    all_printed_lines = ["\n##################  Entrainement !  ##################\n"]
    all_printed_lines.append("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format("Infinitif", "Prétérit", "Participe passé", "Traduction"))
    print_lines(all_printed_lines)

    f = open(file_name)
    lines = f.readlines()
    nombre_max_mots = len(lines)
    nombre_mots_choisis = min(nombre_mots_choisis, nombre_max_mots)
    mots_choisis = rng.sample(range(0, nombre_max_mots), nombre_mots_choisis)
    score = 0
    for line in np.array(lines)[mots_choisis]:
        #print(line)
        score += ask_word(line, all_printed_lines, connu)
    f.close()
    max_score = nombre_mots_choisis * 3
    save_score(score,max_score)
    main()

def save_score(score, total_score):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("\nNouveau score enregistré : ")
    print("\t{} => {}/{} ({}%)".format(d1,score,total_score,round(float(score/total_score*100),2)))
    f = open("scores.txt",'a')
    f.write("{};{};{}\n".format(d1,score,total_score))
    f.close()
    input("\n\nAppuyez sur 'Entrée' pour continuer...")
    return()

def ask_word(line, all_printed_lines, connu):
    words = line.strip().split(';')
    all_printed_lines.append("|{0:-^25s}|{0:-^25s}|{0:-^25s}|{0:-^25s}|".format(""))
    print_lines(all_printed_lines)
    if connu == None:
        connu = rng.randint(0,1)*3
    if connu == 0:
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(words[0], "", "", ""))
        infinitif = words[0]
        print("\nL'infinitif du mot à trouver est '{}'\n".format(words[0]))
        preterit = input("Prétérit ? : ")
        print_lines(all_printed_lines)
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, "", ""))
        print("\nL'infinitif du mot à trouver est '{}'\n".format(words[0]))
        participe_p = input("Participe passé ? : ")
        print_lines(all_printed_lines)
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, participe_p, ""))
        print("\nL'infinitif du mot à trouver est '{}'\n".format(words[0]))
        traduction = input("Signification ? : ")
        print_lines(all_printed_lines)
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, participe_p, traduction))
    else:
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format("", "", "", words[3]))
        traduction = words[3]
        print("\nLe mot à trouver signifie '{}'\n".format(traduction))
        infinitif = input("Infinitif ? : ")
        print_lines(all_printed_lines)
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, "", "", traduction))
        print("\nLe mot à trouver signifie '{}'\n".format(words[3]))
        preterit = input("Prétérit ? : ")
        print_lines(all_printed_lines)
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, "", words[3]))
        print("\nLe mot à trouver signifie '{}'\n".format(words[3]))
        participe_p = input("Participe passé ? : ")
        print_lines(all_printed_lines)
        print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, participe_p, words[3]))

    # Possibilité de modifier un truc ?
    score, correction = verification(words, infinitif, preterit, participe_p, traduction)
    all_printed_lines.append(correction)
    print_lines(all_printed_lines)
    return(score)

def verification(words,infinitif, preterit, participe_p, traduction):
    score = -1
    line = '|'
    if comparaison_but_better(words[0], infinitif):
        line += '\x1b[31m{0:^12}\x1b[39m/\x1b[32m{1:^12}\x1b[39m|'.format(infinitif, words[0])
    else:
        line += '{0:^25}|'.format(words[0])
        score += 1
    if comparaison_but_better(words[1], preterit):
        line += '\x1b[31m{0:^12}\x1b[39m/\x1b[32m{1:^12}\x1b[39m|'.format(preterit, words[1])
    else:
        line += '{0:^25}|'.format(words[1])
        score += 1
    if comparaison_but_better(words[2], participe_p):
        line += '\x1b[31m{0:^12}\x1b[39m/\x1b[32m{1:^12}\x1b[39m|'.format(participe_p, words[2])
    else:
        line += '{0:^25}|'.format(words[2])
        score += 1
    if comparaison_but_better(words[3], traduction):
        line += '\x1b[31m{0:^12}\x1b[39m/\x1b[32m{1:^12}\x1b[39m|'.format(traduction, words[3])
    else:
        line += '{0:^25}|'.format(words[3])
        score += 1
    return(score, line)

def comparaison_but_better(word_one, word_two):
    word_one = word_one.replace(" ", "").upper()
    word_two = word_two.replace(" ", "").upper()
    if word_one != word_two:
        return(True)
    return(False)

def print_lines(all_printed_lines):
    clear_screen()
    for line in all_printed_lines:
        print(line)

def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print("\x1b" + "[39m")

def menu_initial():
    print("\t1. Explication du fonctionnement du programme \n\t2. Voir les meilleurs scores \n\t3. S'entrainer ! \n\t4. Quitter le programme")
    choix = int(input("\nVeuillez taper le chiffre correspondant à votre choix puis faire 'Entrée' : "))
    if choix == 1:
        print("Vous avez choisi : 'Explication du fonctionnement du programme'\n.")
        print_help()
    if choix == 2:
        print("Vous avez choisi : 'Voir les scores'.\n")
        scores()
    if choix == 3:
        print("Vous avez choisi : 'S'entrainer !'.\n")
        menu_entrainement()
    if choix == 4:
        sys.exit("Merci d'avoir utilisé ce programme ! :D\n")

def main():
    clear_screen()
    print("\n##########  Bienvenue dans ce programme !  ##########\n")
    menu_initial()

main()
