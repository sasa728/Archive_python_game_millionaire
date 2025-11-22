import time
from tkinter import *
import json
import random
from tkinter.ttk import Style

button_style = {
    'padx': 24,
    'pady': 1,
    'width': 10,
    'height': 1,
    'font': ("Arial", 16),
    'foreground': '#DADCE0',
    'background': '#3C3F41',
    'activebackground': '#3C3F41'
}

def open_json(jmeno):
    with open(jmeno, 'r+', encoding='utf-8') as f:
        try:
            file_dict = json.load(f)
        except Exception:
            file_dict = []
    return file_dict

scoreboard = open_json("scoreboard.json")
soubor_otazek = open_json("otazky.json")
window = Tk()
window.geometry("480x640")
window.title("Milionari")
icon = PhotoImage(file="dolar.png")
window.iconphoto(True, icon)
window.resizable(False, False)
window.config(background="#262626")
VYHRAL = IntVar()
VYHRAL.set(0)

def openNewWindow(x):
    body2 = x
    jmenohrace = StringVar()
    def okjmeno():
        OK.pack_forget()
        newWindow.destroy()
        input.pack_forget()
        #osetreni prazdenho jmeno
        if len(jmenohrace.get())==0:
            jmenohrace.set("No name")
        #osetreni prilis dlouhych jmeno
        if len(jmenohrace.get())>15:
            y=jmenohrace.get()[0:15]
            jmenohrace.set(y)
        print(jmenohrace.get())
        print(body2)
        #pridani uzivatele do scoreboardu
        usertowrite = {
                "Jmeno": jmenohrace.get(),
                "Skore": body2
                }
        scoreboard.append(usertowrite)
        with open('scoreboard.json', 'r+') as file:
            content = file.read()
            file.seek(0)
            file.write(json.dumps(scoreboard))
    newWindow = Toplevel(window)
    newWindow.title("Zadej svoje jméno")
    newWindow.geometry("200x200")
    Label(newWindow,bg="#3C3F41", pady=10, padx=100, borderwidth=2, relief="raised", width=10,
                       font=("Arial", 14), fg="#DADCE0",
          text=f"Dosažené skóre: {body2}").pack(pady=10)
    newWindow.config(background="#262626")
    newWindow.geometry("320x180")
    newWindow.resizable(False, False)
    OK = Button(newWindow,**button_style,
    text="Potvrdit",
    command=okjmeno)
    input = Entry(newWindow,textvariable=jmenohrace,bg="#3C3F41", borderwidth=2, relief="raised", width=10,
                       font=("Arial", 14), fg="#DADCE0")
    input.pack(pady=10)
    OK.pack()

def zmiz():
    play.pack_forget()
    konec.pack_forget()
    skore.pack_forget()
    zpet.pack(pady=5)
KONECSKORE = IntVar()
KONECSKORE.set(0)

def zobrazskore():
    zmiz()
    pocet=0
    Nadpis=Label(window, bg="#3C3F41", pady=10, padx=100, borderwidth=2, relief="raised",height=1, width=10,
                       font=("Arial", 16), fg="#DADCE0", text="Nejlepší hráči a jejich skóre")

    Nadpis.pack()
    # list labelu, bude obsahovat labely, kazdej label ma jednoho cloveka ze scoreboardu
    label_list = []
    # prochazim json scoreboard a postupne vypisuju kazdeho ve scoreboardu serazeneho podle skore
    for hrac in sorted(scoreboard, key=lambda t: t.get('Skore'), reverse=True):
        pocet+=1
        print(hrac.get('Jmeno'), hrac.get('Skore'))
        skore1 = Label(window, bg="#3C3F41", pady=10, padx=100, borderwidth=2, relief="raised", width=10,
                       font=("Arial", 16), fg="#DADCE0", text=hrac.get('Jmeno') + ' ' + str(hrac.get('Skore')))
        skore1.pack()
        label_list.append(skore1)
        if pocet>=10: break
        # konec skore urci kdy se prestanou zobrazovat a ceka na akci tlacitka zpet
    # setnu var konec na 1, aby cekal na hodnotu 2
    KONECSKORE.set(1)
    window.wait_variable(KONECSKORE)
    Nadpis.pack_forget()
    # smazu vsechny labely z listu labelu
    for label in label_list:
        label.pack_forget()

def objevse():
    play.pack(pady=105)
    skore.pack(pady=25)
    konec.pack(pady=25)
    zpet.pack_forget()
    # variable konecskore ukonci zobrazeni labelu po zmacknuti tlacitka zpet, hodnota var je 2
    KONECSKORE.set(2)

def ukoncihru():
    quit()

