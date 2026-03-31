import customtkinter as ctk

def build_playlists(parent):

  
  # Grid setup
  parent.grid_rowconfigure(0, weight=1)
  parent.grid_columnconfigure(1, weight=1)


  playlist_title = ctk.CTkLabel(
      parent,
      text="Your Playlists",
      font=("Arial",28,"bold")
  )
  playlist_title.grid(row=0, column=0, padx=20, pady=20, sticky="w")


  new_playlist = ctk.CTkButton(
      parent,
      text="+ New Playlist",
      width=160
  )
  new_playlist.grid(row=0, column=1, padx=20, pady=20, sticky="e")

  # Frame for playlist cards
  playlist_frame = ctk.CTkFrame(parent)
  playlist_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

  # Configure grid for playlist layout
  for i in range(3):
      playlist_frame.grid_columnconfigure(i, weight=1)

  for i in range(2):
      playlist_frame.grid_rowconfigure(i, weight=1)


  for row in range(2):
      for col in range(3):

          card = ctk.CTkFrame(
              playlist_frame,
              width=180,
              height=120,
              fg_color="#2b2b2b",
              corner_radius=10
          )

          card.grid(row=row, column=col, padx=15, pady=15)
          card.grid_propagate(False)

          label = ctk.CTkLabel(
              card,
              text="Playlist",
              font=("Arial",16,"bold")
          )

          label.place(relx=0.5, rely=0.5, anchor="center")

