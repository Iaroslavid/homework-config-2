import argparse
import subprocess
from dependencies import get_dependencies, create_graph
from mermaid import generate_mermaid_code

def visualize_graph(package_name, max_depth, output_path, mermaid_path):
    # Получаем зависимости
    dependencies = get_dependencies(package_name, max_depth)
    
    # Создаем граф
    graph = create_graph(dependencies)

    # Генерируем Mermaid код
    mermaid_code = generate_mermaid_code(graph)

    # Сохраняем Mermaid код в файл
    with open('graph.mmd', 'w') as f:
        f.write(mermaid_code)

    # Визуализируем с помощью mermaid-cli
    try:
        subprocess.run([mermaid_path, 'graph.mmd', '-o', output_path], check=True)
        print(f"Граф успешно сохранен в {output_path}")
    except subprocess.CalledProcessError:
        print("Ошибка при рендеринге графа.")

def main():
    parser = argparse.ArgumentParser(description="Визуализатор графа зависимостей пакетов Alpine Linux")
    parser.add_argument("package", help="Имя анализируемого пакета")
    parser.add_argument("max_depth", type=int, help="Максимальная глубина анализа зависимостей")
    parser.add_argument("output_path", help="Путь к файлу с изображением графа")
    parser.add_argument("mermaid_path", help="Путь к программе для визуализации графов")

    args = parser.parse_args()

    visualize_graph(args.package, args.max_depth, args.output_path, args.mermaid_path)

if __name__ == '__main__':
    main()
