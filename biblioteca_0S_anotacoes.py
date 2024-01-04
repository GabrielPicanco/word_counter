import calendar
# Comandos básicos com a biblioteca "OS"

# os.getcwd >>> Mostra o caminho que estou localizado
# os.chdir >>> Muda o caminho que estou localizado para o caminho que eu informar
# os.listdir >>> Lista todos os arquivos que estão dentro do caminho que eu estou
# os.mkdir >>> Cria uma pasta no caminho que estou.
# os.makedirs >>> Pode criar várias pastas de uma vez, precisa receber um caminho como parâmetro.
# os.rmdir >>> Remove uma pasta no caminho que estou.
# os.remove >>> Remove um arquivo no caminho que estou.
# os.rename >>> Renomeia um arquivo no caminho onde estou.
# os.startfile >>> Abre arquivos, não é muito útil, usar o "With open() as arquivo" é mais recomendado.

# os.walk >>> É como se fosse um listdir só que melhorado, dá pra especificar exatamente o tipo de arquivo
# que você quer listar, pode ser (raiz, pasta ou arquivo)

# COMANDOS USANDO O MÓDULO PATH

# os.path.basename >>> Mostra apenas o nome do caminho que estou localizado.

# os.path.commonpath >>> Mostra até onde os caminhos se repetem em 2 ou mais caminhos.

# os.path.commonprefix >>> Bem parecido com o commonpath, mas esse mostra até onde strings se repetem em
# dois caminhos, exemplo: C:\Users\gabri\Área de Trabalho  e  C:\Users\gabri\Área de Trabalho2.
# No exemplo acima, se eu der um print, ele vai me retornar isso: C:\Users\gabri\Área de Trabalho, porque é
# Até onde os dois caminhos se repetem em string.

# os.path.dirname >>> Retorna em que pasta está a pasta que eu estou.

# os.path.join >>> Junta strings e cria um caminho com elas.
