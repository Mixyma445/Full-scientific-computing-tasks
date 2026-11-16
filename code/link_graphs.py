import os

docs_dir = 'docs'
for filename in sorted(os.listdir(docs_dir)):
    if filename.endswith('.md'):
        md_path = os.path.join(docs_dir, filename)
        graph_name = filename.replace('.md', '_graph.png')
        graph_path = os.path.join(docs_dir, graph_name)
        
        if os.path.exists(graph_path):
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            img_reference = f"\n\n## Graph Visualization\n![{filename[:-3]} Graph]({graph_name})\n"
            if graph_name not in content:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content + img_reference)
                print(f"Linked {graph_name} into {filename}")