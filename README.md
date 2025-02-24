# 🔹Configuração de Servidor Web com Monitoramento

### Objetivo: 
Desenvolver habilidades em Linux, AWS e automação de processos para configurar um ambiente de servidor web monitorado.

### 📌 Tecnologias

- **Python** – Linguagem usada para criar o script de monitoramento.
- **Requests** – Biblioteca para fazer requisições HTTP e verificar o status do site.
- **Logging** – Utilizada para registrar logs das verificações do site.
- **Discord Webhook** – Usada para enviar alertas de status do site.
- **Crontab (Linux)** – Ferramenta de agendamento de tarefas para execução periódica do script.
- **SSH** – Protocolo para acesso remoto ao servidor e configurações.
- **IA (Blackbox, ChatGPT, Claude)** – Ferramentas de IA para consultas e automação de processos.

### 📌  Infraestrutura

- **Ubuntu (Linux)** – Sistema operacional utilizado no servidor.
- **Nginx** – Servidor web para hospedar o site monitorado.
- **AWS EC2** – Plataforma de computação em nuvem para hospedagem do site e execução do script.
- **VPC (AWS)** – Rede privada virtual para isolar a infraestrutura do servidor.


---
## 🔹 Tela Inicial da AWS  

Ao acessar o **Console da AWS**, a primeira tela exibida é o **Painel de Gerenciamento**. Nele, você encontra um conjunto de serviços essenciais organizados de forma intuitiva.  

### 📌 Elementos Principais:  
- **Barra de Pesquisa (`Search AWS Services`)**  
  - Permite buscar rapidamente qualquer serviço disponível na AWS.  
  - Você pode utilizá-la para acessar diretamente a criação de uma **VPC** ou uma **Instância EC2**, digitando `"VPC"` ou `"EC2"` e clicando na opção correspondente.  

- **Serviços Recentes**  
  - Exibe atalhos para os serviços mais utilizados recentemente.  

- **Painel de Recursos**  
  - Apresenta um resumo dos principais serviços em uso, incluindo instâncias **EC2**, bancos de dados **RDS** e configurações de rede.  

- **Navegação Global**  
  - No canto superior direito, há opções para gerenciar sua conta, acessar a fatura e alterar a região da AWS.  
## 🔹 Interface Inicial da AWS  

Ao acessar sua conta na **AWS**, esta é a interface inicial exibida:  

