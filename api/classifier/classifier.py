import pickle
import numpy as np

with open('E:\\GraduatedProject\\Backend\\Foodobia\\api\\classifier\\scaler.save', 'rb') as f:
    sc = pickle.load(f)  # loading the saved model

with open('E:\\GraduatedProject\\Backend\\Foodobia\\api\\classifier\\best_rbf.pickle', 'rb') as f:
    loaded_clf = pickle.load(f)  # loading the saved model


# Here i'm defining a function for you to ease the testing process for you,
# all you have to do is to provide the feature array in the next code cell
# ['calories','fat', 'carbs']
# [457.3, 15.71, 22.33]


def predict_diabetes(arr):
        my_arr = np.log(np.array(arr) + 1)
        if len(my_arr) > 1:
            my_arr = sc.transform(my_arr)
        else:
            my_arr = sc.transform(np.reshape(my_arr, (1, -1)))

        return loaded_clf.predict(my_arr)
