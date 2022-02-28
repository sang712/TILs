for i in range(int(input())):
    animal_sound = list(input().split())
    while True:
        line = input()
        if line == "what does the fox say?":
            break
        else:
            animal, goes, sound = line.split()
        idx_list = []
        for i in range(len(animal_sound)-1, -1, -1):
            if sound == animal_sound[i]:
                animal_sound.pop(i)
    print(" ".join(animal_sound))

