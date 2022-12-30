import pandas as pd
import plotly.express as px

df = pd.read_csv("main.csv")

TOEFL_Score = df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.show()

m = 1
c = 0
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()

m = 0.018
c = -1.27
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()

x = 250
y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")

