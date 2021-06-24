import pandas


def run():
    data = pandas.read_csv("Squirrel_Data.csv")

    fur_colors = data["Primary Fur Color"].dropna().unique()
    color_count = []
    for color in fur_colors:
        color_count.append(data[data["Primary Fur Color"] == color]["Primary Fur Color"].count())

    data_dict = {"Primary Fur Color": fur_colors, "Count": color_count}
    pandas.DataFrame(data_dict).to_csv("res.csv")


if __name__ == "__main__":
    run()
