#prompt the user to input pressure in kilopascals and convert it to a floating-point number.
kpa=float(input("input pressure in kilopascals:"))
psi=kpa/6.89475729
mmhg=kpa*760/101.325
atm=kpa/101.325
print("the pressure in pounds per square inch:%.2f psi"%(psi))
print("the pressure in millimeters of mercury:%.2f mmhg"%(mmhg))
print("atmosphere pressure:%.2f atm."%(atm)) 






















