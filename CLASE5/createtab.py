datos = [("Gabriela", 25), ("Oliver", 30), ("Juan", 22)]

with open("archivos/datos.tsv", "w") as f:
    for nombre, edad in datos:
        f.write(f"{nombre}\t{edad}\n")  # \t 
