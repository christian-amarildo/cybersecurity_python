import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+]' + str(hostname) + 'FTP anonymous Login succeded')
        ftp.quit()
        return True
    except Exception:
        print('\n [-]' + str(hostname) + ' FTP anonymous Login fails.')
        return False
    
if __name__ == '__main__':
    anonLogin('90.130.70.73')
    
    