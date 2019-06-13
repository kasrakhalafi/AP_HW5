import os
import shutil

src_dir = os.path.join(os.getcwd(), 'src')
src_files = os.listdir(src_dir)

print(src_dir)


def create_dir(name, address):
    obj_dir = os.path.join(address, '{}'.format(name))
    if not os.path.exists(obj_dir):
        os.mkdir(obj_dir)



def create_file(name, address):
    obj_dir = os.path.join(address, '{}'.format(name))
    if not os.path.exists(name):
        with open(obj_dir, 'a'):
            os.utime(obj_dir, None)


def delete(name, address):
    obj_dir = os.path.join(address, '{}'.format(name))
    if os.path.exists(name):
        shutil.rmtree(obj_dir)


def find(name, address):
    obj_dir = os.path.join(address, '{}'.format(name))
    if os.path.exists(obj_dir):
        print(os.listdir(name))
    else:
        print("this does not exist!")


create_dir("hieveroe", '/home/kasra/AP_Proj/HW5/Q4')
create_file('goodbye', '/home/kasra/AP_Proj/HW5/Q4')
delete('kasra', '/home/kasra/AP_Proj/HW5/Q4')
find('src', '/home/kasra/AP_Proj/HW5/Q5')