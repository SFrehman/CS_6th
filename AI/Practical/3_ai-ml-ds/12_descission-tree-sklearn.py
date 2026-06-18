from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\CS_6th\AI Practical\3_ai-ml-ds\data.csv",
    encoding="utf-8-sig")


dt_model = DecisionTreeClassifier()

x = df[['study', 'attendance', 'assignments']]
y = df['result']

dt_model.fit(x,y)

print(dt_model.predict([[1,70,2]]))


# """
# Decision Plot Tree
# """
# plt.figure(figsize=(10,6))
# plot_tree(dt_model, feature_names=df[['study', 'attendance', 'assignments']].columns, filled=True)
# plt.show()
