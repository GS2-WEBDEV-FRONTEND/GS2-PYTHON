


"""
Global Solution 2025 – Python
Tema: Futuro do Trabalho

Integrantes:
- Nome 1 – RM
- Nome 2 – RM
- Nome 3 – RM

Descrição:
Este programa consome a API JSearch (via RapidAPI) para buscar vagas de emprego
relacionadas ao Futuro do Trabalho, filtra profissões promissoras, exibe dados
relevantes e calcula a soma das taxas de crescimento usando recursão.

Requisitos atendidos:
- Uso de funções
- Acesso a API com requests
- Manipulação de JSON e dicionários
- Estruturas de repetição
- Função recursiva
- Tratamento de exceções
"""

import requests
from typing import List, Dict, Any, Optional


# ============================
# Questão 1 – Acessando a API
# ============================

def adaptar_resposta_api(dados_api: Any) -> List[Dict[str, Any]]:
    """
    Converte o JSON da JSearch para o formato padronizado da GS.

    A JSearch não traz taxa de crescimento real, então criamos
    uma regra simples baseada em salário (apenas para fins didáticos).
    """

    lista_final: List[Dict[str, Any]] = []

    # Na JSearch, os resultados vêm geralmente em "data"
    itens = dados_api.get("data", [])

    for job in itens:
        # Lê salários mínimo e máximo, se existirem
        min_salary = job.get("job_min_salary") or 0
        max_salary = job.get("job_max_salary") or min_salary

        # Calcula um salário médio aproximado
        if min_salary or max_salary:
            salario_medio = (min_salary + max_salary) / 2
        else:
            salario_medio = 0.0

        
        if salario_medio >= 120000:
            taxa_crescimento = 12.5
        elif salario_medio >= 80000:
            taxa_crescimento = 9.0
        else:
            taxa_crescimento = 5.0

        profissao = {
            "nome": job.get("job_title", "Não informado"),
            "setor": job.get("job_employment_type", "Não informado"),
            "habilidades": job.get("job_required_skills", []),
            "taxa_crescimento": float(taxa_crescimento),
            "localizacao": job.get("job_city", "Não informado"),
            "salario_medio": float(salario_medio),
        }

        lista_final.append(profissao)

    return lista_final


def obter_tendencias_emprego(profissao_busca: str) -> List[Dict[str, Any]]:
    """
    Faz requisição real para a API JSearch e retorna lista de profissões,
    usando o termo digitado pelo usuário como base da busca.

    Retorna:
        Lista de dicionários, cada um representando uma profissão.
    """

def obter_tendencias_emprego(profissao_busca: str) -> List[Dict[str, Any]]:
    """
    Faz requisição real para a API JSearch usando o cURL funcional enviado.
    """

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": f"{profissao_busca} jobs in USA",
        "page": "1",
        "num_pages": "1",
        "country": "us",
        "language": "python",
        "date_posted": "all"
    }

    headers = {
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
        "x-rapidapi-key": "e9000e1a8emsh1c8e3458d663a1cp1f98a4jsnc896f75f5cc2"
    }

    try:
        resposta = requests.get(url, headers=headers, params=querystring, timeout=10)
        resposta.raise_for_status()

        dados_json = resposta.json()
        return adaptar_resposta_api(dados_json)

    except Exception as exc:
        print(f"Erro ao acessar a API: {exc}")
        print("Usando dados simulados para não quebrar a GS.\n")

        return [
            {
                "nome": "Python Developer",
                "setor": "FULLTIME",
                "habilidades": ["Python", "APIs", "Banco de Dados"],
                "taxa_crescimento": 12.5,
                "localizacao": "Remote",}

        ]   


# ============================
# Questão 2 – Filtrando profissões
# ============================

def filtrar_profissoes(
    profissoes: List[Dict[str, Any]],
    termo_busca: Optional[str] = None,
    crescimento_minimo: float = 0.0,
) -> List[Dict[str, Any]]:
    """
    Filtra a lista de profissões com base em:
    - termo de busca no nome da profissão (opcional)
    - taxa mínima de crescimento (em %)

    Consideramos "promissoras" as profissões que:
    - Contêm o termo no nome (se termo_busca for fornecido)
    - Possuem taxa_crescimento >= crescimento_minimo
    """

    termo_busca_lower = termo_busca.lower() if termo_busca else None
    filtradas: List[Dict[str, Any]] = []

    for profissao in profissoes:
        nome = profissao.get("nome", "").lower()
        taxa = float(profissao.get("taxa_crescimento", 0.0))

        # Se tiver termo de busca e ele não estiver no nome, pula
        if termo_busca_lower and termo_busca_lower not in nome:
            continue

        # Se não atingir a taxa mínima, pula
        if taxa < crescimento_minimo:
            continue

        filtradas.append(profissao)

    return filtradas


