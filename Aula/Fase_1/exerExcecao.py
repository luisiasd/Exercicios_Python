#-------------------Zero - Division - Error ---------------
def main ():
    try:
        x = 10 * (1/0)
    except ZeroDivisionError:
        print("Divisão por Zero não permitida!")
        
#----------------------------------------------------------
main()