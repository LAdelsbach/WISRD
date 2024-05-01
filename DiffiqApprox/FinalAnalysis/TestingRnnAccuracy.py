# MLP for Pima Indians Dataset with 10-fold cross validation
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
import numpy as np
import tensorflow as tf
import numpy as np
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# load pima indians dataset
def read_and_parse_data(file_path):
    # Initialize lists for each variable
    t = []
    x = []
    z = []
    theta = []

    znot = 0
    xnot = 0
    thetanot = 0


    # Open and read the file
    # def read_data(file_path):
    # Initialize the lists for storing data
    
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        # Read the second line to get initial values
        values = file.readline().strip().split(',')

        znot = float(values[0])
        xnot = float(values[1])
        thetanot = float(values[2])

        # Skip the next line (assuming you want to skip one more line here, if not, remove this next(file))
        next(file)

        # Read each subsequent line, split by comma, and append to lists
        for line in file:
            values = line.strip().split(',')
            t.append(float(values[0]))
            x.append(float(values[1]))
            z.append(float(values[2]))
            theta.append(float(values[3]))

    return znot, xnot, thetanot, t, x, z, theta


# Call the function and store the results

# for i in range(10):
#     filena = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/FinalAnalysis/data0.txt'
#     znot, xnot, thetanot, time, x, z, theta = read_and_parse_data(filena)
#     # for i in range(len(time)):
#     #     time[i] = [time[i], x[i],z[i],theta[i]]
test = []
znot = []
xnot = []
thetanot = []
x = []
z = []
theta = []
print("starting" + "\n")

for i in range(100):
    print("Step: " + str(i) + "\n")
    filena = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/FinalAnalysis/SimulationsData/data' + str(i) + '.txt'
    znot1, xnot1, thetanot1, time, x1, z1, theta1 = read_and_parse_data(filena)
    for i in range(len(time)):
        blah = [time[i], znot1, xnot1, thetanot1]
        test.append(blah)
        znot.append(znot1)
        xnot.append(xnot1)
        thetanot.append(thetanot1)
        z.append(z1[i])
        x.append(x1[i])
        theta.append(theta1[i])
    #TODO fix all that crap
    # Reshape the data

# print(test)
print("Beggining reshaping")
t = np.reshape(test, (len(test), 1, 4))  # Reshape t to (samples, time steps, features(time, znot, xnot, thetanot))

outputs = np.column_stack((x, z, theta))  # Combine x, y, theta into a single matrix for output
# print(t)
# define 10-fold cross validation test harness


cvscores = []

model = tf.keras.models.load_model('/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/rnn_model.h5')

for i in range(len(outputs)):
 # evaluate the model
 scores = model.evaluate(t[i], outputs[i], verbose=0)
 print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
 cvscores.append(scores[1] * 100)
 
print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))