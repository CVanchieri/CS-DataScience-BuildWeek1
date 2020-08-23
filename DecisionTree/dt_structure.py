# necessary imports
import numpy as np

"""
### Decision Tree class ###
Decision trees are one way to display an algorithm that only contains conditional control statements,
commonly used in operations research, specifically in decision analysis, to help identify a strategy
most likely to reach a goal, but are also a popular tool in machine learning.
"""
class DecisionTree(object): # create a decision tree class 'CART'
    pass
    """
    ### Fit: feature, label ###
    Model fitting is a measure of how well a machine learning model generalizes to similar data to that
    on which it was trained. A model that is well-fitted produces more accurate outcomes. A model that is
    overfitted matches the data too closely. A model that is underfitted doesn't match closely enough.
    """
    def fit(self, feature_, label_): # fit method
        pass
    """
    ### Gini Impurity: groups, class labels ###
    Gini impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled
    if it was randomly labeled according to the distribution of labels in the subset.
    """
    def gini_impurity(self, groups, class_labels): # compute gini similiarity method
        pass
    """
    ### Terminal Node: _group ###
    Terminal nodes are the most common class in the group, these are used to make prediction later on.
    """
    def terminal_node(self, group_): # terminal node method
        pass
    """
    ### Split: index, val, data ###
    Splitting the features into two groups based on values.
    """
    def split(self, index, val, data): # split method
        pass
    """
    ### best_split: data ###
    Finding the best split using the gini impurity score.
    """
    def best_split(self, data): # best split method
        pass
    """
    ### split_branch: node, depth ###
    Recursively split the data and check for early stop arguments to create terminal node.
    """
    def split_branch(self, node, depth): # split branch method
        pass
    """
    ### tree_builder: ###
    Build tree recursively with best_splt and split_branch.
    """
    def tree_builder(self): # build tree method
        pass
    """
    ### predict_: node, row ###
    Recursively traverse through the trees to determine the class of unseen sample
    data point during prediction.
    """
    def predict_(self, node, row): # predict method
        pass
    """
    ### predict: test_data ###
    Predict the labels of the data
    """
    def predict(self, test_data): # predict method
        pass
