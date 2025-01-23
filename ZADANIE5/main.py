import tkinter as tk

# Napisz funkcję create_app(), która:
# Tworzy główne okno Tkinter,
# Dodaje etykietę (label) z jakimś wstępnym tekstem (np. "Wpisz coś:"),
# Dodaje pole tekstowe (Entry), w którym użytkownik może coś wpisać,
# Dodaje przycisk (Button), po którego kliknięciu tekst z pola Entry zostanie wyświetlony w drugiej etykiecie (np. "Wpisałeś: <tekst>").


def create_app():
    """
    Tworzy i zwraca główne okno Tkinter z prostym interfejsem.
    1) Etykieta: "Wpisz coś:"
    2) Pole Entry
    3) Przycisk "Pokaż", który wyświetli wpisany tekst w innej etykiecie
    """
    # title - "Prosta aplikacja Tkinter"

    root = tk.Tk()
    root.title("Prosta aplikacja Tkinter")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)

    # label_instruct = umocuj przez pack
    label_instruct = tk.Label(frame, text="Wpisz coś:")
    label_instruct.pack()

    entry_text = tk.Entry(frame)
    entry_text.pack()

    label_result = tk.Label(frame, text="")
    label_result.pack()

    def show_text():
        text = entry_text.get()
        label_result.config(text=f"Wpisane: {text}")

    button_show = tk.Button(frame, text="Pokaż", command=show_text)
    button_show.pack()

    return root

if __name__ == '__main__':
    app = create_app()
    app.mainloop()
