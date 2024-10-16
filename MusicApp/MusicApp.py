#QUESTION 1: 
'''Create a Tkinter application using the concepts of object-oriented
programming, such as, multiple inheritance, multiple decorators,
encapsulation, polymorphism, and method overriding, etc.'''

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Import from PIL for image handling
import pygame  # Import the pygame library

# Initialize pygame mixer for music playback
pygame.mixer.init()

# Encapsulation: MediaData class to hold video/music details
class MediaData:
    def __init__(self):
        self.__media_list = []  # Private attribute for storing media files
    
    # Add a media file to the list
    def add_media_to_data(self, media):
        self.__media_list.append(media)
    
    # Get all media files
    def get_all_media(self):
        return self.__media_list

# Base class for media player functionality
class MediaPlayerBase:
    def play_media(self):
        raise NotImplementedError("You need to implement this method!")

    def stop_media(self):
        raise NotImplementedError("You need to implement this method!")

# Class representing the UI and media player
class MediaPlayerApp(MediaPlayerBase, MediaData):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Music App")
        self.master.geometry("600x420")

        # Flag to stop playback
        self.stop_flag = False
        # Current playing index
        self.current_index = None
        
        # Layout setup
        self.setup_layout()

    # Setting up the background image
    def set_background(self, image_path):
        try:
            # Open image and resize to fit the window
            self.bg_image = Image.open(image_path)
            self.bg_image = self.bg_image.resize((400, 400), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)

            # Create a label to hold the background image
            self.bg_label = tk.Label(self.master, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading image: {e}")

    # Setting up the UI layout
    def setup_layout(self):
        # Left Frame - Media List
        self.left_frame = tk.Frame(self.master, bg="lightgray", width=200, padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Right Frame - Player Controls
        self.right_frame = tk.Frame(self.master, bg="white", padx=10, pady=10)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Listbox for media files
        self.media_listbox = tk.Listbox(self.left_frame, selectmode=tk.SINGLE, width=30, height=20)
        self.media_listbox.pack()

        # Add media button
        self.add_media_button = tk.Button(self.left_frame, text="Add Media", command=self.add_media)
        self.add_media_button.pack(pady=10)

        # Load images for buttons
        self.play_img = ImageTk.PhotoImage(Image.open("./play.png").resize((40, 40), Image.LANCZOS))
        self.stop_img = ImageTk.PhotoImage(Image.open("./stop.png").resize((40, 40), Image.LANCZOS))
        self.previous_img = ImageTk.PhotoImage(Image.open("./previous.png").resize((40, 40), Image.LANCZOS))
        self.next_img = ImageTk.PhotoImage(Image.open("./next.png").resize((40, 40), Image.LANCZOS))

        # Control buttons with images
        self.play_button = tk.Button(self.right_frame, image=self.play_img, command=self.play_media)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.right_frame, image=self.stop_img, command=self.stop_media)
        self.stop_button.pack(pady=10)

        self.previous_button = tk.Button(self.right_frame, image=self.previous_img, command=self.play_previous_media)
        self.previous_button.pack(pady=10)

        self.next_button = tk.Button(self.right_frame, image=self.next_img, command=self.play_next_media)
        self.next_button.pack(pady=10)

        # Volume Control
        self.volume_slider = tk.Scale(self.right_frame, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL,
                                         label="Volume", command=self.update_volume)
        self.volume_slider.set(1)
        self.volume_slider.pack(pady=10)

        # Display for media information
        self.media_info_label = tk.Label(self.right_frame, text="Now Playing: None", bg="white", font=("Helvetica", 12, "bold"))
        self.media_info_label.pack(pady=20)
    
    # Method to update the volume dynamically
    def update_volume(self, volume_value):
        pygame.mixer.music.set_volume(float(volume_value))

    # Method to add media files
    def add_media(self):
        media_file = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp3")])
        if media_file:
            self.add_media_to_list(media_file)

    # This method updates the listbox and the internal media list
    def add_media_to_list(self, media_file):
        self.add_media_to_data(media_file)
        self.media_listbox.insert(tk.END, media_file.split('/')[-1])

    # Method overriding: Play selected media
    def play_media(self):
        selected_indices = self.media_listbox.curselection()
        if selected_indices:
            self.stop_flag = False  # Reset stop flag before starting playback
            self.current_index = selected_indices[0]  # Set current playing index
            self.play_selected_media(self.current_index)
        else:
            messagebox.showwarning("No selection", "Please select a media file to play.")

    # Play the selected media based on index
    def play_selected_media(self, index):
        all_media = self.get_all_media()
        if index is not None and 0 <= index < len(all_media):
            selected_media = all_media[index]
            self.media_info_label.config(text=f"Now Playing: {selected_media.split('/')[-1]}")
            print(f"Playing media: {selected_media}")
            
            # Highlight the current selection in the listbox
            self.media_listbox.select_clear(0, tk.END)
            self.media_listbox.select_set(index)

            # Load and play the selected media
            pygame.mixer.music.load(selected_media)
            pygame.mixer.music.set_volume(self.volume_slider.get())  # Set volume
            pygame.mixer.music.play()

    # Method to play next media
    def play_next_media(self):
        all_media = self.get_all_media()
        if self.current_index is not None and self.current_index + 1 < len(all_media):
            self.current_index += 1
            self.play_selected_media(self.current_index)
        else:
            messagebox.showinfo("End of Playlist", "This is the last track.")

    # Method to play previous media
    def play_previous_media(self):
        if self.current_index is not None and self.current_index > 0:
            self.current_index -= 1
            self.play_selected_media(self.current_index)
        else:
            messagebox.showinfo("Start of Playlist", "This is the first track.")

    # Method overriding: Stop media playback
    def stop_media(self):
        self.stop_flag = True
        self.media_info_label.config(text="Now Playing: None")
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        print("Stopping media.")

# Main function to run the Tkinter app
def main():
    root = tk.Tk()
    app = MediaPlayerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
