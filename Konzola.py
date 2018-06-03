#Konzola

import tkinter as tk
from tkinter import simpledialog
import Operacije_med_matrikami as Op

okno = tk.Tk()

matrike = {}

def identiteta():
    n = simpledialog.askinteger('Identiteta', 'Velikost matrike?', parent=okno,
                                minvalue=1, maxvalue=99)
    if n is not None:
        ime = simpledialog.askstring('Identiteta', 'Ime matrike?', parent=okno)
        if ime is not None:
            matrike[ime]= Op.identiteta(n)

def poljubna_matrika():
    n= simpledialog.askinteger('Poljubna matrika', 'Velikost matrike?', parent=okno,
                               minvalue=1, maxvalue=99)
    if n is not None:
        ime = simpledialog.askstring('Poljubna matrika', 'Ime matrike?', parent=okno)
        if ime is not None:
            matrike[ime]= Op.poljubna_matrika(n)

def transponiraj():
    n = simpledialog.askstring('Transponiraj', 'Katero matriko naj transponiram?', parent=okno,)
    if n is not None:
        ime = simpledialog.askstring('Transponiraj', 'Ime matrike?', parent=okno)
        if ime is not None:
            matrike[ime]= Op.transponiraj(matrike[n])
#za katero matriko vnesi ime prejšnje, nato pa za novo ime vnesi novo črko

def vsota_matrik():
    n = simpledialog.askstring('Vsota matrik', 'Kateri matriki naj seštejem?', parent=okno)
    m = simpledialog.askstring('Vsota matrik', 'Kateri matriki naj seštejem?', parent=okno)
    if n  is not None:
        if m is not None:
            ime = simpledialog.askstring('Vsota matrik', 'Ime matrike?', parent=okno)
            if ime is not None:
                matrike[ime] = Op.vsota_matrik(
                    matrike[n], matrike[m])

def razlika_matrik():
    n = simpledialog.askstring('Razlika matrik', 'Kateri matriki naj seštejem?', parent=okno)
    m = simpledialog.askstring('Razlika matrik', 'Kateri matriki naj seštejem?', parent=okno)
    if n is not None:
        if m is not None:
            ime = simpledialog.askstring('Razlika matrik', 'Ime matrike', parent=okno)
            if ime is not None:
                matrike[ime] = Op.razlika_matrik(matrike[n], matrike[m])
            
def produkt_matrik():
    n = simpledialog.askstring('Produkt matrik', 'Kateri matriki naj seštejem?', parent=okno)
    m = simpledialog.askstring('Produkt matrik', 'Kateri matriki naj seštejem?', parent=okno)
    if n is not None:
        if m is not None:
            ime = simpledialog.askstring('Produkt matrik', 'Ime matrike', parent=okno)
            if ime is not None:
                matrike[ime] = Op.produkt_matrik(matrike[n], matrike[m])

def sled_matrike():
    n = simpledialog.askstring('Sled matrike', 'Kateri matriki naj izračunam sled?', parent=okno)
    if n is not None:
         ime = simpledialog.askstring('Produkt matrik', 'Ime matrike', parent=okno)
         if ime is not None:
             matrike[ime] = Op.sled_matrike(n)
        

    

    

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


gumb_identiteta.grid(row=0, column=0)
gumb_transponiraj.grid(row=0, column=2)
gumb_vsota_matrik.grid(row=0, column=3)
gumb_razlika_matrik.grid(row=0, column=4)
gumb_produkt_matrik.grid(row=0, column=5)
gumb_poljubna_matrika.grid(row=0, column=1)
gumb_sled_matrike .grid(row=0, column=6)


    


okno.mainloop()
