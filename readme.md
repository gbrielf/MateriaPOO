**Repositório da disciplina de Programação Orientada a Objeto.**

**Para "printar" algo em C#, usamos o método Console.WriteLine(). Aqui vai um exemplo simples:**

csharp
Copiar código
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, Chefe!");
    }
}
Esse código vai imprimir "Hello, Chefe!" no console. Simples e direto! Tá precisando de algo mais avançado?
**Como receber uma variável em C#**
Em C#, para receber uma entrada do usuário, você pode usar o método Console.ReadLine(), que sempre retorna uma string. Se você quiser outro tipo de dado (como um número), você precisa fazer uma conversão.

**Exemplo de receber uma string:**
csharp
Copiar código
Console.WriteLine("Digite seu nome:");
string nome = Console.ReadLine();  // Recebe uma string do usuário
Console.WriteLine("Olá, " + nome);
Exemplo de receber um número (inteiro):
csharp
Copiar código
Console.WriteLine("Digite sua idade:");
int idade = int.Parse(Console.ReadLine());  // Converte a string recebida para int
Console.WriteLine("Você tem " + idade + " anos.");
Aqui, usamos int.Parse() para converter a string que o usuário digitou em um número inteiro. Se você estiver esperando um número decimal, pode usar double.Parse() ou float.Parse().

**Principais tipos de variáveis em C#**
C# tem vários tipos de variáveis que são divididos em duas categorias principais: tipos de valor e tipos de referência.

**1. Tipos de Valor (Value Types)**
Os tipos de valor armazenam os dados diretamente na memória. Eles incluem números, booleanos, structs, etc. Alguns dos mais comuns são:

int: Armazena números inteiros (exemplo: 42).
csharp
Copiar código
int idade = 25;
double: Armazena números decimais de precisão dupla (exemplo: 3.14).
csharp
Copiar código
double altura = 1.75;
float: Armazena números decimais de precisão simples (exemplo: 2.5f). É necessário o sufixo f para indicar que o valor é um float.
csharp
Copiar código
float temperatura = 36.5f;
bool: Armazena valores booleanos (verdadeiro ou falso).
csharp
Copiar código
bool ligado = true;
char: Armazena um único caractere.
csharp
Copiar código
char inicial = 'C';
C# tem vários tipos de variáveis que são divididos em duas categorias principais: tipos de valor e tipos de referência.

**1. Tipos de Valor (Value Types)**
Os tipos de valor armazenam os dados diretamente na memória. Eles incluem números, booleanos, structs, etc. Alguns dos mais comuns são:

int: Armazena números inteiros (exemplo: 42).
csharp
Copiar código
int idade = 25;
double: Armazena números decimais de precisão dupla (exemplo: 3.14).
csharp
Copiar código
double altura = 1.75;
float: Armazena números decimais de precisão simples (exemplo: 2.5f). É necessário o sufixo f para indicar que o valor é um float.
csharp
Copiar código
float temperatura = 36.5f;
bool: Armazena valores booleanos (verdadeiro ou falso).
csharp
Copiar código
bool ligado = true;
char: Armazena um único caractere.
csharp
Copiar código
char inicial = 'C';

**2. Tipos de Referência (Reference Types)**
Os tipos de referência armazenam uma referência para os dados na memória, ao invés de armazenarem os dados diretamente. Alguns exemplos comuns incluem:

string: Armazena uma sequência de caracteres (textos).
csharp
Copiar código
string nome = "João";
arrays: Coleção de elementos do mesmo tipo.
csharp
Copiar código
int[] numeros = { 1, 2, 3, 4 };
classes: Objetos definidos pelo usuário.
csharp
Copiar código
class Pessoa {
    public string nome;
    public int idade;
}
**Tabela resumida dos tipos primitivos em C#**
Tipo	Descrição	Tamanho	Exemplo de Valor
int	Número inteiro	4 bytes	42
long	Número inteiro grande	8 bytes	9223372036854775807
float	Número decimal de precisão simples	4 bytes	3.14f
double	Número decimal de precisão dupla	8 bytes	3.14159
bool	Valor booleano	1 byte	true, false
char	Caractere	2 bytes	'A'
string	Sequência de caracteres	Depende	"Olá Mundo"

**Estruturas de Dados (como arrays)**
Em C#, arrays também podem ser alocados dinamicamente:

csharp
Copiar código
int[] numeros = new int[10];  // Aloca dinamicamente um array de inteiros
Neste exemplo, a memória para o array é alocada dinamicamente na heap e gerenciada pelo Garbage Collector.

Se precisar de mais controle...
Embora o Garbage Collector seja muito eficiente, C# também permite alocação manual de memória em alguns casos usando o stackalloc e unsafe code, mas isso é raro e geralmente usado em cenários que exigem altíssimo desempenho ou integração com código nativo.


**E por que não tem isso no C?**


O C foi criado como uma linguagem de baixo nível, próxima ao hardware, e projetado para ser eficiente, sem foco em abstrações como objetos. Já o C# foi desenvolvido com a programação orientada a objetos como um de seus pilares principais. Isso permite a criação de sistemas mais complexos e organizados, especialmente quando se trabalha com grandes projetos.

A POO traz conceitos como herança, polimorfismo, e encapsulamento, que ajudam a modularizar e reutilizar código, algo que em C precisaria de muito mais esforço manual.

