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

def execute_query(query):
    comands = "echo " + query + " cypher-shell -u neo4j -p neo4j2024"
    result = subprocess.run(comands, shell=True, text=True, capture_output=True)
    res = result.stdout
    er = result.stderr
    lines = res.split("\n")
    count = lines[1] 
    time = lines[-4]
    return query, "COUNT: " + count, "TIME: " + time


# Guardar resultados en un archivo
def save_results(results, file_path):
    try:
        with open(file_path, "w") as file:
            file.writelines(results)
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

def main():
    queries = read_queries(ArchivoPruebaConsulta) 
    results = []
    for i, query in enumerate(queries):
        res = execute_query(query)
        results.append(res)
        print (res)
        
    save_results(results, output_file)

if __name__ == "__main__":
    main()
