from config import *

"""
Author: Seyedhadi Hashemi
in this file I made a stand alone GUI which takes all the inputs from the user,
save it in a text file, and show the results.
"""


class MyApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.Label018 = None
        self.Label013 = None
        self.logo = None
        self.Label017 = None
        self.Label016 = None
        self.Label015 = None
        self.Label014 = None
        self.Label012 = None
        self.Label011 = None
        self.Label010 = None
        self.Label009 = None
        self.Label008 = None
        self.MyImage = None
        self.Label007 = None
        self.Label006 = None
        self.Label005 = None
        self.Label004 = None
        self.Label003 = None
        self.Label002 = None
        self.Label001 = None
        self.pop_up2 = None
        self.Label66 = None
        self.Label55 = None
        self.Label44 = None
        self.Label33 = None
        self.Label22 = None
        self.Label11 = None
        self.Label00 = None
        self.pop_up = None
        self.DistanceSD = None
        self.DistanceSS = None
        self.ElevationsStorage = float
        self.ElevationReservoir = float
        self.ElevationTown = float
        self.NumberOfInhabitants = int
        self.CountryName = None
        self.master.title("GUI project")
        self.master.iconbitmap("gui_pics/pipe.ico")

        # Set geometry: upper-left corner of the window
        ww = 1100  # width
        wh = 600  # height
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2
        # assign geometry
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))
        # assign space holders around widgets
        self.dx = 5
        self.dy = 5
        # Image
        logo = tk.PhotoImage(file="gui_pics/image.png")
        logo = logo.subsample(1, 1)  # controls size
        self.l_img = tk.Label(master, image=logo)
        self.l_img.image = logo
        self.l_img.grid(row=11, column=1)
        # Label
        self.Label1 = tk.Label(master, text="Number of inhabitants")
        self.Label1.grid(column=0, row=1, padx=self.dx, pady=self.dy)

        self.Label2 = tk.Label(master, text="Elevation of the storage tank")
        self.Label2.grid(column=0, row=2, padx=self.dx, pady=self.dy)

        self.Label5 = tk.Label(master, text="Distance between Source and "
                                            "Storage tank")
        self.Label5.grid(column=0, row=5, padx=self.dx, pady=self.dy)

        self.Label6 = tk.Label(master, text="Distance between Storage tank "
                                            "and Distribution net")
        self.Label6.grid(column=0, row=6, padx=self.dx, pady=self.dy)

        # Entry

        # Number of Inhabitants
        self.Number_of_Inhabitants = tk.IntVar()
        self.Number_of_Inhabitants = tk.Entry(master, width=20)
        self.Number_of_Inhabitants.grid(column=1, row=1, padx=5, pady=5)

        # Elevation of the town
        self.Elevation_town = tk.IntVar()
        self.Elevation_town = tk.Entry(master, width=20)
        self.Elevation_town.grid(column=1, row=2, padx=5, pady=5)

        # Distance between Source and Storage tank
        self.Distance1 = tk.IntVar()
        self.Distance1 = tk.Entry(master, width=20)
        self.Distance1.grid(column=1, row=5, padx=5, pady=5)

        # Distance between Storage tank and Distribution net
        self.Distance2 = tk.IntVar()
        self.Distance2 = tk.Entry(master, width=20)
        self.Distance2.grid(column=1, row=6, padx=5, pady=5)

        # Combobox
        self.selected_country = tk.StringVar()
        self.cbox = ttk.Combobox(master, width=20,
                                 textvariable=self.selected_country)
        self.cbox.grid(column=0, row=0, padx=self.dx, pady=self.dy)
        self.cbox['state'] = 'readonly'
        with open(file="Countries.txt", mode="r") as ff:
            self.cbox['values'] = ff.read().splitlines()
        self.cbox.set("Country names")
        self.cbox_selection = self.cbox.get()

        # define Button to assign the values
        self.button_country = tk.Button(master, text="Assign",
                                        command=lambda:
                                        self.save_country_name())
        self.button_country.grid(column=3, row=0, padx=self.dx, pady=self.dy)

        self.button1 = tk.Button(master, text="Assign",
                                 command=lambda: self.save_info1())
        self.button1.grid(column=3, row=1, padx=self.dx, pady=self.dy)

        self.button2 = tk.Button(master, text="Assign",
                                 command=lambda: self.save_info2())
        self.button2.grid(column=3, row=2, padx=self.dx, pady=self.dy)

        self.button5 = tk.Button(master, text="Assign",
                                 command=lambda: self.save_info5())
        self.button5.grid(column=3, row=5, padx=self.dx, pady=self.dy)

        self.button6 = tk.Button(master, text="Assign",
                                 command=lambda: self.save_info6())
        self.button6.grid(column=3, row=6, padx=self.dx, pady=self.dy)

        self.button7 = tk.Button(master, text="Check your Inputs", bg="red",
                                 fg="blue",
                                 command=lambda: self.check_inputs())
        self.button7.grid(column=3, row=7, padx=5, pady=5)

        self.button8 = tk.Button(master, text="Show results", bg="pink",
                                 fg="blue",
                                 command=lambda: self.show_results())
        self.button8.grid(column=3, row=8, padx=5, pady=5)

        # if the user wants to see the original pumps figures
        self.button9 = tk.Button(master, text="Show pumps", bg="black",
                                 fg="white",
                                 command=lambda: self.show_pumps())
        self.button9.grid(column=3, row=9, padx=5, pady=5)

        self.button_quit = tk.Button(master, text="Quit", bg="yellow",
                                     fg="red", command=lambda: self.quit_gui())
        self.button_quit.grid(column=3, row=10, padx=5, pady=5)

    def save_country_name(self):
        """
        This method would insert the user's country in a txt file name,
        country.txt So when the user click on Assign button the country name
        wil be written in text file.
        """
        try:
            with open("inputs/country.txt", "w") as file:
                self.CountryName = self.selected_country.get()
                file.write(self.CountryName)
        except OSError:
            showinfo("Error", "Please insert a country name.")

    def save_info1(self):
        """
        This method would insert the user's number of inhabitants in a txt
        file name, Input1.txt .So when the user click on Assign button the
        input wil be written in text file.
        """
        try:
            if type(int(self.Number_of_Inhabitants.get())) == int:
                if 0 < int(self.Number_of_Inhabitants.get()) < 1000000:
                    with open("inputs/Input1.txt", "w") as file:
                        self.NumberOfInhabitants = \
                            self.Number_of_Inhabitants.get()
                        file.write(self.NumberOfInhabitants)
                else:
                    showinfo("Error",
                             "Please insert a number below one million ")
        except ValueError:
            showinfo("Error", "Please insert an integer number.")

    def save_info2(self):
        """
        This method would insert the user's elevation town in a txt file name,
        Input2.txt .So when the user click on Assign button the input
        will be written in text file.
        """
        try:
            if type(int(self.Elevation_town.get())) == int:
                if (int(self.Elevation_town.get())) > 0:
                    with open("inputs/Input2.txt", "w") as file:
                        self.ElevationTown = self.Elevation_town.get()
                        file.write(self.ElevationTown)
                else:
                    showinfo("Error", "Please insert a positive number.")
        except ValueError:
            showinfo("Error", "Please insert an integer number.")

    def save_info5(self):
        """
        This method would insert the user's pipe length between the reservoir
        and tank in a txt file name, Input5.txt .So when the user click on
        Assign button the input will be written in text file.
        """
        try:
            if type(int(self.Distance1.get())) == int:
                if (int(self.Distance1.get())) > 0:
                    with open("inputs/Input5.txt", "w") as file:
                        self.DistanceSS = self.Distance1.get()
                        file.write(self.DistanceSS)
                else:
                    showinfo("Error", "Please insert a positive number.")
        except ValueError:
            showinfo("Error", "Please insert an integer number.")

    def save_info6(self):
        """
        This method would insert the user's pipe length between the tank
        and town in a txt file name, Input6.txt .So when the user click on
        Assign button the input will be written in text file.
        """
        try:
            if type(int(self.Distance2.get())) == int:
                if (int(self.Distance2.get())) > 0:
                    with open("inputs/Input6.txt", "w") as file:
                        self.DistanceSD = self.Distance2.get()
                        file.write(self.DistanceSD)
                else:
                    showinfo("Error", "Please insert a positive number.")
        except ValueError:
            showinfo("Error", "Please insert an integer number")

    def check_inputs(self):
        """
        In this method when the user click on the respective button(Check
        your Inputs), The program navigate to the text files were all the
        inputs are saved. And It shows the values that the user has entered.
        """
        self.pop_up = tk.Toplevel(master=self)
        # Geometry of pop up window
        self.pop_up.geometry("400x400")
        self.pop_up.title("pop_up Window")

        # add a label for showing the selected country
        file1 = open("inputs/country.txt", "r")
        show_country = file1.read()
        file1.close()
        self.Label00 = tk.Label(self.pop_up,
                                text="The name of the "
                                     "Country is: " + show_country)
        self.Label00.grid(column=0, row=1, padx=self.dx, pady=self.dy)

        # add a label for showing the selected country
        file2 = open("inputs/Input1.txt", "r")
        show_inhabitants = file2.read()
        file2.close()
        self.Label11 = tk.Label(self.pop_up,
                                text="Number of "
                                     "inhabitants is: " + show_inhabitants)
        self.Label11.grid(column=0, row=2, padx=self.dx, pady=self.dy)

        # add a label for showing the Elevation town
        file3 = open("inputs/Input2.txt", "r")
        show_elevation = file3.read()
        file3.close()
        self.Label22 = tk.Label(self.pop_up,
                                text="Elevation "
                                     "of the town is: " + show_elevation)
        self.Label22.grid(column=0, row=3, padx=self.dx, pady=self.dy)

        # add a label for showing the Distance between Reservoir and Tank
        file6 = open("inputs/Input5.txt", "r")
        show_distance1 = file6.read()
        file6.close()
        self.Label55 = tk.Label(self.pop_up,
                                text="Distance between Source and "
                                     "Storage tank is: " + show_distance1)
        self.Label55.grid(column=0, row=6, padx=self.dx, pady=self.dy)

        # add a label for showing the Distance between Tank and Town
        file7 = open("inputs/Input6.txt", "r")
        show_distance2 = file7.read()
        file7.close()
        self.Label66 = tk.Label(self.pop_up,
                                text="Distance between Storage"
                                     " tank and "
                                     "Distribution net is: " + show_distance2)
        self.Label66.grid(column=0, row=7, padx=self.dx, pady=self.dy)

    def show_results(self):
        """
        In this Method when the user click on the respective button(Show
        results), It would import all the outputs that we want from this
        project, e.g. The consumption value, The hourly flow discharge,
        Diameter of the pipe,etc.


        """
        from main import consumption, hourly, daily, diameter_transmission, \
            velocity_transmission, reynolds_transmission, \
            diameter_distribution, \
            velocity_distribution, reynolds_distribution, \
            friction_transmission, \
            friction_distribution, slope_transmission, slope_distribution, \
            loss_transmission, head_distribution, plot, explanation

        self.pop_up2 = tk.Toplevel(master=self)
        # Geometry of pop up window
        self.pop_up2.geometry("500x500")
        self.pop_up2.title("Show results")
        # Label for country consumption
        self.Label001 = tk.Label(self.pop_up2,
                                 text="The consumption value is: "
                                      + str(consumption()) + " Lit/day.Capita")
        self.Label001.grid(column=0, row=1, padx=self.dx, pady=self.dy)

        self.Label002 = tk.Label(self.pop_up2,
                                 text="The hourly flow discharge : "
                                      + hourly() + " Lit/hour")
        self.Label002.grid(column=0, row=2, padx=self.dx, pady=self.dy)

        self.Label003 = tk.Label(self.pop_up2,
                                 text="The daily flow discharge : "
                                      + daily() + " Lit/day")
        self.Label003.grid(column=0, row=3, padx=self.dx, pady=self.dy)
        # Label for asserting the transmission and distribution
        self.Label004 = tk.Label(self.pop_up2,
                                 text="Transmission pipeline ")
        self.Label004.grid(column=0, row=4, padx=self.dx, pady=self.dy)

        self.Label005 = tk.Label(self.pop_up2,
                                 text="Distribution pipeline ")
        self.Label005.grid(column=1, row=4, padx=self.dx, pady=self.dy)

        # Label Diameter for Transmission pipeline

        self.Label007 = tk.Label(self.pop_up2,
                                 text="Diameter: "
                                      + diameter_transmission() + " mm")
        self.Label007.grid(column=0, row=5, padx=self.dx, pady=self.dy)

        # Label Diameter for Distribution pipeline
        self.Label008 = tk.Label(self.pop_up2,
                                 text="Diameter: "
                                      + diameter_distribution() + " mm")
        self.Label008.grid(column=1, row=5, padx=self.dx, pady=self.dy)

        # Label for velocity number
        self.Label009 = tk.Label(self.pop_up2,
                                 text="Velocity: "
                                      + velocity_transmission() + " m/sec")
        self.Label009.grid(column=0, row=6, padx=self.dx, pady=self.dy)

        self.Label009 = tk.Label(self.pop_up2,
                                 text="Velocity: "
                                      + velocity_distribution() + " m/sec")
        self.Label009.grid(column=1, row=6, padx=self.dx, pady=self.dy)

        # Label for reynolds
        self.Label010 = tk.Label(self.pop_up2,
                                 text="Reynolds number: "
                                      + reynolds_transmission() + "")
        self.Label010.grid(column=0, row=7, padx=self.dx, pady=self.dy)

        self.Label011 = tk.Label(self.pop_up2,
                                 text="Reynolds number: "
                                      + reynolds_distribution() + "")
        self.Label011.grid(column=1, row=7, padx=self.dx, pady=self.dy)

        # Label Friction loss
        self.Label012 = tk.Label(self.pop_up2,
                                 text="Friction coefficient: "
                                      + friction_transmission() + "")
        self.Label012.grid(column=0, row=8, padx=self.dx, pady=self.dy)

        self.Label013 = tk.Label(self.pop_up2,
                                 text="Friction coefficient: "
                                      + friction_distribution() + "")
        self.Label013.grid(column=1, row=8, padx=self.dx, pady=self.dy)

        # Label Slope

        self.Label014 = tk.Label(self.pop_up2,
                                 text="Slope: "
                                      + slope_transmission() + "%")
        self.Label014.grid(column=0, row=9, padx=self.dx, pady=self.dy)

        self.Label015 = tk.Label(self.pop_up2,
                                 text="Slope: "
                                      + slope_distribution() + "%")
        self.Label015.grid(column=1, row=9, padx=self.dx, pady=self.dy)

        # Label Head loss
        self.Label016 = tk.Label(self.pop_up2,
                                 text="Head loss: "
                                      + loss_transmission() + "")
        self.Label016.grid(column=0, row=10, padx=self.dx, pady=self.dy)

        self.Label017 = tk.Label(self.pop_up2,
                                 text="Head loss: "
                                      + head_distribution() + "")
        self.Label017.grid(column=1, row=10, padx=self.dx, pady=self.dy)

        # plotting the pump that we need
        self.Label018 = tk.Label(self.pop_up2,
                                 text="Amount and type of "
                                      "pump required: " + explanation(),
                                 wraplength=250)
        self.Label018.grid(row=11, padx=self.dx, pady=self.dy)

        plot()

    @staticmethod
    def show_pumps():
        from pumps_figure import plot_pump1, plot_pump2
        plot_pump1()
        plot_pump2()

    def quit_gui(self):
        self.master.destroy()


if __name__ == '__main__':
    MyApp().mainloop()
