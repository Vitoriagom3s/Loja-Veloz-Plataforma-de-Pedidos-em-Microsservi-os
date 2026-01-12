# 🚀 Loja Veloz – Plataforma de Pedidos em Microsserviços

Projeto prático de **Cloud DevOps** que demonstra a entrega contínua de uma aplicação de e-commerce baseada em microsserviços, desde o ambiente local com **Docker Compose** até a operação em **Kubernetes**, incluindo **CI/CD, observabilidade, escalabilidade automática e infraestrutura como código**.

---

## 📌 Contexto do Projeto

A **Loja Veloz** é um e-commerce de médio porte que enfrentava problemas de indisponibilidade em deploys, dificuldade de escalar em picos de acesso e baixa rastreabilidade de falhas entre serviços.  
Este projeto propõe uma **solução cloud-native fim a fim**, alinhada às melhores práticas de DevOps moderno.

---

## 🧱 Arquitetura da Aplicação

A aplicação “Pedidos Veloz” é composta pelos seguintes microsserviços:

- **API Gateway** – Ponto único de entrada HTTP
- **Serviço de Pedidos** – Criação e consulta de pedidos
- **Serviço de Pagamentos** – Integração com gateway externo
- **Serviço de Estoque** – Reserva e baixa de itens
- **Banco de Dados** – PostgreSQL
- **Mensageria (conceitual)** – Eventos de domínio (ex.: `PedidoCriado`)

📐 Estilo arquitetural: **Microserviços Cloud-Native**

---

## 🐳 Ambiente Local – Docker Compose

O ambiente de desenvolvimento local é padronizado utilizando **Docker Compose**, permitindo que todos os serviços sejam iniciados com um único comando.

## 🔹 Benefícios

Ambiente reproduzível

Redução de inconsistências entre máquinas

Onboarding rápido de desenvolvedores

## 📦 Conteinerização

Cada microsserviço possui seu próprio Dockerfile, seguindo boas práticas:

- Imagens base enxutas

- Execução com usuário não-root

- Separação clara de responsabilidades

- Versionamento semântico das imagens (v1.0.0, v1.1.0, etc.)

As imagens podem ser publicadas em:

- Docker Hub

- GitHub Container Registry

## ☸️ Kubernetes – Ambiente de Produção

A aplicação é executada em Kubernetes, utilizando manifests organizados por serviço.

Recursos utilizados:

- Deployment – Gerenciamento de réplicas

- Service – Comunicação interna

- ConfigMap – Configurações não sensíveis

- Secret – Credenciais e dados sensíveis

- Readiness/Liveness Probes – Health checks

- Horizontal Pod Autoscaler (HPA) – Escalabilidade automática

## 🔹 Deploy no cluster
kubectl apply -f k8s/

## 🔁 CI/CD – Integração e Entrega Contínua

O pipeline de CI/CD foi implementado com GitHub Actions, automatizando:

- Build das imagens Docker

- Execução de testes básicos

- Publicação das imagens no registry

- Deploy automatizado no Kubernetes

## 🔐 Segurança

- Secrets armazenados de forma segura no CI

- Nenhuma credencial hardcoded no repositório

## 📈 Estratégia de Deploy e Escalabilidade
🔹 Deploy

- Rolling Update

- Atualizações graduais sem indisponibilidade

🔹 Escalabilidade

- HPA (Horizontal Pod Autoscaler)

- Baseado em consumo de CPU

- Ajuste automático conforme carga

## 👀 Observabilidade

- A observabilidade do sistema é baseada nos três pilares:

📊 Métricas

- Prometheus para coleta

- Grafana para visualização

📜 Logs

- Logs enviados para stdout (12-Factor App)

- Integração futura com Loki ou ELK Stack

🔎 Tracing Distribuído

- OpenTelemetry

- Rastreamento ponta a ponta entre microsserviços

- Base para futura adoção de Service Mesh (Istio)


## 🌍 Infraestrutura como Código (IaC)

A infraestrutura é descrita com Terraform, garantindo:

- Reprodutibilidade

- Versionamento da infraestrutura

- Padronização entre ambientes

- O projeto inclui um esqueleto funcional para criação de namespace e integração com Kubernetes.

## 🎥 Vídeo Pitch

📌 O vídeo de apresentação (até 4 minutos) aborda:

- Visão geral da arquitetura

- Demonstração do ambiente

- Estratégia de CI/CD

- Deploy, observabilidade e escalabilidade

🔗 Link do vídeo: (inserir aqui)

## ✅ Conclusão

A proposta apresentada atende aos objetivos de modernização da Loja Veloz, ao reduzir os riscos durante os processos de deploy, aumentar a escalabilidade da aplicação e melhorar a confiabilidade do ambiente de produção. A integração de Docker, Kubernetes, CI/CD, observabilidade e Infraestrutura como Código demonstra uma abordagem DevOps moderna e alinhada às melhores práticas cloud-native, preparando a empresa para sustentar seu crescimento de forma segura e organizada.

## 
*👩‍💻 Autora: Vitória Gomes*
*📘 Disciplina: Cloud DevOps / Arquitetura Cloud-Native*
*📅 Ano: 2026*

