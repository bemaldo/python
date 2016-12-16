import subprocess,os
def exe(pyfile,dest="",creator=r"C:\Python34\Scripts\pyinstaller.exe",ico=r"C:\my icons\favicon.ico",noconsole=False):
    insert=""
    if dest: insert+='--distpath ""'.format(dest)
    else: insert+='--distpath "" '.format(os.path.split(pyfile)[0])
    if ico: insert+=' --icon="{}" '.format(ico)
    if noconsole: insert+=' --noconsole '
    runstring='"{creator}" "{pyfile}" {insert} -F'.format(**locals())
    subprocess.check_output(runstring)
	
if __name__=='__main__':
	exe('client.py')