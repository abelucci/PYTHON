def ver_puntos(puntos):
    """
    Muestra la cantidad actual de puntos acumulados por el usuario.
    """
    if not isinstance(puntos, int):
        print("❌ Error: el valor de puntos no es válido.")
        return

    print("\n💎 --- Tus Puntos Acumulados ---")
    print(f"⭐ Actualmente tienes {puntos} puntos.")
    print("-------------------------------")

