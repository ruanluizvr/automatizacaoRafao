#registrar todas as paginas do app

from app.pages.funcoesdoapp_page import FuncoesApp

class Application:
    def __init__(self, driver):
        self.funcoesdoapp_page = FuncoesApp(driver)

        