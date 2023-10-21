if __name__ == "__main__":
    from lab_python_oop.rectanglecl import rectangle
    from lab_python_oop.circlecl import circle
    from lab_python_oop.squaresp import squareshape
    from termcolor import colored

    rec = rectangle(19, 19, "blue")
    cir = circle(19, "green")
    sq = squareshape(19, "red")

    print(colored(rec.repr(), "blue"))
    print(colored(cir.repr(), "green"))
    print(colored(sq.repr(), "red"))