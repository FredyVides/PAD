"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides
For Paper, "On Operator Theory-Based Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

from AnomalyDetectorSVD import AnomalyDetectorSVD
from plotAnomalyDetector import plotAnomalyDetector
from matplotlib.pyplot import plot,subplot,grid,tight_layout
from matplotlib.pyplot import figure, savefig
from pandas import read_csv


signal = read_csv('../Data/real_signal_1.csv', header = None)
signal = signal.values.reshape(-1)


L = 75
N_hankel = 1300

#Set the different tolerances

tolerance_1 = 2.4
tolerance_2 = 0.4
tolerance_3 = 0.1


scaling = 0.65
figsize = (10*scaling, 8*scaling)


rest_1 = AnomalyDetectorSVD(signal = signal,
                            L = L, 
                            N_hankel = N_hankel,
                            tolerance = tolerance_1,
                            and_or = "AND")

rest_2 = AnomalyDetectorSVD(signal = signal,
                            L = L,
                            N_hankel = N_hankel,
                            tolerance = tolerance_2,
                            and_or = "AND")
                            
rest_3 = AnomalyDetectorSVD(signal = signal,
                            L = L, 
                            N_hankel = N_hankel,
                            tolerance = tolerance_3,
                            and_or = "AND")


(d1,di,y,x0,x1,xm) = rest_1
(d2,di,y,x0,x1,xm) = rest_2
(d3,di,y,x0,x1,xm) = rest_3



figure(figsize =figsize)

ax1 = subplot(3,1,1)
plot(signal,'blue')
plot(d1*signal,'darkorange')
grid(color='k', linestyle='--', linewidth=0.5)
ax1.set_title('Identified anomalies with tolerance = {:2.2f}'.format(tolerance_1),
              fontsize=12)
tight_layout()



ax2 = subplot(3,1,2)
plot(signal,'blue')
plot(d2*signal,'darkorange')
grid(color='k', linestyle='--', linewidth=0.5)
ax2.set_title('Identified anomalies with tolerance = {:2.2f}'.format(tolerance_2), 
              fontsize=12)
tight_layout()


ax3 = subplot(3,1,3)
plot(signal,'blue')
plot(d3*signal,'darkorange')
grid(color='k', linestyle='--', linewidth=0.5)
ax3.set_title('Identified anomalies with tolerance = {:2.2f}'.format(tolerance_3), fontsize=12)
tight_layout()

savefig("../Figures/real_signal_1_different_tolerances_L=75_N=1300_AndOR=AND.pdf")

