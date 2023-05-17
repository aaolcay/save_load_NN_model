"""
Evaluate the model you loaded:
    Before evaluating the model you saved and loaded, please see the introductions
    in both save.py and load.py shared in this repository. You can evaluate this
    model on any dataset you want.
"""

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))