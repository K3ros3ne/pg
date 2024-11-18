import sys
def read_header(file_name, header_length): 
   with open(file_name, "rb") as A:
      B = A.read(header_length)
      return B 

def is_jpeg(file_name):
       
    try:
        A = read_header(file_name, 2)
        if A == b'\xff\xd8':
           return True
        else:
            return False
    except FileNotFoundError:
         return False

def is_gif(file_name):
    
    try:
       A = read_header(file_name, 2)
       if A == b'GIF87a' or b'GIF89a':
            return True
       else:
            return False
    except FileNotFoundError:
         return False   

def is_png(file_name):
    
    try:
         A = read_header(file_name, 8)
         if A == b'\x89PNG\r\n\x1a\n':
            return True
         else:
            return False
    except FileNotFoundError:
         return False

def print_file_type(file_name):
   
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')

if __name__ == '__main__':
    try:
     file_name = sys.argv[1]
     print_file_type(file_name)
    except:
     print("Argument je nulovy")    
