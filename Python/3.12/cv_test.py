import roboflow

rf = roboflow.Roboflow(api_key="nNNDxwcGa4LCjLShqend")

project = rf.workspace().project("lightweight_objdetect")
model = project.version("6").model

# optionally, change the confidence and overlap thresholds
# values are percentages
model.confidence = 50
model.overlap = 25

# predict on a local image
prediction = model.predict("/Users/hannah_mac/Documents/unimelb/it_proj/naorobotproject/Python/3.12/test/459402929_383984451434756_2849019058358754754_n.jpg ")

# Predict on a hosted image via file name
prediction = model.predict("https://source.roboflow.com/BFqjh8H0RlS3CEPBDGlazdsgLK73/HZ4Nu3h48VPQEW63x0GP/original.jpg", hosted=True)

# Predict on a hosted image via URL
prediction = model.predict("https://...", hosted=True)

# Plot the prediction in an interactive environment
prediction.plot()

# Convert predictions to JSON
prediction.json()