import pygame
import matplotlib.pyplot as plt
import time, random
import sys, os

random.seed(0)

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
    pygame.display.set_caption(name)
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
    return (num_updates/passed_time)

def simple_blit(secs, dim, windowed, dim_shape):
    pygame.display.init()
    screen = init_base(dim, windowed, "simple blit")
    if screen is None:
        return
    screen.fill((25,125,225))
    surf = pygame.Surface((dim_shape,dim_shape))
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
    return (num_updates/passed_time)

def shape_draw(secs, dim, windowed, dim_shape):
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
        pygame.draw.circle(screen,(90,190,150), (int(random.random()*screen.get_width()),int(random.random()*screen.get_height())), max(int(dim_shape/2),1))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.quit()
    print("{:.3f} s passed, updates/s: {:.3f}".format(passed_time,(num_updates/passed_time)))
    return (num_updates/passed_time)

def simple_plot1(time=3, dims=((1000,800),(1100,900),(1200,1000)), reps=5, sd=50):
    max_rep = reps
    test_time = time
    shape_dim = sd
    
    # example dims: [(600,400),(800,600),(1000,800)]
    for d in dims:
        dim = d
        x1 = [];y1 = []
        for i in range(1,max_rep+1):
            x1.append(i)
            y1.append(simple_loop(test_time,dim,True))
        plt.plot(x1,y1,label = "simple loop (dim: "+str(dim)+")")
        
        x2 = [];y2 = []
        for i in range(1,max_rep+1):
            x2.append(i)
            y2.append(simple_blit(test_time,dim,True,shape_dim))
        plt.plot(x2,y2,label = "simple blit (dim: "+str(dim)+",shape_dim: "+str(shape_dim)+")")
        x3 = [];y3 = []
        for i in range(1,max_rep+1):
            x3.append(i)
            y3.append(shape_draw(test_time,dim,True,shape_dim))
        plt.plot(x3,y3,label = "shape draw (dim: "+str(dim)+",shape_dim: "+str(shape_dim)+")")

    plt.xlabel("test run")
    plt.ylabel("updates/s")
    plt.title("Pygame "+pygame.version.ver+" Benchmark")
    plt.legend()
    plt.show()

def simple_plot2(time=3, dim=(1000,800), reps=5, sds=(32,256,1025)):
    max_rep = reps
    test_time = time
    
    for sd in sds:
        shape_dim = sd
        x1 = [];y1 = []
        for i in range(1,max_rep+1):
            x1.append(i)
            y1.append(simple_loop(test_time,dim,True))
        plt.plot(x1,y1,label = "simple loop (dim: "+str(dim)+")")
        x2 = [];y2 = []
        for i in range(1,max_rep+1):
            x2.append(i)
            y2.append(simple_blit(test_time,dim,True,shape_dim))
        plt.plot(x2,y2,label = "simple blit (dim: "+str(dim)+",shape_dim: "+str(shape_dim)+")")
        x3 = [];y3 = []
        for i in range(1,max_rep+1):
            x3.append(i)
            y3.append(shape_draw(test_time,dim,True,shape_dim))
        plt.plot(x3,y3,label = "shape draw (dim: "+str(dim)+",shape_dim: "+str(shape_dim)+")")

    plt.xlabel("test run")
    plt.ylabel("updates/s")
    plt.title("Pygame "+pygame.version.ver+" Benchmark")
    plt.legend()
    plt.show()
    
def main():
    print("Python "+sys.version)
    # sdl_version = str(pygame.version.SDL.major)+"."+str(pygame.version.SDL.minor)+"."+str(pygame.version.SDL.patch)
    # print("__Benchmark for Pygame "+pygame.version.ver+" (SDL "+sdl_version+")__")
    print("__Benchmark for Pygame "+pygame.version.ver+"__")

    # wind = True
    # simple_plot1(time=1, dims=((1000,800),(1100,900),(1200,1000)), reps=5, sd=50)
    simple_plot2(time=1, dim=(1000,800), reps=5, sds=(32,256,1025))
    
    
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()
