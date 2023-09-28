import math
import random
import os
rack_vector = []
signal_vector = []

def link_for_alfresco(rack_name,sase): 
    file_path = f"SASE{sase}/Datacards/alfresco.txt"
    link = ""
    with open(file_path, "r") as file:
            data_card = file.read()
    lines = data_card.split('\n')
    for line in lines:
        if rack_name in line:
            i=lines.index(line) 
            link = lines[i+1]
    return link

def colour_of_sase (sase):
    a = ""
    if sase == 1: 
        a = "#c3d2e9"
    if sase == 2: 
        a = "#e9d2c8"
    if sase == 3: 
        a = "#c8dac8"
    
    return (a)


def scene_overview (rack_name,device_vectors,info):
    print ("##########################################################################")
    print ("/////////////////////////////Device with signals//////////////////////////")
    print ("##########################################################################")
    rack_vector=[]
    for device in device_vectors:
        if device[5] != "0":
            signal_vector = [rack_name,device[2],device[4],device[5],device[6],info[1]]
            if device[6] != "yes":
                signal_vector.append(device[7])
                signal_vector.append(device[8])
                signal_vector.append(device[9])
                signal_vector.append(device[10])
                try: 
                    signal_vector.append(device[11])
                    print (f"for {device[2]} signals are written")
                except:
                    print (f"for {device[2]} signals are written")
            else: 
                print (f"for {device[2]} signals are written")
            rack_vector.append(signal_vector)
    if rack_vector == []:       
         signal_vector = [rack_name,"no_print"]  
         rack_vector.append(signal_vector)
    return(rack_vector)            
