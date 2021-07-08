from abc import ABCMeta, abstractmethod

#インターフェース
class Arranger(metaclass=ABCMeta):

    @abstractmethod
    def arrange(self):
        pass

# 継承
class AbstractArranger(Arranger):
    def arrange(self,json):
        return self.delimiter().join(map(self.format,json))

    @abstractmethod
    def format(self,book):
        pass

    def delimiter(self):
        return "\n"

class SimpleJsonArrangerExt(AbstractArranger):
    def format(self,book):
        return book['title'] + "(" + book['author'] + ")"

#--- 動作確認 ------------------------------------
if __name__=='__main__':
    BOOKS = [{ 'title':'坊ちゃん', 'author': '夏目漱石' },\
            { 'title': '吾輩は猫である', 'author': '夏目漱石' },\
            { 'title': '友情', 'author': '武者小路実篤' },]
    
    print('### 継承版 ###')
    arranger = SimpleJsonArrangerExt()
    print(arranger.arrange(BOOKS))
