# Criptografia de Arquivos
- Esse projeto tem como objetivo criar uma rotina de criptografias dos arquivos informados pelo usuário, 
criando uma chave codigicada e salvando no banco de dados todos os logs de criptografias feito.
### Fluxo de Execução:
    - Verifica extensão de arquivos .csv no diretório informado.
    - Cria a chave codificada e armazena no banco (Caso não exista, ela é criada).
    - Encriptografa o conteúdo de cada arquivo .csv encontrado.
    - Compacta todos os arquivos criptografados em uma pasta .zip
    - Registra o log no banco de dados.
    - Informa ao usuário que a criptografia e a compactação foram realizadas com sucesso.
- Para a criptografia, foi usado o método Fernet a biblioteca Cryptography para a criação da chave codificada e a 
encriptação dos arquivos.
- Armazenamento dos logs e da chave, foi usado o SQL Server, usando a biblioteca SQLAlchemy.

#### Versões de Bibliotecas encontram-se em requirements.txt

## Ideias:
    - Criar uma rotina de criptografias de arquivos de um diretorio especifico para rodar em periodos pré-determinados

## Melhoria desse:
    - Incluir a funcionalidade de descriptografar os arquivos criptografados e salvar em uma pasta que o usuario 
    escolher.