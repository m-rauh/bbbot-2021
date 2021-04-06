import pyautogui
from time import sleep
from PIL import Image
from random import *

brother = Image.open('img/rodolffo.png')
captcha = Image.open('img/capt.png')
votar_nov =  Image.open('img/vot_again.png')

contagem = 0

mouse_func = [pyautogui.easeOutBack, pyautogui.easeInOutQuad, pyautogui.easeOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]

def votar():
	'''
	Clica no captcha e depois em votar novamente
	'''
    sleep(randint(100,120)/100)
    w, z = pyautogui.locateCenterOnScreen(capt)
    pyautogui.moveTo(w+randint(-20,150), z+randint(-30,10), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    sleep(randint(180,200)/100)
    a, b = pyautogui.locateCenterOnScreen(vot)
    pyautogui.moveTo(a+randint(-250,250), b+randint(-15,15), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    sleep(randint(100,120)/100)


while True:
    #Aguarda a tela dar refresh
    sleep(10/100) #0.1s
    
    #Encontra posição do brother na tela e clica
    x, y = pyautogui.locateCenterOnScreen(brother)
    #deixa o movimento meio aleatório pro captcha não pegar
    pyautogui.moveTo(x+randint(-80,300), y+randint(-40,40), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    
    #tempo da pagina carregar
    sleep(randint(100,120)/100)
    
    #vota e clica em votar novamente
    if pyautogui.locateCenterOnScreen(captcha) == None:
        pyautogui.scroll(-300)
        voto()
    else:
        voto()
        
    contagem += 1
    if contagem%30 == 0:
        sleep(120)
        
    print("{} votos confirmados".format(comment))
