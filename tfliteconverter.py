import tensorflow as tf
converter=tf.lite.TFLiteConverter.from_saved_model("models/cnnCat2.h5")
tflite_model=converter.convert()

open("linear.tflite","wb").write(tflite_model)