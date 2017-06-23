from ArrangeData import ArrangeData
from CreatePlot import CreatePlot
from Statistics import Statistics


def main():
    arrange_data = ArrangeData()
    create_plot = CreatePlot()
    statistics = Statistics()

    arrange_data.load_data()
    arrange_data.count_values()

    create_plot.connect_small_values()
    create_plot.bar_plot()

    statistics.percentage()

if __name__ == "__main__":
    main = main()
