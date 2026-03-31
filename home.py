import customtkinter as ctk
def build_home(parent):
	titlemsg = ctk.CTkLabel(parent , text="Good Evening , Devam!" , font=("Arial" , 20 , "bold"),  text_color="white")
	titlemsg.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

	insightframe = ctk.CTkFrame(parent)
	insightframe.grid(row = 2 , column = 0 , padx = 14 , pady = 14)

	voicesession_frame = ctk.CTkFrame(parent)
	voicesession_frame.grid(row = 2, column = 1 , padx = 14 , pady = 14)

	mood_trendd_frame = ctk.CTkFrame(parent)
	mood_trendd_frame.grid(row = 2 , column = 2 , padx = 14 , pady = 14)

	msg2 = ctk.CTkLabel(parent , text = "Recent Reccomendations" , font =("Arial",20 , "bold"), text_color="white")
	msg2.grid(row = 3 , column = 0 , padx = 14, pady = 10)