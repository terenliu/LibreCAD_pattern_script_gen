

import numpy as np

def xy_disp(x0,y0):
    print(str(x0)+','+str(y0)+';\n')

def ci_disp(xc,yc,radius):
    print("ci;\n");
    xy_disp(xc,yc);
    print(str(radius)+';\n');

def circle_poly_generator(xc,yc,radius,div_num=1024):
    
        print("pl;\n");
        for i in range(0,div_num):
            xy_disp(xc+radius*np.cos(np.pi/div_num*2*i) ,yc+radius*np.sin(np.pi/div_num*2*i) );
        print("close;\n");


def rect_disp(x_left,x_span,y_bottom,y_span):
    print("rect;\n");
    xy_disp(x_left,y_bottom);
    xy_disp(x_left+x_span,y_bottom+y_span);


def triangle_disp(x_list,y_list):
    print("pl;\n");
    xy_disp(x_list[0],y_list[0]);
    xy_disp(x_list[1],y_list[1]);
    xy_disp(x_list[2],y_list[2]);
    print("close;\n");

def rect_centre_disp(xc,x_half_span,yc,y_half_span):
    rect_disp(x_left=xc-x_half_span,y_bottom=yc-y_half_span,x_span=2*x_half_span,y_span=2*y_half_span)

def arc_disp(x_list,y_list,xc,yc):
    print("arc;\n")
    xy_disp(x_list[0]+xc,y_list[0]+yc);
    xy_disp(x_list[1]+xc,y_list[1]+yc);
    xy_disp(x_list[2]+xc,y_list[2]+yc);
    print("close;\n");

def mesa_ring_disp(inner,xc,yc,radius,mesa_ring_width):
    if(inner==1):
        ##circle_poly_generator(xc=xc,yc=yc,radius=radius-mesa_ring_width);
        ci_disp(xc=xc,yc=yc,radius=radius-mesa_ring_width)
    else :
        ##circle_poly_generator(xc=xc,yc=yc,radius=radius);
        ci_disp(xc=xc,yc=yc,radius=radius)



 

