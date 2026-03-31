import matplotlib.pyplot as plt
categories=['A','B','C','D']
values=[3,7,8,5]
plt.bar(categories,values,color='green',label='Bar Data')
plt.title("Bar plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()