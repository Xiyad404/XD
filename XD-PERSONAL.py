#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
    os.system('xdfileg-open https://facebook.com/Xiyad.4040.XD/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ex.so')
except:
    pass
os.system('rm -rf ex.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ex.so'):
        os.system('curl -L https://github.com/Xiyad404/XD/blob/main/ex.cpython-311.so?raw=true -o ex.so') 
        import ex  
    else:
        import ex
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    