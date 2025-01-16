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
    comands = "echo \"" + query * 3 + "\" | cypher-shell -u neo4j -p neo4j2024"
    result = subprocess.run(comands, shell=True, text=True, capture_output=True)
    res = str(result.stdout)
    er = str(result.stderr)
    lines = res.splitlines()
    count = lines[1]
    time = int (lines[-4].split(":")[1])
    time2 = int (lines[-15].split(":")[1])
    time3 = int (lines[-26].split(":")[1])
    time  = min(time, time2, time3)
    time = round (time/1000,3)
    return str (i+1) + " " + query + " COUNT: " + str (count) + " TIME: " + str (time) + "\n"


# Guardar resultados en un archivo
def save_results(results, file_path):
    try:
        with open(file_path, "w") as file:
            file.writelines(results)
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

def main():
    queries = read_queries("consultasbd03") 
    results = []
    for i, query in enumerate(queries):
        res = execute_query(i, query)
        results.append(res)
        print (res)

    save_results(results, "output_filebd03")

if __name__ == "__main__":
    main()
