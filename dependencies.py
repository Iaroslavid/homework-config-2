import subprocess
import networkx as nx

def get_dependencies(package_name, max_depth):
    """
    Получает зависимости пакета и его транзитивные зависимости.
    """
    dependencies = set()
    visited = set()

    def fetch_deps(pkg, depth):
        if depth > max_depth or pkg in visited:
            return
        visited.add(pkg)
        try:
            result = subprocess.check_output(['apk', 'info', '--depends', pkg], text=True)
            deps = result.strip().split('\n')
            for dep in deps:
                if dep:
                    dependencies.add((pkg, dep))
                    fetch_deps(dep, depth + 1)
        except subprocess.CalledProcessError:
            pass

    fetch_deps(package_name, 0)
    return dependencies

def create_graph(dependencies):
    """
    Создает граф зависимостей с помощью networkx.
    """
    G = nx.DiGraph()
    for dep in dependencies:
        G.add_edge(dep[0], dep[1])
    return G
