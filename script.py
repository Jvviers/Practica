from neo4j import GraphDatabase
import sys

# Verificar los argumentos del script
if len(sys.argv) < 5:
    print("uso: python3 execute.py [neo4j_uri] [username] [password] [input_file] [output_file]")
    sys.exit(1)

# Variables clave
neo4j_uri = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
input_file = sys.argv[4]
output_file = sys.argv[5]

# Leer las consultas desde un archivo
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

# Ejecutar consultas en Neo4j
def execute_query(driver, query):
    try:
        with driver.session() as session:
            result = session.run(query)
            count = result.consume().counters.nodes_created  # Cambia según lo que necesites contar
            return count, 0  # Tiempo de ejecución no es nativo aquí
    except Exception as e:
        print(f"Error al ejecutar la consulta: {query}")
        print(e)
        return "ERROR", "N/A"

# Guardar resultados en un archivo
def save_results(results, file_path):
    try:
        with open(file_path, "w") as file:
            file.writelines(results)
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
        sys.exit(1)

# Conexión y ejecución de consultas
def main():
    queries = read_queries(input_file)
    results = []
    driver = GraphDatabase.driver(neo4j_uri, auth=(username, password))

    try:
        for i, query in enumerate(queries, start=1):
            print(f"Ejecutando consulta {i}: {query}")
            count, exec_time = execute_query(driver, query)
            results.append(f"{i} {query} COUNT: {count} TIME: {exec_time}s\n")

        save_results(results, output_file)
        print(f"Consultas ejecutadas. Resultados guardados en: {output_file}")
    finally:
        driver.close()

if __name__ == "__main__":
    main()
