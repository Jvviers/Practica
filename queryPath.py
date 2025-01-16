import subprocess
import sys

def read_queries(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)

def execute_query(i, query):
    # Ejecutar la consulta utilizando cypher-shell
    command = f"echo \"{query}\" | cypher-shell -u neo4j -p neo4j2024"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    
    # Obtener resultados
    res = result.stdout.strip()
    er = result.stderr.strip()

    # Manejar errores
    if er:
        print(f"Error en la consulta {i+1}: {er}")
        return f"Error: {er}\n"

    # Guardar los caminos en un archivo separado
    file_path = f"pathConsulta{i+1}"
    try:
        with open(file_path, "w") as file:
            file.write(res + "\n")
        print(f"Resultados guardados en: {file_path}")
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

    return f"Resultados de la consulta {i+1} guardados en {file_path}\n"

def main():
    queries = read_queries("consultasbd03") 
    for i, query in enumerate(queries):
        res = execute_query(i, query)
        print(res)

if __name__ == "__main__":
    main()