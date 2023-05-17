"""
Load your model:
    You can load your model by following the steps below. However, please first
    follow the introduction in README.md, also see save.py shared in this repository
"""
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")