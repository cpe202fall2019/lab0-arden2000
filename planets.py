def weight_on_planets():
    earthW = input("What do you weigh on earth? ")
    earthW = float(earthW)
    marsW = earthW * .38
    jupiterW = earthW * 2.34
    print("\nOn Mars you would weigh ", marsW, " pounds.", "\nOn Jupiter you would weigh ", jupiterW, " pounds.")


if __name__ == '__main__':
    weight_on_planets()