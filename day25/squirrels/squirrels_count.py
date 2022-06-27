import pandas

data = pandas.read_csv("2018_NY_CP_Squirrels_Data.csv")
g_c = len(data[data["Primary Fur Color"] == "Gray"])
c_c = len(data[data["Primary Fur Color"] == "Cinnamon"])
b_c = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [g_c, c_c, b_c],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
