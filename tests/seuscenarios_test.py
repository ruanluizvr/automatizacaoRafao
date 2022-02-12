#arquivo tem o "_test" pq o pytest vai buscar ele pra ver a implementaçao do bdd
from app.mapelements import Elementos 

from pytest_bdd import given, when, then, scenarios

scenarios('./features/seuscenarios.feature')

@given('que eu esteja la na pagina do registro')
def step_impl(request):
    request.

@when('eu digite as informacoes da pessoa')
def step_impl(request):
    #implementação do step

@when('eu clique em finalizar cadastro')
def step_impl(request):
    #implementação do step

@then('o cadastro deve ser realizado com sucesso')
def step_impl(request):
    #implementação do step
