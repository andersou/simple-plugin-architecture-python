# README

## Projeto: Arquitetura de Plugins com Python

### Visão Geral

Este projeto explora o desenvolvimento de uma arquitetura plugável utilizando Python, visando reduzir a complexidade de manutenção e aumentar a flexibilidade no desenvolvimento de sistemas modulares e dinâmicos. O objetivo é permitir a adição de novos componentes ou funcionalidades sem alterar a estrutura central do código, tornando o sistema mais robusto e escalável.

### Motivação

Em muitos projetos, é comum a utilização de um "boilerplate" como ponto de partida para o desenvolvimento de novos projetos derivados. Embora essa abordagem funcione bem em certos contextos, ela pode resultar em um "maintenance hell" quando o número de projetos derivados aumenta. Manter 35 ou mais projetos filhos a partir de um projeto pai, por exemplo, pode tornar a correção de bugs ou a adição de novas funcionalidades uma tarefa extremamente trabalhosa.

Uma solução mais eficaz para esse problema é adotar uma arquitetura modular e plugável, que permite o desenvolvimento de novos projetos a partir de um núcleo comum e facilita a replicação de melhorias para todos os projetos derivados.

### Arquitetura de Plugins

A arquitetura proposta utiliza metaclasses e importação dinâmica de módulos para criar um sistema modular que permite a adição de plugins em tempo de execução.

#### Componentes Principais

1. **Metaclasses**: São usadas para criar classes de plugins, permitindo a construção de um repositório que facilita o acesso a todos os plugins disponíveis no sistema.
   
2. **Importação Dinâmica de Módulos**: Utiliza o módulo `importlib` do Python para carregar módulos dinamicamente durante a execução do programa, permitindo a inclusão de novos plugins sem a necessidade de modificar o código base.

### Implementação

A seguir, um resumo dos arquivos e funções principais:

#### `plugin_core.py`

Este arquivo contém a definição da metaclass `PluginRegistryMeta` e da classe base `PluginBase`:

```python
from abc import ABCMeta, abstractmethod

class PluginRegistryMeta(ABCMeta):
    registered_plugins = []

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        if name != "PluginBase":
            print(f"Plugin {name} encontrado")
            PluginRegistryMeta.registered_plugins.append(cls)

class PluginBase(metaclass=PluginRegistryMeta):
    
    @classmethod
    @abstractmethod
    def get_plugin_name() -> str:
        pass
```

#### `main.py`

Este arquivo contém a lógica para buscar e carregar dinamicamente os plugins:

```python
from plugin_core import PluginRegistryMeta
import os
import importlib

def search_for_plugins():
    print("Pesquisando por plugins")
    plugins_path = os.path.join(os.path.dirname(__file__), "plugins")

    if os.path.exists(plugins_path):
        for plugin_dir in os.listdir(plugins_path):
            if not os.path.isdir(os.path.join(plugins_path, plugin_dir)):
                continue
            for plugin_file in os.listdir(os.path.join(plugins_path, plugin_dir)):
                if plugin_file == "plugin.py" or plugin_file == "plugin.pyc":
                    importlib.import_module(f"plugins.{plugin_dir}.plugin")
                    break
    return PluginRegistryMeta.registered_plugins

if __name__ == "__main__":
    plugins = search_for_plugins()
    if len(plugins) == 0:
        print("Nenhum plugin carregado")
    else:
        for plugin in plugins:
            print(f"Plugin {plugin.get_plugin_name()} disponível")
```

### Como Executar

1. **Clone o Repositório**: Clone este repositório em sua máquina local.

2. **Estrutura de Pastas**:
   - Certifique-se de que a pasta `plugins` esteja presente na raiz do projeto.
   - Cada plugin deve estar em seu próprio diretório dentro da pasta `plugins` e deve conter um arquivo `plugin.py`.

3. **Criando Plugins**: Para adicionar um novo plugin:
   - Crie uma nova pasta dentro de `plugins` com o nome do plugin seguido de "-plugin".
   - Adicione um arquivo `plugin.py` contendo uma classe que estenda `PluginBase`.

4. **Executar o Projeto**: Execute o arquivo `main.py` para carregar e listar todos os plugins disponíveis:
   ```bash
   python main.py
   ```

### Exemplo de Saída

```
Pesquisando por plugins
Plugin Project2Plugin encontrado
Plugin Project1Plugin encontrado
Plugin Project2Plugin disponível
Plugin Project1Plugin disponível
```


### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um PR ou sugerir alguma melhoria.
