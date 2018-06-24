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
                print('Žal je matrika z imenom {} že v slovarju. Izberite drugo ime'.format(ime))       
            else:
                matrike[ime]= Op.identiteta(a)

def poljubna_matrika():
    a = simpledialog.askinteger('Poljubna matrika', 'Število vrstic?', parent=okno,
                               minvalue=1, maxvalue=99)
    b = simpledialog.askinteger('Poljubna matrika', 'Število stolpcev?', parent=okno,
                                minvalue=1, maxvalue=99)
    if a and  b is not None:
        ime = simpledialog.askstring('Poljubna matrika', 'Ime matrike?', parent=okno)
        if ime is not None:
            if ime in matrike:
                print('Žal je matrika z imenom {} že v slovarju. Izberite drugo ime'.format(ime))    
            else:
                matrike[ime]= Op.poljubna_matrika(a, b)

def transponiraj():
    a = simpledialog.askstring('Transponiraj', 'Napišite ime matrike, ki jo želite transponirati?', parent=okno,)
    if a is not None:
        ime = simpledialog.askstring('Transponiraj', 'Ime matrike?', parent=okno)
        if ime is not None:
            if ime in matrike:
                print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
            else:
                matrike[ime]= Op.transponiraj(matrike[a])
#za katero matriko vnesi ime prejšnje, nato pa za novo ime vnesi novo črko

def vsota_matrik():
    a = simpledialog.askstring('Vsota matrik', 'Izberite matriko' , parent=okno)
    b = simpledialog.askstring('Vsota matrik', 'Katero matriko želite sešteti z matriko {}'.format(a), parent=okno)
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
    a = simpledialog.askstring('Razlika matrik', 'Izberite matriko', parent=okno)
    b = simpledialog.askstring('Razlika matrik', 'Katero matriko želite odšteti od matrike {}?'.format(a), parent=okno)
    if a is not None:
        if b is not None:
            ime = simpledialog.askstring('Razlika matrik', 'Ime matrike', parent=okno)
            if ime is not None:
                if ime in matrike:
                    print('Žal je matrika z imenom {} že v slovarju. Izberite si drugo ime'.format(ime))
                else:
                    matrike[ime] = Op.razlika_matrik(matrike[a], matrike[b])
            
def produkt_matrik():
    a = simpledialog.askstring('Produkt matrik', 'Izberite matriko', parent=okno)
    b = simpledialog.askstring('Produkt matrik', 'Katero matriko naj zmnožim z matriko {}?'.format(a), parent=okno)
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

def vrzi_v_datoteko():
    a = simpledialog.askstring('Datoteka', 'Izberi ime matrike?', parent=okno)
    with open('matrika.txt', 'a') as matrika:
        print('{}:{}'.format(a, str(matrike[a])), file=matrika)

#Meni
meni = tk.Menu(okno)
podmeni = tk.Menu(meni, tearoff=0)
podmeni.add_command(label='Izbriši ves seznam matrik', command=vrni_na_začetek)
podmeni.add_command(label='Izbriši sled ali matriko', command=izbriši_matriko)
meni.add_cascade(label='Izbriši', menu=podmeni)
meni.add_command(label='Vrzi v datoteko', command=vrzi_v_datoteko)
okno.configure(menu=meni)
    
gumb_identiteta = tk.Button(okno, text='Ustvari identično matriko',
                            command=identiteta, width=30)
gumb_poljubna_matrika = tk.Button(okno, text='Poljubna matrika',
                                  command=poljubna_matrika, width=30)
gumb_transponiraj = tk.Button(okno, text='Transponiraj matriko',
                              command=transponiraj, width=30)
gumb_vsota_matrik = tk.Button(okno, text='Seštej matriki',
                              command=vsota_matrik, width=30)
gumb_sled_matrike = tk.Button(okno, text='Sled matrike',
                              command=sled_matrike, width=30)
gumb_razlika_matrik = tk.Button(okno, text='Odštej matriki',
                                command=razlika_matrik, width=30)
gumb_produkt_matrik = tk.Button(okno, text='Zmnoži matriki',
                                command=produkt_matrik, width=30)
gumb_izbrana_matrika = tk.Button(okno, text='Dodaj izbrano matriko',
                                 command=izbrana_matrika, width=30)

gumb_identiteta.grid(row=1, column=0)
gumb_transponiraj.grid(row=5, column=0)
gumb_vsota_matrik.grid(row=6, column=0)
gumb_razlika_matrik.grid(row=7, column=0)
gumb_produkt_matrik.grid(row=8, column=0)
gumb_poljubna_matrika.grid(row=2, column=0)
gumb_sled_matrike.grid(row=4, column=0)
gumb_izbrana_matrika.grid(row=3, column=0)

okno.mainloop()
