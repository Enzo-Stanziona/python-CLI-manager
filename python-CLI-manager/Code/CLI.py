import sys
import os
import platform
import win32api
import shutil
from pathlib import Path

class comand:
    def __init__(self, parm, func):
        self.parm = parm
        self.func = (func)

#facilitator
def version(_path) -> str:
    try:
        info = win32api.GetFileVersionInfo(str(_path), '\\')
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        major, minor = win32api.HIWORD(ms), win32api.LOWORD(ms)
        build, revision = win32api.HIWORD(ls), win32api.LOWORD(ls)
        return f'{major}.{minor}.{build}.{revision}'
    except Exception:
        return 'unknow version'

#archives

#new folder
def nf( _title, _path):
    path_ = Path(_path) / _title
    path_.mkdir(parents=True, exist_ok=True)
    print('successfully completed')
#list
def ls(_path):
    path_ = Path(_path)
    for A in path_.iterdir():
        print(A.name)
#search
def sc(_path, _title):
    path_ = Path(_path)
    for A in path_.rglob(f'{_title}.*'):
            print(f'file found - info =\ntype={A.suffix}\nsize={A.stat().st_size}\nDate of last modification={A.stat().st_mtime}\nPath={A}')
#copy
def cp(_path, _title, d_path):
    path_ = Path(_path) / _title
    _d_path = Path(d_path)
    if path_.is_dir():
        shutil.copytree(path_, _d_path)
    else:
        shutil.copy(path_, _d_path)
    print('sucessfully completed')
#move
def mv(_path, _title, d_path):
    path_ = Path(_path) / _title
    _d_path = Path(d_path)
    shutil.move(path_, _d_path)
    print('sucessfully completed')

#system

#OS version
def OS_v():
    print(f'info =\nOS={platform.system()}\nversion={platform.release()}\narchiteture={platform.machine()}')
#enviroment versions
def env_v():
    print(f'info =\nhost={platform.node()}\npython={sys.version}\nenvironment variable=\n')
    for a, b in os.environ.items():
        print(f'{a} : {b}')
#archive version
def arc_v(_path, _title):
    path_ = Path(_path) / _title
    print(f'version={version(path_)}')

_nf = comand(2, nf)
_ls = comand(1, ls)
_sc = comand(2, sc)
_cp = comand(3, cp)
_mv = comand(3, mv)
_OS_v = comand(0, OS_v)
_env_v = comand(0, env_v)
_arc_v = comand(2, arc_v)

router = {
'sys': {
    'os--v': _OS_v,
    'env--v': _env_v,
    'arc--v': _arc_v
},
'arch': {
    'nf': _nf,
    'ls': _ls,
    'sc': _sc,
    'cp': _cp,
    'mv': _mv
}
}

def main():
    _main = input('>')
    _main_ = _main.split()
    _type = _main_[0]
    _func = _main_[1]
    if _type not in router:
        print(f'error: {_main_[0]} isn`t recognized like a type of existent comand')
        return
    elif _func not in router[_type]:
        print(f'error: {_main_[1]} isn`t recognized like a existent comand')
        return
    elif(len(_main_) != router[_type][_func].parm + 2):
        print('error: number of parameters exceeded or insufficient')
        return
    else:
     if router[_type][_func].parm == 0:
        router[_type][_func].func()
     else:
        parameters = []
        for i in range(router[_type][_func].parm):
            parameters.append(_main_[2 + i])
        router[_type][_func].func(*parameters)

while True:
    main()