import small_rack
import datacard_reader 
import overview_maker
import PySimpleGUI as sg
import re
import hashlib
import os
sg.theme('Default1')   # Add a touch of color
# All the stuff inside your window.
layout = [              [sg.Text(text = "--------------------------------------------", font=('Arial', 40), justification='center')],
            [sg.Text(text='Rack Monitor Maker', font=('Arial Bold', 30),
                size=20, expand_x=True,
                 justification='center')],
            [sg.Image('XFEL.png',expand_x=True, expand_y=True)],
            [sg.Text(text = "--------------------------------------------", font=('Arial', 40), justification='center')],
            [sg.Text(text = "", font=('Arial', 12),)],
            [sg.Text(text ='Choose a SASE:                      ', font=('Arial Bold', 15),), 
            sg.Listbox (values = ["SASE1","SASE2","SASE3"], font=('Arial', 12), size = (30,3),)  ],
            [sg.Text(text = "", font=('Arial', 12),)],
            [sg.Text(text = 'What is needed to be made?', font=('Arial Bold', 15),) ,
            sg.Listbox (values = ['Small rack monitor',"Overview Monitor",'Small + Overview monitors'], font=('Arial', 12), size = (30,3),) ],
            [sg.Text(text = "", font=('Arial', 12),)],
            [sg.Text(text = "Name of RACKs:", font=('Arial Bold', 15),)],
            [sg.Text(text = "---->If you need to make scenes for racks 1.01, 1.02, 1.03, than it is needed to be written: 101,102,103", font=('Arial', 12),)],
            [sg.Text(text = "---->Datacards should be in the folder /SASE1/Datacards/ in the format 101.txt", font=('Arial', 12),)],
            [sg.Input(key='RACKs', size = (40,60), font = ('Arial', 12), justification='center')],
            [sg.Text(text = "", font=('Arial', 12),)],
            [sg.Text(text = "Version:", font=('Arial Bold', 15),)],
            [sg.Input(key='version', size = (40,60), font = ('Arial', 12), justification='center')],
            [sg.Text(text = "", font=('Arial', 12),)],
            [sg.Submit(),sg.Cancel()] ]
sase = 0
mode = 0
# Create the Window
window = sg.Window('RACK MONITOR', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    text = values[1][0]
    if event =='Submit':
        if text == str('SASE1'):
            sase = int("1")
        if values[1][0] == 'SASE2':
            sase = int("2")
        if values[1][0] == 'SASE3':
            sase = int("3")
        if values[2][0] == "Small rack monitor":
            mode = 1
        if values[2][0] == "Overview Monitor":
            mode = 2
        if values[2][0] == "Small + Overview monitors":
            mode = 3
        if values["RACKs"]!="all":  
            numbers = values["RACKs"].split(',')
        else: 
            files = os.listdir(path=f"SASE{sase}\Datacards") 
            numbers = []
            for datacard in files:
                if "RACK" in datacard:
                    start_index = datacard.index("RACK") + len("RACK")
                    end_index = datacard.index(".txt")
                    numbers.append(datacard[start_index:end_index])
        numbers.sort()
        version = values["version"]
        break
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()
sase_vector = []
link_for_rack = []
for rack_name in numbers:
    #reading the datacards from the list: 
    device_vectors, rack_vector, device_with_info = datacard_reader.reader_data_cards(rack_name,sase)
    # check, if there are two or more devices with one position 
    grouped_vectors = datacard_reader.group_devices_by_position(device_vectors)
    print ("##########################################################################")
    print ("/////////////////////////////Rack",rack_name,"/////////////////////////////")
    print ("##########################################################################")
    for device in device_vectors: 
        print (device) 
    print ("/////////////////////////////////////////////////////////////////////////")
    print ("/////////////////////////////Double devices//////////////////////////////")
    print ("/////////////////////////","                      ","////////////////////////")
    for group in grouped_vectors: 
        group[2].sort()
        print ("/////////////////////////",group[2],"////////////////////////") 
    # making a small rack monitors for all rack in the list + links for a overview monitor     
    
    link_for_rack = small_rack.make_scene(device_vectors, rack_vector,grouped_vectors,link_for_rack,device_with_info, sase, mode, version)
    # maiking a list of devices which has a signal
    if (mode == 2) or (mode ==3):
        sase_vector.append(overview_maker.scene_overview (rack_name,device_vectors,rack_vector))
 # maiking an overview scene 
if (mode == 2) or (mode == 3):
    overview_maker.scene_maker(sase_vector,link_for_rack,sase,version)
print ("##########################################################################")
print ("///////////////////////////////////DONE///////////////////////////////////")
print ("##########################################################################")

