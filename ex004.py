var = input("Type something: ")

print("Seu tipo primitivo é {}, e é um:(alnum) {},  (alpha) {}, (num)  {}, (upper) {}".format(type(var), var.isalnum(), var.isalpha(), var.isnumeric(), var.isupper()))
