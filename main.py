from model.revolver import Revolver

rev = Revolver()
for i in range(6):
    result = rev.pull_trigger()
    if result:
        print(f"Постріл {i + 1}: БАХ!")
        break
    else:
        print(f"Постріл {i + 1}: клік... пусто")