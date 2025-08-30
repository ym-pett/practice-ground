import os
import traceback
from importlib import util

class Base:
    '''basic resource class which gives tools to dependent classes '''

    plugins = []
    print(plugins)
    
    # how come we can just append these? 
    # 'cl' seems to contain them class 'plugin_b.py.PluginB' same for A 
    def __init_subclass__(cls, **kwargs) -> None:
        print(cls)
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

def load_module(path):
    name = os.path.split(path)[-1]
    #what's that? 
    spec = util.spec_from_file_location(name,path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
# Get current path
path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    if not fname.startswith('.') and \
        not fname.startswith('__') and \
        fname.endswith('.py'):
        try: 
            load_module(os.path.join(dirpath, fname))

        except Exception:
            traceback.print_exc()


