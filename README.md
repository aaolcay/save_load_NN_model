# How to Save and Load a Model Explained
**Reference: https://machinelearningmastery.com/save-load-keras-deep-learning-models/**
## Save:
### Import Libraries
from tensorflow.keras.models import model_from_json
### serialize model to JSON
model_json = model.to_json()

with open("model.json", "w") as json_file:

    json_file.write(model_json)
### serialize weights to HDF5
model.save_weights("model.h5")

print("Saved model to disk")

**Once you have saved your model in the current folder, you can load it in any location by 
  specifying the path to the directory where you saved it.**

## Load:
### load json and create model
json_file = open('model.json', 'r')

loaded_model_json = json_file.read()

json_file.close()

loaded_model = model_from_json(loaded_model_json)
### load weights into new model
loaded_model.load_weights("model.h5")

print("Loaded model from disk") 
## Evaluate your model on your data:
### evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

score = loaded_model.evaluate(X, Y, verbose=0)

print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