# ============================
# Questão 3 – Recursão
# ============================

def calcular_crescimento_total(
    profissoes: List[Dict[str, Any]],
    indice: int = 0,
) -> float:
    """
    Função recursiva que calcula a soma total das taxas
    de crescimento das profissões da lista.

    Caso base:
        - Quando indice >= len(profissoes), retorna 0.

    Passo recursivo:
        - Soma a taxa da profissão atual com o resultado
          da chamada para o próximo índice.
    """
    if indice >= len(profissoes):
        return 0.0

    taxa_atual = float(profissoes[indice].get("taxa_crescimento", 0.0))
    return taxa_atual + calcular_crescimento_total(profissoes, indice + 1)


# ============================
# Questão 4 – Exibição de dados
# ============================

def exibir_profissoes(profissoes: List[Dict[str, Any]]) -> None:
    """
    Exibe no console os dados relevantes de cada profissão,
    utilizando um laço for.
    """

    if not profissoes:
        print("Nenhuma profissão encontrada com os critérios informados.")
        return

    for i, profissao in enumerate(profissoes, start=1):
        print("-" * 60)
        print(f"Profissão #{i}")
        print(f"Nome: {profissao.get('nome', 'Não informado')}")
        print(f"Setor: {profissao.get('setor', 'Não informado')}")
        print(f"Localização: {profissao.get('localizacao', 'Não informado')}")
        print(f"Taxa de crescimento: {profissao.get('taxa_crescimento', 0.0):.2f}%")

        habilidades = profissao.get("habilidades", [])
        if habilidades:
            print(f"Habilidades-chave: {', '.join(habilidades)}")

        salario = profissao.get("salario_medio")
        if salario and salario > 0:
            # Formatação simples em estilo brasileiro
            salario_str = f"{salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            print(f"Salário médio (estimado): R$ {salario_str}")

    print("-" * 60)


# ============================
# Questão 5 – Programa principal
# ============================

def main() -> None:
    print("=" * 60)
    print(" FUTURO DO TRABALHO – TENDÊNCIAS DE EMPREGO ")
    print("=" * 60)

    # Profissão base utilizada para montar a query na JSearch
    profissao_base = input(
        "Digite a profissão que você quer pesquisar em inglês "
        "(ex: data analyst, python developer): "
    ).strip()

    if not profissao_base:
        print("Você não digitou uma profissão. Encerrando o programa.")
        return

    # Obtém tendências de emprego via API
    profissoes = obter_tendencias_emprego(profissao_base)

    if not profissoes:
        print("Não foi possível carregar as tendências de emprego. Tente novamente mais tarde.")
        return

    print(f"\nTotal de vagas retornadas pela API para '{profissao_base}': {len(profissoes)}\n")

    # Opção de usar outro termo para filtrar pelo nome da profissão
    usar_outro_termo = input(
        "Deseja usar outro termo para filtrar pelo nome da profissão? (s/n): "
    ).strip().lower()

    if usar_outro_termo == "s":
        termo_filtro = input("Digite a palavra-chave para filtrar pelo nome da profissão: ").strip()
        termo_para_filtro: Optional[str] = termo_filtro if termo_filtro else None
    else:
        # Reaproveitamos a própria profissão base como filtro
        termo_para_filtro = profissao_base

    # Lê taxa mínima de crescimento
    try:
        entrada_crescimento = input(
            "Taxa mínima de crescimento em % (ex: 5). Deixe vazio para 0: "
        ).strip()
        crescimento_minimo = float(entrada_crescimento) if entrada_crescimento else 0.0
    except ValueError:
        print("Valor inválido para a taxa mínima, usando 0%.")
        crescimento_minimo = 0.0

    # Filtra profissões promissoras
    profissoes_filtradas = filtrar_profissoes(
        profissoes,
        termo_busca=termo_para_filtro,
        crescimento_minimo=crescimento_minimo,
    )

    print("\nProfissões promissoras encontradas:\n")
    exibir_profissoes(profissoes_filtradas)

    # Calcula soma total das taxas de crescimento (recursivo)
    soma_crescimento = calcular_crescimento_total(profissoes_filtradas)
    print(f"\nSoma total das taxas de crescimento das profissões filtradas: {soma_crescimento:.2f}%\n")


if __name__ == "__main__":
    main()

