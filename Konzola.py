#Konzola

import tkinter as tk
from tkinter import simpledialog
import Operacije_med_matrikami as Op

okno = tk.Tk()

matrike = {}

def identiteta():
    a = simpledialog.askinteger('Identiteta', 'Velikost matrike?', parent=okno,
                                minvalue=1, maxvalue=99)
    if a is not None:
        ime = simpledialog.askstring('Identiteta', 'Ime matrike?', parent=okno)
        if ime is not None:
            if ime in matrike:
                print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))       
            else:
                matrike[ime]= Op.identiteta(a)

def poljubna_matrika():
    a = simpledialog.askinteger('Poljubna matrika', 'Velikost matrike?', parent=okno,
                               minvalue=1, maxvalue=99)
    if a is not None:
        ime = simpledialog.askstring('Poljubna matrika', 'Ime matrike?', parent=okno)
        if ime is not None:
            if ime in matrike:
                print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))    
            else:
                matrike[ime]= Op.poljubna_matrika(a)

def transponiraj():
    a = simpledialog.askstring('Transponiraj', 'Katero matriko naj transponiram?', parent=okno,)
    if a is not None:
        ime = simpledialog.askstring('Transponiraj', 'Ime matrike?', parent=okno)
        if ime is not None:
            if ime in matrike:
                print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
            else:
                matrike[ime]= Op.transponiraj(matrike[a])
#za katero matriko vnesi ime prejšnje, nato pa za novo ime vnesi novo črko

def vsota_matrik():
    a = simpledialog.askstring('Vsota matrik', 'Kateri matriki naj seštejem?', parent=okno)
    b = simpledialog.askstring('Vsota matrik', 'Kateri matriki naj seštejem?', parent=okno)
    if a  is not None:
        if b is not None:
            ime = simpledialog.askstring('Vsota matrik', 'Ime matrike?', parent=okno)
            if ime is not None:
                if ime in matrike:
                    print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
                else:
                    matrike[ime] = Op.vsota_matrik(
                    matrike[a], matrike[b])

def razlika_matrik():
    a = simpledialog.askstring('Razlika matrik', 'Kateri matriki naj odštejem?', parent=okno)
    b = simpledialog.askstring('Razlika matrik', 'Kateri matriki naj odštejem?', parent=okno)
    if a is not None:
        if b is not None:
            ime = simpledialog.askstring('Razlika matrik', 'Ime matrike', parent=okno)
            if ime is not None:
                if ime in matrike:
                    print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
                else:
                    matrike[ime] = Op.razlika_matrik(matrike[a], matrike[b])
            
def produkt_matrik():
    a = simpledialog.askstring('Produkt matrik', 'Kateri matriki naj zmnožim?', parent=okno)
    b = simpledialog.askstring('Produkt matrik', 'Kateri matriki naj zmnožim?', parent=okno)
    if a is not None:
        if b is not None:
            ime = simpledialog.askstring('Produkt matrik', 'Ime matrike?', parent=okno)
            if ime is not None:
                if ime in matrike:
                    print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
                else:
                    matrike[ime] = Op.produkt_matrik(matrike[a], matrike[b])

def sled_matrike():
    a = simpledialog.askstring('Sled matrike', 'Kateri matriki naj izračunam sled?', parent=okno)
    if a is not None:
         ime = simpledialog.askstring('Sled matrike', 'Ime sledi? npr: Sled a',
                                      parent=okno) 
         if ime is not None:
                 matrike[ime] = Op.sled_matrike(matrike[a])

def vrni_na_začetek():
    global matrike
    matrike = {}

def izbriši_matriko():
    a = simpledialog.askstring('Izbriši matriko', 'Katero matriko naj izbrišem?', parent=okno)
    if a is not None:
        matrike.pop(a)

def izbrana_matrika():
    a = simpledialog.askstring('Izbrana matrika', 'Vnesite matriko, ki jo želite dodati v slovar', parent=okno)
    if a is not None:
            ime = simpledialog.askstring('Izbrana matrika', 'Ime matrike?', parent=okno)
            if ime is not None:
                if ime in matrike:
                    print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
                else:
                    matrike[ime] = eval(a)
    

gumb_identiteta = tk.Button(okno, text='Identiteta',
                            command=identiteta)
gumb_poljubna_matrika = tk.Button(okno, text='Poljubna matrika',

                                  command=poljubna_matrika)
gumb_transponiraj = tk.Button(okno, text='Transponiraj',
                              command=transponiraj)
gumb_vsota_matrik = tk.Button(okno, text='Seštej matriki',
                              command=vsota_matrik)
gumb_sled_matrike = tk.Button(okno, text='Sled matrike',
                              command=sled_matrike)
gumb_razlika_matrik = tk.Button(okno, text='Odštej matriki',
                                command=razlika_matrik)
gumb_produkt_matrik = tk.Button(okno, text='Zmnoži matriki',
                                command=produkt_matrik)
gumb_vrni_na_začetek = tk.Button(okno, text='Ponastavi',
                                 command=vrni_na_začetek)
gumb_izbriši_matriko = tk.Button(okno, text='Izbriši sled ali matriko',
                                 command=izbriši_matriko)
gumb_izbrana_matrika = tk.Button(okno, text='Dodaj izbrano matriko',
                                 command=izbrana_matrika)

gumb_identiteta.grid(row=0, column=0)
gumb_transponiraj.grid(row=0, column=2)
gumb_vsota_matrik.grid(row=0, column=3)
gumb_razlika_matrik.grid(row=0, column=4)
gumb_produkt_matrik.grid(row=0, column=5)
gumb_poljubna_matrika.grid(row=0, column=1)
gumb_sled_matrike.grid(row=0, column=6)
gumb_vrni_na_začetek.grid(row=2, column=3)
gumb_izbriši_matriko.grid(row=2, column=4)
gumb_izbrana_matrika.grid(row=2, column=6)

okno.mainloop()
