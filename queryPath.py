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
        return f"Consulta {i+1}: Error: {er}\n"

    # Retornar los caminos obtenidos
    return f"Consulta {i+1}:\n{res}\n\n"

# Guardar resultados en un archivo
def save_results(results, file_path):
    try:
        with open(file_path, "w") as file:
            file.writelines(results)
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

def main():
    queries = read_queries("consultaspathbd03") 
    results = []
    for i, query in enumerate(queries):
        res = execute_query(i, query)
        results.append(res)
        # print(res)

    save_results(results, "outputfile_pathbd03")

if __name__ == "__main__":
    main()
