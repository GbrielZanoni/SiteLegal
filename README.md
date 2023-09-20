[![Testes Automátizados](https://github.com/GbrielZanoni/SiteLegal/actions/workflows/testes.yml/badge.svg)](https://github.com/GbrielZanoni/SiteLegal/actions/workflows/testes.yml)

# 🤖 Site Bacana Feito por Mim 🖥️ 

Um site básico feito usando Flask e algumas gambiarras que eu consegui encontrar, muitas delas involvem coisas que eu não sabia que existia no GitHub e que são até que bem úteis. 

## Instalãção

Instalar com o Git:

```
-git clone https://github.com/GbrielZanoni/SiteLegal.git
```

### Rodando o site em um ambiente virtual

Após a instalação expressa do site, é possível rodar ele em um ambiente virtual.
Para a criação do ambiente virtual, é **necessário** utilizar o prompt de comando com o seguinte código: 🖥️

```
python -m venv env
```
### Como o Fluxo de Trabalho funciona?

> De uma forma bem simples! Ele rodará o Pythest que instalará as dependências automáticamente, verificando caso o Python tenha algum update (provavelmente não) e depois executará os arquivos do site, verificando caso há algum erro ou não.

Que irá criar o novo ambiente virtual, então - para inicia-lo ✌️:

Para o Prompt de Comando:
```
.\env\Scripts\Activate.bat
```
Para o Windows PowerShell:
```
.\env\Scripts\Activate.ps1
```
Tenha certeza que o ambiente virtual está ativo, com o comando...
```
(env) C:\Users\Usuário\Desktop\GitClone\NomeSite
```

Tenha em mente que o path do arquivo não importa, porém o ambiente está rodando graças a ao  ***(env)*** no começo do path.

### Instalando dependencias

É necessário instalar as dependências do site, que podem ser facilmente instaladas de forma expressa através do arquivo .txt que está disponível no repositório.

Utilize o Comando:
```
pip install -r requirements.txt
```

E **pronto!** 🙌 Após isso, o usuário pode executar o comando **run.py** e rodar o site localmente;.

## Aqui estão alguns dos objetivos também que precisam ser feitos para o site
   ~~a. Crie um novo repositório no GitHub para o projeto do site estático.~~

  ~~b. Clone o repositório para o seu ambiente de desenvolvimento local.~~
   
   ~~c. Estabeleça uma estrutura básica do projeto, incluindo páginas HTML, estilos CSS e ativos (imagens, ícones etc.).~~

   ~~a. Escolha um gerador de site estático, como Jekyll, Hugo, Gatsby ou Next.js.~~

   ~~b. Desenvolva a estrutura de páginas do seu site, incorporando princípios de reutilização de componentes e templates.~~

   ~~a. Configure um workflow no GitHub Actions para automatizar a construção, testes e implantação do site.~~

   ~~b. Configure o workflow para ser executado em pushes para a branch principal e pull requests.~~

   ~~c. Integre ferramentas de verificação de qualidade de código, como ESLint ou Prettier.~~

   ~~a. Elabore um README.md detalhado com instruções para clonar o projeto, configurar o ambiente local e executar o projeto.~~

  ~~ b. Explique o fluxo de trabalho do GitHub Actions, incluindo como ele constrói, testa e implanta automaticamente o site.~~

   ~~a. Implemente uma versão funcional do seu site, incluindo diferentes páginas e estilos.~~

  ~~b. Crie uma tag para marcar a versão inicial e crie um release no GitHub.~~

**Desafios (opcionais - escolha pelo menos 4):**
   ~~1. **Desafio de Configuração Inicial do GitHub**: Configure um arquivo de configuração `.gitignore` para excluir arquivos desnecessários do repositório.~~
   ~~2. **Desafio de Branch Protegida**: Configure a branch principal como protegida, exigindo revisões de código antes de mesclar pull requests.~~
   3. **Desafio de Fluxo de Trabalho Customizado**: Crie um fluxo de trabalho personalizado no GitHub Actions para um cenário específico do seu projeto.
   4. **Desafio de Rebase Interativo**: Pratique o rebase interativo para consolidar e organizar commits.
   5. **Desafio de Resolução de Conflitos**: Crie um conflito de merge intencionalmente e resolva-o usando as ferramentas do Git.
   6. **Desafio de Dependências Atualizadas**: Configure um fluxo de trabalho para verificar e atualizar automaticamente as dependências do projeto.
   7. **Desafio de Revisão de Código**: Crie uma revisão de código simulada para um pull request, fornecendo comentários construtivos.
   ~~8. **Desafio de Integração com API**: Integre o GitHub Actions com uma API externa, como um serviço de notificação.~~
   9. **Desafio de Configuração de Badge**: Adicione um badge de status do GitHub Actions ao seu README.md para mostrar o status do pipeline.
   10. **Desafio de Integração Contínua Multi-Plataforma**: Configure o pipeline de CI para executar testes em diferentes sistemas operacionais (Linux, Windows, macOS).
   11. **Desafio de Monitoramento de Pull Requests**: Configure um workflow para analisar automaticamente novos pull requests em busca de problemas.
   12. **Desafio de Publicação de GitHub Pages**: Configure o pipeline para publicar automaticamente o site estático no GitHub Pages.
   13. **Desafio de Integração com Chatbot**: Crie um fluxo de trabalho que envie notificações para um chatbot sempre que ocorrerem alterações no repositório.
   14. **Desafio de Testes de Regressão**: Implemente testes de regressão automatizados para garantir que novas alterações não afetem funcionalidades existentes.
   15. **Desafio de Validação de Links**: Crie um script que verifique e reporte links quebrados no seu site estático.
   16. **Desafio de Variáveis de Ambiente**: Utilize variáveis de ambiente no GitHub Actions para armazenar informações sensíveis, como chaves de API.
   17. **Desafio de Análise de Desempenho**: Utilize ferramentas como Lighthouse para avaliar o desempenho do site e implemente otimizações.
   18. **Desafio de Segurança**: Realize uma análise de segurança no código e corrija possíveis vulnerabilidades.
   19. **Desafio de Integração de CDN**: Configure a integração com um serviço de CDN para otimizar a entrega de conteúdo estático.
   20. **Desafio de Redirecionamento 301**: Implemente redirecionamentos 301 para URLs antigas do seu site, mantendo a compatibilidade.
   21. **Desafio de Versionamento Semântico**: Implemente um sistema de versionamento semântico para seu projeto e documente as mudanças em releases.
   22. **Desafio de Ambientes Multi-Estágios**: Configure diferentes ambientes (desenvolvimento, produção etc.) no GitHub Actions.
   23. **Desafio de Integração com Ferramentas de Revisão de Código**: Integre o GitHub Actions com ferramentas de revisão estática de código, como SonarQube.
   24. **Desafio de Autenticação com OAuth**: Configure autenticação OAuth para acessar recursos externos no pipeline de CI/CD.
   25. **Desafio de Integração com Base de Dados**: Crie um fluxo de trabalho que execute testes de integração com uma base de dados.
