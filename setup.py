from cx_Freeze import setup, Executable

base = None    

executables = [Executable("kinterlab2.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "GitMeUp",
    options = options,
    version = "0.0.1",
    description = 'GitMeUp',
    executables = executables
)