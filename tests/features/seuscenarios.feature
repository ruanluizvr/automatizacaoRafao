Feature: Rafao's App

Scenario: register a people
    Given que eu esteja la na pagina do registro
    When eu digite as informacoes da pessoa
    When eu clique em finalizar cadastro
    Then o cadastro deve ser realizado com sucesso
