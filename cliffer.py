import sys
from math import *
from PyQt4 import QtCore, QtGui
from mainWindow import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionYep_quit_now.triggered.connect(self.quit)
        self.buttonRender.clicked.connect(self.iterate)
        self.buttonClose.clicked.connect(self.quit)

    def quit(self):
        self.close()

    def invertColor(self,col):
        col.red=    255-col.red
        col.green=  255-col.green
        col.blue=   255-col.blue
        return col

    def get2ColorPal(self,p,color1,color2):
        color=_color(0,0,0)

        color.red=color1.red+p*(color2.red-color1.red)
        color.green=color1.green+p*(color2.green-color1.green)
        color.blue=color1.blue+p*(color2.blue-color1.blue)

        color.normalize()
        color.invert()

        #print(str(col.red)+' '+str(col.green)+' '+str(col.blue)+'\n')

        return color
    
    def getHue(self,h):
            col=_color(0,0,0)
            h*=6.0
            hi=int(h)
            hf=h-hi
            if hi==0:
                col.red=1.0
                col.green=hf
                col.blue=0.0
            if hi==1:
                col.red=1.0-hf
                col.green=1.0
                col.blue=0.0
            if hi==2:
                col.red=0.0
                col.green=1.0
                col.blue=hf
            if hi==3:
                col.red=0.0
                col.green=1.0-hf
                col.blue=1.0
            if hi==4:
                col.red=hf
                col.green=0.0
                col.blue=1.0
            if hi==5:
                col.red=1.0
                col.green=0.0
                col.blue=1.0-hf

            #col.invert()

            return col

    def iterate(self):
        # Equation parameters
        amin=float(self.txtBoxA.displayText())
        amax=float(self.txtBoxAA.displayText())
        bmin=float(self.txtBoxB.displayText())
        bmax=float(self.txtBoxBB.displayText())
        cmin=float(self.txtBoxC.displayText())
        cmax=float(self.txtBoxCC.displayText())
        dmin=float(self.txtBoxD.displayText())
        dmax=float(self.txtBoxDD.displayText())

        # Colors
        red1=float(self.txtBoxRed.displayText())
        red2=float(self.txtBoxRed2.displayText())
        green1=float(self.txtBoxGreen.displayText())
        green2=float(self.txtBoxGreen2.displayText())
        blue1=float(self.txtBoxBlue.displayText())
        blue2=float(self.txtBoxBlue2.displayText())
        color1=_color(red1,green1,blue1)
        color2=_color(red2,green2,blue2)
        colorMode=str(self.comboBox.currentText())
        
        if colorMode=="HUE shift":
            colorMode=1
            print("Using HUE Shift")
        if colorMode=="2color grad":
            colorMode=2
            print("Using 2Color Grad")
            print(str(int(red1))+','+str(int(green1))+','+str(int(blue1)))
            print(str(int(red2))+','+str(int(green2))+','+str(int(blue2)))
    
        # Image parameters
        screenx=int(self.txtBoxWidth.displayText())
        screeny=int(self.txtBoxHeight.displayText())
        iters=int(self.txtBoxIters.displayText())
        frames=int(self.txtBoxFrames.displayText())
        sens=float(self.txtBoxSens.displayText())

        # Intervals
        mina=acos(amin/2.0)
        maxa=acos(amax/2.0)
        minb=acos(bmin/2.0)
        maxb=acos(bmax/2.0)
        minc=acos(cmin/2.0)
        maxc=acos(cmax/2.0)
        mind=acos(dmin/2.0)
        maxd=acos(dmax/2.0)

        xlow=xhigh=0
        ylow=yhigh=0
        
        debug=open("debug.dat","w")

        # Alocates the bitmap
        bitmap=[]
        for i in range(screenx*screeny):
            bitmap.append(_color(0,0,0))
        
        for l in range(2):
            if l == 0:
                todoFrames=frames*0.10
                todoIters=iters*0.10
                print("Evaluating borders")
            else:
                todoFrames=frames
                todoIters=iters*0.10
                print("Rendering")

            for i in range(int(todoFrames)):                
                p=i/todoFrames
                
                if l==1:
                    if colorMode==1:
                        col=self.getHue(p)
                    if colorMode==2:
                        col=self.get2ColorPal(p,color1,color2)
                        debug.write(str(col.red)+' '+str(col.green)+' '+str(col.blue)+'\n')

                    if (p*100)%2==0:
                        self.progressBar.setValue(int(p*100))
                
                a=cos(mina+p*(maxa-mina))*2
                b=cos(minb+p*(maxb-minb))*2
                c=cos(minc+p*(maxc-minc))*2
                d=cos(mind+p*(maxd-mind))*2

                x=0.0
                y=0.0
                z=0.0
                w=0.0

                for j in range(int(todoIters)):

                    xn=sin(a*y)+c*cos(a*x)
                    yn=sin(b*x)+d*cos(b*y)

                    x=xn
                    y=yn

                    if l==0:
                        if x<xlow:
                            xlow=x
                        if x>xhigh:
                            xhigh=x
                        if y<ylow:
                            ylow=y
                        if y>yhigh:
                            yhigh=y

                    if l==1:
                        xi=(int(x-minx)*int(screenx/(maxx-minx)))
                        yi=(int(y-miny)*int(screeny/(maxy-miny)))



                        if(xi>=0 and xi<screenx and yi>=0 and yi<screeny):
                            bitmap[yi*screenx+xi].red+=col.red
                            bitmap[yi*screenx+xi].green+=col.green
                            bitmap[yi*screenx+xi].blue+=col.blue
            minx=xlow
            maxx=xhigh
            miny=ylow
            maxy=yhigh

        img=open("file.ppm","w")

        img.write('P3\n' + str(screenx) + ' ' + str(screeny) + '\n255\n')
       
        for i in range(screenx*screeny):
            col=bitmap[i]
            col.red=   ((1.0-exp(-sens*col.red))   *255.0)
            col.green= ((1.0-exp(-sens*col.green)) *255.0)
            col.blue=  ((1.0-exp(-sens*col.blue))  *255.0)

            col=self.invertColor(col)

            img.write(str(int(col.red)) + ' ' + str(int(col.green)) + ' ' + str(int(col.blue)) + ' ')
            
        img.close()
        self.progressBar.setValue(100)

class _color():
    def __init__(self,red,green,blue):
        self.red=red
        self.green=green
        self.blue=blue

    def normalize(self):
        self.red=self.red/255
        self.green=self.green/255
        self.blue=self.blue/255

    def invert(self):
        self.red=1-self.red
        self.green=1-self.green
        self.blue=1-self.blue

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
