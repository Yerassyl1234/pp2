import pygame
import os
from random import choice
pygame.init()
w,h = 400,600
begin , is_sing = False,False
global musics
global i
vol,i = 1, 0
stop , volumeUP,volumeDown = True,False,False
icon = None

def load_music():
    songs = []
    list_of_music = os.listdir(r'music')
    for files in list_of_music:
        if files.endswith('.mp3'):
            songs.append(files) 
    return songs  

musics = load_music()

sc = pygame.display.set_mode(( w , h))
pygame.display.set_caption("Media Player")


surf_1 = pygame.Surface((340, 55))

icon_play = pygame.image.load(r'play.png').convert_alpha()
icon_stop = pygame.image.load(r'stop.png').convert_alpha()
icon_next = pygame.image.load(r'next.png').convert_alpha()
icon_previous = pygame.image.load(r'prev.png').convert_alpha()


icon_play = pygame.transform.scale(icon_play,(icon_play.get_width()//8,icon_play.get_height()//8))
icon_stop = pygame.transform.scale(icon_stop,(icon_stop.get_width()//8,icon_stop.get_height()//8))
icon_next = pygame.transform.scale(icon_next,(icon_next.get_width()//10,icon_next.get_height()//10))
icon_previous = pygame.transform.scale(icon_previous,(icon_previous.get_width()//10,icon_previous.get_height()//10))

icon_play_rect = icon_play.get_rect(center = (w//2,h//1.2))
icon_stop_rect = icon_stop.get_rect(center = (w//2,h//1.2))
icon_next_rect = icon_next.get_rect(center = (290,h//1.2))
icon_previous_rect = icon_previous.get_rect(center = (110,h//1.2))
song_end1 = False
song_end = pygame.USEREVENT
pygame.mixer.music.set_endevent(song_end)
clock = pygame.time.Clock()
x = 33
while 1:
    sc.fill((0,0,0))
    sc.blit(icon_play,icon_play_rect)
    sc.blit(icon_next,icon_next_rect)
    sc.blit(icon_previous,icon_previous_rect)
    if pygame.mixer.music.get_busy() == True:
        is_sing = True
    else:
        is_sing = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                begin = True
                music = musics[i]
                i = musics.index(music)
                pygame.mixer.music.load(f'music\{music}')
                pygame.mixer.music.play()
                icon = 0
                x = 33
                stop = False
                
            if event.key == pygame.K_SPACE: 
                if not is_sing:
                    pygame.mixer.music.unpause()
                    stop = False
                else:
                    pygame.mixer.music.pause()
                    stop = True

            if event.key == pygame.K_RIGHT and is_sing:
                x = 33
                if i == len(musics) - 1:
                    i = 0
                    icon = 0
                else:
                    i += 1
                    icon += 1
                pygame.mixer.music.load(f'music\{musics[i]}')
                pygame.mixer.music.play()
                a = pygame.mixer.Sound(f'music\{musics[i]}')
               
            if event.key == pygame.K_LEFT and is_sing:
                x = 33
                if i == 0:
                    icon = len(musics) - 1
                    i = len(musics) - 1
                else:
                    i -= 1
                    icon -= 1
        
                pygame.mixer.music.rewind()
                pygame.mixer.music.load(f'music\{musics[i]}')
                pygame.mixer.music.play()
        
            if event.key == pygame.K_UP: 
                volumeUP = True
                
            if event.key == pygame.K_DOWN:
                volumeDown = True

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP,pygame.K_DOWN]:
                volumeUP , volumeDown = False , False
        if event.type == song_end:
            song_end1 = 1

    font = pygame.font.SysFont('Tahoma', 16, True) 
    
    if song_end1:
        if i == 0:
            i = len(musics) - 1
        else:
            i -= 1
        song_end1 = False
        pygame.mixer.music.load(f'music\{musics[i]}')
        pygame.mixer.music.play()
    
    if stop:
        sc.fill((0,0,0))
        sc.blit(icon_next,icon_next_rect)
        sc.blit(icon_previous,icon_previous_rect)
        sc.blit(icon_play,icon_play_rect)
        
    if stop == False:
        sc.fill((0,0,0))
        sc.blit(icon_next,icon_next_rect)
        sc.blit(icon_previous,icon_previous_rect)
        sc.blit(icon_stop,icon_stop_rect)
        x+=0.5
    
    sc.blit(surf_1, (30, 350))
    surf_1.fill((50,50,50))

    if begin:
        s = font.render(musics[i][:-4], True, 'white')  
        sc.blit(s, (x, 350)) 
    
    if x >=200:
        x = 33

    if volumeUP == True:
        vol += 0.01
        pygame.mixer.music.set_volume(vol)
    if volumeDown == True:
        vol -= 0.01
        pygame.mixer.music.set_volume(vol)


    pygame.display.update()
    clock.tick(60)