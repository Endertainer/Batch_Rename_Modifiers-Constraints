if "batchrename_modcon" in locals():
    importlib.reload(batchrename_modcon)
else:
    from . import batchrename_modcon

def register():
    batchrename_modcon.register()

def unregister():
    batchrename_modcon.unregister()

if __name__ == "__main__":
    register() 