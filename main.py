# Główna aplikacja GUI
import tkinter as tk
from tkinter import simpledialog , messagebox
from utils.controller import get_grouped_map
from utils.model import clients, employees , toll_booth
import webbrowser


def gui_main():
    def open_map(file_name="mapa.html"):
        webbrowser.open(file_name)

    def make_menu(title, dataset, type_):
        window = tk.Toplevel(root)
        window.title(title)


        def refresh_list():
            listbox.delete(0, tk.END)
            for item in dataset:
                toll_booth_info = f"       {item['toll_booth']}" if "toll_booth" in item else ""
                listbox.insert(tk.END, f"{item['name']}       {item['location']}{toll_booth_info}")

        def add():
            name = simpledialog.askstring("Dodaj", "Podaj nazwę:")
            location = simpledialog.askstring("Dodaj", "Podaj lokalizację:")

            if not name or not location:
                messagebox.showwarning("Błąd", "Musisz podać nazwę i lokalizację.")
                return

            if type_ in ["clients", "employees"]:
                # Lista nazw istniejących punktów poboru opłat
                toll_booth_names = [s["name"] for s in toll_booth ]

                # Okno wyboru stacji
                toll_booth_window = tk.Toplevel(window)
                toll_booth_window.title("Wybierz punkt poboru opłat")

                tk.Label(toll_booth_window, text="Wybierz punkt poboru opłat dla tej osoby:").pack(pady=5)
                selected_toll_booth= tk.StringVar()
                selected_toll_booth.set(toll_booth_names[0])  # domyślnie pierwsza stacja

                tk.OptionMenu(toll_booth_window, selected_toll_booth, *toll_booth_names).pack(pady=5)

                def confirm_toll_booth():
                    toll_booth = selected_toll_booth.get()
                    dataset.append({
                        "name": name,
                        "location": location,
                        "station": toll_booth
                    })
                    toll_booth_window.destroy()
                    refresh_list()

                tk.Button(toll_booth_window, text="Zatwierdź", command=confirm_toll_booth).pack(pady=10)
            else:
                dataset.append({
                    "name": name,
                    "location": location
                })
                refresh_list()

        def remove():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Uwaga", "Nie zaznaczono elementu do usunięcia.")
                return
            dataset.pop(idx[0])
            refresh_list()

        def update():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Uwaga", "Nie zaznaczono elementu do edycji.")
                return

            current = dataset[idx[0]]
            new_name = simpledialog.askstring("Nowa nazwa", "Nowa nazwa:", initialvalue=current["name"])
            new_location = simpledialog.askstring("Nowa lokalizacja", "Nowa lokalizacja:",
                                                  initialvalue=current["location"])

            if not new_name or not new_location:
                messagebox.showwarning("Błąd", "Musisz podać nazwę i lokalizację.")
                return

            if type_ in ["clients", "employees"]:
                toll_booth_names = [s["name"] for s in toll_booth]

                toll_booth_window = tk.Toplevel(window)
                toll_booth_window.title("Wybierz nową stację")

                tk.Label(toll_booth_window, text="Wybierz nowy punk poboru opłat:").pack(pady=5)
                selected_toll_booth = tk.StringVar()
                selected_toll_booth.set(current.get("toll_booth", toll_booth_names[0]))

                tk.OptionMenu(toll_booth_window, selected_toll_booth, *toll_booth_names).pack(pady=5)

                def confirm_update():
                    dataset[idx[0]] = {
                        "name": new_name,
                        "location": new_location,
                        "toll_booth": selected_toll_booth.get()
                    }
                    toll_booth_window.destroy()
                    refresh_list()

                tk.Button(toll_booth_window, text="Zatwierdź", command=confirm_update).pack(pady=10)
            else:
                dataset[idx[0]] = {
                    "name": new_name,
                    "location": new_location
                }
                refresh_list()


        def show_map():
            get_grouped_map(dataset, f"{type_}_map.html")
            webbrowser.open(f"{type_}_map.html")

        # UI
        btn_frame = tk.Frame(window)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Dodaj", command=add, width=12).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Usuń", command=remove, width=12).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Aktualizuj", command=update, width=12).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Mapa", command=show_map, width=12).grid(row=0, column=3, padx=5)

        listbox = tk.Listbox(window, width=60, height=15)
        listbox.pack(padx=10, pady=10)

        refresh_list()

    def map_clients_of_toll_booth():
        name = simpledialog.askstring("Punkt poboru opłat", "Podaj nazwę punktu poboru opłat:")
        filtered = [c for c in clients if c['toll_booth'] == name]
        if not filtered:
            messagebox.showinfo("Brak danych", "Brak klientów dla tego punktu poboru opłat.")
            return
        get_grouped_map(filtered, "clients_of_toll_booth.html")
        open_map("clients_of_toll_booth.html")

    def map_employees_of_toll_booth():
            name = simpledialog.askstring("Punkt poboru opłat", "Podaj nazwę Punktu poboru opłat:")
            filtered = [e for e in employees if e['toll_booth'] == name]
            if not filtered:
                messagebox.showinfo("Brak danych", "Brak pracowników dla tego punktu poboru opłat.")
                return
            get_grouped_map(filtered, "employees_of_toll_booth.html")
            open_map("employees_of_toll_booth.html")

    root = tk.Tk()
    root.title("System zarządzania punktami poboru opłat")

    tk.Button(root, text="Punkt poboru opłat", command=lambda: make_menu("Punkt poboru opłat", toll_booth, "toll_booth")).pack(pady=10)
    tk.Button(root, text="Pracownicy", command=lambda: make_menu("Pracownicy", employees, "employees")).pack(pady=10)
    tk.Button(root, text="Klienci", command=lambda: make_menu("Klienci", clients, "clients")).pack(pady=10)

    tk.Button(root, text="Mapa klientów wybranego punktu poboru opłat", command=map_clients_of_toll_booth).pack(pady=10)
    tk.Button(root, text="Mapa pracowników wybranego punktu poboru opłat", command=map_employees_of_toll_booth).pack(pady=10)

    tk.Button(root, text="Zamknij", command=root.destroy).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    gui_main()
