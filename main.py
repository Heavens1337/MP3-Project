import pygame
from guizero import App, PushButton, ListBox, Slider, Text


pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)


def play_track():
    pygame.mixer.music.play()


def pause_track():
    pygame.mixer.music.pause()


def resume_track():
    pygame.mixer.music.unpause()


def volume_alter():
    pygame.mixer.music.set_volume(volume_slider.value * 0.01)


def music_select():
    if song_list.value == "Venom of Venus":
        pygame.mixer.music.load('/Users/calemthomas/music files/Venom of Venus.mp3')

    elif song_list.value == "Armata Strigoi":
        pygame.mixer.music.load('/Users/calemthomas/music files/Armata Strigoi.mp3')

    elif song_list.value == "Army of the Night":
        pygame.mixer.music.load('/Users/calemthomas/music files/Army of the Night.mp3')

    elif song_list.value == "To Hell and Back":
        pygame.mixer.music.load('/Users/calemthomas/music files/To Hell and Back.mp3')

    elif song_list.value == "Shiroyama":
        pygame.mixer.music.load('/Users/calemthomas/music files/Shiroyama.mp3')

    elif song_list.value == "The Last Stand":
        pygame.mixer.music.load('/Users/calemthomas/music files/The Last Stand.mp3')

    elif song_list.value == "Shepherd of Fire":
        pygame.mixer.music.load('/Users/calemthomas/music files/Shepherd of Fire.mp3')

    elif song_list.value == "Bat Country":
        pygame.mixer.music.load('/Users/calemthomas/music files/Bat Country.mp3')

    elif song_list.value == "Unholy Confessions":
        pygame.mixer.music.load('/Users/calemthomas/music files/Unholy Confessions.mp3')

    elif song_list.value == "All Out Life":
        pygame.mixer.music.load('/Users/calemthomas/music files/All Out Life.mp3')

    elif song_list.value == "Before I Forget":
        pygame.mixer.music.load('/Users/calemthomas/music files/Before I Forget.mp3')

    elif song_list.value == "Nero Forte":
        pygame.mixer.music.load('/Users/calemthomas/music files/Nero Forte.mp3')


def queue_func():
    if song_list.value == "Venom of Venus":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Armata Strigoi.mp3')

    elif song_list.value == "Armata Strigoi":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Army of the Night.mp3')

    elif song_list.value == "Army of the Night":
        pygame.mixer.music.queue('/Users/calemthomas/music files/To Hell and Back.mp3')

    elif song_list.value == "To Hell and Back":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Shiroyama.mp3')

    elif song_list.value == "Shiroyama":
        pygame.mixer.music.queue('/Users/calemthomas/music files/The Last Stand.mp3')

    elif song_list.value == "The Last Stand":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Shepherd of Fire.mp3')

    elif song_list.value == "Shepherd of Fire":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Bat Country.mp3')

    elif song_list.value == "Bat Country":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Unholy Confessions.mp3')

    elif song_list.value == "Unholy Confessions":
        pygame.mixer.music.queue('/Users/calemthomas/music files/All Out Life.mp3')

    elif song_list.value == "All Out Life":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Before I Forget.mp3')

    elif song_list.value == "Before I Forget":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Nero Forte.mp3')

    elif song_list.value == "Nero Forte":
        pygame.mixer.music.queue('/Users/calemthomas/music files/Venom of Venus.mp3')


interface = App(title="MP3 Player", height=500, width=400, layout="auto")

song_list = ListBox(interface, items=[
    "Venom of Venus",
    "Armata Strigoi",
    "Army of the Night",
    "To Hell and Back",
    "Shiroyama",
    "The Last Stand",
    "Shepherd of Fire",
    "Bat Country",
    "Unholy Confessions",
    "All Out Life",
    "Before I Forget",
    "Nero Forte"],
    command=music_select,
    scrollbar=True)

play_button = PushButton(interface, command=play_track, text="Play from start")
pause_button = PushButton(interface, command=pause_track, text="Pause")
resume_button = PushButton(interface, command=resume_track, text="Resume")
volume_slider = Slider(interface, start=1, end=100, horizontal=True, command=volume_alter, align="bottom")
slider_title = Text(interface, text="Volume Slider", align="bottom")
queue_next_song = PushButton(interface, text="Queue Next", command=queue_func)


interface.display()
