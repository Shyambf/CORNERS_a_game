import numpy as np
import ctypes
import os
class Api():
    def __init__(self) -> None:
        path = os.getcwd()
        self.lib = ctypes.cdll.LoadLibrary(os.path.join(path, 'core', 'c', 'libtest.so'))
        self.lib.search_move.restype = ctypes.POINTER(ctypes.c_int*64) 
        self.lib.search_move.argtypes = [ctypes.c_int*64, ctypes.c_int, ctypes.c_int]
        self.lib.ai_move.restype = ctypes.POINTER(ctypes.c_int*64) 
        self.lib.ai_move.argtypes = [ctypes.c_int*64] 

    def convert_to_2d(self, array:list):
        return list(np.array(array).flatten())

    def convert_to_3d(self, array:list):
        return list(np.array([array.contents[i] for i in range(64)]).reshape((8, 8)))

    def preper(self, array:list):
        array = self.convert_to_2d(array)
        arr = (ctypes.c_int * len(array))(*array)
        return arr
    
    def search_moves(self, array:list, x, y, flag=False):
        arr = self.preper(array)
        z = ctypes.POINTER(ctypes.c_int)
        z = self.lib.search_move(arr, x, y)
        return self.convert_to_3d(z)

    def ai_move(self, array:list):
        arr= self.preper(array)
        z = ctypes.POINTER(ctypes.c_int)
        z = self.lib.ai_move(arr)
        return self.convert_to_3d(z)
