import pygame
import time
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
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Venom of Venus.mp3')

    elif song_list.value == "Armata Strigoi":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Armata Strigoi.mp3')

    elif song_list.value == "Army of the Night":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Army of the Night.mp3')

    elif song_list.value == "To Hell and Back":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/To Hell and Back.mp3')

    elif song_list.value == "Shiroyama":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Shiroyama.mp3')

    elif song_list.value == "The Last Stand":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/The Last Stand.mp3')

    elif song_list.value == "Shepherd of Fire":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Shepherd of Fire.mp3')

    elif song_list.value == "Bat Country":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Bat Country.mp3')

    elif song_list.value == "Unholy Confessions":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Unholy Confessions.mp3')

    elif song_list.value == "The Blister Exists":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/The Blister Exists.mp3')

    elif song_list.value == "Before I Forget":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Before I Forget.mp3')

    elif song_list.value == "3 Nil":
        pygame.mixer.music.load('/Users/calemthomas/PycharmProjects/MP3-Player/music files/3 Nil.mp3')


def queue_func():
    if song_list.value == "Venom of Venus":
        song_runtime = 209
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Armata Strigoi.mp3')
        song_list.value = "Armata Strigoi"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Armata Strigoi":
        song_runtime = 240
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Army of the Night.mp3')
        song_list.value = "Army of the Night"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Army of the Night":
        song_runtime = 202
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/To  Hell and Back.mp3')
        song_list.value = "To Hell and Back"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "To Hell and Back":
        song_runtime = 209
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Shiroyama.mp3')
        song_list.value = "Shiroyama"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Shiroyama":
        song_runtime = 216
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/The Last Stand.mp3')
        song_list.value = "The Last Stand"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "The Last Stand":
        song_runtime = 239
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Shepherd of Fire.mp3')
        song_list.value = "Shepherd of Fire"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Shepherd of Fire":
        song_runtime = 324
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Bat Country.mp3')
        song_list.value = "Bat Country"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Bat Country":
        song_runtime = 312
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Unholy Confessions.mp3')
        song_list.value = "Unholy Confessions"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Unholy Confessions":
        song_runtime = 284
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/All Out Life.mp3')
        song_list.value = "The Blister Exists"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "The Blister Exists":
        song_runtime = 340
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Before I Forget.mp3')
        song_list.value = "Before I Forget"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "Before I Forget":
        song_runtime = 264
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Nero Forte.mp3')
        song_list.value = "3 Nil"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()

    elif song_list.value == "3 Nil":
        song_runtime = 315
        pygame.mixer.music.play()
        pygame.mixer.music.queue('/Users/calemthomas/PycharmProjects/MP3-Player/music files/Venom of Venus.mp3')
        song_list.value = "Venom of Venus"
        while song_runtime >= 1:
            song_runtime = song_runtime - 1
            time.sleep(1)
        queue_func()


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
    "The Blister Exists",
    "Before I Forget",
    "3 Nil"],
    command=music_select,
    scrollbar=True)

play_button = PushButton(interface, command=play_track, text="Play from start")
pause_button = PushButton(interface, command=pause_track, text="Pause")
resume_button = PushButton(interface, command=resume_track, text="Resume")
volume_slider = Slider(interface, start=1, end=100, horizontal=True, command=volume_alter, align="bottom")
slider_title = Text(interface, text="Volume Slider", align="bottom")
queue_next_song = PushButton(interface, text="Autoplay (Disables Control)", command=queue_func)
autoplay_warning = Text(interface, text="Please set preferred volume before enabling autoplay.", size=10)
joey_quote = Text(interface, text=""" "Slipknot is my baby. It is my life. It means everything.""", size=8)
joey_quote_2 = Text(interface, text="Everything I do means the world to me, but when it comes down to it, ", size=8)
joey_quote_3 = Text(interface, text="""Slipknot... that's my blood." """, size=8)
rip_joey = Text(interface, text="- Joey Jordison, R.I.P.", size=8)


interface.display()
