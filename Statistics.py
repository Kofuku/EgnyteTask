from ArrangeData import ArrangeData
from CreatePlot import CreatePlot
from collections import OrderedDict

class Statistics:

    arrange_data = ArrangeData()
    create_plot = CreatePlot()
    counted_actions = arrange_data.counted_actions
    counted_users = arrange_data.counted_users
    counted_workgroups = arrange_data.counted_workgroups
    counted_dict_list = [counted_actions, counted_users, counted_workgroups]

    def percentage(self):
        sum_list = self.create_plot.count_sum()
        ordered_counted_actions = {}
        ordered_counted_users = {}
        ordered_counted_workgroups = {}
        ordered_dict_list = [ordered_counted_actions, ordered_counted_users, ordered_counted_workgroups]
        percent_actions = {}
        percent_users = {}
        percent_workgroups = {}
        percent_dict_list = [percent_actions, percent_users, percent_workgroups]
        for i in range(0,3):
            current_list = ["actions", "userId", "workgroupID"]
            ordered_dict_list[i] = OrderedDict(sorted(self.counted_dict_list[i].items(), key=lambda x: x[1]))
            percent_dict_list[i]['other'] = 0
            for key, value in ordered_dict_list[i].items():
                if value >=(sum_list[i] / 100):
                    try:
                        percent_dict_list[i][key] = (100 * (value / sum_list[i]))
                    except ZeroDivisionError:
                        print("Error: JSON objects don't contain any %s data" % (current_list[i]))
                        break

                else:
                    percent_dict_list[i]['other'] += value
            try:
                percent_dict_list[i]['other'] = (100 * percent_dict_list[i]['other'] / sum_list[i])
            except ZeroDivisionError:
                print("Error: JSON objects don't contain any %s data" % (current_list[i]))
                continue

            if percent_dict_list[i]['other'] == 0.00:
                del percent_dict_list[i]['other']

            for item in percent_dict_list[i]:
                print (item, round(percent_dict_list[i][item], 2), "%")
