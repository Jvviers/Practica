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
