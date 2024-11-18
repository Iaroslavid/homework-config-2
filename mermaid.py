def generate_mermaid_code(graph):
    """
    Генерирует описание графа в формате Mermaid.
    """
    mermaid_code = "graph TD\n"
    for node in graph.nodes:
        mermaid_code += f"    {node} -->|depends on| {','.join(graph.neighbors(node))}\n"
    return mermaid_code
