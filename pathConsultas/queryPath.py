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

def parse_result(raw_result):
    parsed_lines = []
    extracted_elements = set()

    for line in raw_result.splitlines():
        # Omitir la línea que contiene el nombre de la tabla ("p")
        if line.strip() == "p":
            continue
        
        # Parsear la línea para extraer nodos y relaciones
        elements = line.replace("(", "").replace(")", "").split("-[:")
        parsed_line = []

        for element in elements:
            if "]->" in element:
                relation, node = element.split("]->")
                parsed_line.append(f"[{relation.strip()}] [{node.strip()}]")
                extracted_elements.update([relation.strip(), node.strip()])
            else:
                parsed_line.append(f"[{element.strip()}]")
                extracted_elements.add(element.strip())

        parsed_lines.append(" ".join(parsed_line))
    
    return "\n".join(parsed_lines), extracted_elements

def execute_query(i, query):
    # Ejecutar la consulta utilizando cypher-shell
    command = f"echo \"{query}\" | cypher-shell -u neo4j -p neo4j2024"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    
    # Obtener resultados
    raw_result = result.stdout.strip()
    er = result.stderr.strip()

    # Manejar errores
    if er:
        print(f"Error en la consulta {i+1}: {er}")
        return f"Error: {er}\n"

    # Parsear el resultado
    parsed_result, extracted_elements = parse_result(raw_result)

    # Guardar los caminos en un archivo separado
    file_path = f"pathConsulta{i+1}.txt"
    try:
        with open(file_path, "w") as file:
            file.write(parsed_result + "\n")
        print(f"Resultados guardados en: {file_path}")
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

    # Guardar los elementos extraídos sin duplicados
    elements_file_path = f"elementsConsulta{i+1}.txt"
    try:
        with open(elements_file_path, "w") as file:
            file.write("\n".join(extracted_elements) + "\n")
        print(f"Elementos extraídos guardados en: {elements_file_path}")
    except Exception as e:
        print(f"Error al guardar los elementos: {e}")
        sys.exit(1)

    return f"Resultados de la consulta {i+1} guardados en {file_path}\nElementos guardados en {elements_file_path}\n"

def main():
    queries = read_queries("consultasbd03") 
    for i, query in enumerate(queries):
        res = execute_query(i, query)
        print(res)

if __name__ == "__main__":
    main()
