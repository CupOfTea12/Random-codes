"""
Code by Rebeca Martinakova
II.IT
March 2021

"""
#//---LIBRARIES---//

#//---Algorithm ---//

#//---SPLITTER---//
def split(word):
    return [char for char in word]

def swap(str):
    if len(str) <= 3:
        return str

    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]

while True:
   symbol = (input("Zadajte slovo vacsie nez 4 znaky, alebo K pre ukoncenie programu: "))
   if len(symbol) < 4:
      print( 'Slovo obsahuje menej znakov nez 4, zadajte prosim ine slovo: ')
   elif(symbol=='K'):
       quit()
   elif(len(symbol)>=4):
      print('Slovo je dostatocne dlho, kompilujem...')
      #print(split(symbol))
      print (swap(symbol))











