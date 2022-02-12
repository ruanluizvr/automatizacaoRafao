#criar as funcoes que serão utilizadas mais de uma vez no projeto

class Page:

    #construtor
    def __init__(self, driver): 
        self.driver = driver
    
    #vai receber um locator (Mobily.by) e procurar todos os elementos da tela que tenha esse locator
    #vai retornar uma lista de todos os elementos que tiverem esse locator
    def find_elements(self, locator):
        return self.driver.find_elements(by=locator[0], value=locator[1])

    #vai retornar um elemento com esse locator
    def find_element(self, locator):
        return self.driver.find_element(by=locator[0], value=locator[1])

    #vai receber um locator, chamar a função find_element, enviar o locator do elemento e dar um click
    def click_on_element(self, locator):
        
        element = self.driver.find_element(by=locator[0], value=locator[1])
        
        element.click()
