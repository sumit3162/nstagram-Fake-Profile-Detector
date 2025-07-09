import seaborn as sns
import matplotlib.pyplot as plt

def visualize_confusion_matrix(confusion_mat):
    plt.figure(figsize=(10, 10))
    sns.heatmap(confusion_mat, annot=True)
    plt.show()
