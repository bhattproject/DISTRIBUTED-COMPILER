import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
import os
import re

LOG_DIR = "training_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def extract_features(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
    size = os.path.getsize(file_path)
    lines = code.count("\n") + 1
    functions = len(re.findall(r"\b(?:int|void|double|float|char)\s+\w+\s*\(", code))
    includes = code.count("#include")
    loops = len(re.findall(r"\b(for|while)\s*\(", code))
    classes = len(re.findall(r"\bclass\s+\w+", code))
    templates = len(re.findall(r"\btemplate\s*<", code))
    return [size, lines, functions, includes, loops, classes, templates]

# just training i used this data 
X = np.array([
    [100, 5, 1, 0, 0, 0, 0],
    [500, 50, 2, 2, 0, 0, 0],
    [1000, 100, 4, 3, 2, 1, 0],
    [2000, 200, 8, 5, 4, 2, 1],
    [5000, 500, 15, 10, 10, 5, 2],
    [10000, 1000, 30, 20, 25, 10, 5]
])

y = np.array([0.1, 0.5, 1.0, 2.0, 5.0, 12.0])

model = LinearRegression()
model.fit(X, y)

with open("compile_time_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model generated: compile_time_model.pkl")

# Save feature stats
stats_file = os.path.join(LOG_DIR, "feature_stats.txt")
with open(stats_file, "w") as f:
    for row in X:
        f.write(",".join(map(str,row)) + "\n")

# Example: Predict for a new sample
example_features = np.array([[2500, 250, 10, 5, 5, 2, 1]])
pred = model.predict(example_features)
print(f"Example prediction: {pred[0]:.2f}s")

# Batch predict if multiple files exist
EXAMPLE_DIR = "xyz/dnminsins/aksksn/xxxxxxxxxxxxxxxx/"
if os.path.exists(EXAMPLE_DIR):
    for file in os.listdir(EXAMPLE_DIR):
        if file.endswith(".cpp"):
            path = os.path.join(EXAMPLE_DIR, file)
            feats = np.array([extract_features(path)])
            p = model.predict(feats)
            print(f"{file}: predicted compile time {p[0]:.2f}s")
