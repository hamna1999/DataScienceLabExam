import matplotlib.pyplot as plt
import seaborn as sns
data= sns.load_dataset("iris")
sns.lineplot(x='sepal_length' ,y='petal_length', data = data)
plt.title("Seaborn graph")
plt.xlabel("sepal_length")
plt.ylabel("petal_length")
plt.show()