def hra():
    n1=BooleanVar()
    n2=BooleanVar()
    n1.set(True)
    n2.set(True)
    VYHRAL.set(0)
    zmiz()
    zpet.pack_forget()
    body=1
    while True:
        button_list = []
        # buttony jsou generovany az je vybrana otazka, daji se do listu, buttony obsahuji text jako odpoved z jsonu otazky
        # jako se scoreboardem cekaji pak na variable aby se mohly smazat
        otazka = random.choice(soubor_otazek)
        #Label se současným skore
        skorelabel = Label(text="Současné skóre: "+str(body),bg="#3C3F41", pady=10, padx=100, borderwidth=2, relief="raised", width=1000,
                       font=("Arial", 16), fg="#DADCE0")
        skorelabel.pack(pady=10)
        #Label s otázkou nahoře
        otazkalabel = Label(text=otazka.get("otazka"),bg="#3C3F41", pady=10, padx=100, borderwidth=2, relief="raised", width=1000,
                       font=("Arial", 16), fg="#DADCE0")
        otazkalabel.pack(pady=10)
        #generace random otázky
        vsechny_odpovedi = otazka.get("vsechny")[:]
        vsechny_odpovedi.append(otazka.get("spravna"))
        random.shuffle(vsechny_odpovedi)
        if not button_list:
            for index, odp in enumerate(vsechny_odpovedi):
                t_button = Button(window, text=odp,bg="#3C3F41", pady=10, padx=100, borderwidth=2, relief="raised",
                       font=("Arial", 14), fg="#DADCE0", width=7 ,command=lambda odp=odp: check_answer(odp, otazka))
                t_button.pack(pady=10)
                button_list.append(t_button)
        # --------------------------------------
        def napoveda1():
            smazano=0
            for button in button_list:
                if button.cget('text') != otazka.get("spravna") and smazano<2:
                    smazano+=1
                    button.pack_forget()

            n1.set(False)
            tlacitkonapovedy1.pack_forget()
            print(n1.get())

        def napoveda2():
            odpovedi = otazka.get("vsechny")[:]
            odpovedi.append(otazka.get("spravna"))
            celkem=100
            pocitadlo=0
            maximum=0
            abcd=[]
            for i in range(3):
                pocitadlo=random.randrange(0,celkem)
                abcd.append(pocitadlo)
                celkem-=pocitadlo
            abcd.append(celkem)
            maximum=max(abcd)
            abcd.remove(maximum)
            n2.set(False)
            newWindow2 = Toplevel(window)
            newWindow2.title("Nápověda publika")
            newWindow2.geometry("200x200")
            newWindow2.config(background="#262626")
            newWindow2.geometry("650x370")
            newWindow2.resizable(False, False)
            tlacitkonapovedy2.pack_forget()
            data = abcd
            data.append(maximum)
            c_width = 650  # Define it's width
            c_height = 370  # Define it's height
            c = Canvas(newWindow2, width=c_width, height=c_height, background="#262626")
            c.pack()
            y_stretch = 3
            y_gap = 10
            x_stretch = 10
            x_width = 150
            x_gap = 1
            for x, y in enumerate(data):
                x0 = x * x_stretch + x * x_width + x_gap
                y0 = c_height - (y * y_stretch + y_gap)
                x1 = x * x_stretch + x * x_width + x_width + x_gap
                y1 = c_height - y_gap
                c.create_rectangle(x0, y0, x1, y1, fill="#DADCE0")
                c.create_text(x0 + 2, y0, anchor=SW, text=str(abcd[x])+"% "+odpovedi[x],font=("Arial", 12), fill="#DADCE0")
                print(vsechny_odpovedi)
        if n1.get():
            tlacitkonapovedy1 = Button(**button_style,
                                               text="50/50", command=napoveda1)
            tlacitkonapovedy1.pack(pady=20, side=BOTTOM)
        if n2.get():
            tlacitkonapovedy2 = Button(**button_style,
                                               text="Nápověda publika",
                                               command=napoveda2)
            tlacitkonapovedy2.pack(pady=5, side=BOTTOM)
        # --------------------------------------
        window.wait_variable(VYHRAL)
        print(f"{VYHRAL.get()=}")
        # skore *=
        body*=2
        for button in button_list:
            button.pack_forget()
        #odstraneni stare otazky a "stareho" skore
        otazkalabel.pack_forget()
        skorelabel.pack_forget()
        tlacitkonapovedy1.pack_forget()
        tlacitkonapovedy2.pack_forget()
        # VYHRAL.set(0)
        if VYHRAL.get() == 2:
            # ZADEJ JMENO
            # pridej do souboru scoreboard
            print(body)
            openNewWindow(body)
            otazkalabel.pack_forget()
            skorelabel.pack_forget()
            tlacitkonapovedy1.pack_forget()
            tlacitkonapovedy2.pack_forget()
            break
    objevse()

def check_answer(odp_f, otazka_f):
    print(otazka_f.get('spravna'), odp_f)
    if otazka_f.get('spravna') == odp_f:
        VYHRAL.set(1)
    else:
        VYHRAL.set(2)

zpet = Button(
    # TAKHLE DELAM BUTNY
    **button_style,
    text="Zpet",
    command=objevse)

play = Button(
    **button_style,
    text="Start",
    command=hra,)

skore = Button(
    **button_style,
    text="Tabulka skore",
    command=zobrazskore)

konec = Button(
    window,
    **button_style,
    text="Konec",
    command=ukoncihru)

play.pack(pady=105)
skore.pack(pady=25)
konec.pack(pady=25)

window.mainloop()