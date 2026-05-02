
from pdf import PDF

# Criando uma instância da classe PDF com o arquivo "gato-xadrez.pdf"
pdf = PDF("gato-xadrez.pdf")

# Separando apenas a capa página do PDF
pdf.split('capa', start=0, end=1)

# Separando os gatos
pdf.split('gato-azul', 5, 6)
pdf.split('gato-vermelho', 7, 8)
pdf.split('gato-amarelo', 9, 10)
pdf.split('gato-verde', 11, 12)
pdf.split('gato-colorido', 13, 14)
pdf.split('gato-laranja', 15, 16)
pdf.split('gato-marrom', 17, 18)
pdf.split('gato-rosa', 19, 20)
pdf.split('gato-preto', 21, 22)
pdf.split('gato-branco', 23, 24)
pdf.split('gato-xadrez', 24, 25)

pdf.save("apenas-gatos-sem-reordenacao", output_folder="gato-xadrez")

pdf.join([
    'capa', 
    # juntando gatos monocromáticos
    'gato-azul', 'gato-vermelho', 'gato-amarelo', 
    'gato-verde', 'gato-laranja', 'gato-marrom', 
    'gato-rosa', 'gato-preto', 'gato-branco',
    # reordenando gato colorido
    'gato-colorido',
    # juntando gato xadrez por último
    'gato-xadrez'
])

# Salvando o novo PDF com as páginas da capa e contracapa
pdf.save("apenas-gatos", output_folder="gato-xadrez")
