import ftplib

def anonLogin(hostname):
    try:
        # Cria uma instância do objeto FTP, conectando-se ao servidor FTP no endereço "hostname".
        ftp = ftplib.FTP(hostname)
        # Tenta fazer login como usuário anônimo.
        ftp.login('anonymous')
        # Se o login for bem-sucedido, exibe uma mensagem indicando o sucesso.
        print('\n [+] ' + str(hostname) + ' FTP anonymous Login succeeded')
        # Fecha a conexão com o servidor FTP.
        ftp.quit()
        # Retorna "True" para indicar que o login foi bem-sucedido.
        return True
    except Exception:
        # Se ocorrer uma exceção (erro) durante o login, exibe uma mensagem indicando o erro.
        print('\n [-] ' + str(hostname) + ' FTP anonymous Login fails.')
        # Retorna "False" para indicar que o login falhou.
        return False

if __name__ == '__main__':
    # Chama a função "anonLogin()" com o endereço IP "90.130.70.73" para tentar fazer login anônimo no servidor FTP.
    anonLogin('90.130.70.73')
