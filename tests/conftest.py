from appium import webdriver
#comunicação do dispositivo com os testes

from app.aplication import Aplication

#será executado antes de todos os testes
#nome da função é do pytest_bdd
def pytest_bdd_before_scenario(request, scenario):
    
    request.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                desired_capabilities={
                                    'platformName': 'Android',
                                    'platformVersion': '11.0',
                                    'deviceName': 'Android 11.0 x86',
                                    'app': '', #colocar o caminho do apk. Pode colocar na raiz do projeto e colocar o caminho aqui
                                    'appPackage': 'com.alguma coisa normalmente', #pode ser obtido pelo apk info
                                    'appWaitActivity': 'activity de entrada', #pode ser obtido pelo apk info
                                    'autoGrantPermissions': 'true', #autoriza as permissões de acesso, qd necessárias
                                })

    request.driver.implicitly_wait(30) #espera 30 segundos pra falhar o teste, caso elemento nao renderize na tela

    request.app = Aplication(request.driver)

def pytest_bdd_after_scenario(request, scenario):
    request.driver.quit() #apos cada cenário, vai fechar o app