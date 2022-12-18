import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  
import math


def calculatedegree(m,n,p):
    if m and n and p !=0:
        g=np.arccos((n**2+p**2-m**2)/(2*n*p))
        h=np.arccos((m**2+p**2-n**2)/(2*m*p))
        i=np.arccos((m**2+n**2-p**2)/(2*m*n))
    else:
        g=math.nan
        h=math.nan
        i=math.nan
    return g,h,i



st.header("Triangle visual calculator")
col1, col2 = st.columns(2)
with col1:
    x1 = st.slider('p Enter a value of x1',key=1) 
    x2 = st.slider('q Enter a value of x2',key=2)
    x3 = st.slider('r Enter a value of x3',key=3)
with col2:
    y1 = st.slider('p Enter a value of y1',key=4)
    y2 = st.slider('q Enter a value of y2',key=5)
    y3 = st.slider('r Enter a value of y3',key=6)
a=x1-x2
b=y1-y2
c=x1-x3
d=y1-y3
e=x2-x3
f=y2-y3 
m = math.sqrt(a ** 2 + b ** 2)
n = math.sqrt(c ** 2 + d ** 2)
p = math.sqrt(e ** 2 + f ** 2)
plt.axis()

X = np.array([[x1,y1],[x2,y2],[x3,y3]])
plt.figure()
plt.scatter(0,0,color='white')
t1=plt.Polygon(X[:3,:],fc="white",ec="black")
plt.gca().add_patch(t1)

t2 = plt.Polygon(X[:,:],fc="white",ec="black")
plt.gca().add_patch(t2)
#def name1(*text,**string):

g,h,i=calculatedegree(m,n,p)

plt.text(x1, y1, "p "+u"\u2220"+str(round(np.degrees(i),2))+chr(176), fontsize=15,color='magenta')
plt.text(x2, y2, "q "+u"\u2220"+str(round(np.degrees(h),2))+chr(176), fontsize=15,color='magenta')
plt.text(x3, y3, "r "+u"\u2220"+str(round(np.degrees(g),2))+chr(176), fontsize=15,color='magenta')

plt.text((x1+x2)/2, (y1+y2)/2, round(m,2), fontsize=10,color='red')
plt.text((x2+x3)/2, (y2+y3)/2, round(p,2), fontsize=10,color='red')
plt.text((x3+x1)/2, (y3+y1)/2, round(n,2), fontsize=10,color='red')



#plt.text(x1, y1+1, u"\u2220"+str(round(np.degrees(2),2))+chr(176), fontsize=15,color='magenta')

st.set_option('deprecation.showPyplotGlobalUse', False)

st.pyplot()

latext = r'''
## Triangle properties
### area 
$$ 
area=1/2*m/n
$$  
'''
# st.write('area of an triangle',z)
st.write(latext)
# m=1
# n=1
if m and n != 0:
    z = 1/2*(m/n)
else:
    z=math.nan;#st.write('value mismatch')
#z = 1/2*m/n
st.write('area of an triangle',z)
g=m+n+p
latext = r'''
### circumferrence
$$ 
circumferrence=m+n+p
$$ '''
st.write(latext)
st.write('circumferrence of a triange',g)
# m=1
# n=1
# p=1
# g=np.arccos((n**2+p**2-m**2)/(2*n*p))
# h=np.arccos((m**2+p**2-n**2)/(2*m*p))
# i=np.arccos((m**2+n**2-p**2)/(2*m*n))

if m and n and p !=0:
    g=np.arccos((n**2+p**2-m**2)/(2*n*p))
    h=np.arccos((m**2+p**2-n**2)/(2*m*p))
    i=np.arccos((m**2+n**2-p**2)/(2*m*n))
else:
    g=math.nan
    h=math.nan
    i=math.nan

latext = r'''
### degree
$$ 
dergee  = arccos((n^2+p^2-m^2)/2np)
$$ '''
st.write(latext)
st.write('degree for p',np.degrees(g),u"\u2220",round(np.degrees(g),2),chr(176))
st.write('degree for q',np.degrees(h),u"\u2220",round(np.degrees(h),2),chr(176))
st.write('degree for r',np.degrees(i),u"\u2220",round(np.degrees(i),2),chr(176))

# plt.text(x1, y1+1, str(np.degrees(g))+u"\u2220"+str(round(np.degrees(g),2))+chr(176), fontsize=15,color='magenta')
# plt.text(x2, y2+1, "q", fontsize=15,color='magenta')
# plt.text(x3, y3+1, "r", fontsize=15,color='magenta')