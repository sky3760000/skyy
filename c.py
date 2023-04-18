from fastapi import FastAPI
import pickle
import joblib
import numpy as np
app = FastAPI()
new_data=[86802, 46192, 53291, 23391, 81227, 17776, 21633, 69637, 34981, 18440, 70405, 16692, 9319, 39004, 80555, 87875, 55940, 39041, 43576, 55396, 56742, 80264, 67422, 82578, 83835, 38368, 16867, 83621, 14448, 71920, 73248, 521, 89665, 21498, 68293, 71943, 72662, 35940, 45200, 1780, 98848, 72518, 94096, 6896, 1850, 11926, 19492, 34154, 18235, 61763, 93672, 7928, 47192, 58479, 95211, 59811, 73616, 52246, 87147, 90660, 74366, 8629, 64949, 91189, 51428, 72456, 15841, 26532, 71672, 47076, 78321, 82057, 63849, 43709, 63490, 534, 57585, 643, 68878, 22066, 64759, 83367, 11583, 97492, 42639, 84506, 28574, 67454, 42764, 28847, 84477, 60810, 65592, 14450, 64510, 93467, 8722, 11442, 75271, 37315, 14047, 27767, 45522, 51515, 69130, 23039, 38770, 86055, 96424, 31290, 16112, 59030, 20801, 45486, 21245, 87372, 35328, 67911, 71095, 85670, 73107, 11018, 22461, 98205, 59916, 28276, 43602, 55399, 83377, 41164, 67497, 79708, 38835, 55582, 2410, 78355, 98047, 55676, 27109, 56425, 4759, 99881, 33599, 34872, 46418, 93657, 15584, 46489, 11967, 62076, 83267, 73672, 87962, 75441, 59262, 10026, 92084, 95267, 61681, 34315, 18445, 46413, 21697, 18465, 5020, 42511, 56342, 17141, 52050, 81213, 80917, 33566, 20562, 63785, 20375, 75011, 52702, 15103, 47058, 97396, 10964, 59378, 20966, 57271, 90117, 7520, 51605, 11840, 7327, 78144, 83265, 65632, 42322, 8734, 44459, 57352, 8632, 32489, 36421, 94248, 93075, 90880, 14914, 91534, 51974, 54959, 27999, 13503, 81855, 41361, 69921, 44210]


# # Load the pickled model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)
model = joblib.load('life_expectancy_model.pkl')
new_data = np.array(new_data)
new_data = new_data.reshape(1,-1)
predictions = model.predict(new_data)
print(predictions)
y=predictions
y=list(y)
@app.get("/")
def read_root(x: int = y):
    return {"predictions value": f"{x}"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8060)