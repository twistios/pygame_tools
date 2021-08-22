import pygame
import time, random
import sys, os

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

display_info = pygame.display.Info()

def init_base(dim, windowed, name):
    ok = (dim[0] <= display_info.current_w and dim[1] <= display_info.current_h)
    screen = None
    if windowed:
        print(name+" (windowed), dim:"+str(dim)+", ok: "+str(ok))
        if ok:
            screen = pygame.display.set_mode(dim)
        else:
            pygame.display.quit()
    else:
        print(name+" (fullscreen), dim:"+str(dim)+", ok: "+str(ok))
        if ok:
            screen = pygame.display.set_mode(dim,pygame.FULLSCREEN)
        else:
            pygame.display.quit()
    return screen

def simple_loop(secs,dim,windowed):
    pygame.display.init()
    screen = init_base(dim, windowed, "simple loop, no blit")
    if screen is None:
        return
    screen.fill((25,125,225))
    passed_time = 0
    num_updates = 0
    start_time = time.time()
    while passed_time < secs:
        num_updates += 1
        pygame.display.update()
        passed_time = time.time() - start_time
        # print(passed_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.quit()
    print("{:.3f} s passed, updates/s: {:.3f}".format(passed_time,(num_updates/passed_time)))

def simple_blit(secs, dim, windowed):
    pygame.display.init()
    screen = init_base(dim, windowed, "simple blit")
    if screen is None:
        return
    screen.fill((25,125,225))
    surf = pygame.Surface((100,100))
    surf.fill((90,190,150))
    passed_time = 0
    num_updates = 0
    start_time = time.time()
    while passed_time < secs:
        num_updates += 1
        pygame.display.update()
        passed_time = time.time() - start_time
        # print(passed_time)
        screen.blit(surf,(int(random.random()*screen.get_width()),int(random.random()*screen.get_height())))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.quit()
    print("{:.3f} s passed, updates/s: {:.3f}".format(passed_time,(num_updates/passed_time)))

def shape_draw(secs, dim, windowed):
    pygame.display.init()
    screen = init_base(dim, windowed, "shape drawing")
    if screen is None:
        return
    screen.fill((25,125,225))
    # surf = pygame.Surface((100,100))
    # surf.fill((80,180,200))
    passed_time = 0
    num_updates = 0
    start_time = time.time()
    while passed_time < secs:
        num_updates += 1
        pygame.display.update()
        passed_time = time.time() - start_time
        # print(passed_time)
        pygame.draw.circle(screen,(90,190,150), (int(random.random()*screen.get_width()),int(random.random()*screen.get_height())), 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.quit()
    print("{:.3f} s passed, updates/s: {:.3f}".format(passed_time,(num_updates/passed_time)))
    

def main():
    print("Python "+sys.version)
    # sdl_version = str(pygame.version.SDL.major)+"."+str(pygame.version.SDL.minor)+"."+str(pygame.version.SDL.patch)
    # print("__Benchmark for Pygame "+pygame.version.ver+" (SDL "+sdl_version+")__")
    print("__Benchmark for Pygame "+pygame.version.ver+"__")

    wind = True
##    simple_loop(3,(600,400),wind)
##    simple_loop(3,(750,500),wind)
##    simple_loop(3,(900,600),wind)
##    simple_loop(3,(1050,700),wind)
##    simple_loop(3,(1200,800),wind)
##    simple_loop(3,(1350,900),wind)
##    simple_loop(3,(1500,1000),wind)
##    simple_loop(3,(1650,1100),wind)
##    simple_loop(3,(1800,1200),wind)
##    simple_loop(3,(1950,1300),wind)
    
##    simple_loop(3,(900,600),True)
##    simple_loop(3,(900,600),True)
##    simple_loop(3,(900,600),True)
##    simple_loop(3,(900,600),True)
##    simple_loop(3,(900,600),True)
##    print("###\n")
##    simple_blit(3,(900,600),True)
##    simple_blit(3,(900,600),True)
##    simple_blit(3,(900,600),True)
##    simple_blit(3,(900,600),True)
##    simple_blit(3,(900,600),True)
##    print("###\n")
##    shape_draw(3,(900,600),True)
##    shape_draw(3,(900,600),True)
##    shape_draw(3,(900,600),True)
##    shape_draw(3,(900,600),True)
##    shape_draw(3,(900,600),True)
    
    simple_loop(3,(900,600),True)
    simple_blit(3,(900,600),True)
    shape_draw(3,(900,600),True)
    
    
    pygame.quit()
    sys.exit()

main()
