import os


files = os.listdir("clear_the_clutter")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clear_the_clutter/{file}",f"clear_the_clutter/{i}.png")
        i = i + 1