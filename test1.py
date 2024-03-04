#pour creer une exception
class MyException(Exception):
    def __init__(self,msg):
        self.Msg=msg
