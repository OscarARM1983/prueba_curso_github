def mcd_mcm(num1, num2):
    if num1 < num2:
        x = range(num1, 0, -1)
        for y in x:
            if num1%y == 0 and num2%y == 0:
                #print(f"El MCD entre {num1} y {num2} es {mcd}")
                #print(f"El MCM entre {num1} y {num2} es {num1*num2/mcd}")
                mcd = y
                mcm = num1*num2/y
                break
    elif num2 < num1:
        x = range(num2, 0, -1)
        for y in x:
            if num1%y == 0 and num2%y == 0:
                #print(f"El MCD entre {num1} y {num2} es {mcd}")
                #print(f"El MCM entre {num1} y {num2} es {num1*num2/mcd}")
                mcd = y
                mcm = num1*num2/y
                break
    else:
        #print(f"El MCD entre {num1} y {num2} es {num1}")
        #print(f"El MCM entre {num1} y {num2} es Indeterminado")
        mcd = num1
        mcm = "indefinido"
    
    return(mcd, mcm)

print(mcd_mcm(30, 50))




