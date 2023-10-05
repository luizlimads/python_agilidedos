import re
from mysql.connector import Error as mysql_error

class Handle_Erros_Mysql():
    __error = None
    __message:str = None
    def __init__(self, error:  mysql_error) -> None:
          self.__error = error

    def message(self) -> str:
        e = self.__error
        if e.errno == 1062:
            value_duplicate = re.findall("'([a-zA-Z.@]*)'", e.msg)
            if re.match('.*(email).*',value_duplicate[1]):
                self.__message = \
                "Este email já está sendo usado"
            elif re.match('.*(login).*',value_duplicate[1]):
                self.__message = \
                "Este login já está sendo usado"
            else:
                self.__message = \
                "Valores já estão sendo usados"
        return self.__message
