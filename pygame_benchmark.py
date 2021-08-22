from pygame_benchmark_simple import init_base, simple_loop, simple_blit,\
     shape_draw, simple_plot1, simple_plot2
from pygame_benchmark_blending import plot_simple_blend,simple_blend
import pygame

def main():
    simple_plot1(time=1, dims=((1000,800),(1200,1000)), reps=5, sd=50)
    plot_simple_blend(time=1,reps=5,dim=(1000,800),sizes=(32,256,1024),modes=pygame.BLEND_ADD)

if __name__ == "__main__":
    main()
