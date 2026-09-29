# 📘 Assignment: Testing Python Programs with unittest

## 🎯 Objective

Aprenda a verificar programas Python automaticamente usando a biblioteca padrão `unittest`. Você escreverá testes para funções, casos-limite, exceções e comportamentos de uma classe.

## 📝 Tasks

### 🛠️ Testar funções com diferentes entradas

#### Descrição

Complete os testes de `calculate_discount()` e `format_username()` no starter code. Use casos de entrada normais para confirmar que cada função retorna o resultado esperado.

#### Requisitos

O programa concluído deve:

- Criar métodos de teste dentro de uma classe que herde de `unittest.TestCase`.
- Usar `assertEqual()` para verificar pelo menos três resultados de `calculate_discount()`.
- Usar `assertEqual()` para verificar nomes em maiúsculas e minúsculas com `format_username()`.
- Executar os testes com `python starter-code.py` sem falhas.

### 🛠️ Verificar casos-limite e exceções

#### Descrição

Adicione testes para entradas que exigem tratamento especial, como valores vazios, quantidades negativas e valores fora do intervalo permitido.

#### Requisitos

O programa concluído deve:

- Verificar o comportamento de `format_username()` quando recebe uma string vazia.
- Usar `assertRaises()` para confirmar que `calculate_discount()` rejeita um percentual inválido.
- Usar `assertRaises()` para confirmar que `ShoppingCart.add_item()` rejeita uma quantidade menor ou igual a zero.
- Incluir pelo menos um teste para valor zero e um teste para o limite máximo aceito.

### 🛠️ Testar uma classe com setUp

#### Descrição

Complete os testes da classe `ShoppingCart`. Use `setUp()` para criar um carrinho novo antes de cada teste e verifique suas operações principais.

#### Requisitos

O programa concluído deve:

- Implementar `setUp()` para preparar uma instância independente de `ShoppingCart`.
- Verificar a adição de itens e o cálculo do total do carrinho.
- Verificar a remoção de um item existente.
- Verificar que a remoção de um item inexistente não altera o carrinho.
- Ter pelo menos oito testes automatizados passando no total.
