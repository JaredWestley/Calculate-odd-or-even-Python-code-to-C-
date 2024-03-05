# Open a new file or overwrite the existing one
with open("Odd_Even_Gen.c", "w") as file:
    file.write("#include <stdio.h>\n")
    file.write("#include <stdint.h>\n")
    file.write("#include <stdlib.h>\n\n")

    file.write("int main(int argc, char* argv[])\n")
    file.write("{\n")

    # Ensuring the command line argument is properly used
    file.write("    if (argc < 2) return -1; // Ensure there's an argument passed\n")
    file.write("    uint8_t number = atoi(argv[1]);\n\n")

    for i in range(2**24):
        file.write("    if (number == "+str(i)+")\n")
        if i % 2 == 0:
            file.write("        printf(\"even\\n\");\n")
        else:
            file.write("        printf(\"odd\\n\");\n")

    file.write("    return 0;\n")
    file.write("}\n")

# Let the user know the process is completed
print("C code has been written to Odd_Even_Gen.c")
