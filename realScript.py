import subprocess
import sys

# Verificar los argumentos del script
comands = "cypher-shell -u neo4j -p neo4j2024 -f inputWalk"
result = subprocess.run(comands, shell=True, text=True, capture_output=True)
res = result.stdout
er = result.stderr
print (res, er)
