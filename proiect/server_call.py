import socket
import pygame
import time

pygame.init()
window = pygame.display.set_mode((600, 600))
centru = pygame.Rect(250,250, 100, 100)#dreptunghiul din centru
sus = pygame.Rect(250,0, 100, 250)#dreptunghiul de sus
jos = pygame.Rect(250,350, 100, 250)#dreptunghiul de jos
stanga = pygame.Rect(0,250, 250, 100)#dreptunghiul din stanga
dreapta = pygame.Rect(350,250, 250, 100)#dreptunghiul din dreapta
stanga_sus = pygame.Rect(0,0, 250, 250)#dreptunghiul din stanga_sus
dreapta_sus = pygame.Rect(350,0, 250, 250)
stanga_jos = pygame.Rect(0,350, 250, 250)
dreapta_jos = pygame.Rect(350,350, 250, 250)

color = 'white'
color1 = 'red'
mesaj = "stam"
last_mesaj = None

run = True

my_socket = socket.socket()
port = 5055
ip = "192.168.23.142"  # Verifică adresa IP actuală a Arduino

my_socket.connect((ip, port))
 # my_socket.sendall("Hello ESP8266!\n".encode()) {asa trimiti mesaj catre arduino}
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #point = pygame.mouse.get_pos()
    #print(point)

    button = pygame.key.get_pressed()

    #collide_centru = centru.collidepoint(point)
    color_centru = color
    if button:
        color_centru = color1
        mesaj = "stam\n"

    #collide_sus = sus.collidepoint(point)
    color_sus = color 
    if button[pygame.K_w]:
        color_sus = color1
        color_centru = color
        mesaj = "inainte\n"

    #collide_jos = jos.collidepoint(point)
    color_jos = color 
    if button[pygame.K_s]:
        color_jos = color1
        color_centru = color
        mesaj = "inapoi\n"

    #collide_stanga = stanga.collidepoint(point)
    color_stanga = color 
    if button[pygame.K_a]:
        color_stanga = color1
        color_centru = color
        mesaj = "stanga\n"

    #collide_dreapta = dreapta.collidepoint(point)
    color_dreapta = color 
    if button[pygame.K_d]:
        color_dreapta = color1
        color_centru = color
        mesaj = "dreapta\n"

    #collide_stanga_sus = stanga_sus.collidepoint(point)
    color_stanga_sus = color 
    if button[pygame.K_w] and button[pygame.K_a]:
        color_stanga_sus = color1
        color_centru = color
        color_stanga = color
        color_sus = color  
        mesaj = "inainte si stanga\n"

    #collide_dreapta_sus = dreapta_sus.collidepoint(point)
    color_dreapta_sus = color 
    if button[pygame.K_w] and button[pygame.K_d]:
        color_dreapta_sus = color1
        color_centru = color
        color_sus = color
        color_dreapta = color 
        mesaj = "inainte si dreapta\n"

    #collide_stanga_jos = stanga_jos.collidepoint(point)
    color_stanga_jos = color 
    if button[pygame.K_s] and button[pygame.K_a]:
        color_stanga_jos = color1
        color_centru = color
        color_stanga = color 
        color_jos = color 
        mesaj = "inapoi si stanga\n"

    #collide_dreapta_jos = dreapta_jos.collidepoint(point)
    color_dreapta_jos = color 
    if button[pygame.K_s] and button[pygame.K_d]:
        color_dreapta_jos = color1
        color_centru = color
        color_jos = color
        color_dreapta = color 
        mesaj = "inapoi si dreapta\n"
    
    print(mesaj)

    window.fill(0)
    pygame.draw.rect(window, color_centru, centru)
    pygame.draw.rect(window, 'red', centru,5)

    pygame.draw.rect(window, color_sus, sus)
    pygame.draw.rect(window, 'red', sus,5)

    pygame.draw.rect(window, color_jos, jos)
    pygame.draw.rect(window, 'red', jos,5)

    pygame.draw.rect(window, color_stanga, stanga)
    pygame.draw.rect(window, 'red', stanga,5)

    pygame.draw.rect(window, color_dreapta, dreapta)
    pygame.draw.rect(window, 'red', dreapta,5)

    pygame.draw.rect(window, color_stanga_sus, stanga_sus)
    pygame.draw.rect(window, 'red', stanga_sus,5)

    pygame.draw.rect(window, color_dreapta_sus, dreapta_sus)
    pygame.draw.rect(window, 'red', dreapta_sus,5)

    pygame.draw.rect(window, color_stanga_jos, stanga_jos)
    pygame.draw.rect(window, 'red', stanga_jos,5)

    pygame.draw.rect(window, color_dreapta_jos, dreapta_jos)
    pygame.draw.rect(window, 'red', dreapta_jos,5)

    pygame.display.flip()

    if mesaj != last_mesaj:
        my_socket.sendall((mesaj).encode())
        last_mesaj = mesaj

pygame.quit()
exit()