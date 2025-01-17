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
    lel = set()  # Usamos un conjunto para evitar duplicados
    for line in raw_result.splitlines():
        # Omitir líneas que no son relevantes (como el encabezado "p")
        if line.strip() == "p":
            continue

        # Parsear la línea para extraer nodos y relaciones
        elements = line.replace("(", "").replace(")", "").split("-[:")
        parsed_line = []

        for element in elements:
            if "]->" in element:
                # Si tiene relación, dividirla y formatear
                relation, node = element.split("]->")
                parsed_line.append(f"{relation.strip()} {node.strip()}")
            else:
                # Nodo inicial
                parsed_line.append(element.strip())

        # Unir la línea procesada y eliminar redundancias
        clean_line = " ".join(parsed_line)
        clean_line = clean_line.replace("[:Nodes {id: ", "").replace(", label: ", "")
        clean_line = clean_line.replace("}]", "").replace("[", "").replace("]", "")
        clean_line = clean_line.replace('"', ' ').strip()  # Eliminar comillas y espacios extra

        # Reducir elementos redundantes como "f97 f97"
        parts = clean_line.split()
        unique_parts = []
        seen = set()
        for part in parts:
            if part not in seen:
                unique_parts.append(part)
                seen.add(part)

        # Agregar la línea limpia y única al conjunto
        lel.add(" ".join(unique_parts))

    # Ordenar las líneas resultantes (opcional) y devolver
    return "\n".join(sorted(lel))

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
    parsed_result = parse_result(raw_result)

    # Guardar los caminos en un archivo separado
    file_path = f"pathConsulta{i+1}"
    try:
        with open(file_path, "w") as file:
            file.write(parsed_result + "\n")
        print(f"Resultados guardados en: {file_path}")
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

    return f"Resultados de la consulta {i+1} guardados en {file_path}\n"

def main():
    queries = read_queries("consultaspathbd03") 
    for i, query in enumerate(queries):
        res = execute_query(i, query)
        print(res)

if __name__ == "__main__":
    main()
