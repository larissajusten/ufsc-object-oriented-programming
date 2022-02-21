"""
Arquivo da classe EmpresaDAO

Classes:
    EmpresaDAO
"""
import pickle
import sys


class EmpresaDAO:
    '''Data Access Object do objeto Empresa'''

    def __init__(self, datasource='empresa.pkl'):
        self.datasource = datasource
        self.objCache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        '''Metodo privado para salvar no arquivo'''
        file = open(self.datasource, 'wb')
        pickle.dump(self.objCache, file)
        file.close()

    def __load(self):
        '''Metodo privado para carregar do arquivo'''
        file = open(self.datasource, 'rb')
        self.objCache = pickle.load(file)
        file.close()

    def add(self, key, obj):
        '''Metodo para salvar'''
        self.objCache[key] = obj
        self.__dump()

    def get(self, key):
        '''Metodo para carregar objeto do arquivo'''
        try:
            return self.objCache[key]
        except KeyError:
            print('Chave não encontrada', file=sys.stderr)

    def remove(self, key):
        '''Metodo para remover objeto do arquivo'''
        print('>>remove')
        try:
            self.objCache.pop(key)
            self.__dump()
            return True
        except KeyError:
            print('Chave não encontrada', file=sys.stderr)

    def get_all(self):
        '''Metodo para carregar todos objetos do arquivo'''
        return self.objCache.items()
