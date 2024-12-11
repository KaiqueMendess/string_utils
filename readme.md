String Utils
Um pacote Python que fornece funções úteis para manipulação de strings.

Funções
inverter_string(s): Inverte a string fornecida.
contar_vogais(s): Conta o número de vogais na string fornecida.

Exemplos de uso

from string_utils import inverter_string, contar_vogais

print(inverter_string("hello"))  # Saída: "olleh"
print(contar_vogais("hello"))  # Saída: 2

Testes
O pacote inclui testes unitários para garantir a correta funcionalidade das funções. Os testes podem ser executados usando o comando python -m unittest discover.

CI/CD
O pacote utiliza o GitHub Actions para automatizar a execução dos testes e a criação de artefatos. O fluxo de trabalho é definido no arquivo .github/workflows/ci.yml.

Instalação
Para instalar o pacote, basta baixar o arquivo string_utils.zip e descompactá-lo em um diretório de sua escolha.

Contribuição
Contribuições são bem-vindas! Se você encontrar um erro ou deseja adicionar uma nova funcionalidade, por favor, abra uma issue ou envie um pull request.