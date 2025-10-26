FROM kalilinux/kali-rolling

ENV NVM_DIR=/root/.nvm
ENV NODE_VERSION=22

ENV N8N_HOST=skita.saveriovale.me
ENV N8N_PROTOCOL=https
ENV WEBHOOK_URL=https://skita.saveriovale.me/
ENV N8N_PROXY_HOPS=1
ENV N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
ENV N8N_RUNNERS_ENABLED=true
# Aggiorna il sistema e installa le dipendenze necessarie
RUN apt update -y

RUN apt install -y \
    curl \
    wget \
    git \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    sudo

WORKDIR /home

# Installa Node.js via NVM e n8n
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && \
    . "$NVM_DIR/nvm.sh" && \
    nvm install $NODE_VERSION && \
    nvm use $NODE_VERSION && \
    npm install -g n8n

RUN echo '#!/bin/bash' > /start.sh && \
    echo 'export NVM_DIR="$NVM_DIR"' >> /start.sh && \
    echo '. "$NVM_DIR/nvm.sh"' >> /start.sh && \
    echo 'nvm use $NODE_VERSION' >> /start.sh && \
    echo 'exec n8n' >> /start.sh && \
    chmod +x /start.sh

# Comando di avvio
CMD ["/bin/bash", "/start.sh"]
