'''
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No

d={input():input()}
print(d)
key=input()
value=int(input())
if key in d:
    d[key]+=[value]
elif (2*key) in d:
    d[2*key]+=[value]
else: d.update({2*key:[value]})
print(d)
'''


n=int(input())
graph={}
for i in range(n):
    a,*b=input().replace(":", " ").split()
    graph.update({a:list(b)})

def find_path(graph, start, end, path=[]):

        path = path + [start]

        if start == end:

            return path

        if not graph.__contains__(start):

            return None

        for node in graph[start]:

            if node not in path:
               
                newpath = find_path(graph, node, end, path)

                if newpath:
                   
                    return newpath
                
        return None

q=int(input())
for i in range(q):
    s,d=input().split()
    if find_path(graph, d, s):
        print ('Yes')
    else: print('No')
