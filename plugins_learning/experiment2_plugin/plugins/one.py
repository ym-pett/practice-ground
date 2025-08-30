class Plugin:
    def _init__(self, *args, **kwargs):
        print('Plugin init- ("one"):',args, kwargs)

    def execute(self, a,b):
        return a + b