# FTP Scanner

Este é um pequeno script Python que permite fazer uma varredura em servidores FTP em busca de login anônimo.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema para executar este script.

## Uso

1. Faça o download do código-fonte para o seu computador.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde você salvou o arquivo do script.
4. Execute o script usando o seguinte comando:

python ftp_scanner.py

5. O script tentará fazer login anônimo em um servidor FTP em um endereço IP específico. O resultado será exibido no terminal.

## Como funciona

O script utiliza a biblioteca `ftplib` para se conectar ao servidor FTP no endereço IP especificado. Ele tentará fazer login como usuário anônimo e exibirá uma mensagem indicando se o login foi bem-sucedido ou falhou.

Se o login for bem-sucedido, a mensagem "[+] 'hostname' FTP anonymous Login succeeded" será exibida, onde 'hostname' é o endereço IP do servidor FTP.

Se o login falhar (por exemplo, se o servidor não permitir login anônimo), a mensagem "[-] 'hostname' FTP anonymous Login fails." será exibida.

## Nota

Este script é fornecido apenas para fins educacionais e de demonstração. Não utilize este script para fins maliciosos ou ilegais. Respeite a privacidade e a segurança dos servidores FTP que você está verificando.
