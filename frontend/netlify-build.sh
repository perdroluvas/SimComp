#!/bin/bash

# Aborta o script em caso de erro
set -e

echo "--- Instalando Bun ---"
# Instala o Bun. Você pode fixar uma versão específica se preferir, e.g., ?version=1.0.0
curl -fsSL https://bun.sh/install | bash

# Adiciona o diretório do Bun ao PATH para que o Netlify o encontre
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

echo "--- Verificando a versão do Bun ---"
bun --version

echo "--- Instalando dependências com Bun ---"
# 'bun install' vai usar o bun.lock e instalar as dependências
bun install

echo "--- Executando o build do projeto com Bun ---"
# Seu comando de build que usa o Bun.
# Presumindo que 'bun run build' no seu package.json executa 'build.ts'
bun run build
