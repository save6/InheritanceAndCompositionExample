from abc import ABCMeta, abstractmethod

#インターフェース
class Arranger(metaclass=ABCMeta):

    @abstractmethod
    def arrange(self):
        pass

#インターフェース
class BookFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format(self):
        pass

# コンポジション
class SimpleBookFormatter(BookFormatter):
    def format(self,book):
        return book['title'] + "(" + book['author'] + ")"

class JsonArranger(Arranger):
    def __init__(self,formatter):
        self.formatter = formatter
    
    def arrange(self,json):
        return "\n".join(map(self.formatter.format,json))


#--- 動作確認 ------------------------------------
if __name__=='__main__':
    BOOKS = [{ 'title':'坊ちゃん', 'author': '夏目漱石' },\
            { 'title': '吾輩は猫である', 'author': '夏目漱石' },\
            { 'title': '友情', 'author': '武者小路実篤' },]
    
    print('### コンポジション版 ###')
    arranger = JsonArranger(SimpleBookFormatter())
    print(arranger.arrange(BOOKS))
