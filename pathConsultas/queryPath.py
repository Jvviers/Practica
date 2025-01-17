import subprocess
import sys

def read_queries(file_path):
    """
    Lee las consultas desde un archivo y las devuelve como una lista de cadenas.
    """
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        sys.exit(f"Archivo no encontrado: {file_path}")
    except Exception as e:
        sys.exit(f"Error al leer el archivo: {e}")

def parse_result(raw_result):
    """
    Parsea el resultado crudo de una consulta y lo transforma en un formato limpio.
    """
    cleaned_lines = []

    for line in raw_result.splitlines():
        if line.strip() == "p":
            continue

        line = (
            line.replace("[:Nodes {id: ", "")
            .replace(", label: ", "")
            .replace("}]", "")
            .replace("(", "")
            .replace(")", "")
            .replace("[", "")
            .replace("]", "")
            .replace('"', " ")
        )

        unique_elements = list(dict.fromkeys(line.split()))  # Elimina duplicados preservando el orden
        cleaned_lines.append(" ".join(unique_elements))

    return "\n".join(cleaned_lines)

def execute_query(index, query):
    """
    Ejecuta una consulta Cypher usando cypher-shell y guarda el resultado.
    """
    command = f"echo \"{query}\" | cypher-shell -u neo4j -p neo4j2024"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.stderr.strip():
        return f"Error en la consulta {index + 1}: {result.stderr.strip()}\n"

    parsed_result = parse_result(result.stdout.strip())
    file_path = f"pathConsulta{index + 1}"

    try:
        with open(file_path, "w") as file:
            file.write(parsed_result + "\n")
        return f"Resultados de la consulta {index + 1} guardados en {file_path}\n"
    except Exception as e:
        return f"Error al guardar los resultados de la consulta {index + 1}: {e}\n"

def main():
    """
    Lee las consultas desde un archivo y las ejecuta secuencialmente.
    """
    input_file = "consultaspathbd03"
    queries = read_queries(input_file)

    if not queries:
        sys.exit(f"El archivo {input_file} no contiene consultas válidas.")

    for index, query in enumerate(queries):
        result = execute_query(index, query)
        print(result)

if __name__ == "__main__":
    main()
