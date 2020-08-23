# necessary imnports
from dt import DecisionTree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

"""
Accuracy score function, computes raw accuaracy scores.
"""
def accuracy_score(prediction, actual): # accuracy score funtion
    correct_count = 0 # set the correct count equal to 0
    prediction_len = len(prediction) # set the prediction_len equal to the length of the prediction
    for i in range(prediction_len): # for loop, i in range of the prediciton_len
        if int(prediction[i]) == actual[i]: # if the prediction value is eqaul to the actual value
            correct_count += 1 # add 1 to the correct_count
    return correct_count/prediction_len # return the correct_count divded by the prediction_len
"""
Model function, loads data and computes decision trees.
"""
def model(): # model function
    iris = load_iris() # load the sklearn iris data set
    feature = iris.data[:,:2] # set the features of the data
    label = iris.target # set the label as the target
    X_train, X_test, y_train, y_test = train_test_split(feature, label, random_state= 42) # split the data into train and test
    """
    ### Created Decision Tree Model ###
    """
    decision_tree_model =  DecisionTree(max_depth_ = 5, min_splits_ = 20) # create our decision tree model with params
    decision_tree_model.fit(X_train, y_train) # fit the decision tree model
    prediction = decision_tree_model.predict(X_test) # create predicitons from the decision tree model
    """
    ### Sklearn Decision Tree Model ###
    """
    sk_dt_model = DecisionTreeClassifier(max_depth= 5, min_samples_split= 20) # use the decision tree model from Sklearn with params
    sk_dt_model.fit(X_train, y_train) # fit the decision tree model
    sk_dt_prediction = sk_dt_model.predict(X_test) # create predicitons from the decision tree model
    """
    ### Results ###
    """
    print("Created Model Accuracy : {0}".format(accuracy_score(prediction, y_test))) # print the created models accuracy score
    print("SK-Learn Model Accuracy : {0}".format(accuracy_score(sk_dt_prediction, y_test))) # print the sklearn models accuracy score
    print(list(zip(prediction, sk_dt_prediction, y_test))) # print the created models prediction, sklearn models prediction, and the actual value

if  __name__ == "__main__":
    model()
