import json
import glob
import sys
import msvcrt
import tkinter
from tkinter import filedialog


class ArrangeData:

    data = []
    counted_actions = {}
    counted_workgroups = {}
    counted_users = {}

    def load_data(self):
        root = tkinter.Tk()
        dir_name = filedialog.askdirectory(parent=root, initialdir="/",
                                            title='Please select a directory')
        file_list = glob.glob("%s/*" % (dir_name))
        root.destroy()
        if not file_list:
            print ("Files not found. Press any key to exit.")
            msvcrt.getch()
            sys.exit()
        for file_path in file_list:
            with open(file_path, encoding='utf8') as data_file:
                current_line = 0
                for line in data_file:
                    current_line += 1
                    try:
                        self.data.append(json.loads(line))
                    except json.JSONDecodeError:
                        print ("Error: File %s at line %d contains inappropriate JSON object." % (file_path, current_line))


    def add_or_create(self, key, dict):
        if key == None:
            pass
        else:
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1

    def count_values(self):
        for data_element in self.data:
            try:
                test_action = data_element["eventBody"]["action"]
            except KeyError:
                test_action = None
            try:
                test_users = data_element["eventBody"]["userId"]
            except KeyError:
                test_users = None
            try:
                test_workgroups = data_element["eventHeader"]["workgroupID"]
            except KeyError:
                test_workgroups = None

            needed_data = [test_action, test_users, test_workgroups]
            needed_dict = [self.counted_actions, self.counted_users, self.counted_workgroups]

            for i in range(0, 3):
                self.add_or_create(needed_data[i], needed_dict[i])

        if not self.counted_actions and not self.counted_users and not self.counted_workgroups:
            print ("Error: Files don't contain any data about actions, userId or workgroupID.  Press any key to exit.")
            msvcrt.getch()
            sys.exit()


