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
    lel = []
    parsed_lines = []
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
            else:
                parsed_line.append(f"[{element.strip()}]")

        parsed_lines.append(" ".join(parsed_line))

        for idx, line in enumerate(parsed_lines):
            # print(line)
            line = line.replace("[:Nodes {id: ", "")
            line = line.replace(", label: ", "")
            line = line.replace("}]", "")
            line = line.replace("[", "")
            line = line.replace("]", "")
            line.replace('"', "")
            # print (line)
            xd = line.split(" ")
            res = []
            for i in xd:
                if i not in res:
                    res.append(i)
            line = " ".join(res)
            lel.append(line)
            
    
    return "\n".join(lel)

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
