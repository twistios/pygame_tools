from pygame_benchmark_simple import init_base
import pygame,time,sys,random,os
import matplotlib.pyplot as plt

random.seed(0)

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

display_info = pygame.display.Info()

def simple_blend(secs,dim,windowed,dim_shape,blend_mode):
    pygame.display.init()
    if blend_mode == pygame.BLEND_ADD:
        str_blend = "BLEND_ADD"
    elif blend_mode == pygame.BLEND_SUB:
        str_blend = "BLEND_SUB"
    elif blend_mode == pygame.BLEND_MULT:
        str_blend = "BLEND_MULT"
    elif blend_mode == pygame.BLEND_MIN:
        str_blend = "BLEND_MIN"
    elif blend_mode == pygame.BLEND_MAX:
        str_blend = "BLEND_MAX"
    else:
        str_blend = "BLEND"
    screen = init_base(dim, windowed, "simple blend "+str_blend)
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
        screen.blit(surf,(int(random.random()*screen.get_width()),int(random.random()*screen.get_height())),special_flags=blend_mode)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.quit()
    print("{:.3f} s passed, updates/s: {:.3f}".format(passed_time,(num_updates/passed_time)))
    return (num_updates/passed_time)

def plot_simple_blend(time=1, reps=5,dim=(1000,800),sizes=(32,256,1024),modes=None):
    max_rep = reps
    test_time = time
    
    d = dim
    # for d in [(1000,800),(1100,900),(1200,1000)]:

    # Blend modes:
    # 1.8: BLEND_ADD, BLEND_SUB, BLEND_MULT, BLEND_MIN, BLEND_MAX
    # new in 1.8.1: BLEND_RGBA_ADD, BLEND_RGBA_SUB, BLEND_RGBA_MULT, BLEND_RGBA_MIN, BLEND_RGBA_MAX BLEND_RGB_ADD, BLEND_RGB_SUB, BLEND_RGB_MULT, BLEND_RGB_MIN, BLEND_RGB_MAX
    # new in 1.9.2: BLEND_PREMULTIPLIED
    # new in 2.0.0: BLEND_ALPHA_SDL2
    
    for sd in sizes:
        dim = d
        shape_dim = sd

        if modes is None:
            x1 = [];y1 = []
            for i in range(1,max_rep+1):
                x1.append(i)
                y1.append(simple_blend(test_time,dim,True,shape_dim,pygame.BLEND_ADD))
            plt.plot(x1,y1,label = "BLEND_ADD, dim: "+str(dim)+",shape_dim: "+str(shape_dim))
            x2 = [];y2 = []
            for i in range(1,max_rep+1):
                x2.append(i)
                y2.append(simple_blend(test_time,dim,True,shape_dim,pygame.BLEND_SUB))
            plt.plot(x2,y2,label = "BLEND_SUB, dim: "+str(dim)+",shape_dim: "+str(shape_dim))
            
            x3 = [];y3 = []
            for i in range(1,max_rep+1):
                x3.append(i)
                y3.append(simple_blend(test_time,dim,True,shape_dim,pygame.BLEND_MULT))
            plt.plot(x3,y3,label = "BLEND_MULT, dim: "+str(dim)+",shape_dim: "+str(shape_dim))
            
            x4 = [];y4 = []
            for i in range(1,max_rep+1):
                x4.append(i)
                y4.append(simple_blend(test_time,dim,True,shape_dim,pygame.BLEND_MIN))
            plt.plot(x4,y4,label = "BLEND_MIN, dim: "+str(dim)+",shape_dim: "+str(shape_dim))
            x5 = [];y5 = []
            for i in range(1,max_rep+1):
                x5.append(i)
                y5.append(simple_blend(test_time,dim,True,shape_dim,pygame.BLEND_MAX))
            plt.plot(x5,y5,label = "BLEND_MAX, dim: "+str(dim)+",shape_dim: "+str(shape_dim))
        elif modes in (pygame.BLEND_ADD,pygame.BLEND_SUB,pygame.BLEND_MULT,pygame.BLEND_MIN,pygame.BLEND_MAX):
            x = [];y = []
            for i in range(1,max_rep+1):
                x.append(i)
                y.append(simple_blend(test_time,dim,True,shape_dim,modes))
            plt.plot(x,y,label = "BLEND_ADD, dim: "+str(dim)+",shape_dim: "+str(shape_dim))

    plt.xlabel("test run")
    plt.ylabel("updates/s")
    plt.title("Pygame "+pygame.version.ver+" Benchmark")
    plt.legend()
    plt.show()

def main():
    # example for sizes: (32,64,128,256,512,1024)
    plot_simple_blend(time=1,reps=5,dim=(1000,800),sizes=(32,256,1024),modes=pygame.BLEND_ADD)

if __name__ == "__main__":
    main()
