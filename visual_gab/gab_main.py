import pandas as pd
import matplotlib.pyplot as plt
import visual_gab as visual

df_2019 = pd.read_csv(r"C:\Users\Acer\Desktop\Apagar\PandENEM\2019_filtrado.csv", encoding='unicode_escape', engine='python')
df_2020 = pd.read_csv(r"C:\Users\Acer\Desktop\Apagar\PandENEM\2020_filtrado.csv", encoding='unicode_escape', engine='python')
df_2021 = pd.read_csv(r"C:\Users\Acer\Desktop\Apagar\PandENEM\2021_filtrado.csv", encoding='unicode_escape', engine='python')
df_2022 = pd.read_csv(r"C:\Users\Acer\Desktop\Apagar\PandENEM\2022_filtrado.csv", encoding='unicode_escape', engine='python')




"""
Essa analise nao leva em consideracao alunos treineiros do ENEM, apenas de alunos com nao faltantes em ambos dias durante a pandemia do COVID-19.

Sera analisado o desempenho dos participantes do ENEM nos anos de 2019, 2020, 2021 e 2022, onde e designada o principio da pandemia do COVID-19 no inicio do ano de 2020

Investigaremos se houve uma queda no desempenho de 2019 para 2020 e se os anos seguintes melhoraram ou pioraram, onde a hipotese e de melhora, pois proximo ao fim do ano de 2021 as aulas presenciais comecaram a retornar na maioria das escolas brasileiras.

Com base nisso podemos analisar o grafico abaixox que relaciona a media de todos alunos em cada materia em seus respectivos anos.

Podemos observar (observacao)

Porem, durante a pandemia outro criterio muito importe foi a prenseca do acesso a internet, pois como as aulas presenciais foram
impossibilitadas, alunos sem acesso a internet tiveram menor acesso ao estudo. Como podemos ver abaixo tanana

Outra analise de suma importancia e se o desempenho de alunos de escolas particulares sofreram maior interferencia em seu desempenho durante a pandemia do que alunos de escolas publicas.

(grafico)

com isso podemos calcular o desvio padrao: 
formula:

Algo que tambem pode ser analisado porem incerto qual sera o impacto eh o que relaciona a renda dos alunos com o desempenho, pois os alunos de renda mais baixa possivelmente largaram os estudos ou estudaram menos para auxiliarem seus pais durante os tempos duros de pandemia, porem continua sendo incerto pois esses mesmos participantes poderiam ja estar auxiliando os pais mesmo antes da pandemia.




Disclaimer: Para realizar uma analise nesse topico seria necessario um maior teor social e educacional, onde com o auxilio de um especialista ou estudante de ciencias sociais poderia gerar hipoteses e analises resultantes melhores.


o numero de faltantes nao treineiros de 2019 eh 4478504 - 3174212 = 1304292
o numero de faltantes nao treineiros de 2020 eh 5225684 - 2242169 = 2983515
o numero de faltantes nao treineiros de 2021 eh 2952642 - 1870734 = 1081908
o numero de faltantes nao treineiros de 2022 eh 2963373 - 1927753 = 1035620

"""
















