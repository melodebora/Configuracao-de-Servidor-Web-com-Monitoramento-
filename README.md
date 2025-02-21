# Configuração de Servidor Web com Monitoramento 

 ### Objetivo deste Projeto: 
Desenvolver e testar habilidades em 
Linux, AWS e automação de processos 
através da configuração de um ambiente 
de servidor web monitorado. 

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

![Tela Inicial da AWS](inicialAWS.png)  
 
A **barra de pesquisa** permite acessar rapidamente os serviços necessários para a criação do nosso projeto. Basta digitar **"VPC"** ou **"EC2"** para ser direcionado diretamente à área de configuração desses recursos, iniciando assim o processo de implantação.  

![alt text](procurando.png)


## 1️⃣ Criando uma VPC na AWS
A **VPC (Virtual Private Cloud)** é uma rede virtual na AWS que permite isolar e organizar seus recursos de forma segura.

### 📌 Passos:

1. **Acesse o Console da AWS**  
   - Vá para o serviço **VPC** no painel da AWS.

2. **Crie uma nova VPC**  
   - Clique em **Criar VPC** e escolha um nome.
   - Escolha um **IPv4 CIDR Block** (exemplo: `10.0.0.0/16`).

![alt text](vpc.png)

3. **Criar Sub-redes**  
   - **Duas sub-redes públicas** (para acesso externo).  
     - Exemplo: `10.0.1.0/24` e `10.0.2.0/24`  
   - **Duas sub-redes privadas** (para futuras expansões).  
     - Exemplo: `10.0.3.0/24` e `10.0.4.0/24`  

![alt text](subredes.png)
4. **Criar e anexar um Internet Gateway**  
   - Vá até **Internet Gateways** → **Criar Internet Gateway**.  
   - Após criar, **anexe à VPC** criada. 

![alt text](image.png)

5. **Criar Tabela de Rotas**  
   - Modifique a tabela de rotas das sub-redes públicas para permitir tráfego externo.  
   - Adicione uma regra:  
    - Destino: `0.0.0.0/0`  
    - Alvo: **Internet Gateway** criado.

  ![alt text](rotas.png)
---

## 2️⃣ Criando uma Instância EC2

A **EC2 (Elastic Compute Cloud)** é um servidor virtual na nuvem.

### 📌 Passos:

1. **Acesse o Console da AWS**  
   - Vá até o serviço **EC2** e clique em **Executar instância**.

2. **Escolha uma AMI (Imagem do Servidor)**  
   - Escolha um sistema operacional Linux, como:  
**Ubuntu**, **Debian** ou **Amazon Linux**. ( a escolha para o projeto foi **Ubuntu** )

    ![alt text](ami.png)

3. **Configurar Rede**  
   - Escolha a **VPC** criada anteriormente.  
   - Selecione uma das **sub-redes públicas**.  

4. **Configurar Segurança**  
   - Crie um **Security Group** permitindo:  
     - **HTTP (porta 80)** → Para acesso ao servidor via navegador.  
     - **SSH (porta 22)** → Para conexões remotas (opcional).  

5. **Escolha o tipo de instância**  
   - Para testes, selecione uma opção gratuita, como **t2.micro**.
![alt text](t2micro.png)

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
![alt text](dentroEC2.png)
---
### 💡 Dica  

Uma dica é sempre buscar as últimas atualizações e comandos recomendados ao iniciar um processo de instalação de pacotes. Como vamos seguir com a instalação do Nginx, primeiro atualize os pacotes disponíveis no sistema:  

```bash
sudo apt update && sudo apt upgrade -y
```

![alt text](upgrade.png)

## 4️⃣ Acesso e Instalação do Nginx via SSH  

Este passo a passo foi utilizado para acessar meu servidor via SSH, instalar o Nginx e realizar algumas configurações básicas para o projeto.  

### 📌 Instalação do Nginx  

Atualize os pacotes e instale o Nginx com o seguinte comando:  

```bash
sudo apt update && sudo apt install nginx -y
```
![alt text](instalarNginx.png)
📌 Verificação do Serviço
Após a instalação, verifique se o Nginx está rodando:


```bash
sudo systemctl status nginx
```
![alt text](nginxRodando.png)

Caso o serviço não esteja ativo, inicie-o com:

```bash
sudo systemctl start nginx
```


Para garantir que o Nginx inicie automaticamente ao ligar o servidor, utilize:

```bash
sudo systemctl enable nginx
```
![alt text](nginxAutomatico.png)
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
    <title>My Space</title>
    <style>
        body {
            background-color: #f4f4f9;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #2c3e50;
        }
        p {
            font-size: 18px;
            color: #34495e;
        }
    </style>
</head>
<body>
    <h1>Bem-vindo ao Meu Site!</h1>
    <p>Este é um exemplo de site básico configurado com o Nginx.</p>
</body>
</html>
```

### 📌 Salvando as Alterações

Após editar o arquivo `index.html`, siga os passos abaixo para salvar:

1. Pressione **`CTRL + X`** para sair do editor.
2. Quando solicitado, pressione **`Y`** para confirmar as alterações.
3. Pressione **`Enter`** para salvar o arquivo.

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

## Passo 2: Substituir o Código
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

![alt text](alertaCaiu-1.png)

Ligue o Nginx novamente:
```bash
sudo systemctl start nginx
```
O Discord deve receber ✅ "O site voltou ao ar!"

![alt text](alertaVoltou-1.png)

Para conferir os registro de Log:

````bash
cat /var/log/monitoramento.log
`````
![alt text](registrosLog.png)

# Tecnologias Utilizadas

## 📌 Linguagem de Programação
- **Python** – Utilizado para desenvolver o script de monitoramento.

## 📌 Bibliotecas Python
- **Requests** – Para fazer requisições HTTP e verificar o status do site.
- **Logging** – Para registrar logs das verificações do site.

## 📌 Notificações
- **Discord Webhook** – API utilizada para enviar alertas sobre o status do site.

## 📌 Automação de Tarefas
- **Crontab (Linux)** – Agendador de tarefas para executar o script periodicamente.

## 📌 Infraestrutura
- **Ubuntu (Linux)** – Sistema operacional utilizado no servidor.
- **Nginx** – Servidor web para hospedar o site monitorado.
- **AWS EC2** – Serviço de computação na nuvem para hospedar o site e rodar o script.
- **VPC (AWS)** – Rede virtual privada para isolar e gerenciar a infraestrutura do servidor.

---
🚀 *Esse conjunto de tecnologias permite um monitoramento eficiente e automatizado do site, garantindo notificações rápidas no Discord em caso de falhas.*  

---
## ✅ Conclusão
Este documento fornece um teste de conhecimentos basicos como forma de  criar um passo a passo que te possibilite configurar uma **VPC**, lançar uma **instância EC2**, instalar **Nginx**, personalizar um site e automatizar tarefas criando alertas vinculadas a uma API no discord com o servidor. 🚀
#   C o n f i g u r a c a o - d e - S e r v i d o r - W e b - c o m - M o n i t o r a m e n t o - 
 
 