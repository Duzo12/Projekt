#Konzola

import tkinter as tk
from tkinter import simpledialog
import Operacije_med_matrikami as Op

okno = tk.Tk()

matrike = {}

def identiteta():
    n = simpledialog.askinteger('Identiteta', 'Velikost matrike?', parent=okno,
                                minvalue=1, maxvalue=4)
    if n is not None:
        ime = simpledialog.askstring('Identiteta', 'Ime matrike?', parent=okno)
        if ime is not None:
            matrike[ime]= Op.identiteta(n)

def transponiraj():
    a = simpledialog.askstring('Transponiraj', 'Katero matriko naj transponiram?', parent=okno,)
    if a is not None:
        ime = simpledialog.askstring('Transponiraj', 'Ime matrike?', parent=okno)
        if ime is not None:
            matrike[ime]= Op.transponiraj(matrike[a])
#za katero matriko vnesi ime prejšnje, nato pa za novo ime vnesi novo črko    

    

gumb_identiteta = tk.Button(okno, text='Identiteta',
                            command=identiteta)
gumb_transponiraj = tk.Button(okno, text='Transponiraj',
                              command=transponiraj)
gumb_vsota_matrik = tk.Button(okno, text='Seštej matriki',
                              command=Op.vsota_matrik)
gumb_razlika_matrik = tk.Button(okno, text='Odštej matriki',
                                command=Op.razlika_matrik)
gumb_produkt_matrik = tk.Button(okno, text='Zmnoži matriki',
                                command=Op.produkt_matrik)

gumb_identiteta.grid(row=0, column=0)
gumb_transponiraj.grid(row=0, column=1)
gumb_vsota_matrik.grid(row=0, column=2)
gumb_razlika_matrik.grid(row=0, column=3)
gumb_produkt_matrik.grid(row=0, column=4)


    


okno.mainloop()
