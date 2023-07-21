# Port Scanner (Scanner de Portas)

O Port Scanner, também conhecido como Scanner de Portas, é uma aplicação projetada para verificar um servidor ou host em busca de portas abertas. Esse tipo de aplicativo pode ser utilizado por administradores para verificar as políticas de segurança de suas redes e por atacantes para identificar os serviços de rede em execução em um host e explorar vulnerabilidades.

## Funcionamento

O funcionamento do Port Scanner baseia-se na tentativa de se conectar a uma série de portas em um determinado host e verificar se elas estão abertas ou fechadas. Uma porta aberta indica que há um serviço em execução e disponível para conexões, enquanto uma porta fechada significa que o serviço não está respondendo a conexões naquela porta específica.

## Uso por Administradores

Os administradores de rede podem usar o Port Scanner como uma ferramenta de monitoramento para garantir que apenas as portas necessárias estejam abertas em seus servidores, reduzindo assim a superfície de ataque e melhorando a segurança da rede. Isso ajuda a identificar portas não autorizadas ou serviços não essenciais que possam representar riscos de segurança.

## Uso por Atacantes

Por outro lado, os atacantes podem utilizar o Port Scanner como uma ferramenta para mapear os serviços em um host e identificar possíveis vulnerabilidades que possam ser exploradas para ganhar acesso não autorizado. Eles podem, por exemplo, procurar por portas de serviços conhecidos com vulnerabilidades conhecidas e tentar explorá-las para obter acesso não autorizado.

## Execução do Código

O código fornecido no exemplo é um programa de Port Scanner em Python. Ele demonstra como realizar a verificação de uma única porta em um host específico e, em seguida, como escanear múltiplas portas em um determinado host.

O código utiliza a biblioteca `socket` para estabelecer conexões TCP com os hosts e verificar o status das portas. É importante lembrar que o uso de um Port Scanner em ambientes não autorizados pode ser ilegal e violar a política de segurança de redes. Portanto, seu uso deve ser sempre de forma ética e com permissão dos responsáveis pela rede ou sistema em questão.
