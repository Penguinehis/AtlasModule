#/usr/bin/python
# -*- coding: utf-8 -*-
#atlasremove.sh
import os
import sys
import time
nomearquivo = sys.argv[1]
arquivo = open(nomearquivo, 'r')
usuarios = arquivo.readlines()
for usuario in usuarios:
    os.system('./atlascreate.sh ' + usuario)
    print('Usuario ' + usuario + ' Criado com sucesso')
    time.sleep(0.5)
arquivo.close()
os.system('rm ' + nomearquivo)