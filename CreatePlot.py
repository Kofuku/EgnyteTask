from ArrangeData import ArrangeData
import matplotlib.pyplot as plt

class CreatePlot:

    arrange_data = ArrangeData()
    counted_actions = arrange_data.counted_actions
    counted_users = arrange_data.counted_users
    counted_workgroups = arrange_data.counted_workgroups
    counted_dict_list = [counted_actions, counted_users, counted_workgroups]
    bar_plot_list = []

    def count_sum(self):
        actions_values_sum = 0
        users_values_sum = 0
        workgroups_values_sum = 0
        sum_list = [actions_values_sum, users_values_sum, workgroups_values_sum]
        for i in range(0,3):
            for key, value in self.counted_dict_list[i].items():
                sum_list[i] += value
        return sum_list

    def connect_small_values(self):
        sum_list = self.count_sum()
        counted_dict_list = [self.counted_actions, self.counted_users, self.counted_workgroups]
        actions_plot = {}
        users_plot = {}
        workgroups_plot = {}
        dict_list_plot = [actions_plot, users_plot, workgroups_plot]
        for i in range(len(counted_dict_list)):
            dict_list_plot[i]['other'] = 0
            for key, value in counted_dict_list[i].items():
                if value >=(sum_list[i] / 100):
                    try:
                        dict_list_plot[i][key] = value
                    except ZeroDivisionError:
                        break
                else:
                    dict_list_plot[i]['other'] += value
            try:
                dict_list_plot[i]['other'] = dict_list_plot[i]['other']
            except ZeroDivisionError:
                continue
            self.bar_plot_list.append(dict_list_plot[i])

    def bar_plot(self):
        for item_2 in self.bar_plot_list:
            plt.bar(range(len(item_2)), item_2.values(), align='center')
            plt.xticks(range(len(item_2)), item_2.keys())
            plt.show()
