import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
iris = datasets.load_iris()
x= iris.data
y=iris.target
x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=42, test_size=0.1)
model = tree.DecisionTreeClassifier()
model.fit(x_train, y_train)
prediction= model.predict(x_test)
accuracy =  model.score(x_test,y_test)
print("Accuracy", accuracy)
plt.figure(figsize= [10,10])
tree.plot_tree(model,filled=True)
plt.show()

