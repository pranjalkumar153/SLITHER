import cx_Freeze

executables = [cx_Freeze.Executable("SNAKE GAME.py")]

cx_Freeze.setup(
    name = "Snake Rules!!",
    options = {"build_exe" :{"packages": ["pygame", "random"], "include_files": ["apple.png",
                                                                                 "snake_icon.png",
                                                                                 "snake_head.png",
                                                                                 "button_click.wav",
                                                                                 "eating_apple.wav",
                                                                                 "game_over.wav",
                                                                                 "intro_sound.wav"]}},
    description  = "A simple snake game",
    executables = executables
)