"""
Save your model:
    After training your model with the training dataset, you can name your model
    anything you want. However, notice that the code below assumes that you named
    your model as 'model':
        -> model.to_json()

"""
# Import libraries required:
from tensorflow.keras.models import model_from_json
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")