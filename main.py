from tkinter import *
from tkinter import messagebox
import sensor_gathering_data as sgd
import geocoding as gc
from pathlib import Path
def clear():
    thresh_input.delete(0, END)
    max_input.delete(0, END)
    loc_input.delete(0, END)
    ran_input.delete(0, END)
def inst():
    file = Toplevel(window)
    configfile = Text(file)
    configfile.grid(row = 0, column = 1, sticky = N+S+E+W)

    file.rowconfigure(0, weight=1)
    file.columnconfigure(1, weight=1)

    with open("previous_api_call.txt", 'r') as f:
        configfile.insert(INSERT, f.read())
    configfile.config(state = DISABLED)

def error_handler():
    x = [thresh_input.get(),max_input.get(),loc_input.get(),ran_input.get()]


    if thresh_input.get() == '' or isinstance(thresh_input.get(), (int, float)):
        messagebox.showwarning("AQI Error", "Please enter a valid integer.")
    elif max_input.get() == '' or isinstance(max_input.get(), (int, float)):
        messagebox.showwarning("Max Outputs Error", "Please enter a valid integer.")
    elif loc_input.get() == '':
        messagebox.showwarning("Location Error", "Please enter a location.")
    elif ran_input.get() == '' or isinstance(ran_input.get(), (int, float)):
        messagebox.showwarning("Range Error", "Please enter a valid integer.")
    else: return True

def file_existence(path):
    s = r'{}'.format(path)
    x = Path(s)
    if x.exists():
        try:
            test = sgd.Sensors()
            test.add_file(s)
            test.collect_data(api = False)
        except:
            return False
        return True
    else:
        return False

def file_or_api_chooser():
    def ender():
        file_or_api = fi_inp.get()

        if file_or_api != '':
            if file_existence(file_or_api):
                file.destroy()
                runner(aqi_threshold, max_outputs, location, ranger, file=file_or_api)
            else:
                messagebox.showwarning("File Error", "Please enter a valid file.")
        else:
            file.destroy()
            runner(aqi_threshold, max_outputs, location, ranger)

    aqi_threshold = thresh_input.get()
    max_outputs = max_input.get()
    location = loc_input.get()
    ranger = ran_input.get()

    if error_handler():
        thresh_input.config(state=DISABLED)
        max_input.config(state=DISABLED)
        loc_input.config(state=DISABLED)
        ran_input.config(state=DISABLED)

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.config(state=DISABLED)

        file = Toplevel(window)
        fi = Label(file, text="Input a File Path to Retrieve Data from a previous call to the PurpleAir API.\nLeave blank to use the API.")
        fi_inp = Entry(file)
        fi.pack()
        fi_inp.pack()
        enter = Button(file, text="Enter to Continue", command=ender)
        enter.pack()

def runner(thresh, max, location, ranger, file = None):
    all = sgd.Sensors()
    geo = gc.Geocode()
    geo.add_location(location)
    coords = geo.get_coords()
    all.add_coords(int(coords[0]),int(coords[1]))
    try:
        if file != None:
            all.add_file(file)

            all.collect_data(api=False)
            info = all.sorted_sensor_list(all.data, int(ranger), int(thresh))

            geo.add_sensors(info)
            final_lst = geo.get_locations(int(max))
        else:
            all.collect_data()
            info = all.sorted_sensor_list(all.data, int(ranger), int(thresh))
            geo.add_sensors(info)
            final_lst = geo.get_locations(int(max))

        display.config(state=NORMAL)

        if len(final_lst) == 0:
            display.insert(INSERT, "No areas matched your criteria, please try again" + '\n\n')
        for i in final_lst:
            codex = f"AQI Value: {i[2]}\nLat/Lon: ({i[0]},{i[1]})\nLocation: {i[3]}"
            display.insert(INSERT, str(codex)+'\n\n')
        display.config(state=DISABLED)
        thresh_input.config(state=NORMAL)
        max_input.config(state=NORMAL)
        loc_input.config(state=NORMAL)
        ran_input.config(state=NORMAL)
    except:
        messagebox.showwarning("API Error", "Please try again later. A problem occured when accessing the API servers.")
        display.config(state=DISABLED)
        thresh_input.config(state=NORMAL)
        max_input.config(state=NORMAL)
        loc_input.config(state=NORMAL)
        ran_input.config(state=NORMAL)

window = Tk()
window.geometry("600x800")
window.title("Air Quality Index Calculator")
#Variables that will be used in the program aspect
aqi_or_file = None


framer = LabelFrame(window,text = "Options")
framer.grid(column = 0, row = 0, sticky = NW)

loc = Label(framer, text = "Location")
loc_input = Entry(framer)
loc.grid(row = 1 , column = 0)
loc_input.grid(row = 1 , column = 1)

thresh = Label(framer, text = "Minimum AQI")
thresh_input = Entry(framer)
thresh.grid(row = 2 , column = 0)
thresh_input.grid(row = 2 , column = 1)


ran = Label(framer, text = "Range (In Miles)")
ran_input = Entry(framer)
ran.grid(row = 3 , column = 0)
ran_input.grid(row = 3 , column = 1)


max_o = Label(framer, text = "Max Outputs")
max_input = Entry(framer)
max_o.grid(row = 4 , column = 0)
max_input.grid(row = 4 , column = 1)


display = Text(window, state = DISABLED)
display.grid(row = 0, column = 1,sticky = N + S + E + W)

window.rowconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
v=Scrollbar(window, orient='vertical')
v.grid(row = 0, column = 2,sticky = E)

display.config(yscrollcommand=v.set)
v.config(command=display.yview)

start = Button(framer, text = "Start",command = file_or_api_chooser)
start.grid(row = 5, column = 0, sticky = W)

clear = Button(framer, text = "Clear",command = clear)
clear.grid(row = 5, column = 1, sticky = W)

help = Button(framer, text = "Instructions", command = inst)
help.grid(row = 5, column = 2, sticky = E)


window.mainloop()

