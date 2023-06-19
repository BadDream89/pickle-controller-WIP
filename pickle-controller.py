import pickle


def user_datatype(vtype: str):
    
    transformed_value = None
    
    try:
                    
        match vtype:
                        
            case "int":
                transformed_value = int(value)
            case "float":
                transformed_value = float(value)
            case "string":
                transformed_value = str(value)
            case "bool":
                
                if value == "True" or value == 1 or value == "true":
                    transformed_value = True
                elif value == "False" or value == 0 or value == "false":
                    transformed_value = False
                else:
                    print("Unknown boolean value")
                    
            case "list":
                
                intermediate_value = list(value)
                intermediate_value.remove(intermediate_value[0])
                intermediate_value.remove(intermediate_value[-1])
                
                intermediate_value = "".join(intermediate_value)
                transformed_value = intermediate_value.split(", ")
                
            case "None":
                transformed_value = None
            case "dict":   
                print("Use adddict.")
            case _:
                transformed_value = None
                print("Unknown type.")
                    
            # here will be tuple put function  
            
    except TypeError:
                    print("Exception: TypeError. Unable to make your value to chosen type. NoneType returned")
    
    return transformed_value


# only for pickle-files

print("\n\n\nPickle controller is for only pickle-files!!!\n\n\n")

file: str = input("Filename: ") # will be used to read/write pickle-file

print("\n\n   Ctrl+C to leave from program. \n\n")

while True:
    
    try:    
        
        menu: str = input(">>> ")
        
        match menu:
         
            case "help":
                print("Avaible commands:\n   read - reading pickle file\n   put - putting key and value into a choosed dictionary. It doesnt support putting dictionaries\n   remove - removing key\n   edit - editing key's value\n   goto - usable when you have another dictionaries in main dict\n   back - returning to last dictionary\n   adddict - adding dictionary into pickle-file")
                
            case "read":
                
                try:
                    with open(file, "rb") as f:
                        data = pickle.load(f)
                        print(data)
                except EOFError:
                    print("Detected new file. Creating pickle structure...")
                    with open(file, "wb") as f:
                        
                        new_data = {}
                        pickle.dump(new_data, f)
                        print("Pickle structure created.")
                    
            case "put":
                
                key: str = input("Key: ")
                value = input("Value: ")                
                vtype = input("Value type: ") # vtype - value type 
                
                transformed_value = user_datatype(vtype)
                
                with open(file, "rb") as f:
                    data = pickle.load(f)
                    data.update({key: transformed_value}) # type: ignore
                
                with open(file, "wb") as f:
                    pickle.dump(data, f)
                    print("Successful process")
                    
            #here will be adddict, back, goto, edit
                
            case "remove":
                
                key = input("Key: ")
                
                with open(file, "rb") as f:
                    data = pickle.load(f)
                
                data.pop(key)
                
                with open(file, "wb") as f:
                    pickle.dump(data, f)
            
    except KeyboardInterrupt: # exit function on Ctrl+C
        print("\n\nExited from the program.")
        break
            
        
                
            
