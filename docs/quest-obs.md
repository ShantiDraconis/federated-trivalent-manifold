# Meta Quest → OBS: modelo operacional

## 1. Espelhamento USB/TCP com scrcpy

`scrcpy` espelha a superfície de ecrã Android; não equivale a acesso irrestrito
às câmaras físicas. A latência depende do dispositivo, codificador, ligação,
resolução, taxa de bits e captura do OBS. Use captura de janela no OBS para o
modo interativo. Teste áudio separadamente no Quest: políticas Android podem
impedir ou alterar o encaminhamento da saída.

Exemplo inicial, ajustável à versão instalada:

```sh
scrcpy --max-size=1024 --video-bit-rate=8M --max-fps=60
```

Não construa comandos com `shell=True` e dados do utilizador. Invoque cada
programa com uma lista de argumentos e ligue pipes explicitamente.

## 2. Casting oficial

O casting do ponto de vista do utilizador é a via apropriada para capturar o
que aparece no headset, sujeito à conta, rede e políticas atuais da Meta. No
OBS, capture a janela do navegador. Não confunda casting com Passthrough Camera
API.

## 3. Passthrough Camera API

É uma API de desenvolvimento para modelos compatíveis e versões suportadas do
Horizon OS. Exige permissões e tratamento de dados do utilizador. A textura da
câmara pode ter resolução e campo de visão diferentes do que o utilizador vê.

## 4. RTMP/SRT e OBS

Um URL `rtmp://localhost/...` só funciona se houver um servidor RTMP a escutar,
publicar e disponibilizar o stream. “Media Source” não transforma o OBS num
servidor RTMP. Para baixa latência local, valide SRT, UDP/MPEG-TS, NDI ou um
servidor RTMP real conforme a instalação.

## 5. Teardown verificável

O teardown deve ser idempotente e observado, não apenas anunciado:

1. terminar os processos filhos com prazo;
2. forçar encerramento apenas se necessário;
3. executar `adb disconnect SERIAL`;
4. tentar restaurar USB enquanto o transporte ainda responde;
5. consultar `adb devices` e portas locais;
6. emitir um resultado estruturado por etapa.

Fechar ADB TCP no dispositivo não é o mesmo que “fechar 0.0.0.0:5555” no PC.
`0.0.0.0` é um endereço de bind local; o destino ADB normalmente é
`IP_DO_QUEST:5555`.
