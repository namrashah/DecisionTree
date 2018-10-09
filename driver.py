from DecisionTree import *
import pandas as pd
from sklearn import model_selection
from sklearn.model_selection import train_test_split
 
header = ['area A', 'perimeter P', 'compactness C', 'length of kernel', 'width of kernel', 'asymmetry coefficient', 'length of kernel groove', 'Class']
df = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/wheat-seeds.csv', header=None, names=['area A', 'perimeter P', 'compactness C', 'length of kernel', 'width of kernel', 'asymmetry coefficient', 'length of kernel groove', 'Class'])
lst = df.values.tolist()
t = build_tree(lst,0, 0, header)
print_tree(t)

print("********** Leaf nodes ****************")
leaves = getLeafNodes(t)
for leaf in leaves:
    print("id = " + str(leaf.id) + " depth =" + str(leaf.depth))
print("********** Non-leaf nodes ****************")
innerNodes = getInnerNodes(t)
for inner in innerNodes:
    print("id = " + str(inner.id) + " depth =" + str(inner.depth))

trainDF, testDF = model_selection.train_test_split(df, test_size=0.1)
train = trainDF.values.tolist()
test = testDF.values.tolist()

t = build_tree(train, 0, 0, header)
print("*************Tree before pruning*******")
print_tree(t)
acc = computeAccuracy(test, t)
print("Accuracy on test = " + str(acc))

## TODO: You have to decide on a pruning strategy
t_pruned = prune_tree(t, [20, 19])

print("*************Tree after pruning*******")
print_tree(t_pruned)
acc = computeAccuracy(test, t)
print("Accuracy on test = " + str(acc))
