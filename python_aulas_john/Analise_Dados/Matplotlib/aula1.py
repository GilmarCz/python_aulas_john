import matplotlib.pyplot as plt
import numpy as np

# Gráfico de linha
x= [1,2,3,5,6]
y= [2,5,6,8,6]

plt.plot(x,y)
plt.title("Teste Matplotlib")
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.show()

# Gráfico de Barra
categorias = ['a','b','c']
valores = [10,2,30]

plt.bar(categorias,valores)
plt.title('Barras')
plt.show()

# Gráfico de Pizza
plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Pizza')
plt.show()

# Histograma
dados = np.random.randn(1000)
plt.hist(dados,bins=30)
plt.title('Histograma')
plt.show()

# Dispersão
x1 = np.random.rand(50)
y1 = x1 + np.random.randn(50)*0.1
plt.scatter(x1,y1)
plt.title('Dispersão')
plt.show()