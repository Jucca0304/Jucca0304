import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def fire():
    try:
        networth = int(ent_networth.get())
        income = int(ent_income.get())
        expenses = int(ent_expenses.get())
        swr = int(ent_swr.get())
        interest = int(ent_interest.get())
        income_change = int(ent_income_change.get())
        expenses_change = int(ent_expenses_change.get())
        taxrate = int(ent_taxrate.get())
        years = 0
        x = []
        y_income = []
        y_networth = []
        y_expenses = []
        y_sr = []
        while networth < expenses / (100 - taxrate) * 100 * (100 / swr):
            income = income / 100 * (100 + income_change)
            expenses = expenses / 100 * (100 + expenses_change)
            networth = (networth + income - expenses) / 100 * (100 + interest)
            years = years + 1
            x.append(years)
            y_income.append(income)
            y_networth.append(networth)
            y_expenses.append(expenses)
            if years >= 50:
                lbl_result["text"] = 'Fire is not achievable under these condition'
                break
            else:
                ## Figure
                fig, ax = plt.subplots(figsize = (7, 5),
                             dpi = 100)
                ## Plots
                ax.plot(x, y_income, color='green')
                ax.plot(x, y_expenses, color='red')
                ax.plot(x, y_networth, color='blue')

                ## Styling
                ax.legend(['Income', 'Expenses', 'Networth'])
                plt.title("Your FIRE networth of {:,.0f} € is reached after {} years".format(int(networth), years))
                plt.style.use('ggplot')
                plt.ylabel('€')
                plt.xlabel('YEARS')
                ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x / 1000) + 'K'))
                plt.xticks(np.arange(min(x), max(x)+1, 1))
                plt.yticks(np.arange(0, max(y_networth), 100000))

                ## Adding to Window
                canvas = FigureCanvasTkAgg(fig, master=window)
                canvas.draw()
                canvas.get_tk_widget().grid(row=3, column=0, padx=10)
                frm_toolbar = tk.Frame(master=window)
                frm_toolbar.grid(row=4, column=0, padx=10)
                toolbar = NavigationToolbar2Tk(canvas, frm_toolbar)
                toolbar.update()

    except ValueError:
        lbl_result["text"] = 'Please make sure to enter values in all fields!'



# Initiate Main Window
window = tk.Tk()
window.title('FIRE Calculator')

# Entry Frame
frm_entry = tk.Frame(master=window)

## Networth
lbl_networth = tk.Label(master=frm_entry, text="Networth:")
ent_networth = tk.Entry(master=frm_entry, width=10)
lbl_networth_cur = tk.Label(master=frm_entry, text="€")

lbl_networth.grid(row=2, column=0, sticky="w")
ent_networth.grid(row=2, column=1, sticky="e")
lbl_networth_cur.grid(row=2, column=2, sticky="w")

## Income
lbl_income = tk.Label(master=frm_entry, text="Income:")
ent_income = tk.Entry(master=frm_entry, width=10)
lbl_income_cur = tk.Label(master=frm_entry, text="€")

lbl_income.grid(row=0, column=0, sticky="w")
ent_income.grid(row=0, column=1, sticky="e")
lbl_income_cur.grid(row=0, column=2, sticky="w")

## Expenses
lbl_expenses = tk.Label(master=frm_entry, text="Expenses:")
ent_expenses = tk.Entry(master=frm_entry, width=10)
lbl_expenses_cur = tk.Label(master=frm_entry, text="€")

lbl_expenses.grid(row=1, column=0, sticky="w")
ent_expenses.grid(row=1, column=1, sticky="e")
lbl_expenses_cur.grid(row=1, column=2, sticky="w")

## Income Change
lbl_income_change = tk.Label(master=frm_entry, text="Income Change:")
ent_income_change = tk.Entry(master=frm_entry, width=10)
lbl_income_change_cur = tk.Label(master=frm_entry, text="%")
ent_income_change.insert(0, '0')

lbl_income_change.grid(row=0, column=3, sticky="w")
ent_income_change.grid(row=0, column=4, sticky="e")
lbl_income_change_cur.grid(row=0, column=5, sticky="w")

## Expenses Change
lbl_expenses_change = tk.Label(master=frm_entry, text="Expenses Change:")
ent_expenses_change = tk.Entry(master=frm_entry, width=10)
lbl_expenses_change_cur = tk.Label(master=frm_entry, text="%")
ent_expenses_change.insert(0, '0')

lbl_expenses_change.grid(row=1, column=3, sticky="w")
ent_expenses_change.grid(row=1, column=4, sticky="e")
lbl_expenses_change_cur.grid(row=1, column=5, sticky="w")

## Interest
lbl_interest = tk.Label(master=frm_entry, text="Interest:")
ent_interest = tk.Entry(master=frm_entry, width=10)
lbl_interest_cur = tk.Label(master=frm_entry, text="%")
ent_interest.insert(0, '6')
lbl_interest.grid(row=0, column=6, sticky="w")
ent_interest.grid(row=0, column=7, sticky="e")
lbl_interest_cur.grid(row=0, column=8, sticky="w")

## SWR
lbl_swr = tk.Label(master=frm_entry, text="SWR:")
ent_swr = tk.Entry(master=frm_entry, width=10)
lbl_swr_cur = tk.Label(master=frm_entry, text="%")
ent_swr.insert(0, '4')

lbl_swr.grid(row=1, column=6, sticky="w")
ent_swr.grid(row=1, column=7, sticky="e")
lbl_swr_cur.grid(row=1, column=8, sticky="w")

## Taxrate
lbl_taxrate = tk.Label(master=frm_entry, text="Taxrate:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="%")
ent_taxrate.insert(0, '0')

lbl_taxrate.grid(row=2, column=6, sticky="w")
ent_taxrate.grid(row=2, column=7, sticky="e")
lbl_taxrate_cur.grid(row=2, column=8, sticky="w")

#Calculate Button
btn_calculate = tk.Button(
    master=window,
    text="Calculate",
    command=fire
)

# Result
## Text
lbl_result = tk.Label(master=window)
frm_entry.grid(row=0, column=0, padx=10)
btn_calculate.grid(row=1, column=0, pady=10)
lbl_result.grid(row=2, column=0, padx=10)

#Run
window.mainloop()
