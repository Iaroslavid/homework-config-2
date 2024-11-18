import pytest
from dependencies import get_dependencies, create_graph
from mermaid import generate_mermaid_code

def test_get_dependencies():
    dependencies = get_dependencies('bash', max_depth=2)
    assert isinstance(dependencies, set)
    assert ('bash', 'libc') in dependencies

def test_create_graph():
    dependencies = {('bash', 'libc'), ('bash', 'coreutils')}
    graph = create_graph(dependencies)
    assert graph.number_of_nodes() == 3
    assert graph.number_of_edges() == 2

def test_generate_mermaid_code():
    from networkx import DiGraph
    graph = DiGraph()
    graph.add_edges_from([('bash', 'libc'), ('bash', 'coreutils')])
    mermaid_code = generate_mermaid_code(graph)
    assert "bash -->|depends on| libc,coreutils" in mermaid_code
