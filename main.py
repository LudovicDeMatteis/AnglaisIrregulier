import random as rng
import numpy as np
import sys
from os import system, name, getcwd


file_name = 'liste_verbes.txt'

def print_help():
    print("Cette fonctionnalité n'a pas encore été developpée...")

def scores():
    print("Cette fonctionnalité n'a pas encore été developpée...")

def entrainement():
    '''Cette fonction a pour but de s'entrainer aux verbes irreguliers
    Cette fonction lira le fichier stockant les verbes irréguliers et posera des questions'''
    clear_screen()
    all_printed_lines = []
    all_printed_lines.append("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format("Infinitif", "Prétérit", "Participe passé", "Traduction"))
    print_lines(all_printed_lines)

    f = open(file_name)
    lines = f.readlines()
    nombre_max_mots = len(lines)
    nombre_mots_choisis = 2
    mots_choisis = rng.sample(range(0, nombre_max_mots), nombre_mots_choisis)
    for line in np.array(lines)[mots_choisis]:
        #print(line)
        ask_english_from_french(line, all_printed_lines)

def ask_english_from_french(line, all_printed_lines):
    words = line.strip().split(';')
    all_printed_lines.append("|{0:-^25s}|{0:-^25s}|{0:-^25s}|{0:-^25s}|".format(""))
    print_lines(all_printed_lines)
    print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format("", "", "", words[3]))

    print("\nLe mot à trouver signifie '{}'\n".format(words[3]))
    infinitif = input("Infinitif ? : ")
    print_lines(all_printed_lines)
    print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, "", "", words[3]))
    print("\nLe mot à trouver signifie '{}'\n".format(words[3]))
    preterit = input("Prétérit ? : ")
    print_lines(all_printed_lines)
    print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, "", words[3]))
    print("\nLe mot à trouver signifie '{}'\n".format(words[3]))
    participe_p = input("Participe passé ? : ")
    print_lines(all_printed_lines)
    print("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(infinitif, preterit, participe_p, words[3]))
    # Possibilité de modifier un truc ?
    all_printed_lines.append(verification(words, infinitif, preterit, participe_p))
    print_lines(all_printed_lines)

def verification(words,infinitif, preterit, participe_p):
    return("|{0:^25}|{1:^25}|{2:^25}|{3:^25}|".format(words[0], words[1], words[2], words[3]))

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
        print("Vous avez choisi : 'Voir les meilleurs scores'.\n")
        scores()
    if choix == 3:
        print("Vous avez choisi : 'S'entrainer !'.\n")
        entrainement()
    if choix == 4:
        sys.exit("Program exited succesfully\n")

def main():
    clear_screen()
    print("\n##########  Bienvenue dans ce programme !  ##########\n")
    menu_initial()

main()
