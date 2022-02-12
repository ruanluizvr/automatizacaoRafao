
from app.pages.funcoesBase import Page

#instanciando Page
#teremos portanto, o clicj
class FuncoesApp(Page): 
    
    def click (self, elemento):
        self.click_on_element(elemento)
    