![Image](https://github.com/user-attachments/assets/c72a8abb-1078-46b3-a6af-3b33953e2b01) 
 
A **barra de pesquisa** permite acessar rapidamente os serviços necessários para a criação do nosso projeto. Basta digitar **"VPC"** ou **"EC2"** para ser direcionado diretamente à área de configuração desses recursos, iniciando assim o processo de implantação.  

![Image](https://github.com/user-attachments/assets/72162e20-afef-48a8-9395-8a4fae4a197c)


## 1️⃣ Criando uma VPC na AWS
A **VPC (Virtual Private Cloud)** é uma rede virtual na AWS que permite isolar e organizar seus recursos de forma segura.

### 📌 Passos:

1. **Acesse o Console da AWS**  
   - Vá para o serviço **VPC** no painel da AWS.

2. **Crie uma nova VPC**  
   - Clique em **Criar VPC** e escolha um nome.
   - Escolha um **IPv4 CIDR Block** (exemplo: `10.0.0.0/16`).

![Image](https://github.com/user-attachments/assets/5144b4ed-a137-46af-9b79-ce4a5829c87f)

3. **Criar Sub-redes**  
   - **Duas sub-redes públicas** (para acesso externo).  
     - Exemplo: `10.0.1.0/24` e `10.0.2.0/24`  
   - **Duas sub-redes privadas** (para futuras expansões).  
     - Exemplo: `10.0.3.0/24` e `10.0.4.0/24`  

![Image](https://github.com/user-attachments/assets/5fa0d58f-182e-4691-97da-c918a331b0a8)


---

## 2️⃣ Criando um Grupo de Segurança na AWS EC2 


### 📌 Passos:

1. **Acesse a AWS Console** e vá para o serviço **EC2**.
2. No menu lateral, clique em **Security Groups** (Grupos de Segurança).
3. Clique em **Create Security Group** (Criar Grupo de Segurança).
4. Preencha os campos:
   - **Name**: Nome do grupo de segurança (exemplo: `meu-grupo-seguranca`).
   - **Description**: Uma descrição do grupo.
    ![Image](https://github.com/user-attachments/assets/c5e29afb-c56b-4009-8910-d5d321af62b3)
   - **VPC**: Escolha a VPC onde ele será vinculado(neste caso a que criamos anteriormente).
  ![Image](https://github.com/user-attachments/assets/6a97bab7-6953-42fd-a8d5-b7549ec8c8be)
     
5. **Adicione regras de entrada (Inbound Rules)**:
   - Clique em **Add Rule**.

     ![Image](https://github.com/user-attachments/assets/91cea99d-1865-4589-a198-2f96588865c2)
   - Escolha um protocolo, porta e origem (por exemplo, **SSH (porta 22, IP específico)**).
6. **Adicione regras de saída (Outbound Rules)** (por padrão, todas são liberadas).
7. Clique em **Create Security Group**.




## 2️⃣ Criando uma Instância EC2

A **EC2 (Elastic Compute Cloud)** é um servidor virtual na nuvem.

### 📌 Passos:

1. **Acesse o Console da AWS**  
   - Vá até o serviço **EC2** e clique em **Executar instância**.

2. **Escolha uma AMI (Imagem do Servidor)**  
   - Escolha um sistema operacional Linux, como:  
**Ubuntu**, **Debian** ou **Amazon Linux**. ( a escolha para o projeto foi **Ubuntu** )

    ![Image](https://github.com/user-attachments/assets/fbb681bc-78cf-459e-bc26-7d0bd538a458)

3. **Configurar Rede**  
   - Escolha a **VPC** criada anteriormente.  
   - Selecione uma das **sub-redes públicas**.  

4. **Configurar Segurança**  
   - Crie um **Security Group** permitindo:  
     - **HTTP (porta 80)** → Para acesso ao servidor via navegador.  
     - **SSH (porta 22)** → Para conexões remotas (opcional).
     - Na situação atual já foi realizada a criação do nosso security group, só precisamos vincular agora.
 ![Image](https://github.com/user-attachments/assets/c437eebf-21ae-46fd-9664-a74cafb73fbb)

5. **Escolha o tipo de instância**  
   - Para testes, selecione uma opção gratuita, como **t2.micro**.
    
![Image](https://github.com/user-attachments/assets/59ef57c8-5117-4492-8e9e-32f56ed91fdb)

6. **Criar e associar um IP público**  
   - Em **Elastic IPs**, aloque um IP e associe à instância EC2.

---

## 3️⃣ Acessando a Instância via SSH

Após iniciar a instância, você pode acessá-la pelo terminal.

### 📌 Passos:

1. **Obtenha o IP da instância**  
   - No console da AWS, copie o **Endereço IPv4 Público** da EC2.

2. **Conectar via SSH**  
   - No terminal (Linux/Mac) execute:  

   ```sh
   ssh -i "seu-arquivo.pem" ubuntu@ip_da_instancia
   ```

### 🔹 Agora estamos dentros da nossa EC2
![Image](https://github.com/user-attachments/assets/fd75df3d-b997-40e9-a8fb-d15c91ddb6f8)
---
### 💡 Dica  

Uma dica é sempre buscar as últimas atualizações e comandos recomendados ao iniciar um processo de instalação de pacotes. Como vamos seguir com a instalação do Nginx, primeiro atualize os pacotes disponíveis no sistema:  

```bash
sudo apt update && sudo apt upgrade -y
```

![Image](https://github.com/user-attachments/assets/409f8ada-f376-443a-82dd-bc8ddf494842)

## 4️⃣ Acesso e Instalação do Nginx via SSH  

Este passo a passo foi utilizado para acessar meu servidor via SSH, instalar o Nginx e realizar algumas configurações básicas para o projeto.  

### 📌 Instalação do Nginx  

Atualize os pacotes e instale o Nginx com o seguinte comando:  

```bash
sudo apt update && sudo apt install nginx -y
```
![Image](https://github.com/user-attachments/assets/e6227726-d5a0-4657-80fb-560a8164f0e5)

📌 Verificação do Serviço
Após a instalação, verifique se o Nginx está rodando:


```bash
sudo systemctl status nginx
```
![Image](https://github.com/user-attachments/assets/ddc8728c-d7d1-4037-a5b1-5aebcb678c5c)

Caso o serviço não esteja ativo, inicie-o com:

```bash
sudo systemctl start nginx
```


Para garantir que o Nginx inicie automaticamente ao ligar o servidor, utilize:

```bash
sudo systemctl enable nginx
```
![Image](https://github.com/user-attachments/assets/3db2523e-0eaa-4183-98dd-6d4a8771a9fb)

## Essa incialmente será a interface que o site vai apresentar ao acessar pelo navegador:

![Image](https://github.com/user-attachments/assets/af787c1b-65e1-4f33-8e3f-d7a62792f7f2)
---
## 5️⃣ Como Editar e Estilizar o HTML do Seu Site no Nginx
Agora podemos editar o arquivo HTML do site, que está sendo servido pelo Nginx, fazendo uma estilização básica.

### 📌 Localizando o Arquivo HTML

O arquivo HTML do seu site está localizado no diretório configurado como **`root`** no arquivo de configuração do Nginx. No meu caso, a raiz estava configurada para **`/usr/share/nginx/html`**.

### 📌 Editando o Arquivo HTML

Para editar o arquivo **`index.html`** dentro de **`/usr/share/nginx/html`**, siga os seguintes passos:

Abra o terminal e execute o seguinte comando para editar o arquivo com o **nano** (um editor de texto no terminal):

```bash
sudo nano /usr/share/nginx/html/index.html
```

Dentro do arquivo `index.html`, você pode adicionar ou modificar o código HTML do seu site conforme suas preferências.

### 📌 Exemplo de código HTML:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Servidor web na AWS com Nginx.">
    <meta name="keywords" content="AWS, Nginx, EC2">
    <title>Servidor Web AWS</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 20px; }
        h1, h2 { color: #333; }
        a { color: #007BFF; text-decoration: none; }
        a:hover { text-decoration: underline; }
        section { background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        img { max-width: 100%; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Servidor Web na AWS com Nginx</h1>
    <p>Projeto com Nginx, EC2.</p>

    <section>
        <h2>Sobre</h2>
        <p>Servidor web na AWS com Nginx e monitoramento.</p>
    </section>

    <section>
        <h2>Funcionalidades</h2>
        <ul>
            <li>Hospedagem de sites</li>
            <li>Monitoramento em tempo real</li>
        </ul>
    </section>

    <section>
        <h2>Os primeiros Passos:</h2>
        <ol>
            <li>Configure AWS</li>
            <li>Inicie EC2 e Nginx</li>
        </ol>
    </section>

    <section>
        <h2>Contato</h2>
        <p>Email: <a href="mailto:debora.emaildecontato.com.br">debora.emaildecontato.com.br</a></p>
    </section>
</body>
</html>
```

### 📌 Salvando as Alterações

Após editar o arquivo `index.html`, siga os passos abaixo para salvar:

1. Pressione **`CTRL + X`** para sair do editor.
2. Quando solicitado, pressione **`Y`** para confirmar as alterações.
3. Pressione **`Enter`** para salvar o arquivo.


### Com as alteraçãoes realizadas no arquivo **`index.html`** do site como no exemplo acima, eu gerei essa nova interface:

![Image](https://github.com/user-attachments/assets/1d66a9fe-a048-4424-8383-7516bdf6f5f8)
---

## 6️⃣ Monitoramento de Site com Python e Discord Webhook

## Passo 1: Criar o Diretório e o Arquivo
Crie um diretório para armazenar o script:
```bash
mkdir -p /home/ubuntu/
cd /home/ubuntu/
```
Agora, crie o arquivo `monitoramento.py`:
```bash
touch monitoramento.py
```

## Passo 2: Criação do Script com o Código (meu exemplo com python)
Construa um codigo que atenda as necessidades do seu monitoramento, no meu caso utilizei **`python`**, mas pode ser feito em **`bash`** também, logo depois cole código como no exemplo utilizado abaixo:

```python
import requests
import logging
import os

# Configuração do log
log_file = "/home/ubuntu/monitoramento.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Webhook do Discord
webhook_url = "https://discord.com/api/webhook/o_link_do_seu_webhook_aqui"

# URL do site a ser monitorado
site_url = "http://ip_da_sua_instancia/"

# Arquivo para armazenar o último status do site
status_file = "/home/ubuntu/ultimo_status.txt"

def enviar_notificacao_discord(mensagem):
    payload = {"content": mensagem}
    requests.post(webhook_url, json=payload)

def verificar_site():
    try:
        resposta = requests.get(site_url)
        site_ok = resposta.status_code == 200
    except requests.RequestException:
        site_ok = False

    # Lendo o último status salvo
    if os.path.exists(status_file):
        with open(status_file, "r") as f:
            ultimo_status = f.read().strip()
    else:
        ultimo_status = "desconhecido"

    # Comparando o status atual com o último salvo
    if site_ok and ultimo_status == "offline":
        mensagem = f"✅ O site {site_url} voltou ao ar!"
        logging.info(mensagem)
        enviar_notificacao_discord(mensagem)
    elif not site_ok and ultimo_status == "online":
        mensagem = f"🚨 Alerta! O site {site_url} caiu!"
        logging.warning(mensagem)
        enviar_notificacao_discord(mensagem)

    # Salvando o status atual
    with open(status_file, "w") as f:
        f.write("online" if site_ok else "offline")

if __name__ == "__main__":
    verificar_site()
```

## Passo 3: Salvar e Sair
Para salvar e sair do nano:
1. Pressione `CTRL + X`
2. Pressione `S` para salvar
3. Pressione `Enter` para confirmar

## Passo 4: Testar Manualmente
Execute o script manualmente para testar:
```bash
python3 /home/ubuntu/monitoramento.py
```
Se o site estiver no ar, nada será enviado ao Discord.
Se o site estiver fora do ar, o alerta será enviado ao Discord.

## Passo 5: Configurar para Rodar Automaticamente (Crontab)
Abra o crontab para edição:
```bash
crontab -e
```
Se for a primeira vez, ele pode perguntar qual editor usar. Escolha `nano`.

Adicione esta linha no final do arquivo:
```bash
* * * * * /usr/bin/python3 /home/ubuntu/monitoramento.py
```
Isso executa o script a cada 1 minuto.

Salvar e sair:
1. Pressione `CTRL + X`
2. Pressione `S` e `Enter`

## Passo 6: Verificar se Está Rodando
Para ver se o cron está rodando corretamente, rode:
```bash
tail -f /home/ubuntu/monitoramento.log
```
Isso mostrará os logs do script em tempo real.

Para listar os processos do cron rodando no sistema:
```bash
ps aux | grep cron
```
Para listar as tarefas do crontab registradas:
```bash
crontab -l
```
Confirme que a linha com `monitoramento.py` está lá.

## Passo 7: Testar Alertas Automaticamente
Desligue o Nginx para simular uma falha:
```bash
sudo systemctl stop nginx
```
O Discord deve receber um alerta 🚨 "O site caiu!"

![Image](https://github.com/user-attachments/assets/3873c0d4-6f66-4517-9014-91573b12d1a2)

Ligue o Nginx novamente:
```bash
sudo systemctl start nginx
```
O Discord deve receber ✅ "O site voltou ao ar!"

![Image](https://github.com/user-attachments/assets/ccccfae0-756b-4294-bec7-deec219e20cd)

Para conferir os registro de Log:

````bash
cat /var/log/monitoramento.log
`````
![Image](https://github.com/user-attachments/assets/cb48075a-0199-4335-ba00-2eb038615dec)


---
## ✅ Conclusão
Este documento fornece um teste de conhecimentos basicos como forma de  criar um passo a passo que te possibilite configurar uma **VPC**, lançar uma **instância EC2**, instalar **Nginx**, personalizar um site e automatizar tarefas criando alertas vinculadas a uma API garantindo notificações rápidas no Discord em caso de falhas. 🚀
#
