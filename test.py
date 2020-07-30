import tkinter as tk
gui = tk.Tk()
gui.geometry('600x480')
gui.title('Hex & RGB to RGB %')

rgbLabel = tk.Label(gui, text='Enter RGB')
rgbLabel.pack()

# r = tk.Entry(gui)
# g= tk.Entry(gui)
# b= tk.Entry(gui)

rgbEntryValues = {'R': tk.Entry(gui), 'G': tk.Entry(gui), 'B': tk.Entry(gui)}
for entry in rgbEntryValues:
    rgbEntryValues[entry].pack()
    

rgbLabelValues = {
    'R': tk.StringVar(gui),
    'G': tk.StringVar(gui),
    'B': tk.StringVar(gui),
}

for value in rgbLabelValues:
    label = tk.Label(gui, textvariable=rgbLabelValues[value])
    label.pack()

def run():
    for value in rgbLabelValues:
        text = '{}'.format(rgbEntryValues[value].get())
        rgbLabelValues[value].set(text)

run()

update = tk.Button(gui, text='Update', command=run)
update.pack()
gui.mainloop()