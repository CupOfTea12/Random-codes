dlzka_cm = 10

def palec_premena(dlzka_cm):
   palec = dlzka_cm * 0.39370
   return(palec)

def stopa_premena(dlzka_cm):
    stopa = dlzka_cm * 0.032808
    return(stopa)

def yard_premena(dlzka_cm):
     yard = dlzka_cm*0.010963
     return(yard)
print(f'Dlzka {dlzka_cm} cm je :\n{palec_premena(dlzka_cm)} palcov\n{stopa_premena(dlzka_cm)} stopa\n{yard_premena(dlzka_cm)} yard')
