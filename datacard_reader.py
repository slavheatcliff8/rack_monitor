import small_rack



def group_devices_by_position(device_vectors):
    position_module_dict = {}  # Словарь для хранения устройств по комбинации позиции и номера модуля
    for device_vector in device_vectors:
        module_number, position, *_ = device_vector  # Извлекаем номер модуля и позицию
        key = (module_number, position)  # Формируем ключ комбинации
        if key not in position_module_dict:
            position_module_dict[key] = set()  # Создаем пустое множество для данной комбинации
        position_module_dict[key].add(device_vector[2])  # Добавляем имя устройства в множество

    grouped_vectors = []  # Список для хранения сгруппированных векторов
    for key, devices in position_module_dict.items():
        if len(devices) > 1:  # Учитываем только комбинации с более чем одним устройством
            module_number, position = key
            grouped_vectors.append([module_number, position, list(devices)])  # Добавляем группированный вектор

    return grouped_vectors
# Создаем список для хранения данных векторов
def reader_data_cards(rack_name):
    file_path = f"SASE1/Datacards/RACK{rack_name}.txt"
    device_vectors = []

# Читаем данные из файла
    with open(file_path, "r") as file:
        data_card = file.read()

# Создаем список для хранения данных векторов
    device_vectors = []
    sg =[]

# Разделяем данные на строки
    lines = data_card.split('\n')
# Для счета количества устройств

# Переменные для хранения информации о рэке
    rack_number = ""
    module_count = ""
    slots_per_module = ""
    cooling_module_position = ""
    device_vector = []
    device_with_info = []
    standart = "yes"
# Проходимся по каждой строке
    for line in lines:

    # Извлекаем информацию о рэке
        if line.strip().startswith("|               Rack Number:"):
            rack_number = line.split("[")[1].split("]")[0].strip()
        if line.strip().startswith("|               XTD:"):
            xtd_number = line.split("[")[1].split("]")[0].strip()
        elif line.strip().startswith("|          Number of Modules:"):
            module_count = line.split("[")[1].split("]")[0].strip()
        elif line.strip().startswith("|         Slots per Module:"):
            slots_per_module = line.split("[")[1].split("]")[0].strip()
        elif line.strip().startswith("|         Cooling Module Position:"):
            cooling_module_position = line.split("[")[1].split("]")[0].strip()
    
    # Извлекаем номер модуля
    
        if line.strip().startswith("| Module: "):
            module_number = ""
            module_number = line.split("[")[1].split("]")[0].strip()
    # Проверяем, является ли строка информацией об устройстве
        position = ""
        if line.strip().startswith("| Position: "):

            position = line.split("[")[1].split("]")[0].strip()
            device_vector.append(module_number)        
            device_vector.append(position)
        crate_name = ""  
        if line.strip().startswith("| Crate Name: "):
        # Извлекаем имя устройства
            crate_name = line.split("[")[1].split("]")[0].strip()
            crate_with_info = crate_name
            device_vector.append(crate_name)
        if line.strip().startswith("| Info: "):
        # Извлекаем имя устройства
            info = line.split("[")[1].split("]")[0].strip()
            device_with_info.append(crate_with_info)
            device_with_info.append(info)
            crate_with_info = ""
        unit_count = ""
        if line.strip().startswith("| Crate Size in units: "):

            unit_count = line.split("[")[1].split("]")[0].strip()
            device_vector.append(unit_count)   
        loop = ""
        if line.strip().startswith("| Loop: "):

            loop = line.split("[")[1].split("]")[0].strip()
            device_vector.append(loop)
    
        if line.strip().startswith("| Standart: "):
            standart = line.split("[")[1].split("]")[0].strip()
        
        signals = ""
        if line.strip().startswith("| Signals: "):

            signals = line.split("[")[1].split("]")[0].strip()
            device_vector.append(signals)
        
            device_vector.append(standart)
            if (standart == "yes") : 
                device_vectors.append(device_vector)
                device_vector = []
                standart = "yes"
            
            
        signal = ""
        if line.strip().startswith("| Signal1: "):
    
            signal = line.split("[")[1].split("]")[0].strip()
            device_vector.append(signal)  

        signal = ""     
        if line.strip().startswith("| Signal2: "):

            signal = line.split("[")[1].split("]")[0].strip()
            device_vector.append(signal)   
        
        signal = "" 
        if line.strip().startswith("| Signal3: "):

            signal = line.split("[")[1].split("]")[0].strip()
            device_vector.append(signal) 
        
        signal = ""          
        if line.strip().startswith("| Signal4: "):

            signal = line.split("[")[1].split("]")[0].strip()
        
            device_vector.append(signal)  
            if signals == "4" or standart== "IPUMP_CONTR" or standart== "FASTVALVE_CONTR" :
                device_vectors.append(device_vector)
                device_vector = [] 
                standart = "yes"
    
        
        signal = ""
        if line.strip().startswith("| Signal5: "):

            signal = line.split("[")[1].split("]")[0].strip()
            device_vector.append(signal)  
            device_vectors.append(device_vector)  
            device_vector = [] 
            standart = "yes"
           
    
    
       

# Создаем вектор для рэка
    rack_vector = [rack_number,xtd_number, module_count, slots_per_module, cooling_module_position]
    return device_vectors, rack_vector, device_with_info