import cv2
import os
import subprocess
import inquirer
import platform

host_file = os.getcwd() + '/code/data/hosts'

def os_check():
    # for windows
    if platform.system() == 'Windows':
        print('Windows OS detected.')
        print('WARNING! Some functions may not work properly on your OS')
    # for mac and linux(here, os.name is 'posix')
    else:
        print('POSIX system detected.')

def check_full_path(path):
    if os.path.isabs(path) == True:
        return path
    else:
        if os.path.isabs(os.getcwd() + '/' + path) == True:
            return os.getcwd() + '/' + path
        else:
            raise Exception('Path not found')

def save_new_host():
    host = input('Enter hostname or IP: ')
    user = input('Enter username: ')
    with open(check_full_path(host_file), 'a') as f:
        f.write(host + ' ' + user + '\n')

def choose_host():
    hosts = []
    with open(check_full_path(host_file), 'r') as f:
        for line in f:
            hosts.append(line.strip())
    hosts.append('Add new host')        
    questions = [inquirer.List('host', message='Choose host', choices=hosts)]
    answers = inquirer.prompt(questions)
    if answers['host'] == 'Add new host':
        save_new_host()
        return choose_host()
    else:
        return answers['host']

#Grabs biggest dimension and scales the photo so that max dim is now 1280
def resizeTo(image, newhigh=1280, newwid=1280, inter=cv2.INTER_AREA):
    (height, width) = image.shape[:2]
    if height>width:
        newheight = newhigh
        heightratio = height/newheight
        newwidth = int(width/heightratio)
        resized = cv2.resize(image, dsize=(newwidth, newheight), interpolation=inter)
        return resized, newheight, newwidth
    elif width>height:
        newwidth = newwid
        widthratio = width/newwidth
        newheight = int(height/widthratio)
        resized = cv2.resize(image, dsize=(newwidth, newheight), interpolation=inter)
        return resized, newheight, newwidth
    else: 
        pass

def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()
    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines) 

def get_file_remote(name, ssh):
    array = []
    name = '*'+name+'*'    
    proc = subprocess.run(["ssh", ssh, "-t", "find" , "/", "-name", name, '-print', ' 2>/dev/null'], stdout=subprocess.PIPE)
    out = str(proc.stdout.decode('utf-8'))
    out = out.split('\n')
    for line in out:
        li = line.strip('\r')
        if ': Permission denied' in str(li):
            pass
        elif 'Connection to' in str(li):
            pass
        else:
            if len(li) != 0:
                array.append(li)
            else:
                pass    
    return array

def get_file_local(name):
    array = []
    name = '*'+name+'*'
    proc = subprocess.run(["find" , "/", "-name", name, '-print', ' 2>/dev/null'], stdout=subprocess.PIPE)
    out = str(proc.stdout.decode('utf-8'))
    out = out.split('\n')
    for line in out:
        li = line.strip('\r')
        if ': Permission denied' in str(li):
            pass
        elif 'Connection to' in str(li):
            pass
        else:
            if len(li) != 0:
                array.append(li)
            else:
                pass    
    return array

def get_file_over(dest, name):
    loc = input('Local or Remote? (l/r): ')
    if loc == 'l':
        local = True
        array = get_file_local(name)
    elif loc == 'r':
        local = False
        host = choose_host()
        array = get_file_remote(name, host)
    if os.path.exists(dest) == False:
        os.mkdir(dest)
    dest = check_full_path(dest)
    question = [inquirer.List('file',
                           message="Which file do you want to copy?",
                           choices=array,
                       ),]
    answer = inquirer.prompt(question)
    print(answer['file'])
    if local == True:
        os.system('cp ' + answer['file'] + ' ' + dest)
    elif local == False:
        os.system('scp ' + host + ':' + answer['file'] + ' ' + dest)

def cat_file(file):
    os.system('cat ' + file)

def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir)) + '/'