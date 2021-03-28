## AUTORE: Alessandro Pisent
import os
from unicodedata import category, normalize

##ISTRUZIONE PER FARGLI CAPIRE DOVE SONO I FILES
os.chdir(os.path.abspath(os.path.dirname(__file__)))

#Costante del file da modificare:
FILE_NAME = "prova.txt"
FILE_NAME_OUTPUT = "provaOutput.txt"

#Array con le lettere accentate da cambiare e la loro sostituzione
accentate = ["à","è","é","ì","ò","ù"]
nonAccentate = ["a\'","e\'","e\'","i\'","o\'","u\'"]


EndFile=""

#Apertura del file da modificare
with open(FILE_NAME,"r", encoding="utf-8") as f:
    #For che fa ogni linea del file
    for line in f.readlines():

        #For che fa ogni carattere
        for char in line:

            #predefinito che $charInternational = $char
            charInternational = char

            #Se il charattere e' accentato
            if(category(char)=="Ll"):

                #Fa tutto l'array delle accentate
                for i in range(len(accentate)):

                    #Travata corrispondeza tra i caratteri accentati e $char
                    if(char==accentate[i]):
                        #Sostituzione con quello giusto
                        charInternational=nonAccentate[i]

            #la stringa che contiene tutto il file viene Composta
            EndFile = EndFile + charInternational

        
        
with open(FILE_NAME_OUTPUT,"w",encoding="utf-8") as f:
    f.writelines(EndFile)