from tkinter import *

my_sum = lambda x, y: x+y
my_dif = lambda x, y: x-y
my_mult = lambda x, y: x*y
my_div = lambda x, y: x/y
my_power = lambda x, y: x**y

new_calc = ""

def clear_input(ingresso):
    ingresso = ingresso.replace(" ", "")
    ingresso = ingresso.replace("**", "^")
    return ingresso

def check_input(ingresso):
    for char in ingresso:
        if char not in "1234567890+-*/^().":
            raise TypeError("CARATTERE NON VALIDO! -> {}".format(char))

def organize_input(ingresso):
    lista = [ingresso[0]]
    for char in ingresso[1:]:
        if char in "1234567890." and all([c in "1234567890." for c in lista[-1]]):
            lista[-1] += char
        else:
            lista += char
    
    return lista

def check_list(lista):
    if lista.count("(") != lista.count(")"):
        raise TypeError("PARENTESI NON VALIDE!")


def compute_input(lista):
    my_operands = []
    my_operators = []
    operators = ["+", "-", "*", "/", "^"]
    operators_precedence = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2,
        "(": -1,
        ")": -1
    }

    for term in lista:
        if all([c in "1234567890." for c in term]):
            my_operands.append(float(term))
        elif term in operators and my_operators == []:
            my_operators.append(term)
        elif term in operators and operators_precedence[term] >= operators_precedence[my_operators[-1]]:
            my_operators.append(term)
        elif term == "(":
            my_operators.append(term)
        elif term == ")":
            while my_operators[-1] != "(":
                my_operands, my_operators = go_back(my_operands, my_operators)
            my_operators.pop()      
        else:
            my_operands, my_operators = go_back(my_operands, my_operators)
            my_operators.append(term)
    
    while my_operators != []:
        my_operands, my_operators = go_back(my_operands, my_operators)
    
    global new_calc
    new_calc = ""

    return my_operands

def go_back(my_operands, my_operators):
    global new_calc
    value1 = float(my_operands.pop())
    operator = my_operators.pop()
    value2 = float(my_operands.pop())

    if operator == "+":
        result = my_sum(value2, value1)
        my_operands.append(result)
        # print(value2, operator, value1, "=", result)
        calc = ">> " + str(value2) + str(operator) + str(value1) + " = " + str(result) + "\n"
        new_calc += calc
        output3.configure(text=new_calc)
    elif operator == "-":
        result = my_dif(value2, value1)
        my_operands.append(result)
        # print(value2, operator, value1, "=", result)
        calc = ">> " + str(value2) + str(operator) + str(value1) + " = " + str(result) + "\n"
        new_calc += calc
        output3.configure(text=new_calc)
    elif operator == "*":
        result = my_mult(value2, value1)
        my_operands.append(result)
        # print(value2, operator, value1, "=", result)
        calc = ">> " + str(value2) + str(operator) + str(value1) + " = " + str(result) + "\n"
        new_calc += calc
        output3.configure(text=new_calc)
    elif operator == "/":
        result = my_div(value2, value1)
        my_operands.append(result)
        # print(value2, operator, value1, "=", result)
        calc = ">> " + str(value2) + str(operator) + str(value1) + " = " + str(result) + "\n"
        new_calc += calc
        output3.configure(text=new_calc)
    elif operator == "^":
        result = my_power(value2, value1)
        my_operands.append(result)
        # print(value2, operator, value1, "=", result)
        calc = ">> " + str(value2) + str(operator) + str(value1) + " = " + str(result) + "\n"
        new_calc += calc
        output3.configure(text=new_calc)
        
    return my_operands, my_operators

def calcola():
    espressione = insert.get() # " 10**2 * (10-2*4.5) "
    ingresso = espressione

    ingresso = clear_input(ingresso)
    #print("Input:", ingresso, "\n")
    i = "Espressione Inserita: " + ingresso + "\n"
    output1.configure(text=i)

    check_input(ingresso)
    lista = organize_input(ingresso)
    check_list(lista)

    result = compute_input(lista)
    #print("\nResult:", result[0])
    result = "Risultato: " + str(result[0])
    output2.configure(text=result)


def pulisci():
    insert.delete(0, END)
    insert.configure(text="")
    output1.configure(text="")
    output2.configure(text="")
    output3.configure(text="")


root = Tk()
root.title("Risolutore Espressioni Python Tkinter")
root.geometry("600x400")
#root.resizable(False, False)
root.config(bg="lightblue")

alta = Frame(root, bg='lightblue')
alta.pack()

testo = Label(alta, text="Risolutore Espressioni", bg='lightblue', font="Arial 18")
testo.grid(column=0, row=0, columnspan=2, padx=5, pady=15)

text = Label(alta, text="Inserisci espressione:", bg='lightblue', font="Arial 15")
text.grid(column=0, row=1, sticky=W, padx=5)

insert = Entry(alta, width=35, justify=CENTER)
insert.focus_set()
insert.grid(column=1, row=1, padx=5, pady=5)

bassa = Frame(root, bg='lightblue')
bassa.pack(pady=5)

calcola = Button(bassa, text="CALCOLA", bg='cyan', command=calcola)
calcola.grid(column=0, row=0, sticky=W, padx=5, pady=5)

pulisci = Button(bassa, text="PULISCI", bg='cyan', command=pulisci)
pulisci.grid(column=1, row=0, sticky=W, padx=5, pady=5)

esci = Button(bassa, text="ESCI", bg='cyan', command=quit)
esci.grid(column=2, row=0, sticky=W, padx=5, pady=5)

zona_output = Frame(root, bg='lightblue')
zona_output.pack()

output1 = Label(zona_output, text="", bg='lightblue', font="Arial 15")
output1.grid(column=0, row=0)

output3 = Label(zona_output, text="", bg='lightblue', font="Arial 15")
output3.grid(column=0, row=1)

output2 = Label(zona_output, text="", bg='lightblue', font="Arial 15")
output2.grid(column=0, row=2)

root.mainloop()
