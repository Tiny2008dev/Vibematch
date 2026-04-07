import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

def buildinsight(parent):
				insight_title = ctk.CTkLabel(parent , text="Your Insights")
				insight_title.grid(row = 0 , column = 0 , pady= 20 , padx = 20 , sticky="w")

				frame1 = ctk.CTkFrame(parent , width = 200 , height = 140)
				frame1.grid(row=1 , column = 0 , padx =5 , pady = 5)
				frame2 = ctk.CTkFrame(parent, width = 200 , height = 140)
				frame2.grid(row = 1 , column = 1, padx =5 , pady = 5)
				frame3 = ctk.CTkFrame(parent, width = 200 , height = 140)
				frame3.grid(row = 1 , column = 2, padx =5 , pady = 5)
				frame4 = ctk.CTkFrame(parent, width = 200 , height = 140)
				frame4.grid(row = 1 , column = 3, padx =5 , pady = 5)


				frame5 = ctk.CTkFrame(parent , width = 500 , height = 150)
				frame5.grid(row = 2 , column = 0 ,columnspan = 4, padx = 5 , pady = 5, sticky ="nsew")


				frame6 = ctk.CTkFrame(parent , width = 250 , height = 170)
				frame6.grid(row = 3 , column = 0 , columnspan = 2 , padx = 5 , pady = 5 , sticky ="nsew")

				#trying graph in frame

				fig , ax = plt.subplots(figsize = (3 , 2) , dpi = 100)

				languages =['Python' , 'JS' , 'C++' , 'Java']
				usage = [85 , 70 , 55 , 45]
				ax.bar(languages , usage , color = '#1f6aa5')
				ax.set_title("Tech Usage")

				canvas = FigureCanvasTkAgg(fig , master = frame1)
				canvas.draw()

				canvas.get_tk_widget().grid(row = 0 , column = 0 , padx = 10 , pady = 10)

				















