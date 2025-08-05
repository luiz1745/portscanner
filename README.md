Port Scanner Simples em Python
Um script básico para escanear portas abertas em um host específico usando sockets em Python.

Como funciona
O script tenta conectar a todas as portas TCP de 1 a 6534 no endereço IP definido na variável LHOST.

Para cada porta, ele verifica se está aberta.

Se a conexão for bem-sucedida, ele imprime a porta como aberta.

Uso
Altere o valor da variável LHOST para o IP do host que deseja escanear.

Execute o script com Python 3:

bash
Copiar
Editar
python3 portscanner.py
Aguarde os resultados, portas abertas serão listadas no terminal.

Atenção
Use esse script apenas em redes e dispositivos que você tem permissão para escanear.

Escanear redes sem autorização pode ser ilegal.

Requisitos
Python 3.x

Biblioteca padrão socket (já incluída no Python)

Contato
Dúvidas ou melhorias? Me chama!
Luiz (xiaodree)
