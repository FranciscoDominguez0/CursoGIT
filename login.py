# Un login sencillo en Python

usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("¡Login exitoso!")
else:
    print("Usuario o contraseña incorrectos.")