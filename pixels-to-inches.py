from cmath import sqrt
import cv2
def setPixelRatio(cardPts, refL, refH):
    L1_px=sqrt((cardPts[0][0]-cardPts[1][0])**2+(cardPts[0][1]-cardPts[1][1]))#sqrt((x0-x1)^2-(y0-y1)^2)
    H1_px=sqrt((cardPts[1][0]-cardPts[2][0])**2+(cardPts[1][1]-cardPts[2][1]))
    L2_px=sqrt((cardPts[2][0]-cardPts[3][0])**2+(cardPts[2][1]-cardPts[3][1]))#sqrt((x0-x1)^2-(y0-y1)^2)
    H2_px=sqrt((cardPts[3][0]-cardPts[0][0])**2+(cardPts[3][1]-cardPts[0][1]))
    ratio1Avg = (L1_px+L2_px)/(2*refL)
    ratio2Avg = (H1_px+H2_px)/(2*refH)
    ratioAvg = (ratio1Avg+ratio2Avg)/2
    return ratioAvg
def pixelToInches(line, ratio):
    L_px=sqrt((line[0][0]-line[1][0])**2+(line[0][1]-line[1][1]))#sqrt((x0-x1)^2-(y0-y1)^2)
    L = L_px/ratio
    return L

if __name__=="__main__":
    print("Hello")