def scene_maker(sase_vector,b,sase,version):
    if os.path.exists(f"SASE{sase}/Scene/{version}"):
        name_of_scene = f"SASE{sase}/Scene/{version}/SASE{sase}"+"_OVERVIEW_RACK_MONITOR.svg"
    else:
        os.mkdir(f"SASE{sase}/Scene/{version}/")
        name_of_scene = f"SASE{sase}/Scene/{version}/SASE{sase}"+"_OVERVIEW_RACK_MONITOR.svg"
    uuid = random.randint(101, 999) #uniqe number of scene, which is used in uuid number 
    file = open(name_of_scene, "w")

    number_of_racks = len (sase_vector)
    layers = math.ceil (number_of_racks/8)
    size_of_scene_x = 1860
    
    number_of_racks_in_line = 8 
    height_of_the_logo = 71
    bufer = 35 
    size_of_crate_x = ((size_of_scene_x -(number_of_racks_in_line-1)*12)/number_of_racks_in_line)
    max_num = 0

    for rack in sase_vector:
        if len(rack)> max_num:
            max_num = len(rack) 
    size_of_crate_y = 20*max_num + (max_num-1)*10 +35
    size_of_scene_y = bufer*(1+layers) + height_of_the_logo + size_of_crate_y*layers 
    #making of karabo-scene file. uuid is used here:
    file.write(f"<svg:svg xmlns:krb=\"http://karabo.eu/scene\" xmlns:svg=\"http://www.w3.org/2000/svg\" krb:version=\"2\" krb:uuid=\"{uuid}b5d4e-273b-4460-bba3-11a99d8ddbdc\" height=\"{size_of_scene_y}\" width=\"{size_of_scene_x}\">")
    #head with logo and name of SASE and RACK :
    file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"{colour_of_sase(sase)}\" fill-opacity=\"1.0\" x=\"35\" y=\"17.5\" width=\"{745}\" height=\"{height_of_the_logo}\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"120\" y=\"25\" width=\"600\" height=\"60\" krb:text=\"               SASE{sase}      RACK MONITOR\" krb:font=\"Source Sans Pro,25,-1,5,75,0,0,0,0,0\" krb:foreground=\"#000000\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
    #XFEL LABEL : 
    file.write(f"<svg:g krb:class=\"FixedLayout\" krb:x=\"47\" krb:y=\"25\" krb:height=\"30\" krb:width=\"30\">")
    file.write("<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x=\"47\" y=\"25\" width=\"55\" height=\"57\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"49\" y=\"45\" width=\"60\" height=\"22\" krb:text=\"European\" krb:font=\"Source Sans Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"#000000\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"50\" y=\"54\" width=\"59\" height=\"34\" krb:text=\"XFEL\" krb:font=\"Source Sans Pro,16,-1,5,63,0,0,0,0,0\" krb:foreground=\"#000000\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
    file.write(f"<svg:rect stroke=\"#3a005a\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#3a005a\" fill-opacity=\"1.0\" x=\"79\" y=\"28\" width=\"12\" height=\"3\" />")
    file.write(f"<svg:rect stroke=\"#3a005a\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#3a005a\" fill-opacity=\"1.0\" x=\"49\" y=\"28\" width=\"28\" height=\"3\" />")
    file.write(f"<svg:rect stroke=\"#ffaa00\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#ffaa00\" fill-opacity=\"1.0\" x=\"93\" y=\"28\" width=\"5\" height=\"3\" />")
    file.write(f"</svg:g>")
   
       #construction of legend 
    legend_x = 780 + 45
    legend_y = 6
    legend_width = 900
    legend_height = 94

    file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x=\"{legend_x}\" y=\"{legend_y}\" width=\"{legend_width}\" height=\"{legend_height}\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x + 20}\" y=\"{legend_y+10}\" width=\"98\" height=\"43\" krb:text=\"Legend\" krb:font=\"Source Code Pro,16,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"2\" krb:background=\"transparent\" />")   
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160}\" y=\"{legend_y + 5}\" width=\"200\" height=\"20\" krb:text=\"G - Gauge Controller \" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")   
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160}\" y=\"{legend_y+20}\" width=\"200\" height=\"20\" krb:text=\"I - Ion Pump Controller \" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160}\" y=\"{legend_y+35}\" width=\"200\" height=\"20\" krb:text=\"V - Vacuum crate \" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160 + 200}\" y=\"{legend_y+5}\" width=\"200\" height=\"20\" krb:text=\"M - Motion crate \" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160 +200}\" y=\"{legend_y+20}\" width=\"200\" height=\"20\" krb:text=\"E - EPS crate\" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160+200}\" y=\"{legend_y+35}\" width=\"200\" height=\"20\" krb:text=\"F - Fast Valve Controller\" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+160+400}\" y=\"{legend_y+5}\" width=\"200\" height=\"20\" krb:text=\"4U - Size of crate\" krb:font=\"Source Sans Pro,12,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />") 
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x + 10}\" y=\"{legend_y + 50}\" width=\"841\" height=\"30\" krb:text=\"The only devices present in this scene are the ones transmitting the signal to the KARABO.\" krb:font=\"Source Sans Pro,12,-1,5,75,1,0,0,0,0\" krb:foreground=\"#123bc2\" krb:frameWidth=\"0\" krb:background=\"transparent\" />") 
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x + 10}\" y=\"{legend_y + 65}\" width=\"841\" height=\"30\" krb:text=\"To view all devices in the rack, open the individual rack scene.\" krb:font=\"Source Sans Pro,12,-1,5,75,1,0,0,0,0\" krb:foreground=\"#123bc2\" krb:frameWidth=\"0\" krb:background=\"transparent\" />") 
    eplan_in_alfresco = link_for_alfresco ("EPLAN",sase)
 #   eplan_in_alfresco = "https://docs.xfel.eu/share/page/site/vacuum/document-details?nodeRef=workspace://SpacesStore/03280f8f-5f35-45e5-ab0d-45e4d9efe4f6"
    file.write (f"<svg:rect krb:class=\"WebLink\" x=\"{legend_x + 720}\" y=\"{legend_y +10}\" width=\"130\" height=\"{height_of_the_logo}\" krb:target=\"{eplan_in_alfresco}\" krb:text=\"Eplan for rack\" krb:font=\"Source Sans Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"3\" krb:background=\"transparent\" krb:alignh=\"4\" />")
   
    number_of_line = 1
    i =0
    y = 0
    #calculation of rack's coordinates 

    for rack in sase_vector:
        name = str(rack[0][0])
        name_of_rack_mode = name[:1] + "." + name[1:]
        rack_x = 35 + (sase_vector.index(rack) - (number_of_line-1)*8)*(12+size_of_crate_x)
        rack_y = 35 + height_of_the_logo + (number_of_line-1)*(24+size_of_crate_y)
        i +=1 
        y +=1
        
        if (i % 8) == 0:
            number_of_line +=1
        

        #rack box :
        file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#dee6f0\" x=\"{rack_x}\" y=\"{rack_y}\" width=\"{size_of_crate_x}\" height=\"{size_of_crate_y}\" />")
        #link to the small rack monitor (need to be changed) :
        file.write(f"<svg:rect krb:class=\"SceneLink\" x=\"{rack_x}\" y=\"{rack_y}\" width=\"{size_of_crate_x}\" height=\"30\" krb:background=\"transparent\" krb:text=\"\" krb:font=\"Source Sans Pro,10,-1,5,50,0,0,0,0,0\" krb:foreground=\"\" krb:target=\"{b[y-1]}\" krb:frameWidth=\"1\" krb:target_window=\"dialog\" />")
        # lines inside of the rack box (dashed lines)
        file.write (f"<svg:line stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"4.0 2.0 1.0 2.0\" stroke-style=\"4\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x1=\"{rack_x}\" y1=\"{rack_y+30}\" x2=\"{rack_x+size_of_crate_x}\" y2=\"{rack_y+30}\" />")
        file.write (f"<svg:line stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"4.0 2.0 1.0 2.0\" stroke-style=\"4\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x1=\"{rack_x+100}\" y1=\"{rack_y+30}\" x2=\"{rack_x+100}\" y2=\"{rack_y+size_of_crate_y}\" />")
        #name of the rack on the top of the box :
        file.write(f"<svg:rect krb:class=\"Label\" x=\"{rack_x+60}\" y=\"{rack_y +5}\" width=\"280\" height=\"20\" krb:text=\"RACK {name_of_rack_mode}\" krb:font=\"Source Serif Pro,15,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />") 
        #caclulation of shift between the names of the crate in one rack. if there are a lot of crates inside one rack, more complicated formula was implemented 
        if rack[0][1] != "no_print":
            for device in rack:
                if len(rack)>7:
                    shift = (size_of_crate_y - 40 - 20*len(rack))/(len(rack))
                else: 
                    shift = 10
            #signals for crates with a four signal:
                if device[3] == "4":
                    #for four standart signals 
                    if device[4] == "yes":
                        rack_name = device[0]
                        name_of_xtd = device[5]
                        shift_lamp = (size_of_crate_x - 100 -80)/5 #shift between the lamps 
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{device[1]}_T1OK.state\" x=\"{rack_x + +100 + shift_lamp}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{device[1]}_T2OK.state\" x=\"{rack_x + 2*shift_lamp +120}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{device[1]}_T3BALOK.state\" x=\"{rack_x + 3*shift_lamp +140}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{device[1]}_T3REDOK.state\" x=\"{rack_x + 4*shift_lamp +160}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"DisplayStateColor\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_{device[2]}/MONITOR/{device[1]}.state\" x=\"{rack_x+5}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"90\" height=\"20\" krb:show_string=\"false\" />")   
                    #for four not standart signals (which are extra written in the datacard)
                    else:
                        rack_name = device[0]
                        name_of_xtd = device[5]
                        shift_lamp = (size_of_crate_x - 100 -80)/5 #shift between the lamps 
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[6]}.state\" x=\"{rack_x + +100 + shift_lamp}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[7]}.state\" x=\"{rack_x + 2*shift_lamp +120}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[8]}.state\" x=\"{rack_x + 3*shift_lamp +140}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[9]}.state\" x=\"{rack_x + 4*shift_lamp +160}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"DisplayStateColor\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_{device[2]}/MONITOR/{device[1]}.state\" x=\"{rack_x+5}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"90\" height=\"20\" krb:show_string=\"false\" />")   
            #signals for crates with a five signal:           
                if device[3] == "5":
                        rack_name = device[0]
                        name_of_xtd = device[5]
                        shift_lamp = (size_of_crate_x - 100 -100)/6
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[6]}.state\" x=\"{rack_x + +100 + shift_lamp}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[7]}.state\" x=\"{rack_x + 2*shift_lamp +120}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[8]}.state\" x=\"{rack_x + 3*shift_lamp +140}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[9]}.state\" x=\"{rack_x + 4*shift_lamp +160}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[10]}.state\" x=\"{rack_x + 5*shift_lamp +180}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")
                        file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"DisplayStateColor\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_{device[2]}/MONITOR/{device[1]}.state\" x=\"{rack_x+5}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"90\" height=\"20\" krb:show_string=\"false\" />")   
            #signals for IPUMP and FAST VALVE Controllers with a four signal:   
                if device[3] == "1":

                        rack_name = device[0]
                        name_of_xtd = device[5]
                        shift_lamp = (size_of_crate_x - 120 )/2
                        #for IPUMP just one "state" signal 
                        if device[4] == "IPUMP_CONTR":
                                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{rack_name[:1]}_XTD{name_of_xtd}_VAC/ICTRL/{device[1]}.state\" x=\"{rack_x + 100 + shift_lamp}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")       
                        if device[4] == "FASTVALVE_CONTR":
                                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[6]}.state\" x=\"{rack_x + 100 + shift_lamp}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"20\" height=\"20\" />")   
                                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"DisplayStateColor\" krb:keys=\"{device[6]}.state\" x=\"{rack_x+5}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"90\" height=\"20\" krb:show_string=\"false\" />")
                #name of the crate or controller 
                file.write(f"<svg:rect krb:class=\"Label\" x=\"{rack_x+10}\" y=\"{rack_y + 40 + shift*(rack.index(device)) + rack.index(device)*20}\" width=\"95\" height=\"20\" krb:text=\"{device[1]}\" krb:font=\"Source Serif Pro,13,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")   


#end of the file
    file.write("</svg:svg>")
    file.close()