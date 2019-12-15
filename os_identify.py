# !/usr/bin/python3
import os
import sys

print('Identificando seu OS...')
if sys.platform.startswith('aix'):
    # Aix specific code here...
    print('Aix')
elif sys.platform.startswith('linux'):
    # Linux specific code here...
    print('Linux')
elif sys.platform.startswith('win32'):
    # Windows code here...
    print('Windows')
elif sys.platform.startswith('cygwin'):
    # Win cygwin specific code here...
    print('Win cygwin')
elif sys.platform.startswith('darwin'):
    # MacOS specific code here...
    print('MacOS')
else:
    #outra coisa
    print('Algo deu errado...')

'''
AIX             - 'aix'
Linux           - 'linux'
Windows         - 'win32'
Windows/Cygwin  - 'cygwin'
macOS           - 'darwin'
'''
