import os as os
#caminho = r'C:\Users\joaoh\Downloads\segundo treinamento\agua\bla'
#os.makedirs(caminho)
os.startfile(r'C:\Users\joaoh\Downloads\segundo treinamento\ultimo.txt')
print(os.getcwd())
#os.rename('oi.txt','tchau.txt')
#os.rename('tchau.txt','voltei.txt')
#os.rename('voltei.txt','ultimo.txt')
#os.remove('AGUA.TXT')
caminho2 = r'C:\Users\joaoh\Downloads\SEGUNDO TREINAMENTO'
os.chdir(caminho2)
for root, dir, files in os.walk(os.getcwd()):
    print(root)
