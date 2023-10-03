from rembg import remove


input_path = input("Type the name and extension of the file such as Image.jpg: ")
output_path = "Output.png"

while True:
    try:
        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input_file = i.read()
                output_file = remove(input_file)
                o.write(output_file)
    except FileNotFoundError:
        print("File not found")
        input_path = input("Type the name and extension of the file such as Image.jpg: ")
    except:
        print("Error")
    else:
        break


