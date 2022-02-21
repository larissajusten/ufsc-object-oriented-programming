"""
Arquivo da classe EmpresaDuplicadaException.

Classes:
    EmpresaDuplicadaException
"""


class EmpresaDuplicadaException(Exception):
    '''Exception para cenarios onde a empresa ja existe no banco de dados'''

    def __init__(self):
        super().__init__("Empresa duplicada!")
