# Tangle package
## A simply way to organize your Python project and execute it
If you're on Windows you can use the command `tang ...`. Else use `python tang.py ...`. For the arguments, the first argument must be the path of folder or .tpk file. If it's a folder, then the program build the .tpk package and with the argument `-r`, to place after, the program build and execute the package. Else it's a .tpk file, the program just execute it.
To make a folder ready to be build to a package, follow this instructions :
Your folder treeview must be like this (it's the minimum) :
```
mypackage/
    package/
        __init__.py
    entry.tip
    exit.tip
    info.tip
```
`entry.tip` must be like this at minimum :
```json
{
    "start": "", # To change (nothing if not but must be here)
    "log": True, # To change
    "clear": False, # To change
    "init": True # To change
}
```
`exit.tip` must be like this at minimum :
```json
{
    "finish": "", # To change (nothing if not but must be here)
    "log": True # To change
}
```
`info.tip` must be like this :
```json
{
    "name": "MyPackage", 
    "author": "John Doe",
    "version": "1.0.0",
    "desc": "My description."
}
```
> Coming soon : a package installer.