Então, class no C# é uma ferramenta poderosa para organizar e estruturar o código de forma eficiente e modular, enquanto no C o foco é em simplicidade e performance.
Os conceitos de Programação Orientada a Objetos (POO) podem parecer meio complexos no começo, mas quando você pega a ideia, fica tranquilo. Vou te dar um panorama básico dos principais conceitos pra ver se fica mais claro:

**1. Classe e Objeto**
Classe: Como já falamos, é o molde que define como será o objeto.
Objeto: É a "instância" de uma classe. Ou seja, quando você cria algo a partir da classe, isso é um objeto.
Exemplo:

Classe: Carro
Objeto: um carro específico, tipo um Fusca vermelho.
**2. Herança**
A herança permite que uma classe "filha" herde as propriedades e métodos de uma classe "pai". Isso ajuda a evitar código duplicado.

Exemplo:

csharp
Copiar código
class Animal {
    public void Dormir() {
        Console.WriteLine("O animal está dormindo.");
    }
}

class Cachorro : Animal {
    public void Latir() {
        Console.WriteLine("O cachorro está latindo.");
    }
}
Aqui, a classe Cachorro herda o método Dormir da classe Animal. Isso significa que o cachorro pode tanto latir quanto dormir, sem você ter que reescrever o método Dormir.

**3. Polimorfismo**
O polimorfismo permite que métodos com o mesmo nome se comportem de maneiras diferentes, dependendo do objeto que os está chamando. Isso pode acontecer de duas formas: sobrecarga de métodos ou sobrescrita de métodos.

Exemplo:

csharp
Copiar código
class Animal {
    public virtual void FazerSom() {
        Console.WriteLine("O animal faz um som.");
    }
}

class Gato : Animal {
    public override void FazerSom() {
        Console.WriteLine("O gato mia.");
    }
}
Quando você chama FazerSom(), o comportamento muda dependendo do tipo do objeto (Animal ou Gato).

**4. Encapsulamento**
Encapsulamento é a ideia de "esconder" detalhes internos de uma classe, expondo apenas o que for necessário. Isso é feito usando modificadores de acesso, como public, private, protected.

Exemplo:

csharp
Copiar código
class Pessoa {
    private string nome;
    
    public void SetNome(string novoNome) {
        nome = novoNome;
    }
    
    public string GetNome() {
        return nome;
    }
}
Aqui, o nome é privado, então só pode ser acessado através dos métodos SetNome e GetNome.

**5. Abstração**
A abstração é o processo de esconder a complexidade e mostrar apenas a funcionalidade essencial. Isso pode ser feito criando classes e métodos que representam conceitos abstratos.

Exemplo: Se você criar uma classe abstrata Forma com um método CalcularArea(), outras formas, como Circulo ou Retangulo, podem implementá-la de maneiras diferentes, dependendo da forma geométrica.

Resumo:
Herança: Reaproveitar código entre classes.
Polimorfismo: Um método pode se comportar de formas diferentes.
Encapsulamento: Esconder detalhes e expor só o essencial.
Abstração: Simplificar a complexidade com conceitos.
Se a ideia for criar sistemas organizados e reutilizáveis, a POO é uma baita mão na roda! Quer se aprofundar em algum desses conceitos?

**Conceitos Básicos:**

_entidade:_ algo do mundo real que a gente
 precisa representar no software

_classificação:_ grupo de objetos com 
características semelhantes
Ex: triangulos, bolas, pássaros...

_abstração:_ é a identificação do que é
importante na representação de um ob-
jeto para o Sistema Computacional

"struct"

**modelando os dados (uma estrutura) struct
modelando as operações (uma função) function**

na POO, as entidades são modeladas em uma classe:
	- Os dados são os campos (ou atributos) de uma classe
	- As operações são realizadas pelos métodos
	- A classe com seus campos e métodos define um novo tipo de variável



**Como funciona a alocação de memória em C#?**
Em C#, toda vez que você cria um objeto usando new, a memória para esse objeto é alocada dinamicamente na heap (memória dinâmica). A grande vantagem do C# é que ele tem o Garbage Collector que gerencia a liberação de memória automaticamente, então você não precisa se preocupar em liberar a memória manualmente como faria no C.

**Exemplo de alocação dinâmica em C#**:
csharp
Copiar código
class Pessoa
{
    public string Nome;
}

Pessoa p = new Pessoa();  // Aloca memória para o objeto 'Pessoa'
p.Nome = "João";
Aqui, o objeto Pessoa é alocado dinamicamente na heap quando você usa new Pessoa(). Quando o objeto p não for mais utilizado e não houver nenhuma referência a ele, o Garbage Collector eventualmente vai liberar a memória.

**Diferenças para o C:**
C: Em C, você faz a alocação e a liberação de memória manualmente usando malloc() e free().
C#: Em C#, a alocação é feita com new, e a liberação é automática pelo Garbage Collector, sem necessidade de usar algo como free().
Mais detalhes sobre o Garbage Collector
O Garbage Collector roda em segundo plano e, quando detecta que a memória de um objeto não está mais sendo referenciada por nenhuma variável, ele libera essa memória para evitar vazamentos. Ele segue uma abordagem conhecida como geracional, o que significa que ele trabalha de forma otimizada com base na "idade" dos objetos, liberando primeiro os mais antigos ou não utilizados.


