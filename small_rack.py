import random
import os


def link_for_alfresco(rack_name): 
    file_path = f"SASE1/Datacards/alfresco.txt"
    link = ""
    with open(file_path, "r") as file:
            data_card = file.read()
    lines = data_card.split('\n')
    for line in lines:
        if rack_name in line:
            i=lines.index(line) 
            link = lines[i+1]
    return link


def colour_of_crates (n,l):
    a = ""
    if (n != 0) or (l!=""): 
        a = "#f8e8d9"
    else:
        a = "#dae3c0"

    return (a)

def make_scene(device_vectors, rack_vector, grouped_vectors,link_for_rack,device_with_info, sase,mode,version):
    cool_name = ['c','o','o','l','i','n','g',' ','u','n','i','t']
    name_of_rack = rack_vector[0]
    name_of_rack_mode = name_of_rack[:1] + "." + name_of_rack[1:]
    name_of_xtd = rack_vector[1]
    name_of_sase = "SASE"+f"{sase}"
    if os.path.exists(f"SASE1/Scene/{version}"):
        name_of_scene = f"SASE{sase}/Scene/{version}/RACK{name_of_rack}"+".svg"
    else:
        os.mkdir(f"SASE{sase}/Scene/{version}/")
        name_of_scene = f"SASE{sase}/Scene/{version}/RACK{name_of_rack}"+".svg"
    uuid = random.randint(101, 999) #uniqe number of scene, which is used in uuid number 

    file = open(name_of_scene, "w")
    #calculation of size. all sizes in px
    width_of_the_module = 300 
    width_of_the_cool_module = 30 #cooling module between the modules
    height_of_the_slot = 23 #slot in rack 
    height_of_the_logo = 71
    height_of_the_free_space = 100 
    width_of_the_free_space = 200
    number_of_modules = int(rack_vector[2])
    number_of_slots = int(rack_vector[3])
    position_of_cool_module = int(rack_vector[4])
    height_of_the_module = height_of_the_slot * number_of_slots
    height_of_the_scene = number_of_slots * height_of_the_slot + height_of_the_logo + height_of_the_free_space 
    width_of_the_scene = number_of_modules * width_of_the_module + width_of_the_cool_module + width_of_the_free_space 
    width_of_the_logo = width_of_the_scene -60
    link_for_rack.append (f"RACK{name_of_rack}:{uuid}b5d4e-{uuid}b-4460-bba3-11a99d8ddbdc")
    file.write(f"<svg:svg xmlns:krb=\"http://karabo.eu/scene\" xmlns:svg=\"http://www.w3.org/2000/svg\" krb:version=\"2\" krb:uuid=\"{uuid}b5d4e-{uuid}b-4460-bba3-11a99d8ddbdc\" height=\"{height_of_the_scene}\" width=\"{width_of_the_scene}\">")
    #head with logo and name of SASE and RACK 
    file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#c3d2e9\" fill-opacity=\"1.0\" x=\"35\" y=\"17.5\" width=\"{width_of_the_logo}\" height=\"{height_of_the_logo}\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"120\" y=\"25\" width=\"400\" height=\"60\" krb:text=\"{name_of_sase}            RACK {name_of_rack_mode}\" krb:font=\"Source Sans Pro,25,-1,5,75,0,0,0,0,0\" krb:foreground=\"#000000\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
    #XFEL LABEL 
    file.write(f"<svg:g krb:class=\"FixedLayout\" krb:x=\"47\" krb:y=\"25\" krb:height=\"30\" krb:width=\"30\">")
    file.write("<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x=\"47\" y=\"25\" width=\"55\" height=\"57\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"49\" y=\"45\" width=\"60\" height=\"22\" krb:text=\"European\" krb:font=\"Source Sans Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"#000000\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"50\" y=\"54\" width=\"59\" height=\"34\" krb:text=\"XFEL\" krb:font=\"Source Sans Pro,16,-1,5,63,0,0,0,0,0\" krb:foreground=\"#000000\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
    file.write(f"<svg:rect stroke=\"#3a005a\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#3a005a\" fill-opacity=\"1.0\" x=\"79\" y=\"28\" width=\"12\" height=\"3\" />")
    file.write(f"<svg:rect stroke=\"#3a005a\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#3a005a\" fill-opacity=\"1.0\" x=\"49\" y=\"28\" width=\"28\" height=\"3\" />")
    file.write(f"<svg:rect stroke=\"#ffaa00\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#ffaa00\" fill-opacity=\"1.0\" x=\"93\" y=\"28\" width=\"5\" height=\"3\" />")
    file.write(f"</svg:g>")
    #contruction of modules and slots 
    l = 0
    for i in range (number_of_modules):
        if i >=position_of_cool_module:
            shift_mod = width_of_the_cool_module
        else: 
            shift_mod = 0  
        x_module = 35 + shift_mod + width_of_the_module*i
        y_module = 35 + height_of_the_logo
        file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#dee6f0\" x=\"{x_module}\" y=\"{y_module}\" width=\"{width_of_the_module}\" height=\"{height_of_the_module}\" />")
        for j in range (number_of_slots-1):
            x_slot_1 = x_module
            x_slot_2 = x_module + width_of_the_module 
            y_slot = y_module + (j+1) * height_of_the_slot
            file.write (f"<svg:line stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"4.0 2.0 1.0 2.0\" stroke-style=\"4\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x1=\"{x_slot_1}\" y1=\"{y_slot}\" x2=\"{x_slot_2}\" y2=\"{y_slot}\" />")
            if i == 0: 
                file.write(f"<svg:rect krb:class=\"Label\" x=\"10\" y=\"{y_slot-height_of_the_slot+5}\" width=\"30\" height=\"20\" krb:text=\"{j+1}\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
                if j == number_of_slots-2:
                    file.write(f"<svg:rect krb:class=\"Label\" x=\"10\" y=\"{y_slot+5}\" width=\"30\" height=\"20\" krb:text=\"{number_of_slots}\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
                if j == round(0.25*number_of_slots):
                    for p in cool_name: 
                        file.write(f"<svg:rect krb:class=\"Label\" x=\"{48+width_of_the_module*position_of_cool_module}\" y=\"{y_slot+height_of_the_slot*l}\" width=\"30\" height=\"20\" krb:text=\"{p}\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
                        l = l + 1
    #construction of legend 
    legend_x = width_of_the_cool_module + width_of_the_module*number_of_modules + 45 
    legend_y = 35 + height_of_the_logo
    legend_width = 130 
    legend_height = 210

    file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"none\" x=\"{legend_x}\" y=\"{legend_y}\" width=\"{legend_width}\" height=\"{legend_height}\" />")
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x}\" y=\"{legend_y}\" width=\"130\" height=\"40\" krb:text=\"Legend\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"3\" krb:background=\"transparent\" krb:alignh=\"4\"  />")   
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+40}\" width=\"130\" height=\"20\" krb:text=\"G - Gauge Controller \" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")   
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+60}\" width=\"130\" height=\"20\" krb:text=\"I - Ion Pump Controller \" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+80}\" width=\"130\" height=\"20\" krb:text=\"V - Vacuum crate \" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+100}\" width=\"130\" height=\"20\" krb:text=\"M - Motion crate \" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+120}\" width=\"130\" height=\"20\" krb:text=\"E - EPS crate\" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+140}\" width=\"130\" height=\"20\" krb:text=\"F - Fast Valve Controller\" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")  
    file.write(f"<svg:rect krb:class=\"Label\" x=\"{legend_x+5}\" y=\"{legend_y+160}\" width=\"130\" height=\"20\" krb:text=\"4U - Size of crate\" krb:font=\"Source Serif Pro,8,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />") 
    link_in_alfresco = link_for_alfresco ("RACK"+f"{name_of_rack}")
    file.write (f"<svg:rect krb:class=\"WebLink\" x=\"{legend_x}\" y=\"{legend_y + legend_height + 10}\" width=\"{legend_width}\" height=\"50\" krb:target=\"{link_in_alfresco}\" krb:text=\"Photo of rack\" krb:font=\"Source Sans Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"3\" krb:background=\"transparent\" krb:alignh=\"4\" />")
    eplan_in_alfresco = "https://docs.xfel.eu/share/page/site/vacuum/document-details?nodeRef=workspace://SpacesStore/03280f8f-5f35-45e5-ab0d-45e4d9efe4f6"
    file.write (f"<svg:rect krb:class=\"WebLink\" x=\"{legend_x}\" y=\"{legend_y + legend_height + 70}\" width=\"{legend_width}\" height=\"50\" krb:target=\"{eplan_in_alfresco}\" krb:text=\"Eplan for rack\" krb:font=\"Source Sans Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"3\" krb:background=\"transparent\" krb:alignh=\"4\" />")
    #construction of cooling module 
   
    file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"#dee6f0\" x=\"{35+width_of_the_module*position_of_cool_module}\" y=\"{y_module}\" width=\"{width_of_the_cool_module}\" height=\"{height_of_the_module}\" />")

    #construction of crates 
    for device in device_vectors: 
        number_of_module = int(device[0])
        position_of_device = int(device[1])
        name_of_device = device[2]
        size_of_device = int(device[3])
        loop_of_device = device[4]
        number_of_signals = int(device[5])
        colour_of_crate = colour_of_crates (number_of_signals,loop_of_device)
        if number_of_module > position_of_cool_module:
            shift_cr = width_of_the_cool_module
        else: 
            shift_cr = 0  
        x_crate = 35 + shift_cr +width_of_the_module*(number_of_module-1)
        y_crate = 35 + height_of_the_logo + (position_of_device-1)*height_of_the_slot
        height_of_the_crate = height_of_the_slot * size_of_device
        #check for the 2 or 3 deivice in one slot space 
        double = "no"
        shift_x = 0
        for group in grouped_vectors:
            for p in group[2]:
             if (number_of_module == int(group [0]) and position_of_device == int(group[1]) and name_of_device in group[2]):
                    double = "yes"
                    best = group[2]
                    shift_x = (group[2].index(f"{name_of_device}"))*width_of_the_module/len(group[2])
                    if len(group[2]) == 2:
                        size_of_the_shrift = 7
                    if len(group[2]) == 3:
                         size_of_the_shrift = 5
        if double == "yes":
               file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"{colour_of_crate}\" x=\"{x_crate+shift_x}\" y=\"{y_crate}\" width=\"{width_of_the_module/len(best)}\" height=\"{height_of_the_crate}\" />")
               file.write(f"<svg:rect krb:class=\"Label\" x=\"{round(x_crate + shift_x + round(0.05*width_of_the_module/len(best)))}\" y=\"{y_crate + round(0.15*height_of_the_slot*size_of_device)}\" width=\"210\" height=\"20\" krb:text=\"{name_of_device}," ",{size_of_device}U\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
               if device[2] in device_with_info:
                    index1 = device_with_info.index(device[2])
                    file.write(f"<svg:rect krb:class=\"Label\" x=\"{round(x_crate + shift_x + round(0.05*width_of_the_module/len(best)))}\" y=\"{y_crate + round(0.15*height_of_the_slot*size_of_device)+20}\" width=\"280\" height=\"20\" krb:text=\"{device_with_info[index1+1]}\" krb:font=\"Source Serif Pro,9,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
                    device_with_info.remove(device_with_info[index1])
                    device_with_info.remove(device_with_info[index1])        
        else: 
                file.write(f"<svg:rect stroke=\"#000000\" stroke-opacity=\"1.0\" stroke-linecap=\"butt\" stroke-dashoffset=\"0.0\" stroke-width=\"1.0\" stroke-dasharray=\"\" stroke-style=\"1\" stroke-linejoin=\"miter\" stroke-miterlimit=\"4.0\" fill=\"{colour_of_crate}\" x=\"{x_crate}\" y=\"{y_crate}\" width=\"{width_of_the_module}\" height=\"{height_of_the_crate}\" />")
                file.write(f"<svg:rect krb:class=\"Label\" x=\"{round(x_crate + round(0.05*width_of_the_module))}\" y=\"{y_crate + round(0.15*height_of_the_slot*size_of_device)}\" width=\"280\" height=\"20\" krb:text=\"{name_of_device},{size_of_device}U\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
                if device[2] in device_with_info:
                    index1 = device_with_info.index(device[2])
                    file.write(f"<svg:rect krb:class=\"Label\" x=\"{round(x_crate + round(0.05*width_of_the_module))}\" y=\"{y_crate + round(0.15*height_of_the_slot*size_of_device)+20}\" width=\"280\" height=\"20\" krb:text=\"{device_with_info[index1+1]}\" krb:font=\"Source Serif Pro,11,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")
                    device_with_info.remove(device_with_info[index1])
                    device_with_info.remove(device_with_info[index1])
#signals 
         
        if number_of_signals == 4: 

            if device[6] == "no": 
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[7]}.state\" x=\"{x_crate + round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[8]}.state\" x=\"{x_crate + 40 + 2*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[9]}.state\" x=\"{x_crate + 80 + 3*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[10]}.state\" x=\"{x_crate + 120 +4*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot }\" width=\"40\" height=\"40\" />")
            else:
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{name_of_device}_T1OK.state\" x=\"{x_crate + round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{name_of_device}_T2OK.state\" x=\"{x_crate + 40 + 2*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{name_of_device}_T3BALOK.state\" x=\"{x_crate + 80 + 3*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_SYS/SWITCH/{name_of_device}_T3REDOK.state\" x=\"{x_crate + 120 +4*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot }\" width=\"40\" height=\"40\" />")
            x_lamp = x_crate +width_of_the_module - 2*height_of_the_slot 
            y_lamp = y_crate + 0.3*height_of_the_slot
            file.write(f"<svg:rect krb:class=\"Label\" x=\"{x_lamp - 50}\" y=\"{y_lamp +10}\" width=\"280\" height=\"20\" krb:text=\"OK:\" krb:font=\"Source Serif Pro,15,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")            
            file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_{loop_of_device}/MONITOR/{name_of_device}.state\" x=\"{x_lamp}\" y=\"{y_lamp}\" width=\"40\" height=\"40\" />")
        if number_of_signals == 5: 

            if device[6] == "no": 
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[7]}.state\" x=\"{x_crate + round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[8]}.state\" x=\"{x_crate + 40 + 2*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[9]}.state\" x=\"{x_crate + 80 + 3*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot}\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[10]}.state\" x=\"{x_crate + 120 +4*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot }\" width=\"40\" height=\"40\" />")
                file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[11]}.state\" x=\"{x_crate + 120 +4*round((width_of_the_module - number_of_signals*40)/(number_of_signals+1)) }\" y=\"{y_crate + height_of_the_crate - 2 * height_of_the_slot }\" width=\"40\" height=\"40\" />")
            x_lamp = x_crate +width_of_the_module - 2*height_of_the_slot 
            y_lamp = y_crate + 0.3*height_of_the_slot
            file.write(f"<svg:rect krb:class=\"Label\" x=\"{x_lamp - 50}\" y=\"{y_lamp +10}\" width=\"280\" height=\"20\" krb:text=\"OK:\" krb:font=\"Source Serif Pro,15,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")            
            file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_{loop_of_device}/MONITOR/{name_of_device}.state\" x=\"{x_lamp}\" y=\"{y_lamp}\" width=\"40\" height=\"40\" />")
        if device[6] == "IPUMP_CONTR":
            if double == "yes":
                index = best.index(name_of_device)
                lenlen = len(group[2])
                size_icon = 20 #for IPUMPS
                small_shift = (width_of_the_module/lenlen - 4*size_icon)/5 #for ION PUMPS 
                x_lamp = x_crate +(index+1)*width_of_the_module/lenlen - 2*height_of_the_slot
                y_lamp = y_crate + 0.3*height_of_the_slot
            else:
                size_icon = 20
                small_shift = (width_of_the_module*0.5 - 4*size_icon)/5
                x_lamp = x_crate +width_of_the_module - 2*height_of_the_slot 
                y_lamp = y_crate + 0.3*height_of_the_slot
             #lamps of the main signal    
            file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_{loop_of_device}/ICTRL/{name_of_device}.state\" x=\"{x_lamp}\" y=\"{y_lamp}\" width=\"40\" height=\"40\" />")
            #lamp of the ion pumps 
            for i in range (len(device)-4, len(device)):
                if double == "yes":
                  x_sig = x_crate+(index)*width_of_the_module/lenlen+small_shift*(i-6)+size_icon*(i-7)
                  y_sig = y_crate+height_of_the_crate-1.2*height_of_the_slot
                  x_chan = x_crate+(index)*width_of_the_module/lenlen+small_shift*(i-6)+size_icon*(i-7)+0.2*size_icon
                  y_chan = y_crate+height_of_the_crate-2*height_of_the_slot
                else:
                  x_sig = x_crate+small_shift*(i-6)+size_icon*(i-7)
                  y_sig = y_crate+height_of_the_crate-1.2*height_of_the_slot
                  x_chan = x_crate+small_shift*(i-6)+size_icon*(i-7)+0.2*size_icon
                  y_chan = y_crate+height_of_the_crate-2*height_of_the_slot                  
                if device[i] !="":
                    file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"StatefulIconWidget\" krb:keys=\"SA{name_of_rack[:1]}_XTD{name_of_xtd}_{loop_of_device}/IPUMP/{device[i]}.state\" x=\"{x_sig}\" y=\"{y_sig}\" width=\"{size_icon}\" height=\"{size_icon}\" krb:icon_name=\"icon_ion_pump\" />")
                    file.write(f"<svg:rect krb:class=\"Label\" x=\"{x_chan}\" y=\"{y_chan}\" width=\"40\" height=\"20\" krb:text=\"ch{i-6}\" krb:font=\"Source Serif Pro,9,-1,5,75,0,0,0,0,0\" krb:foreground=\"\" krb:frameWidth=\"0\" krb:background=\"transparent\" />")

        # fastvalve crate 
        if device[6] == "FASTVALVE_CONTR":
            if double == "yes":

                index = group[2].index(name_of_device)
                lenlen = len(group[2])
                size_icon = 40/(lenlen - 0.5) #for IPUMPS
                small_shift = (width_of_the_module/lenlen - 4*size_icon)/5 #for ION PUMPS 
                x_lamp = x_crate +(lenlen-index)*width_of_the_module/lenlen - 2*height_of_the_slot 
                y_lamp = y_crate + 0.3*height_of_the_slot
            else:
                size_icon = 40
                small_shift = (width_of_the_module - 4*size_icon)/5
                x_lamp = x_crate +width_of_the_module - 2*height_of_the_slot 
                y_lamp = y_crate + 0.3*height_of_the_slot
             #lamps of the main signal    
            file.write(f"<svg:rect krb:class=\"DisplayComponent\" krb:widget=\"Lamp\" krb:keys=\"{device[7]}.state\" x=\"{x_lamp}\" y=\"{y_lamp}\" width=\"40\" height=\"40\" />")
    
    #end of the file 
    file.write("</svg:svg>")
    file.close()
    if mode == 2:
        os.remove (name_of_scene)
    return(link_for_rack)


