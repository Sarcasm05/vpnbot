def __init__():

    for module in __all__:
        try:
            exec("import {}".format(module) in globals())
        except:
            pass

__all__ = ['qiwi_wallet', 'SQLite', 'WalletQiwi']
__version__ = '1.0'

if __name__ == '__main__':
    __init__()
