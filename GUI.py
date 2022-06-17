import tkinter as tk

root = tk.Tk()

entries = []
j = 1
k = 0

for i in range(81):
    
    k += 1
    if i % 9 == 0 and i != 0:
        j += 22
        k = 1

    if i % 3 == 0:
        tk.Label(root, text = "||").place(x = k * 25, y = j)
        k += 1
    
    if i != 0 and i % 27 == 0:
        tk.Label(root, text = "----").place(x = k * 25, y = j)
        j += 10


    en = tk.Entry(root, width = 3)
    en.place(x = k * 25, y = j)
    entries.append(en)

print(len(entries))
root.mainloop()