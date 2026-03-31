import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,7,6,8,7]
plt.scatter(x,y,color='blue',label='scatter Points')
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")    
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()



